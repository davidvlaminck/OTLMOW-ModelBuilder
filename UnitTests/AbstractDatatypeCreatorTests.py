import os
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.DatatypeBuilderFunctions import get_non_single_field_from_type_uri
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class AbstractDatatypeCreatorTests(unittest.TestCase):
    #TODO add tests for writing a file

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
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(list_of_attributes, ['BooleanField'])

        self.assertEqual(['BooleanField', 'KwantWrdTest', 'StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Empty_start_list(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(list_of_attributes)

        self.assertEqual(['KwantWrdTest', 'StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_with_ComplexType(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "Complex" in x.name, list_of_attributes))

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(complex_attributes_list)

        self.assertEqual(['DtcTestComplexType2'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_two_StringField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "String" in x.name, list_of_attributes))

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(complex_attributes_list)

        self.assertEqual(['StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_two_StringField_and_two_BooleanField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "String" in x.name or "Boolean" in x.name, list_of_attributes))

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(complex_attributes_list)

        self.assertEqual(['BooleanField', 'StringField'], list_of_fields)

    def test_get_fields_and_names_from_list_of_attributes(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: x.name in ['testStringField', 'testBooleanField', 'testComplexType2'], list_of_attributes))

        list_of_fields = creator.get_fields_and_names_from_list_of_attributes(complex_attributes_list)
        self.assertEqual([('BooleanField', 'testBooleanField'), ('DtcTestComplexType2', 'testComplexType2'), ('StringField', 'testStringField')], list_of_fields)

    def test_get_type_link_from_attribuut_Boolean(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        attribute = next(c for c in collector.complex_datatype_attributen if c.type == 'http://www.w3.org/2001/XMLSchema#boolean')

        typeLink = creator.get_type_link_from_attribuut(attribute)
        self.assertEqual("OSLODatatypePrimitive", typeLink.item_tabel)

    def test_get_type_link_from_attribuut_DtcTestComplexType2(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        attribute = next(c for c in collector.complex_datatype_attributen if c.type == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        typeLink = creator.get_type_link_from_attribuut(attribute)
        self.assertEqual("OSLODatatypeComplex", typeLink.item_tabel)



