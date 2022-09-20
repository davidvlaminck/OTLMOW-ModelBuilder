import os
import unittest
from pathlib import Path
from unittest.mock import MagicMock

import rdflib

from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLOEnumeration import OSLOEnumeration
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator, KeuzelijstWaarde
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedKeuzelijst = ['# coding=utf-8',
                      'import random',
                      'from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField',
                      'from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde',
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
                      '        return random.choice(list(map(lambda x: x.invulwaarde,',
                      '                                      '
                      "filter(lambda option: option.status == 'ingebruik', cls.options.values()))))",
                      '']


class OTLEnumerationCreatorTests(unittest.TestCase):
    def test_InvalidOSLOEnumerationEmptyUri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLEnumerationCreator(collector)
        osloEnumeration = OSLOEnumeration(name='name', objectUri='', definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.create_block_to_write_from_enumerations(osloEnumeration)
        self.assertEqual(str(exception_empty_uri.exception), "OSLOEnumeration.objectUri is invalid. Value = ''")

    def test_InvalidOSLOEnumerationBadUri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLEnumerationCreator(collector)
        osloEnumeration = OSLOEnumeration(name='name', objectUri='Bad objectUri', definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.create_block_to_write_from_enumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_uri.exception), "OSLOEnumeration.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLOEnumerationEmptyName(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLEnumerationCreator(collector)
        osloEnumeration = OSLOEnumeration(name='',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                          definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_enumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_name.exception), "OSLOEnumeration.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_primitive = True
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLEnumerationCreator(collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_enumerations(bad_primitive)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLOEnumeration")

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_KlTestKeuzelijst(self):
        collector = self.setUp()
        creator = OTLEnumerationCreator(collector)
        KlAIMToestand = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        dataToWrite = creator.create_block_to_write_from_enumerations(KlAIMToestand)

        self.assertEqual(expectedKeuzelijst, dataToWrite)

    def test_get_keuzelijstwaardes_by_name(self):
        collector = self.setUp()
        creator = OTLEnumerationCreator(collector)
        keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        keuzelijst_waarden = creator.get_keuzelijstwaardes_by_name(keuzelijst.name)
        self.assertTrue(len(keuzelijst_waarden) > 0)
        self.assertIsInstance(keuzelijst_waarden[0], KeuzelijstWaarde)

        waarde_2 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-2')
        self.assertEqual('waarde-2', waarde_2.invulwaarde)
        self.assertEqual('waarde 2', waarde_2.label)
        self.assertEqual('', waarde_2.definitie)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-2',
                         waarde_2.objectUri)

    def test_get_keuzelijstwaardes_from_graph(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/KlTestKeuzelijst.ttl'
        g = rdflib.Graph()
        g.parse(file_location, format="turtle")
        list = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g)
        self.assertEqual(6, len(list))

    def test_get_adm_status_from_graph(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/KlTestKeuzelijst.ttl'
        g = rdflib.Graph()
        g.parse(file_location, format="turtle")
        status = OTLEnumerationCreator.get_adm_status_from_graph(g, name='KlTestKeuzelijst')
        self.assertEqual('ingebruik', status)

    def test_get_keuzelijstwaardes_from_graph_new_format(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/new_format_ttl.ttl'
        g = rdflib.Graph()
        g.parse(file_location, format="turtle")
        list = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g)
        self.assertEqual(2, len(list))

    def test_get_adms_status_for_options(self):
        collector = self.setUp()
        creator = OTLEnumerationCreator(collector)
        keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        keuzelijst_waarden = creator.get_keuzelijstwaardes_by_name(keuzelijst.name)

        waarde_4 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-4')
        self.assertEqual('ingebruik', waarde_4.status)

        waarde_5 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-5')
        self.assertEqual('uitgebruik', waarde_5.status)

        waarde_6 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-6')
        self.assertEqual('verwijderd', waarde_6.status)
