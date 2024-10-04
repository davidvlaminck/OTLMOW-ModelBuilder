import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import rdflib
from rdflib import Graph, compare, URIRef

from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator, KeuzelijstWaarde
from otlmow_modelbuilder.SQLDataClasses.OSLOEnumeration import OSLOEnumeration

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedKeuzelijst = ['# coding=utf-8',
                      'from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField',
                      'from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde',
                      '',
                      '',
                      '# Generated with OTLEnumerationCreator. To modify: extend, do not edit',
                      'class KlTestKeuzelijst(KeuzelijstField):',
                      '    """Keuzelijst met test waarden."""',
                      "    naam = 'KlTestKeuzelijst'",
                      "    label = 'Test keuzelijst'",
                      "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst'",
                      "    definition = 'Keuzelijst met test waarden.'",
                      "    status = 'ingebruik'",
                      "    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestKeuzelijst'",
                      '    options = {',
                      "        'waarde-1': KeuzelijstWaarde(invulwaarde='waarde-1',",
                      "                                     label='waarde 1',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-1'),",
                      "        'waarde-2': KeuzelijstWaarde(invulwaarde='waarde-2',",
                      "                                     label='waarde 2',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-2'),",
                      "        'waarde-3': KeuzelijstWaarde(invulwaarde='waarde-3',",
                      "                                     label='waarde 3',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-3'),",
                      "        'waarde-4': KeuzelijstWaarde(invulwaarde='waarde-4',",
                      "                                     label='waarde 4',",
                      "                                     status='ingebruik',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-4'),",
                      "        'waarde-5': KeuzelijstWaarde(invulwaarde='waarde-5',",
                      "                                     label='waarde 5',",
                      "                                     status='uitgebruik',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-5'),",
                      "        'waarde-6': KeuzelijstWaarde(invulwaarde='waarde-6',",
                      "                                     label='waarde 6',",
                      "                                     status='verwijderd',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-6')",
                      '    }',
                      '',
                      '    @classmethod',
                      '    def create_dummy_data(cls):',
                      '        return cls.create_dummy_data_keuzelijst(cls.options)',
                      '']

enumeration_validation_rules = {
    "valid_uri_and_types": {},
    "valid_regexes": [
        "^https://wegenenverkeer.data.vlaanderen.be/ns/.+"]
}


# def test_refactor():
#     collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
#     creator = OTLEnumerationCreator(collector, env='unittest')
#     creator.download_unzip_and_parse_to_dict(env='tei')


def create_test_enumeration_creator() -> OTLEnumerationCreator:
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        creator.graph_dict['prd'] = creator.parse_graph_to_dict(Path(__file__).parent / 'KlTestKeuzelijst.ttl')
        return creator


def test_parse_graph_to_dict_all_test_ttl():
    current_dir = Path(__file__).parent
    file_location = Path(current_dir) / 'all_test.ttl'
    graph_dict = OTLEnumerationCreator.parse_graph_to_dict(file_location)

    assert len(graph_dict) == 2
    assert 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand' in graph_dict
    assert 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/AntiParkeerpaalType' in graph_dict

    expected_graph_1 = Graph()
    expected_graph_1.parse(Path(current_dir) / 'unittest_antiparkeerpaaltype_extracted.ttl', format="turtle")
    actual_graph_1 = graph_dict['https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/AntiParkeerpaalType']

    assert set(sorted(actual_graph_1)) == set(sorted(expected_graph_1))

    epxected_graph_2 = Graph()
    epxected_graph_2.parse(Path(current_dir) / 'unittest_toestand_extracted.ttl', format="turtle")
    actual_graph_2 = graph_dict['https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand']

    assert set(sorted(actual_graph_2)) == set(sorted(epxected_graph_2))


def test_InvalidOSLOEnumerationEmptyUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        oslo_enumeration = OSLOEnumeration(name='name', objectUri='', definition='', label='', usagenote='',
                                           deprecated_version='', codelist='')

        with pytest.raises(ValueError) as exception_empty_uri:
            creator.create_block_to_write_from_enumerations(
                oslo_enumeration, enumeration_validation_rules=enumeration_validation_rules)
        assert str(exception_empty_uri.value) == "OSLOEnumeration.objectUri is invalid. Value = ''"


def test_InvalidOSLOEnumerationBadUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        oslo_enumeration = OSLOEnumeration(name='name', objectUri='Bad objectUri', definition='', label='',
                                           usagenote='', deprecated_version='', codelist='')

        with pytest.raises(ValueError) as exception_bad_uri:
            creator.create_block_to_write_from_enumerations(
                oslo_enumeration, enumeration_validation_rules=enumeration_validation_rules)
        assert str(exception_bad_uri.value) == "OSLOEnumeration.objectUri is invalid. Value = 'Bad objectUri'"


def test_InvalidOSLOEnumerationEmptyName():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        oslo_enumeration = OSLOEnumeration(
            name='', definition='', label='', usagenote='', deprecated_version='', codelist='',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')

        with pytest.raises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_enumerations(
                oslo_enumeration, enumeration_validation_rules=enumeration_validation_rules)
        assert str(exception_bad_name.value) == "OSLOEnumeration.name is invalid. Value = ''"


def test_InValidType():
    bad_primitive = True
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        with pytest.raises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_enumerations(
                bad_primitive, enumeration_validation_rules=enumeration_validation_rules)
        assert str(exception_bad_name.value) == "Input is not a OSLOEnumeration"


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def test_KlTestKeuzelijst():
    collector = set_up()
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        creator.graph_dict['prd'] = creator.parse_graph_to_dict(Path(__file__).parent / 'KlTestKeuzelijst.ttl')

        kl_test_keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        data_to_write = creator.create_block_to_write_from_enumerations(
            kl_test_keuzelijst, enumeration_validation_rules=enumeration_validation_rules)

        assert data_to_write == expectedKeuzelijst


def test_get_keuzelijstwaardes_by_name():
    collector = set_up()
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        creator.graph_dict['prd'] = creator.parse_graph_to_dict(Path(__file__).parent / 'KlTestKeuzelijst.ttl')
        keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        keuzelijst_waarden = creator.get_keuzelijstwaardes_by_uri(keuzelijst.codelist)
        assert len(keuzelijst_waarden) > 0
        assert isinstance(keuzelijst_waarden[0], KeuzelijstWaarde)

        waarde_2 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-2')
        assert waarde_2.invulwaarde == 'waarde-2'
        assert waarde_2.label == 'waarde 2'
        assert waarde_2.definitie == ''
        assert waarde_2.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-2'


def test_get_keuzelijstwaardes_from_graph():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = f'{base_dir}/KlTestKeuzelijst.ttl'
    g = rdflib.Graph()
    g.parse(file_location, format="turtle")
    list_values = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g)
    assert len(list_values) == 6


def test_get_adm_status_from_graph():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = f'{base_dir}/KlTestKeuzelijst.ttl'
    g = rdflib.Graph()
    g.parse(file_location, format="turtle")
    status = OTLEnumerationCreator.get_adm_status_from_graph(
        g, uri='https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestKeuzelijst')
    assert status == 'ingebruik'


def test_get_keuzelijstwaardes_from_graph_new_format():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = f'{base_dir}/new_format_ttl.ttl'
    g = rdflib.Graph()
    g.parse(file_location, format="turtle")
    list_values = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g)
    assert len(list_values) == 2


def test_get_adms_status_for_options():
    collector = set_up()
    with OTLEnumerationCreator(collector, env='unittest') as creator:
        creator.graph_dict['prd'] = creator.parse_graph_to_dict(Path(__file__).parent / 'KlTestKeuzelijst.ttl')
        keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        keuzelijst_waarden = creator.get_keuzelijstwaardes_by_uri(keuzelijst.codelist)

        waarde_4 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-4')
        assert waarde_4.status == 'ingebruik'

        waarde_5 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-5')
        assert waarde_5.status == 'uitgebruik'

        waarde_6 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-6')
        assert waarde_6.status == 'verwijderd'
