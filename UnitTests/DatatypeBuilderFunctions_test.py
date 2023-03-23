import os
from pathlib import Path

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_non_single_field_from_type_uri, \
    get_type_name_of_complex_attribuut, get_type_link_from_attribuut, get_fields_and_names_from_list_of_attributes
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    sql_reader = SQLDbReader(file_location)
    oslo_creator = OSLOInMemoryCreator(sql_reader)
    collector = OSLOCollector(oslo_creator)
    collector.collect()
    return collector


def test_get_non_single_field_from_type_uri_ComplexField():
    types_list = get_non_single_field_from_type_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType',
        valid_uri_and_types={})
    expected_list = ['ComplexField', 'DtcTestComplexType']

    assert types_list == expected_list


def test_get_non_single_field_from_type_uri_DteField():
    types_list = get_non_single_field_from_type_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType',
        valid_uri_and_types={})
    expected_list = ['ComplexField', 'DteTestEenvoudigType']

    assert types_list == expected_list


def test_get_non_single_field_from_type_uri_KwantWrdField():
    types_list = get_non_single_field_from_type_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest', valid_uri_and_types={})
    expected_list = ['ComplexField', 'KwantWrdTest']

    assert types_list == expected_list


def test_getNonPrimitiveFieldFromTypeUri_UnionTypeField():
    types_list = get_non_single_field_from_type_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType', valid_uri_and_types={})
    expected_list = ['UnionTypeField', 'DtuTestUnionType']

    assert types_list == expected_list


def test_get_non_single_field_from_type_uri_Keuzelijst():
    types_list = get_non_single_field_from_type_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTestKeuzelijst',
        valid_uri_and_types={})
    expected_list = ['KeuzelijstField', 'KlTestKeuzelijst']

    assert types_list == expected_list


def test_get_type_name_of_complex_attribute_String():
    collector = set_up()
    dtcIdentificator = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
    type_name = get_type_name_of_complex_attribuut(dtcIdentificator[0].type, valid_uri_and_types={})
    assert type_name == 'string'


def test_get_type_link_from_attribuut_Boolean():
    collector = set_up()
    attribute = next(
        c for c in collector.complex_datatype_attributen if c.type == 'http://www.w3.org/2001/XMLSchema#boolean')

    type_link = get_type_link_from_attribuut(collector, attribute)
    assert type_link.item_tabel == 'OSLODatatypePrimitive'


def test_get_type_link_from_attribuut_DtcTestComplexType2():
    collector = set_up()
    attribute = next(c for c in collector.complex_datatype_attributen if
                     c.type == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

    type_link = get_type_link_from_attribuut(collector, attribute)
    assert type_link.item_tabel == 'OSLODatatypeComplex'


def test_get_fields_and_names_from_list_of_attributes():
    collector = set_up()
    list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
    complex_attributes_list = list(
        filter(lambda x: x.name in ['testStringField', 'testBooleanField', 'testComplexType2'], list_of_attributes))

    list_of_fields = get_fields_and_names_from_list_of_attributes(complex_attributes_list, valid_uri_and_types={})
    assert list_of_fields == [('BooleanField', 'testBooleanField'),
                              ('DtcTestComplexType2', 'testComplexType2'),
                              ('StringField', 'testStringField')]
