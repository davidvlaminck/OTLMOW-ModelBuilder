import os
import unittest
from pathlib import Path
from unittest import skip

from otlmow_modelbuilder.GenericBuilderFunctions import get_white_space_equivalent, add_attributen_to_data_block, \
    get_fields_to_import_from_list_of_attributes, write_to_file
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class GenericBuilderFunctionsTests(unittest.TestCase):
    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Non_empty_start_list(self):
        collector = self.setUp()
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        list_of_fields = get_fields_to_import_from_list_of_attributes(collector, list_of_attributes, ['BooleanField'])

        self.assertEqual(['BooleanField', 'KwantWrdTest', 'StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Empty_start_list(self):
        collector = self.setUp()
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        list_of_fields = get_fields_to_import_from_list_of_attributes(collector, list_of_attributes)

        self.assertEqual(['KwantWrdTest', 'StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_with_ComplexType(self):
        collector = self.setUp()
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "Complex" in x.name, list_of_attributes))

        list_of_fields = get_fields_to_import_from_list_of_attributes(collector, complex_attributes_list)

        self.assertEqual(['DtcTestComplexType2'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_two_StringField(self):
        collector = self.setUp()
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "String" in x.name, list_of_attributes))

        list_of_fields = get_fields_to_import_from_list_of_attributes(collector, complex_attributes_list)

        self.assertEqual(['StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_two_StringField_and_two_BooleanField(self):
        collector = self.setUp()
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "String" in x.name or "Boolean" in x.name, list_of_attributes))

        list_of_fields = get_fields_to_import_from_list_of_attributes(collector, complex_attributes_list)

        self.assertEqual(['BooleanField', 'StringField'], list_of_fields)

    def test_get_white_space_equivalent_empty_string(self):
        result = get_white_space_equivalent('')
        self.assertEqual('', result)

    def test_get_white_space_equivalent_string_of_1_length(self):
        result = get_white_space_equivalent('a')
        self.assertEqual(' ', result)

    def test_get_white_space_equivalent_string_of_2_length(self):
        result = get_white_space_equivalent('aa')
        self.assertEqual('  ', result)

    def test_add_attributen_to_dataBlock_StringField(self):
        attribuut = OSLODatatypeComplexAttribuut('huisnummer', 'huisnummer',
                                                 'Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                                 '1', '1',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',
                                                 'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')

        expected_datablock = ['        self._huisnummer = OTLAttribuut(field=StringField,',
                              "                                        naam='huisnummer',",
                              "                                        label='huisnummer',",
                              "                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',",
                              "                                        definition='Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',",
                              "                                        owner=self)",
                              '',
                              '    @property',
                              '    def huisnummer(self):',
                              '        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""',
                              '        return self._huisnummer.get_waarde()',
                              '',
                              '    @huisnummer.setter',
                              '    def huisnummer(self, value):',
                              '        self._huisnummer.set_waarde(value, owner=self._parent)',
                              '']

        self.assertEqual(expected_datablock, add_attributen_to_data_block([attribuut], []))

    def test_add_attributen_to_dataBlock_DteField(self):
        attribuut = OSLOAttribuut('toestandBuis', 'toestand buis', 'Opmerkingen van de toestand en staat van de buis.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok', 0,
                                  '', 0, '',
                                  '')

        expected_datablock = ['        self._toestandBuis = OTLAttribuut(field=DteTekstblok,',
                              "                                          naam='toestandBuis',",
                              "                                          label='toestand buis',",
                              "                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',",
                              "                                          definition='Opmerkingen van de toestand en staat van de buis.',",
                              "                                          owner=self)",
                              '',
                              '    @property',
                              '    def toestandBuis(self):',
                              '        """Opmerkingen van de toestand en staat van de buis."""',
                              '        return self._toestandBuis.get_waarde()',
                              '',
                              '    @toestandBuis.setter',
                              '    def toestandBuis(self, value):',
                              '        self._toestandBuis.set_waarde(value, owner=self._parent)',
                              '']

        self.assertEqual(expected_datablock, add_attributen_to_data_block([attribuut], []))

    def test_add_attributen_to_dataBlock_KwantWrd(self):
        attribuut = OSLOAttribuut('lengte', 'lengte',
                                  'De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter',
                                  0, '', 0,
                                  '', '')

        expected_datablock = ['        self._lengte = OTLAttribuut(field=KwantWrdInMeter,',
                              "                                    naam='lengte',",
                              "                                    label='lengte',",
                              "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',",
                              "                                    definition='De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',",
                              "                                    owner=self)",
                              '',
                              '    @property',
                              '    def lengte(self):',
                              '        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""',
                              '        return self._lengte.get_waarde()',
                              '',
                              '    @lengte.setter',
                              '    def lengte(self, value):',
                              '        self._lengte.set_waarde(value, owner=self._parent)',
                              '']

        self.assertEqual(expected_datablock, add_attributen_to_data_block([attribuut], []))

    def test_add_attributen_to_data_block_DtcAdres(self):
        attribuut = OSLODatatypeComplexAttribuut('adres', 'adres', 'Adres dat men kan aanschrijven of bezoeken.',
                                                 'https://schema.org/ContactPoint', '0', '1',
                                                 'https://schema.org/ContactPoint.adres',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                                 0,
                                                 '', 0, '', '')

        expected_datablock = ['        self._adres = OTLAttribuut(field=DtcAdres,',
                              "                                   naam='adres',",
                              "                                   label='adres',",
                              "                                   objectUri='https://schema.org/ContactPoint.adres',",
                              "                                   kardinaliteit_min='0',",
                              "                                   definition='Adres dat men kan aanschrijven of bezoeken.',",
                              "                                   owner=self)",
                              '',
                              '    @property',
                              '    def adres(self):',
                              '        """Adres dat men kan aanschrijven of bezoeken."""',
                              '        return self._adres.get_waarde()',
                              '',
                              '    @adres.setter',
                              '    def adres(self, value):',
                              '        self._adres.set_waarde(value, owner=self._parent)',
                              '']

        self.assertEqual(expected_datablock, add_attributen_to_data_block([attribuut], []))

    @skip('change the write_file test') # TODO change this test
    def test_WriteToFileContainerBuis(self):
        collector, creator = self.set_up_real_collector_and_creator()
        containerBuis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
        dataToWrite = creator.create_blocks_to_write_from_classes(containerBuis)
        write_to_file(containerBuis, 'Classes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Classes/ContainerBuis.py'))
        self.assertTrue(os.path.isfile(filelocation))
