import os
import unittest
from pathlib import Path

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_non_single_field_from_type_uri, \
    get_type_name_of_complex_attribuut
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