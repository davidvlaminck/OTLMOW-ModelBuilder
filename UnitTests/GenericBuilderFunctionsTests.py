import os
from pathlib import Path

from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    add_attributen_to_data_block as rust_add_attributen_to_data_block,
)

from otlmow_modelbuilder.GenericBuilderFunctions import add_attributen_to_data_block
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import (
    OSLODatatypeComplexAttribuut,
)


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def extract_lookup_data(collector: OSLOCollector):
    type_links_data = [(t.item_uri, t.item_tabel) for t in collector.typeLinks]
    enumerations_data = [(e.objectUri, e.name) for e in collector.enumerations]
    complex_datatypes_data = [(c.objectUri, c.name) for c in collector.complex_datatypes]
    union_datatypes_data = [(u.objectUri, u.name) for u in collector.union_datatypes]
    return type_links_data, enumerations_data, complex_datatypes_data, union_datatypes_data


class TestAddAttributenToDataBlockComparison:
    def test_string_field_matches_python(self):
        collector = set_up()
        attribuut = OSLODatatypeComplexAttribuut(
            'testStringField', 'Test StringField', 'Test attribuut voor StringField',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            '1', '1',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField',
            'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        py_result = add_attributen_to_data_block(
            collector, [attribuut], [], valid_uri_and_types={})
        rust_result = rust_add_attributen_to_data_block(
            [attribuut], [], [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_dtEenvoudig_type_matches_python(self):
        collector = set_up()
        attribuut = OSLOAttribuut(
            'testEenvoudigType', 'Test EenvoudigType', 'Test attribuut voor een eenvoudige waarde',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            '1', '1',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType',
            0, '', 0, '', '')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        py_result = add_attributen_to_data_block(
            collector, [attribuut], [], valid_uri_and_types={})
        rust_result = rust_add_attributen_to_data_block(
            [attribuut], [], [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_kwantt_wrd_matches_python(self):
        collector = set_up()
        attribuut = OSLOAttribuut(
            'testKwantWrd', 'Test KwantWrd', 'Test attribuut voor een kwantitatieve waarde',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            '1', '1',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest',
            0, '', 0, '', '')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        py_result = add_attributen_to_data_block(
            collector, [attribuut], [], valid_uri_and_types={}, type_field='KwantWrd')
        rust_result = rust_add_attributen_to_data_block(
            [attribuut], [], [], type_links, enums, complexes, unions, False, 'KwantWrd')
        assert rust_result == py_result

    def test_dtc_adres_matches_python(self):
        collector = set_up()
        attribuut = OSLODatatypeComplexAttribuut(
            'assetId', 'asset-id',
            'Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
            '1', '1',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
            0, '', 0, '', '')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        py_result = add_attributen_to_data_block(
            collector, [attribuut], [], valid_uri_and_types={})
        rust_result = rust_add_attributen_to_data_block(
            [attribuut], [], [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_multiple_attributes_sorted(self):
        collector = set_up()
        type_links, enums, complexes, unions = extract_lookup_data(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')

        py_result = add_attributen_to_data_block(
            collector, attrs, [], valid_uri_and_types={})
        rust_result = rust_add_attributen_to_data_block(
            attrs, [], [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_complex_datatype_type2(self):
        collector = set_up()
        type_links, enums, complexes, unions = extract_lookup_data(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        py_result = add_attributen_to_data_block(
            collector, attrs, [], valid_uri_and_types={})
        rust_result = rust_add_attributen_to_data_block(
            attrs, [], [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_with_for_class_use(self):
        collector = set_up()
        type_links, enums, complexes, unions = extract_lookup_data(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        py_result = add_attributen_to_data_block(
            collector, attrs, [], valid_uri_and_types={}, for_class_use=True)
        rust_result = rust_add_attributen_to_data_block(
            attrs, [], [], type_links, enums, complexes, unions, True, "")
        assert rust_result == py_result

    def test_with_preexisting_datablock(self):
        collector = set_up()
        type_links, enums, complexes, unions = extract_lookup_data(collector)

        attribuut = OSLODatatypeComplexAttribuut(
            'testStringField', 'Test StringField', 'Test attribuut voor StringField',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            '1', '1',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField',
            'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')

        preexisting = ['# coding=utf-8', 'from ...BaseClasses.OTLObject import OTLAttribuut']

        py_result = add_attributen_to_data_block(
            collector, [attribuut], list(preexisting), valid_uri_and_types={})
        rust_result = rust_add_attributen_to_data_block(
            [attribuut], preexisting, [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_with_valid_uri_and_types(self):
        collector = set_up()
        type_links, enums, complexes, unions = extract_lookup_data(collector)

        attrs = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attrs = list(filter(lambda x: "Complex" in x.name, attrs))

        valid_uri_and_types = {}
        py_result = add_attributen_to_data_block(
            collector, complex_attrs, [], valid_uri_and_types=valid_uri_and_types)
        rust_result = rust_add_attributen_to_data_block(
            complex_attrs, [], [], type_links, enums, complexes, unions, False, "")
        assert rust_result == py_result

    def test_union_type_matches_python(self):
        collector = set_up()
        type_links, enums, complexes, unions = extract_lookup_data(collector)

        attrs = collector.find_union_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType')

        py_result = add_attributen_to_data_block(
            collector, attrs, [], valid_uri_and_types={}, type_field='UnionType')
        rust_result = rust_add_attributen_to_data_block(
            attrs, [], [], type_links, enums, complexes, unions, False, 'UnionType')
        assert rust_result == py_result
