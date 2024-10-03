import logging
import os
import re
from os.path import abspath
from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

import rdflib
from rdflib import URIRef, Graph, RDF

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.GenericBuilderFunctions import get_white_space_equivalent
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLOEnumeration import OSLOEnumeration
from otlmow_modelbuilder.HelperFunctions import wrap_in_quotes


class KeuzelijstWaarde:
    def __init__(self, invulwaarde='', label='', definitie='', objectUri='', status=''):
        self.invulwaarde = invulwaarde
        self.label = label
        self.definitie = definitie
        self.objectUri = objectUri
        self.status = status

    def print(self):
        if self.status in ('', 'ingebruik'):
            return self.invulwaarde

        return f'{self.invulwaarde} ({self.status})'


class OTLEnumerationCreator(AbstractDatatypeCreator):
    default_environment = 'prd'
    graph_dict: dict[str, dict[str, Graph]] = {'prd': {}, 'tei': {}, 'dev': {}}
    oslo_github_branch_mapping = {
        'prd': 'master',
        'tei': 'test',
        'dev': 'dev'
    }

    def __init__(self, oslo_collector: OSLOCollector, env: str = default_environment):
        super().__init__(oslo_collector)
        self.osloCollector = oslo_collector
        logging.info("Created an instance of OTLEnumerationCreator")
        if env != 'unittest':
            self.download_unzip_and_parse_to_dict(env=env)
            logging.info("Downloaded, unzipped and parsed the enumerations ttl file")

    def create_block_to_write_from_enumerations(self, oslo_enumeration: OSLOEnumeration, enumeration_validation_rules,
                                                environment: str = default_environment) -> [str]:
        if not isinstance(oslo_enumeration, OSLOEnumeration):
            raise ValueError(f"Input is not a OSLOEnumeration")

        if oslo_enumeration.objectUri == '':
            raise ValueError(f"OSLOEnumeration.objectUri is invalid. Value = '{oslo_enumeration.objectUri}'")

        if oslo_enumeration.objectUri in enumeration_validation_rules['valid_uri_and_types'].keys():
            pass
        else:
            match_re = False
            for regex in enumeration_validation_rules["valid_regexes"]:
                match_re = re.match(pattern=regex, string=oslo_enumeration.objectUri)
                if match_re:
                    break
            if not match_re:
                raise ValueError(
                    f"OSLOEnumeration.objectUri is invalid. Value = '{oslo_enumeration.objectUri}'")

        if oslo_enumeration.name == '':
            raise ValueError(f"OSLOEnumeration.name is invalid. Value = '{oslo_enumeration.name}'")

        return self.create_block_to_write_from_enumeration(oslo_enumeration=oslo_enumeration, environment=environment)

    def create_block_to_write_from_enumeration(self, oslo_enumeration: OSLOEnumeration,
                                               environment: str = default_environment) -> [str]:
        keuzelijst_waardes = self.get_keuzelijstwaardes_by_uri(oslo_enumeration.codelist, env=environment)
        adm_status = self.get_adm_status_by_uri(oslo_enumeration.codelist, env=environment)

        datablock = ['# coding=utf-8',
                     'from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField']
        if len(keuzelijst_waardes) > 0:
            datablock.append('from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde')

        datablock.extend(['',
                          '',
                          f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit',
                          f'class {oslo_enumeration.name}(KeuzelijstField):',
                          f'    """{oslo_enumeration.definition}"""',
                          f'    naam = {wrap_in_quotes(oslo_enumeration.name)}',
                          f'    label = {wrap_in_quotes(oslo_enumeration.label)}',
                          f'    objectUri = {wrap_in_quotes(oslo_enumeration.objectUri)}',
                          f'    definition = {wrap_in_quotes(oslo_enumeration.definition)}'])

        if adm_status is not None and adm_status != '':
            datablock.append(f'    status = {wrap_in_quotes(adm_status)}')
        if oslo_enumeration.deprecated_version != '':
            oslo_enumeration.deprecated_version = oslo_enumeration.deprecated_version.split('-')[0]
            datablock.append(f'    deprecated_version = {wrap_in_quotes(oslo_enumeration.deprecated_version)}')
        datablock.append(f'    codelist = {wrap_in_quotes(oslo_enumeration.codelist)}')
        datablock.append('    options = {')

        for waarde in sorted(keuzelijst_waardes, key=lambda w: w.invulwaarde):
            if oslo_enumeration.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieCode':
                waarde.definitie = waarde.definitie.replace('²', '^2')
                waarde.invulwaarde = waarde.invulwaarde.replace("'", "\\'")
                waarde.label = waarde.label.replace("'", "\\'")
                waarde.objectUri = waarde.objectUri.replace("'", "\\'")

            whitespace = get_white_space_equivalent(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(")
            datablock.append(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(invulwaarde='{waarde.invulwaarde}',")
            datablock.append(f"{whitespace}label={wrap_in_quotes(waarde.label)},")
            if waarde.status != '':
                datablock.append(f"{whitespace}status='{waarde.status}',")
            if waarde.definitie != '':
                datablock.append(f"{whitespace}definitie={wrap_in_quotes(waarde.definitie)},")
            datablock.append(f"{whitespace}objectUri='{waarde.objectUri}'),")

        if len(keuzelijst_waardes) > 0:
            datablock[-1] = datablock[-1][:-1]
        datablock.append('    }')

        # dummy values part
        datablock.append("")
        datablock.append("    @classmethod")
        datablock.append("    def create_dummy_data(cls):")
        datablock.append("        return cls.create_dummy_data_keuzelijst(cls.options)")
        datablock.append('')

        return datablock

    @classmethod
    def get_graph_from_location(cls, keuzelijstnaam: str, env: str = default_environment):
        raise NotImplementedError("This method is not implemented in the OTLEnumerationCreator class")
        if env is None or env == '':
            env = cls.default_environment

        if env in ['prd', 'UnitTests.TestClasses']:
            env = 'master'
        elif env == 'tei':
            env = 'test'
        elif env == 'dev':
            env = 'dev'
        elif env == 'aim':
            raise ValueError(f"Environment '{env}' is not supported for fetching the keuzelijst")

        # create a Graph
        g = rdflib.Graph()
        keuzelijst_link = f"https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/{env}/codelijsten/{keuzelijstnaam}.ttl"

        # parse the turtle file hosted on github
        try:
            g.parse(keuzelijst_link, format="turtle")
        except Exception as exc:
            if 'KlTestKeuzelijst' in keuzelijstnaam:
                base_dir = os.path.dirname(os.path.realpath(__file__))
                keuzelijst_link = abspath(f'{base_dir}/../UnitTests/KlTestKeuzelijst.ttl')
                g.parse(keuzelijst_link, format="turtle")
            else:
                logging.error(f"Could not get ttl file for {keuzelijstnaam}")
                raise exc
        OTLEnumerationCreator.most_recent_graph = (keuzelijstnaam, env, g)
        return g

    @classmethod
    def get_graph(cls, keuzelijstnaam: str, env: str = default_environment):
        # check if the most_recent_graph holds the correct graph. If so, return that one, else fetch the correct one
        keuzelijst_graph = OTLEnumerationCreator.graph_dict[env].get(keuzelijstnaam)
        if keuzelijst_graph is not None:
            return keuzelijst_graph

        return OTLEnumerationCreator.get_graph_from_location(keuzelijstnaam=keuzelijstnaam, env=env)

    def download_unzip_and_parse_to_dict(self, env: str = default_environment) -> dict[str:dict[str, Graph]]:
        path_zip_file = Path("all.ttl.zip")
        path_ttl_file = Path("all.ttl")
        directory_to_extract_to = path_zip_file.parent
        urlretrieve(f"https://github.com/Informatievlaanderen/OSLO-codelistgenerated/raw/refs/heads/wegenenverkeer-{self.oslo_github_branch_mapping[env]}/all.ttl.zip", path_zip_file)
        with ZipFile(path_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

        self.graph_dict[env] = self.parse_graph_to_dict(path_ttl_file=path_ttl_file)

    @staticmethod
    def parse_graph_to_dict(path_ttl_file: Path) -> dict[str, Graph]:
        g = rdflib.Graph()
        g.parse(path_ttl_file, format="turtle")
        print(g)

        keuzelijst_dict = {}
        keuzelijst_uris = set(g.objects(predicate=URIRef('http://www.w3.org/2004/02/skos/core#inScheme')))

        for keuzelijst_uri in keuzelijst_uris:
            keuzelijst_waarde_uris = g.subjects(predicate=URIRef('http://www.w3.org/2004/02/skos/core#inScheme'),
                                                object=keuzelijst_uri)
            keuzelijst_graph = Graph()
            for keuzelijst_waarde_uri in keuzelijst_waarde_uris:
                for triple in g.triples((keuzelijst_waarde_uri, None, None)):
                    keuzelijst_graph.add(triple)

            keuzelijst_dict[str(keuzelijst_uri)] = keuzelijst_graph
        rdflib.term.URIRef('https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestKeuzelijst')
        return keuzelijst_dict

    @classmethod
    def get_keuzelijstwaardes_by_uri(cls, uri: str, env: str = default_environment) -> [KeuzelijstWaarde]:
        g = cls.graph_dict[env][uri]
        return cls.get_keuzelijstwaardes_from_graph(g, env)

    @classmethod
    def get_keuzelijstwaardes_from_graph(cls, g: Graph, env: str = default_environment):
        lijst_keuze_opties = []

        subjects = set(g.subjects(predicate=None, object=None))
        distinct_subjects_list = sorted(subjects, key=lambda x: str(x))

        for distinct_subject in distinct_subjects_list:
            subject_str = str(distinct_subject)
            if subject_str.startswith('https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/'):
                continue
            elif env == 'tei' and subject_str.startswith(
                    'https://wegenenverkeer-test.data.vlaanderen.be/id/conceptscheme/'):
                continue
            waarde = KeuzelijstWaarde()
            waarde.objectUri = subject_str
            status = g.value(subject=distinct_subject, predicate=URIRef('https://www.w3.org/ns/adms#status'))
            if status is not None:
                waarde.status = str(status).replace(
                    'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/', '')
            waarde.invulwaarde = str(
                g.value(subject=distinct_subject, predicate=URIRef('http://www.w3.org/2004/02/skos/core#notation')))
            waarde.definitie = str(
                g.value(subject=distinct_subject, predicate=URIRef('http://www.w3.org/2004/02/skos/core#definition')))
            waarde.label = str(
                g.value(subject=distinct_subject, predicate=URIRef('http://www.w3.org/2004/02/skos/core#prefLabel')))
            lijst_keuze_opties.append(waarde)

        return lijst_keuze_opties

    @classmethod
    def get_adm_status_by_uri(cls, keuzelijst_uri: str, env: str = default_environment) -> str:
        g = OTLEnumerationCreator.get_graph(keuzelijst_uri, env=env)
        return cls.get_adm_status_from_graph(g, name=keuzelijst_uri, env=env)

    @classmethod
    def get_adm_status_from_graph(cls, g: Graph, name: str, env: str = default_environment) -> str:
        scheme_uri = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/' + name
        if env == 'tei':
            scheme_uri = 'https://wegenenverkeer-test.data.vlaanderen.be/id/conceptscheme/' + name

        status = g.value(subject=URIRef(scheme_uri), predicate=URIRef('https://www.w3.org/ns/adms#status'))

        if status is not None:
            return str(status).replace('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/', '')
        else:
            return ''
