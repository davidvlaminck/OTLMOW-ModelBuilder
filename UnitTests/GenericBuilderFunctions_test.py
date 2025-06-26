import os
from pathlib import Path
from unittest import skip

from UnitTests.OTLClassCreator_test import set_up_real_collector_and_creator
from otlmow_modelbuilder.GenericBuilderFunctions import get_white_space_equivalent, add_attributen_to_data_block, \
    get_fields_to_import_from_list_of_attributes, write_to_file
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut

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
    collector = set_up()
    attribuut = OSLODatatypeComplexAttribuut('testStringField','Test StringField','Test attribuut voor StringField','https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass','1','1','https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField','http://www.w3.org/2001/XMLSchema#string',0,'',0,'','')

    expected_datablock = [
        '        self._testStringField = OTLAttribuut(field=StringField,',
        "                                             naam='testStringField',",
        "                                             label='Test StringField',",
        '                                             '
        "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField',",
        "                                             definition='Test attribuut voor "
        "StringField',",
        '                                             owner=self)',
        '',
        '    @property',
        '    def testStringField(self) -> str:',
        '        """Test attribuut voor StringField"""',
        '        return self._testStringField.get_waarde()',
        '',
        '    @testStringField.setter',
        '    def testStringField(self, value):',
        '        self._testStringField.set_waarde(value, owner=self._parent)',
        '']

    assert add_attributen_to_data_block(collector,[attribuut], [], valid_uri_and_types={}) == expected_datablock


def test_add_attributen_to_dataBlock_DteField():
    collector = set_up()
    attribuut = OSLOAttribuut('testEenvoudigType','Test EenvoudigType','Test attribuut voor een eenvoudige waarde','https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass','1','1','https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType',0,'',0,'','')

    expected_datablock = [
        '        self._testEenvoudigType = OTLAttribuut(field=DteTestEenvoudigType,',
        "                                               naam='testEenvoudigType',",
        "                                               label='Test EenvoudigType',",
        '                                               '
        "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType',",
        "                                               definition='Test attribuut "
        "voor een eenvoudige waarde',",
        '                                               owner=self)',
        '',
        '    @property',
        '    def testEenvoudigType(self) -> DteTestEenvoudigTypeWaarden:',
        '        """Test attribuut voor een eenvoudige waarde"""',
        '        return self._testEenvoudigType.get_waarde()',
        '',
        '    @testEenvoudigType.setter',
        '    def testEenvoudigType(self, value):',
        '        self._testEenvoudigType.set_waarde(value, owner=self._parent)',
        '']

    assert add_attributen_to_data_block(collector, [attribuut], [], valid_uri_and_types={}) == expected_datablock


def test_add_attributen_to_dataBlock_KwantWrd():
    collector = set_up()
    attribuut = OSLOAttribuut('testKwantWrd','Test KwantWrd','Test attribuut voor een kwantitatieve waarde','https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass','1','1','https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest',0,'',0,'','')

    expected_datablock = [
        '        self._testKwantWrd = OTLAttribuut(field=KwantWrdTest,',
        "                                          naam='testKwantWrd',",
        "                                          label='Test KwantWrd',",
        '                                          '
        "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd',",
        "                                          definition='Test attribuut voor "
        "een kwantitatieve waarde',",
        '                                          owner=self)',
        '',
        '    @property',
        '    def testKwantWrd(self) -> KwantWrdTestWaarden:',
        '        """Test attribuut voor een kwantitatieve waarde"""',
        '        return self._testKwantWrd.get_waarde()',
        '',
        '    @testKwantWrd.setter',
        '    def testKwantWrd(self, value):',
        '        self._testKwantWrd.set_waarde(value, owner=self._parent)',
        '']

    assert add_attributen_to_data_block(collector, [attribuut], [], valid_uri_and_types={}) == expected_datablock


def test_add_attributen_to_data_block_DtcAdres():
    collector = set_up()
    attribuut = OSLODatatypeComplexAttribuut('assetId','asset-id','Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject','1','1','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',0,'',0,'','')

    expected_datablock = [
        '        self._assetId = OTLAttribuut(field=DtcIdentificator,',
        "                                     naam='assetId',",
        "                                     label='asset-id',",
        '                                     '
        "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId',",
        "                                     definition='Unieke identificatie van de "
        'asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering '
        "door de leverancier.',",
        '                                     owner=self)',
        '',
        '    @property',
        '    def assetId(self) -> DtcIdentificatorWaarden:',
        '        """Unieke identificatie van de asset zoals toegekend door de '
        'assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""',
        '        return self._assetId.get_waarde()',
        '',
        '    @assetId.setter',
        '    def assetId(self, value):',
        '        self._assetId.set_waarde(value, owner=self._parent)',
        '']

    assert add_attributen_to_data_block(collector, [attribuut], [], valid_uri_and_types={}) == expected_datablock


@skip('change the write_file test')  # TODO change this test
def test_WriteToFileContainerBuis():
    collector, creator = set_up_real_collector_and_creator()
    container_buis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
    data_to_write = creator.create_blocks_to_write_from_classes(container_buis)
    write_to_file(container_buis.name, 'Classes', data_to_write, '../../src/OTLMOW/')

    file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Classes/ContainerBuis.py'))
    assert os.path.isfile(file_location)
