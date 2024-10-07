import logging
import os
import re
from os.path import abspath
from pathlib import Path
from typing import Dict
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
    graph_dict: Dict[str, Dict[str, Graph]] = {'prd': {}, 'tei': {}, 'dev': {}}
    oslo_github_branch_mapping = {
        'prd': 'master',
        'tei': 'test',
        'dev': 'dev'
    }

    def __init__(self, oslo_collector: OSLOCollector, env: str = default_environment, 
                 include_kl_test_keuzelijst: bool = False):
        super().__init__(oslo_collector)
        self.oslo_collector = oslo_collector
        self.env = env
        self.include_kl_test_keuzelijst = include_kl_test_keuzelijst
        logging.info("Created an instance of OTLEnumerationCreator")

    def __enter__(self):
        self.path_zip_file = Path(__file__).parent / "all.ttl.zip"
        self.path_ttl_file = Path(__file__).parent / "all.ttl"
        if self.env != 'unittest':
            self.graph_dict[self.env] = self.download_unzip_and_parse_to_dict(env=self.env)
            logging.info("Downloaded, unzipped and parsed the enumerations ttl file")
        if self.include_kl_test_keuzelijst:
            self.add_kl_test_keuzelijst(env=self.env)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.path_zip_file.exists():
            self.path_zip_file.unlink()
        if self.path_ttl_file.exists():
            self.path_ttl_file.unlink()

    def add_kl_test_keuzelijst(self, env):
        kl_test_keuzelijst_path = Path(__file__ ).parent.parent / 'UnitTests/KlTestKeuzelijst.ttl'
        if not kl_test_keuzelijst_path.exists():
            url = 'https://raw.githubusercontent.com/davidvlaminck/OTLMOW-ModelBuilder/refs/heads/master/UnitTests/KlTestKeuzelijst.ttl'
            urlretrieve(url, kl_test_keuzelijst_path)
        self.graph_dict[env].update(self.parse_graph_to_dict(path_ttl_file=kl_test_keuzelijst_path))

    def create_block_to_write_from_enumerations(self, oslo_enumeration: OSLOEnumeration, enumeration_validation_rules,
                                                environment: str = default_environment) -> [str]:
        if not isinstance(oslo_enumeration, OSLOEnumeration):
            raise ValueError("Input is not a OSLOEnumeration")

        if oslo_enumeration.objectUri == '':
            raise ValueError(f"OSLOEnumeration.objectUri is invalid. Value = '{oslo_enumeration.objectUri}'")

        if oslo_enumeration.objectUri not in enumeration_validation_rules['valid_uri_and_types'].keys():
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
    def get_graph(cls, keuzelijstnaam: str, env: str = default_environment):
        keuzelijst_graph = OTLEnumerationCreator.graph_dict[env].get(keuzelijstnaam)
        if keuzelijst_graph is not None:
            return keuzelijst_graph
        raise ValueError(f"Graph for {keuzelijstnaam} not found in the graph_dict")

    def download_unzip_and_parse_to_dict(self, env: str = default_environment) -> Dict[str, Graph]:
        directory_to_extract_to = self.path_zip_file.parent
        urlretrieve(f"https://github.com/Informatievlaanderen/OSLO-codelistgenerated/raw/refs/heads/wegenenverkeer-{self.oslo_github_branch_mapping[env]}/all.ttl.zip", self.path_zip_file)
        with ZipFile(self.path_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

        return self.parse_graph_to_dict(path_ttl_file=self.path_ttl_file)

    @staticmethod
    def parse_graph_to_dict(path_ttl_file: Path) -> Dict[str, Graph]:
        g = rdflib.Graph()
        g.parse(path_ttl_file, format="turtle")

        keuzelijst_dict = {}
        keuzelijst_uris = set(g.subjects(predicate=RDF.type, object=URIRef('http://www.w3.org/2004/02/skos/core#ConceptScheme')))

        for keuzelijst_uri in keuzelijst_uris:
            keuzelijst_graph = Graph()
            for triple in g.triples((keuzelijst_uri, None, None)):
                keuzelijst_graph.add(triple)

            keuzelijst_waarde_uris = g.subjects(predicate=URIRef('http://www.w3.org/2004/02/skos/core#inScheme'),
                                                object=keuzelijst_uri)
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
        return cls.get_adm_status_from_graph(g, uri=keuzelijst_uri, env=env)

    @classmethod
    def get_adm_status_from_graph(cls, g: Graph, uri: str, env: str = default_environment) -> str:
        if env == 'tei':
            uri = uri.replace('wegenenverkeer', 'wegenenverkeer-test')

        status = g.value(subject=URIRef(uri), predicate=URIRef('https://www.w3.org/ns/adms#status'))

        if status is not None:
            return str(status).replace('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/', '')
        else:
            return ''
