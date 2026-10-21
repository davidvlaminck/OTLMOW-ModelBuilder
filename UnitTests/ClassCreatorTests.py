import os
from pathlib import Path

import pytest

from otlmow_modelbuilder._otlmow_modelbuilder_rs import create_block_from_class as rust_create_block
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator


CURRENT_DIR = Path(__file__).parent


def set_up() -> OSLOCollector:
    file_location = CURRENT_DIR / 'OTL_AllCasesTestClass.db'
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def extract_inheritance(i):
    return (i.base_name, i.base_uri, i.class_name, i.class_uri, i.deprecated_version)


def extract_relation(r):
    return (r.bron_uri, r.doel_uri, r.objectUri, r.richting, r.deprecated_version)


class_validation_rules = {
    "valid_uri_and_types": {},
    "valid_regexes": ["^https://wegenenverkeer.data.vlaanderen.be/ns/.+#.+"]
}


class TestCreateBlockClassComparison:
    def test_all_cases_test_class_matches_python(self):
        collector = set_up()
        creator = OTLClassCreator(collector)
        oslo_class = collector.find_class_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass')

        type_links_data = [(t.item_uri, t.item_tabel) for t in collector.typeLinks]
        enumerations_data = [(e.objectUri, e.name) for e in collector.enumerations]
        complex_datatypes_data = [(c.objectUri, c.name) for c in collector.complex_datatypes]
        union_datatypes_data = [(u.objectUri, u.name) for u in collector.union_datatypes]

        inheritance_map = collector.get_inheritance_map()
        inh_map_for_class = inheritance_map.get(oslo_class.objectUri, [])

        geo_geometry_types = creator.get_geometry_types_from_uri(oslo_class.objectUri)

        relations = collector.find_all_relations(oslo_class.objectUri, allow_duplicates=False)
        inheritances = collector.find_inheritances_by_class(oslo_class)
        attributen = collector.find_attributes_by_class(oslo_class)

        python_result = creator.create_block_from_class(
            oslo_class,
            model_location='',
            valid_uri_and_types={})

        rust_result = rust_create_block(
            [a for a in attributen],
            [extract_inheritance(i) for i in inheritances],
            [extract_relation(r) for r in relations],
            [],
            type_links_data,
            enumerations_data,
            complex_datatypes_data,
            union_datatypes_data,
            inh_map_for_class,
            geo_geometry_types,
            oslo_class.name,
            oslo_class.definition,
            oslo_class.objectUri,
            oslo_class.abstract,
            oslo_class.deprecated_version,
            "OTLClassCreator")

        assert rust_result == python_result

    def test_container_buis_matches_python(self):
        collector = set_up()

        # ContainerBuis is abstract with no inheritances, but has geometry types
        # It inherits from nothing but uses ABC base class
        oslo_class = collector.find_class_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie')

        type_links_data = [(t.item_uri, t.item_tabel) for t in collector.typeLinks]
        enumerations_data = [(e.objectUri, e.name) for e in collector.enumerations]
        complex_datatypes_data = [(c.objectUri, c.name) for c in collector.complex_datatypes]
        union_datatypes_data = [(u.objectUri, u.name) for u in collector.union_datatypes]

        inheritance_map = collector.get_inheritance_map()
        inh_map_for_class = inheritance_map.get(oslo_class.objectUri, [])

        inheritances = collector.find_inheritances_by_class(oslo_class)
        attributen = collector.find_attributes_by_class(oslo_class)
        relations = collector.find_all_relations(oslo_class.objectUri, allow_duplicates=False)

        python_creator = OTLClassCreator(collector)
        python_result = python_creator.create_block_from_class(
            oslo_class,
            model_location='',
            valid_uri_and_types={})

        rust_result = rust_create_block(
            [a for a in attributen],
            [extract_inheritance(i) for i in inheritances],
            [extract_relation(r) for r in relations],
            [],
            type_links_data,
            enumerations_data,
            complex_datatypes_data,
            union_datatypes_data,
            inh_map_for_class,
            [],
            oslo_class.name,
            oslo_class.definition,
            oslo_class.objectUri,
            oslo_class.abstract,
            oslo_class.deprecated_version,
            "OTLClassCreator")

        assert rust_result == python_result
