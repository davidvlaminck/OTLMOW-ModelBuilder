import os
from pathlib import Path

import pytest

from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder._otlmow_modelbuilder_rs import create_block_to_write_from_complex_primitive_or_union_types as rust_create_block
from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator


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


class TestCreateBlockComparison:
    def test_complex_dtype_dtc_identificator_matches_python(self):
        collector = set_up()
        creator = OTLComplexDatatypeCreator(collector)
        datatype = collector.find_complex_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        python_result = creator.create_block_to_write_from_complex_types(
            datatype,
            complex_datatype_validation_rules={'valid_uri_and_types': {}, 'valid_regexes': ["^https://.*#Dtc.+"]})

        rust_result = rust_create_block(
            [extract_attribuut(a) for a in collector.find_complex_datatype_attributes_by_class_uri(datatype.objectUri)],
            [],
            type_links, enums, complexes, unions,
            "Complex", "", datatype.name, datatype.definition, datatype.label,
            datatype.objectUri, datatype.usagenote, datatype.deprecated_version,
            "OTLComplexDatatypeCreator")
        assert rust_result == python_result

    def test_primitive_dtype_dte_test_eenvoudig_matches_python(self):
        collector = set_up()
        creator = OTLPrimitiveDatatypeCreator(collector)
        datatype = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        python_result = creator.create_block_to_write_from_primitive_types(
            datatype,
            primitive_datatype_validation_rules={'valid_uri_and_types': {}, 'valid_regexes': ["^https://.*#Dte.+"]})

        rust_result = rust_create_block(
            [extract_attribuut(a) for a in collector.find_primitive_datatype_attributes_by_class_uri(datatype.objectUri)],
            [],
            type_links, enums, complexes, unions,
            "Primitive", "", datatype.name, datatype.definition, datatype.label,
            datatype.objectUri, datatype.usagenote, datatype.deprecated_version,
            "OTLPrimitiveDatatypeCreator")
        assert rust_result == python_result

    def test_kwant_wrd_matches_python(self):
        collector = set_up()
        creator = OTLPrimitiveDatatypeCreator(collector)
        datatype = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        python_result = creator.create_block_to_write_from_primitive_types(
            datatype,
            primitive_datatype_validation_rules={'valid_uri_and_types': {}, 'valid_regexes': ["^https://.*#KwantWrd.+"]})

        rust_result = rust_create_block(
            [extract_attribuut(a) for a in collector.find_primitive_datatype_attributes_by_class_uri(datatype.objectUri)],
            [],
            type_links, enums, complexes, unions,
            "KwantWrd", "", datatype.name, datatype.definition, datatype.label,
            datatype.objectUri, datatype.usagenote, datatype.deprecated_version,
            "OTLPrimitiveDatatypeCreator")
        assert rust_result == python_result

    def test_union_dtype_matches_python(self):
        collector = set_up()
        creator = OTLUnionDatatypeCreator(collector)
        datatype = collector.find_union_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType')

        type_links, enums, complexes, unions = extract_lookup_data(collector)

        python_result = creator.create_block_to_write_from_union_types(
            datatype,
            union_datatype_validation_rules={'valid_uri_and_types': {}, 'valid_regexes': ["^https://.*#Dtu.+"]})

        rust_result = rust_create_block(
            [extract_attribuut(a) for a in collector.find_union_datatype_attributes_by_class_uri(datatype.objectUri)],
            [],
            type_links, enums, complexes, unions,
            "UnionType", "", datatype.name, datatype.definition, datatype.label,
            datatype.objectUri, datatype.usagenote, datatype.deprecated_version,
            "OTLUnionDatatypeCreator")
        assert rust_result == python_result


def extract_attribuut(obj):
    return obj
