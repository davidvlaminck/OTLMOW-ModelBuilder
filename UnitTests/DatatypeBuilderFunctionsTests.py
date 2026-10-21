import os
import pytest

from pathlib import Path
from otlmow_modelbuilder.DatatypeBuilderFunctions import (
    get_single_field_from_type_uri,
    get_non_single_field_from_type_uri,
    get_type_name_of_complex_attribuut,
    get_type_name_of_union_attribuut,
    get_field_name_from_type_uri,
    get_field_name_by_type_uri,
)
from otlmow_modelbuilder.GenericBuilderFunctions import (
    get_fields_to_import_from_list_of_attributes,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    get_single_field_from_type_uri as rust_get_single_field_from_type_uri,
    get_non_single_field_from_type_uri as rust_get_non_single_field_from_type_uri,
    get_type_name_of_complex_attribuut as rust_get_type_name_of_complex_attribuut,
    get_type_name_of_union_attribuut as rust_get_type_name_of_union_attribuut,
    get_field_name_from_type_uri as rust_get_field_name_from_type_uri,
    get_field_name_by_type_uri as rust_get_field_name_by_type_uri,
    get_fields_to_import_from_list_of_attributes as rust_get_fields_to_import_from_list_of_attributes,
)
from otlmow_modelbuilder.OSLOCollector import OSLOCollector


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def collector_type_links(collector: OSLOCollector):
    return [(t.item_uri, t.item_tabel) for t in collector.typeLinks]


def collector_enumerations(collector: OSLOCollector):
    return [(e.objectUri, e.name) for e in collector.enumerations]


def collector_complex_datatypes(collector: OSLOCollector):
    return [(c.objectUri, c.name) for c in collector.complex_datatypes]


def collector_union_datatypes(collector: OSLOCollector):
    return [(u.objectUri, u.name) for u in collector.union_datatypes]


class TestGetSingleFieldFromTypeUri:
    @pytest.mark.parametrize("field_type, expected", [
        ("http://www.w3.org/2001/XMLSchema#decimal", "FloatOrDecimalField"),
        ("http://www.w3.org/2001/XMLSchema#string", "StringField"),
        ("http://www.w3.org/1999/02/22-rdf-syntax-ns#langString", "StringField"),
        ("http://www.w3.org/2001/XMLSchema#boolean", "BooleanField"),
        ("http://www.w3.org/2001/XMLSchema#integer", "IntegerField"),
        ("http://www.w3.org/2001/XMLSchema#nonNegativeInteger", "NonNegIntegerField"),
        ("http://www.w3.org/2001/XMLSchema#date", "DateField"),
        ("http://www.w3.org/2001/XMLSchema#dateTime", "DateTimeField"),
        ("http://www.w3.org/2001/XMLSchema#time", "TimeField"),
        ("http://www.w3.org/2001/XMLSchema#anyURI", "URIField"),
        ("https://schema.org/OpeningHoursSpecification", "DtcOpeningsurenSpecificatie"),
        ("https://schema.org/ContactPoint", "DtcContactinfo"),
        ("http://www.w3.org/2000/01/rdf-schema#Literal", "StringField"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DteTestEenvoudigType", "DteTestEenvoudigType"),
    ])
    def test_matches_python(self, field_type, expected):
        assert rust_get_single_field_from_type_uri(field_type) == get_single_field_from_type_uri(field_type)
        assert rust_get_single_field_from_type_uri(field_type) == expected


class TestGetNonSingleFieldFromTypeUri:
    @pytest.mark.parametrize("field_type, expected", [
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType", ["ComplexField", "DtcTestComplexType"]),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DteTestEenvoudigType", ["ComplexField", "DteTestEenvoudigType"]),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#KwantWrdTest", ["ComplexField", "KwantWrdTest"]),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtuTestUnionType", ["UnionTypeField", "DtuTestUnionType"]),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#KlTestKeuzelijst", ["KeuzelijstField", "KlTestKeuzelijst"]),
    ])
    def test_matches_python(self, field_type, expected):
        assert rust_get_non_single_field_from_type_uri(field_type, []) == get_non_single_field_from_type_uri(field_type, {})
        assert rust_get_non_single_field_from_type_uri(field_type, []) == expected

    def test_valid_uri_and_types(self):
        field_type = "https://example.com/ns/test#CustomType"
        valid_uri_and_types = [(field_type, "CustomType")]
        assert rust_get_non_single_field_from_type_uri(field_type, valid_uri_and_types) == \
               get_non_single_field_from_type_uri(field_type, {field_type: "CustomType"})


class TestGetTypeNameOfComplexAttribuut:
    @pytest.mark.parametrize("type_uri, expected", [
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType2", "DtcTestComplexType2"),
        ("http://www.w3.org/2001/XMLSchema#string", "string"),
    ])
    def test_matches_python(self, type_uri, expected):
        assert rust_get_type_name_of_complex_attribuut(type_uri, []) == \
               get_type_name_of_complex_attribuut(type_uri, {})
        assert rust_get_type_name_of_complex_attribuut(type_uri, []) == expected

    def test_valid_uri_and_types(self):
        type_uri = "https://example.com/ns/test#CustomType"
        valid_uri_and_types = [(type_uri, "MappedName")]
        assert rust_get_type_name_of_complex_attribuut(type_uri, valid_uri_and_types) == \
               get_type_name_of_complex_attribuut(type_uri, {type_uri: "MappedName"})
        assert rust_get_type_name_of_complex_attribuut(type_uri, valid_uri_and_types) == "MappedName"


class TestGetTypeNameOfUnionAttribuut:
    @pytest.mark.parametrize("type_uri, expected", [
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtuTestUnionType", "DtuTestUnionType"),
    ])
    def test_matches_python(self, type_uri, expected):
        assert rust_get_type_name_of_union_attribuut(type_uri) == get_type_name_of_union_attribuut(type_uri)
        assert rust_get_type_name_of_union_attribuut(type_uri) == expected


class TestGetFieldNameFromTypeUri:
    @pytest.mark.parametrize("attribuut_type, expected", [
        ("http://www.w3.org/2001/XMLSchema#string", "StringField"),
        ("http://www.w3.org/2001/XMLSchema#boolean", "BooleanField"),
        ("http://www.w3.org/2001/XMLSchema#integer", "IntegerField"),
        ("http://www.w3.org/2001/XMLSchema#decimal", "FloatOrDecimalField"),
        ("http://www.w3.org/2001/XMLSchema#date", "DateField"),
        ("http://www.w3.org/2001/XMLSchema#dateTime", "DateTimeField"),
        ("http://www.w3.org/2001/XMLSchema#time", "TimeField"),
        ("http://www.w3.org/2001/XMLSchema#anyURI", "URIField"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType", "DtcTestComplexType"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DteTestEenvoudigType", "DteTestEenvoudigType"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#KwantWrdTest", "KwantWrdTest"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtuTestUnionType", "DtuTestUnionType"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#KlTestKeuzelijst", "KlTestKeuzelijst"),
    ])
    def test_matches_python(self, attribuut_type, expected):
        assert rust_get_field_name_from_type_uri(attribuut_type, []) == \
               get_field_name_from_type_uri(attribuut_type, {})
        assert rust_get_field_name_from_type_uri(attribuut_type, []) == expected


class TestGetFieldNameByTypeUri:
    def test_matches_python_with_real_data(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)
        enumerations_data = collector_enumerations(collector)
        complex_data = collector_complex_datatypes(collector)
        union_data = collector_union_datatypes(collector)

        type_uris = []
        for attr in collector.complex_datatype_attributen:
            if attr.type and attr.type.split('#')[0] not in ('http://www.w3.org/2001/XMLSchema',):
                type_uris.append(attr.type)
        for attr in collector.primitive_datatype_attributen:
            type_uris.append(attr.type)
        for attr in collector.union_datatype_attributen:
            type_uris.append(attr.type)

        distinct_uris = sorted(set(type_uris))

        for type_uri in distinct_uris:
            py_result = get_field_name_by_type_uri(collector, type_uri)
            rust_result = rust_get_field_name_by_type_uri(
                type_uri, type_links_data, enumerations_data, complex_data, union_data
            )
            assert rust_result == py_result, (
                f"Mismatch for {type_uri}: Rust='{rust_result}' vs Python='{py_result}'"
            )

    def test_xsd_types(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)
        enumerations_data = collector_enumerations(collector)
        complex_data = collector_complex_datatypes(collector)
        union_data = collector_union_datatypes(collector)

        type_uris = [
            "http://www.w3.org/2001/XMLSchema#string",
            "http://www.w3.org/2001/XMLSchema#boolean",
            "http://www.w3.org/2001/XMLSchema#integer",
            "http://www.w3.org/2001/XMLSchema#decimal",
            "http://www.w3.org/2001/XMLSchema#date",
            "http://www.w3.org/2001/XMLSchema#dateTime",
            "http://www.w3.org/2001/XMLSchema#time",
            "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
            "http://www.w3.org/2001/XMLSchema#anyURI",
        ]
        for type_uri in type_uris:
            py_result = get_field_name_by_type_uri(collector, type_uri)
            rust_result = rust_get_field_name_by_type_uri(
                type_uri, type_links_data, enumerations_data, complex_data, union_data
            )
            assert rust_result == py_result, (
                f"Mismatch for {type_uri}: Rust='{rust_result}' vs Python='{py_result}'"
            )


class TestGetFieldsToImportFromListOfAttributes:
    def test_matches_python_complex_dtype_attrs(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            "https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType2")
        attribute_types = [a.type for a in attrs]

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, attrs, valid_uri_and_types={})
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            attribute_types, type_links_data, [], [])
        assert rust_result == py_result

    def test_matches_python_with_start_list(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            "https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType2")
        attribute_types = [a.type for a in attrs]

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, attrs, valid_uri_and_types={}, list_to_start_from=["BooleanField"])
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            attribute_types, type_links_data, [], ["BooleanField"])
        assert rust_result == py_result

    def test_matches_python_dtc_test_complex_type(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            "https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType")
        attribute_types = [a.type for a in attrs]

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, attrs, valid_uri_and_types={})
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            attribute_types, type_links_data, [], [])
        assert rust_result == py_result

    def test_matches_python_empty_attributes(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, [], valid_uri_and_types={})
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            [], type_links_data, [], [])
        assert rust_result == py_result

    def test_matches_python_primitive_dtype_attrs(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        attrs = collector.find_primitive_datatype_attributes_by_class_uri(
            "https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DteTestEenvoudigType")
        attribute_types = [a.type for a in attrs]

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, attrs, valid_uri_and_types={})
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            attribute_types, type_links_data, [], [])
        assert rust_result == py_result

    def test_matches_python_union_dtype_attrs(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        attrs = collector.find_union_datatype_attributes_by_class_uri(
            "https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtuTestUnionType")
        attribute_types = [a.type for a in attrs]

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, attrs, valid_uri_and_types={})
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            attribute_types, type_links_data, [], [])
        assert rust_result == py_result

    def test_matches_python_with_valid_uri_and_types(self):
        collector = set_up()
        type_links_data = collector_type_links(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            "https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement#DtcTestComplexType")
        attribute_types = [a.type for a in attrs]

        valid_uri_and_types = {"https://schema.org/ContactPoint": "DtcContactinfo"}
        valid_uri_and_types_data = list(valid_uri_and_types.items())

        py_result = get_fields_to_import_from_list_of_attributes(
            collector, attrs, valid_uri_and_types=valid_uri_and_types)
        rust_result = rust_get_fields_to_import_from_list_of_attributes(
            attribute_types, type_links_data, valid_uri_and_types_data, [])
        assert rust_result == py_result
