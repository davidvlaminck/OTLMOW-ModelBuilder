import os
from pathlib import Path
from unittest import skip

from UnitTests.OTLClassCreator_test import set_up_real_collector_and_creator
from otlmow_modelbuilder.GenericBuilderFunctions import get_white_space_equivalent, add_attributen_to_data_block, \
    get_fields_to_import_from_list_of_attributes, write_to_file
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

complex_datatype_validation_rules = {'valid_uri_and_types': {},
                                     'valid_regexes': ["^https://wegenenverkeer.data.vlaanderen.be/ns/.+#Dtc.+"]}


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Non_empty_start_list():
    collector = set_up()
    list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

    list_of_fields = get_fields_to_import_from_list_of_attributes(collector, list_of_attributes,
                                                                  list_to_start_from=['BooleanField'],
                                                                  valid_uri_and_types={})
    assert list_of_fields == ['BooleanField', 'KwantWrdTest', 'StringField']


def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Empty_start_list():
    collector = set_up()
    list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

    list_of_fields = get_fields_to_import_from_list_of_attributes(collector, list_of_attributes,
                                                                  valid_uri_and_types={})
    assert list_of_fields == ['KwantWrdTest', 'StringField']


def test_get_fields_to_import_from_list_of_attributes_List_with_ComplexType():
    collector = set_up()
    list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
    complex_attributes_list = list(filter(lambda x: "Complex" in x.name, list_of_attributes))

    list_of_fields = get_fields_to_import_from_list_of_attributes(collector, complex_attributes_list,
                                                                  valid_uri_and_types={})
    assert list_of_fields == ['DtcTestComplexType2']


def test_get_fields_to_import_from_list_of_attributes_List_two_StringField():
    collector = set_up()
    list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
    complex_attributes_list = list(filter(lambda x: "String" in x.name, list_of_attributes))

    list_of_fields = get_fields_to_import_from_list_of_attributes(collector, complex_attributes_list,
                                                                  valid_uri_and_types={})
    assert list_of_fields == ['StringField']


def test_get_fields_to_import_from_list_of_attributes_List_two_StringField_and_two_BooleanField():
    collector = set_up()
    list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
    complex_attributes_list = list(filter(lambda x: "String" in x.name or "Boolean" in x.name, list_of_attributes))

    list_of_fields = get_fields_to_import_from_list_of_attributes(collector, complex_attributes_list,
                                                                  valid_uri_and_types={})
    assert list_of_fields == ['BooleanField', 'StringField']


def test_get_white_space_equivalent_empty_string():
    result = get_white_space_equivalent('')
    assert result == ''


def test_get_white_space_equivalent_string_of_1_length():
    result = get_white_space_equivalent('a')
    assert result == ' '


def test_get_white_space_equivalent_string_of_2_length():
    result = get_white_space_equivalent('aa')
    assert result == '  '


def test_add_attributen_to_dataBlock_StringField():
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
                          '    def huisnummer(self) -> str:',
                          '        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""',
                          '        return self._huisnummer.get_waarde()',
                          '',
                          '    @huisnummer.setter',
                          '    def huisnummer(self, value):',
                          '        self._huisnummer.set_waarde(value, owner=self._parent)',
                          '']

    assert add_attributen_to_data_block([attribuut], [], valid_uri_and_types={}) == expected_datablock


def test_add_attributen_to_dataBlock_DteField():
    attribuut = OSLOAttribuut('toestandBuis', 'toestand buis', 'Opmerkingen van de toestand en staat van de buis.',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok', 0,
                              '', 0, '', '')

    expected_datablock = ['        self._toestandBuis = OTLAttribuut(field=DteTekstblok,',
                          "                                          naam='toestandBuis',",
                          "                                          label='toestand buis',",
                          "                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',",
                          "                                          definition='Opmerkingen van de toestand en staat van de buis.',",
                          "                                          owner=self)",
                          '',
                          '    @property',
                          '    def toestandBuis(self) -> DteTekstblokWaarden:',
                          '        """Opmerkingen van de toestand en staat van de buis."""',
                          '        return self._toestandBuis.get_waarde()',
                          '',
                          '    @toestandBuis.setter',
                          '    def toestandBuis(self, value):',
                          '        self._toestandBuis.set_waarde(value, owner=self._parent)',
                          '']

    assert add_attributen_to_data_block([attribuut], [], valid_uri_and_types={}) == expected_datablock


def test_add_attributen_to_dataBlock_KwantWrd():
    attribuut = OSLOAttribuut('lengte', 'lengte',
                              'De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter',
                              0, '', 0, '', '')

    expected_datablock = ['        self._lengte = OTLAttribuut(field=KwantWrdInMeter,',
                          "                                    naam='lengte',",
                          "                                    label='lengte',",
                          "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',",
                          "                                    definition='De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',",
                          "                                    owner=self)",
                          '',
                          '    @property',
                          '    def lengte(self) -> KwantWrdInMeterWaarden:',
                          '        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""',
                          '        return self._lengte.get_waarde()',
                          '',
                          '    @lengte.setter',
                          '    def lengte(self, value):',
                          '        self._lengte.set_waarde(value, owner=self._parent)',
                          '']

    assert add_attributen_to_data_block([attribuut], [], valid_uri_and_types={}) == expected_datablock


def test_add_attributen_to_data_block_DtcAdres():
    attribuut = OSLODatatypeComplexAttribuut('adres', 'adres', 'Adres dat men kan aanschrijven of bezoeken.',
                                             'https://schema.org/ContactPoint', '0', '1',
                                             'https://schema.org/ContactPoint.adres',
                                             'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                             0, '', 0, '', '')

    expected_datablock = ['        self._adres = OTLAttribuut(field=DtcAdres,',
                          "                                   naam='adres',",
                          "                                   label='adres',",
                          "                                   objectUri='https://schema.org/ContactPoint.adres',",
                          "                                   kardinaliteit_min='0',",
                          "                                   definition='Adres dat men kan aanschrijven of bezoeken.',",
                          "                                   owner=self)",
                          '',
                          '    @property',
                          '    def adres(self) -> DtcAdresWaarden:',
                          '        """Adres dat men kan aanschrijven of bezoeken."""',
                          '        return self._adres.get_waarde()',
                          '',
                          '    @adres.setter',
                          '    def adres(self, value):',
                          '        self._adres.set_waarde(value, owner=self._parent)',
                          '']

    assert add_attributen_to_data_block([attribuut], [], valid_uri_and_types={}) == expected_datablock


@skip('change the write_file test')  # TODO change this test
def test_WriteToFileContainerBuis():
    collector, creator = set_up_real_collector_and_creator()
    container_buis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
    data_to_write = creator.create_blocks_to_write_from_classes(container_buis)
    write_to_file(container_buis, 'Classes', data_to_write, '../../src/OTLMOW/')

    file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Classes/ContainerBuis.py'))
    assert os.path.isfile(file_location)
