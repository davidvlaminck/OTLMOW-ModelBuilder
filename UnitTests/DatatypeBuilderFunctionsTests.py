import os
import unittest
from pathlib import Path

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_non_single_field_from_type_uri, \
    get_type_name_of_complex_attribuut, get_type_link_from_attribuut, get_fields_and_names_from_list_of_attributes
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class DatatypeBuilderFunctionsTests(unittest.TestCase):
    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_get_non_single_field_from_type_uri_ComplexField(self):
        types_list = get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        expected_list = ['ComplexField', 'DtcTestComplexType']

        self.assertEqual(expected_list, types_list)

    def test_get_non_single_field_from_type_uri_DteField(self):
        types_list = get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType')
        expected_list = ['ComplexField', 'DteTestEenvoudigType']

        self.assertEqual(expected_list, types_list)

    def test_get_non_single_field_from_type_uri_KwantWrdField(self):
        types_list = get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest')
        expected_list = ['ComplexField', 'KwantWrdTest']

        self.assertEqual(expected_list, types_list)

    def test_getNonPrimitiveFieldFromTypeUri_UnionTypeField(self):
        types_list = get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType')
        expected_list = ['UnionTypeField', 'DtuTestUnionType']

        self.assertEqual(expected_list, types_list)

    def test_get_non_single_field_from_type_uri_Keuzelijst(self):
        types_list = get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTestKeuzelijst')
        expected_list = ['KeuzelijstField', 'KlTestKeuzelijst']

        self.assertEqual(expected_list, types_list)

    def test_get_type_name_of_complex_attribute_String(self):
        collector = self.setUp()
        dtcIdentificator = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
        type_name = get_type_name_of_complex_attribuut(dtcIdentificator[0].type)
        self.assertEqual("string", type_name)

    def test_get_type_link_from_attribuut_Boolean(self):
        collector = self.setUp()
        attribute = next(c for c in collector.complex_datatype_attributen if c.type == 'http://www.w3.org/2001/XMLSchema#boolean')

        type_link = get_type_link_from_attribuut(collector, attribute)
        self.assertEqual("OSLODatatypePrimitive", type_link.item_tabel)

    def test_get_type_link_from_attribuut_DtcTestComplexType2(self):
        collector = self.setUp()
        attribute = next(c for c in collector.complex_datatype_attributen if c.type == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        type_link = get_type_link_from_attribuut(collector, attribute)
        self.assertEqual("OSLODatatypeComplex", type_link.item_tabel)

    def test_get_fields_and_names_from_list_of_attributes(self):
        collector = self.setUp()
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: x.name in ['testStringField', 'testBooleanField', 'testComplexType2'], list_of_attributes))

        list_of_fields = get_fields_and_names_from_list_of_attributes(complex_attributes_list)
        self.assertEqual([('BooleanField', 'testBooleanField'), ('DtcTestComplexType2', 'testComplexType2'), ('StringField', 'testStringField')], list_of_fields)


