from __future__ import annotations

import concurrent.futures
import csv
import json
import logging

logger = logging.getLogger(__name__)
import os
import shutil
import subprocess
from collections import defaultdict
from concurrent.futures import FIRST_COMPLETED
from datetime import datetime
from os import path
from pathlib import Path

from tqdm import tqdm

from otlmow_modelbuilder.Exceptions.NestedListAttributeError import (
    NestedListAttributeError,
)
from otlmow_modelbuilder.GenericBuilderFunctions import write_to_file
from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.HelperFunctions import (
    get_class_directory_from_ns,
    get_ns_and_name_from_uri,
    get_titlecase_from_ns,
)
from otlmow_modelbuilder.LegacyClassCreator import LegacyClassCreator
from otlmow_modelbuilder.ModelData import EnumerationData, Lookups, ModelData
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator
from otlmow_modelbuilder.OTLExtraChecker import OTLExtraChecker
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass

CLASS_DIRECTORIES = [
    'Classes/Abstracten',
    'Classes/ImplementatieElement',
    'Classes/Installatie',
    'Classes/Legacy',
    'Classes/Levenscyclus',
    'Classes/Onderdeel',
    'Classes/ProefEnMeting',
]

PRIMITIVE_DATATYPES_TO_SKIP = (
    'http://www.w3.org/2000/01/rdf-schema#Literal',
    'http://www.w3.org/2001/XMLSchema#dateTime',
    'http://www.w3.org/2001/XMLSchema#integer',
    'http://www.w3.org/2001/XMLSchema#decimal',
    'http://www.w3.org/2001/XMLSchema#time',
    'http://www.w3.org/2001/XMLSchema#date',
    'http://www.w3.org/2001/XMLSchema#nonNegativeInteger',
    'http://www.w3.org/2001/XMLSchema#string',
    'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString',
    'http://www.w3.org/2001/XMLSchema#boolean',
    'http://www.w3.org/2001/XMLSchema#anyURI',
)

LEGACY_CLASS_NAME_ALIASES = {
    'RIS': 'RISLegacy',
    'Fietstel': 'FietstelLegacy',
    'Brug': 'BeweegbareBrug',
    'Voedingskeuzeschakelaar': 'VKS',
}

LEGACY_BASE_CLASS_NAMES = ('AIMDBStatus', 'AIMToestand', 'AIMVersie')
LEGACY_OBJECT_URI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject'
AGENT_URI = 'http://purl.org/dc/terms/Agent'
IGNORED_CLASS_LABEL = 'ignore this class when generating the model'
DEFAULT_NESTED_LIST_EXCEPTIONS = [
    'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard']


class OTLModelCreator:
    def __init__(self):
        pass

    @staticmethod
    def create_full_model(directory: Path, oslo_collector: OSLOCollector,
                          geo_artefact_collector: GeometrieArtefactCollector | None, settings: dict, include_legacy: bool,
                          environment: str = '', include_kl_test_keuzelijst: bool = False):
        """Create the model: the datatypes, the classes and the helpers of the OTL subset."""
        logger.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        OTLModelCreator._prepare_the_model(directory=directory, oslo_collector=oslo_collector, settings=settings)
        model_data = OTLModelCreator._collect_the_model_data(oslo_collector=oslo_collector, environment=environment,
                                                             settings=settings,
                                                             include_kl_test_keuzelijst=include_kl_test_keuzelijst)
        model_name = OTLModelCreator.get_model_name_from_directory_path(directory / 'OtlmowModel')

        if OTLModelCreator._use_rust():
            OTLModelCreator._create_the_model_with_rust(
                directory=directory, oslo_collector=oslo_collector, geo_artefact_collector=geo_artefact_collector,
                settings=settings, model_name=model_name, model_data=model_data, environment=environment,
                include_kl_test_keuzelijst=include_kl_test_keuzelijst)
        else:
            OTLModelCreator._create_the_model_with_python(
                directory=directory, oslo_collector=oslo_collector, geo_artefact_collector=geo_artefact_collector,
                settings=settings, class_validation_rules=model_data.class_validation_rules, environment=environment,
                include_kl_test_keuzelijst=include_kl_test_keuzelijst)

        if include_legacy:
            oslo_collector = OTLModelCreator.create_legacy_classes(oslo_collector=oslo_collector,
                directory=directory / 'OtlmowModel', legacy_types_path=Path(__file__).parent / 'legacy_types.csv')
        OTLExtraChecker.modify_for_extra_checks(directory=directory / 'OtlmowModel')
        OTLModelCreator.add_generated_info(
            directory=directory / 'OtlmowModel', oslo_collector=oslo_collector)
        logger.info(f'finished creating model in {directory} at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    @staticmethod
    def _prepare_the_model(directory: Path, oslo_collector: OSLOCollector, settings: dict) -> None:
        """Create the directories of the model and check the subset before generating it."""
        OTLModelCreator.check_and_create_subdirectories(directory)
        oslo_collector.query_correct_base_classes(valid_base_class_uris=settings['valid_base_class_uris'])
        OTLModelCreator.add_inheritances(oslo_collector=oslo_collector,
                                         additional_inheritances=settings['additional_inheritances'])
        OTLModelCreator.check_for_attributes_with_different_case(
            oslo_collector, attributes_with_different_cases_uris=settings['attributes_with_different_cases_uris'])
        OTLModelCreator.check_for_nested_attributes_in_classes(
            collector=oslo_collector, known_attribute_uris=settings['nested_list_attribute_uris'])

    @staticmethod
    def _collect_the_model_data(oslo_collector: OSLOCollector, environment: str, settings: dict,
                                include_kl_test_keuzelijst: bool) -> ModelData:
        """Collect the data that the rust and the python implementation of the model need."""
        enumeration_data = OTLModelCreator._read_the_enumerations(
            oslo_collector=oslo_collector, environment=environment, settings=settings,
            include_kl_test_keuzelijst=include_kl_test_keuzelijst)
        lookups = OTLModelCreator._build_the_lookups(oslo_collector)
        return ModelData(
            type_links=[(t.item_uri, t.item_tabel) for t in oslo_collector.typeLinks],
            enumerations=[(e.objectUri, e.name) for e in oslo_collector.enumerations],
            complex_datatypes=[(c.objectUri, c.name) for c in oslo_collector.complex_datatypes],
            union_datatypes=[(u.objectUri, u.name) for u in oslo_collector.union_datatypes],
            enumeration_waardes=enumeration_data.waardes,
            enumeration_adm_status=enumeration_data.adm_status,
            inheritance_map=oslo_collector.get_inheritance_map(),
            lookups=lookups,
            class_validation_rules=OTLModelCreator._merge_the_class_validation_rules(settings))

    @staticmethod
    def _read_the_enumerations(oslo_collector: OSLOCollector, environment: str, settings: dict,
                               include_kl_test_keuzelijst: bool) -> EnumerationData:
        """Read the values of every enumeration of the subset."""
        waardes = {}
        adm_status = {}
        with OTLEnumerationCreator(oslo_collector, env=environment,
                                   enumeration_locations_by_environment=settings['enumeration_locations_by_environment'],
                                   include_kl_test_keuzelijst=include_kl_test_keuzelijst) as creator:
            for enumeration in oslo_collector.enumerations:
                try:
                    waardes[enumeration.objectUri] = creator.get_keuzelijstwaardes_by_uri(
                        enumeration.codelist, env=environment or 'prd')
                    adm_status[enumeration.objectUri] = creator.get_adm_status_by_uri(
                        enumeration.codelist, env=environment or 'prd') or ''
                except Exception:  # noqa: BLE001 - fallback to empty on any enumeration lookup failure
                    waardes[enumeration.objectUri] = []
                    adm_status[enumeration.objectUri] = ''
        return EnumerationData(waardes=waardes, adm_status=adm_status)

    @staticmethod
    def _build_the_lookups(oslo_collector: OSLOCollector) -> Lookups:
        """Look up the attributes, the inheritances and the relations of every class."""
        return Lookups(
            attributes_by_class_uri=OTLModelCreator._build_the_attributes_by_class_uri(oslo_collector),
            inheritances_by_class_uri=OTLModelCreator._build_the_inheritances_by_class_uri(oslo_collector),
            relations_by_object_uri=OTLModelCreator._build_the_relations_by_object_uri(oslo_collector))

    @staticmethod
    def _build_the_attributes_by_class_uri(oslo_collector: OSLOCollector) -> dict[str, list]:
        """The attributes of every class, sorted by their uri."""
        if oslo_collector._attributes_by_class_uri is not None:
            attributes_by_class_uri = {
                oslo_class.objectUri: sorted(
                    oslo_collector._attributes_by_class_uri.get(oslo_class.objectUri, []),
                    key=lambda attribute: attribute.objectUri)
                for oslo_class in oslo_collector.classes}
        else:
            attributes_by_class_uri = {
                oslo_class.objectUri: oslo_collector.find_attributes_by_class(oslo_class, sort_by_uri=True)
                for oslo_class in oslo_collector.classes}
        OTLModelCreator._add_the_datatype_attributes(attributes_by_class_uri, oslo_collector)
        return attributes_by_class_uri

    @staticmethod
    def _add_the_datatype_attributes(attributes_by_class_uri: dict[str, list], oslo_collector: OSLOCollector) -> None:
        """Add the attributes of the datatypes to the lookup map of the classes."""
        for attribute in OTLModelCreator._datatype_attributes(oslo_collector):
            attributes_by_class_uri.setdefault(attribute.class_uri, []).append(attribute)
        class_uris = [oslo_class.objectUri for oslo_class in oslo_collector.classes]
        for uri in list(attributes_by_class_uri.keys()):
            if uri not in class_uris:
                attributes_by_class_uri[uri] = sorted(attributes_by_class_uri[uri],
                                                      key=lambda attribute: attribute.objectUri)

    @staticmethod
    def _datatype_attributes(oslo_collector: OSLOCollector) -> list:
        """The attributes of the primitive, the complex and the union datatypes."""
        attributes: list = []
        attributes.extend(oslo_collector.primitive_datatype_attributen or [])
        attributes.extend(oslo_collector.complex_datatype_attributen or [])
        attributes.extend(oslo_collector.union_datatype_attributen or [])
        return attributes

    @staticmethod
    def _build_the_inheritances_by_class_uri(oslo_collector: OSLOCollector) -> dict[str, list]:
        """The inheritances of every class, sorted by the uri of their base class."""
        if oslo_collector._inheritances_by_class_uri is not None:
            return {
                oslo_class.objectUri: sorted(
                    oslo_collector._inheritances_by_class_uri.get(oslo_class.objectUri, []),
                    key=lambda inheritance: inheritance.base_uri)
                for oslo_class in oslo_collector.classes}
        return {
            oslo_class.objectUri: oslo_collector.find_inheritances_by_class(oslo_class, sort_by_uri=True)
            for oslo_class in oslo_collector.classes}

    @staticmethod
    def _build_the_relations_by_object_uri(oslo_collector: OSLOCollector) -> dict[str, list]:
        """The relations of every class, without the duplicated ones."""
        if oslo_collector._relations_by_uri is not None:
            return {
                oslo_class.objectUri: OTLModelCreator._filter_the_relations(
                    oslo_collector._relations_by_uri.get(oslo_class.objectUri, []), oslo_class.objectUri)
                for oslo_class in oslo_collector.classes}
        return {
            oslo_class.objectUri: oslo_collector.find_all_relations(oslo_class.objectUri, allow_duplicates=False)
            for oslo_class in oslo_collector.classes}

    @staticmethod
    def _filter_the_relations(relations: list, object_uri: str) -> list:
        """Keep the relations of the object, without the ones that are inherited."""
        filtered = [relation for relation in relations
                    if OTLModelCreator._is_a_relation_of_the_object(relation, object_uri)]
        return sorted(filtered, key=lambda relation: relation.objectUri)

    @staticmethod
    def _is_a_relation_of_the_object(relation, object_uri: str) -> bool:
        """A relation of the object is not inherited, and points to the object when it is not directional."""
        if relation.bron_overerving != '' or relation.doel_overerving != '':
            return False
        if relation.richting == 'Unspecified':
            return relation.bron_uri == object_uri
        return True

    @staticmethod
    def _merge_the_class_validation_rules(settings: dict) -> dict:
        """The validation rules of the classes, extended with the ones of the complex datatypes."""
        class_validation_rules = settings['class_validation_rules'].copy()
        class_validation_rules['valid_uri_and_types'] = class_validation_rules['valid_uri_and_types'].copy()
        class_validation_rules['valid_uri_and_types'].update(
            settings['complex_datatype_validation_rules']['valid_uri_and_types'])
        return class_validation_rules

    @staticmethod
    def _use_rust() -> bool:
        """The rust implementation is used, unless it is switched off with an environment variable."""
        use_rust = os.environ.get('OTLMOW_USE_RUST', '1') != '0'
        logger.info(f'OTLMOW_USE_RUST={os.environ.get("OTLMOW_USE_RUST", "1")} -> use_rust={use_rust}')
        return use_rust

    @staticmethod
    def _create_the_model_with_rust(directory: Path, oslo_collector: OSLOCollector,
                                    geo_artefact_collector: GeometrieArtefactCollector | None, settings: dict,
                                    model_name: str, model_data: ModelData, environment: str,
                                    include_kl_test_keuzelijst: bool) -> None:
        """Generate the model with the rust implementation, and fall back to python when it is not available."""
        geometry_type_map = OTLModelCreator._build_the_geometry_type_map(oslo_collector, geo_artefact_collector)
        try:
            from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
                generate_model_optimized as rust_generate,
            )
            logger.info('Attempting Rust batch generation (using _otlmow_modelbuilder_rs.generate_model_optimized)...')
            files_written, errors = rust_generate(
                directory=str(directory / 'OtlmowModel'),
                model_name=model_name,
                settings=settings,
                type_links=model_data.type_links,
                enumerations_lookup=model_data.enumerations,
                complex_datatypes_lookup=model_data.complex_datatypes,
                union_datatypes_lookup=model_data.union_datatypes,
                primitive_datatypes=oslo_collector.primitive_datatypes,
                complex_datatypes=oslo_collector.complex_datatypes,
                union_datatypes=oslo_collector.union_datatypes,
                enumerations=oslo_collector.enumerations,
                enumeration_waardes=model_data.enumeration_waardes,
                enumeration_adm_status=model_data.enumeration_adm_status,
                classes=oslo_collector.classes,
                geometry_type_map=geometry_type_map,
                inheritance_map=model_data.inheritance_map,
                attributes_by_class_uri=model_data.lookups.attributes_by_class_uri,
                inheritances_by_class_uri=model_data.lookups.inheritances_by_class_uri,
                relations_by_object_uri=model_data.lookups.relations_by_object_uri,
                complex_datatype_validation_rules=settings['complex_datatype_validation_rules']['valid_uri_and_types'],
                primitive_datatype_validation_rules=settings['primitive_datatype_validation_rules'][
                    'valid_uri_and_types'],
                union_datatype_validation_rules=settings['union_datatype_validation_rules']['valid_uri_and_types'],
                enumeration_validation_rules=settings['enumeration_validation_rules']['valid_uri_and_types'],
                class_validation_rules=model_data.class_validation_rules['valid_uri_and_types'],
                include_kl_test_keuzelijst=include_kl_test_keuzelijst,
            )
            logger.info(f'Rust batch generation: {files_written} files, {errors} errors')
        except ImportError as e:
            logger.warning(f'Falling back to Python path (Rust batch generation unavailable): {e}')
            if "No module named 'otlmow_modelbuilder._otlmow_modelbuilder_rs'" in str(e):
                logger.warning('Rust extension not built. Build it with: source .venv/bin/activate && maturin develop --release (or --release depending on build)')
            # Fallback to Python per-item generation
            logger.info('Using Python path for model creation...')
            OTLModelCreator._create_the_model_with_python(
                directory=directory, oslo_collector=oslo_collector, geo_artefact_collector=geo_artefact_collector,
                settings=settings, class_validation_rules=model_data.class_validation_rules, environment=environment,
                include_kl_test_keuzelijst=include_kl_test_keuzelijst)

    @staticmethod
    def _build_the_geometry_type_map(oslo_collector: OSLOCollector,
                                      geo_artefact_collector: GeometrieArtefactCollector | None) -> dict[str, list]:
        """The geometry types of every class, when there are geometry artefacts."""
        geometry_type_map: dict = {}
        if geo_artefact_collector is None:
            return geometry_type_map
        class_creator = OTLClassCreator(oslo_collector, geo_artefact_collector)
        for oslo_class in oslo_collector.classes:
            geom_types = class_creator.get_geometry_types_from_uri(oslo_class.objectUri)
            if geom_types:
                geometry_type_map[oslo_class.objectUri] = geom_types
        return geometry_type_map

    @staticmethod
    def _create_the_model_with_python(directory: Path, oslo_collector: OSLOCollector,
                                      geo_artefact_collector: GeometrieArtefactCollector | None, settings: dict,
                                      class_validation_rules: dict, environment: str,
                                      include_kl_test_keuzelijst: bool) -> None:
        """Generate the model with the python implementation."""
        model_directory = directory / 'OtlmowModel'
        OTLModelCreator.create_primitive_datatypes(
            directory=model_directory, oslo_collector=oslo_collector,
            primitive_datatype_validation_rules=settings['primitive_datatype_validation_rules'])
        OTLModelCreator.create_complex_datatypes(
            directory=model_directory, oslo_collector=oslo_collector,
            complex_datatype_validation_rules=settings['complex_datatype_validation_rules'])
        OTLModelCreator.create_union_datatypes(
            directory=model_directory, oslo_collector=oslo_collector,
            union_datatype_validation_rules=settings['union_datatype_validation_rules'])
        OTLModelCreator.create_enumerations(
            directory=model_directory, environment=environment, oslo_collector=oslo_collector,
            enumeration_validation_rules=settings['enumeration_validation_rules'],
            enumeration_locations_by_environment=settings['enumeration_locations_by_environment'],
            include_kl_test_keuzelijst=include_kl_test_keuzelijst)
        OTLModelCreator.create_classes(
            directory=model_directory, oslo_collector=oslo_collector,
            geo_artefact_collector=geo_artefact_collector,
            class_validation_rules=class_validation_rules)

    @staticmethod
    def create_primitive_datatypes(directory, oslo_collector, primitive_datatype_validation_rules):
        creator = OTLPrimitiveDatatypeCreator(oslo_collector)

        for prim_datatype in tqdm(oslo_collector.primitive_datatypes):
            if prim_datatype.objectUri in PRIMITIVE_DATATYPES_TO_SKIP:
                logger.info(f"Skip creating class for {prim_datatype.name}")
                continue

            try:
                data_to_write = creator.create_block_to_write_from_primitive_types(
                    prim_datatype, model_location=OTLModelCreator.get_model_name_from_directory_path(directory),
                    primitive_datatype_validation_rules=primitive_datatype_validation_rules)
                OTLModelCreator._write_the_datatype(prim_datatype.name, data_to_write, directory)
            except Exception as e:  # noqa: BLE001 - per-item error logging, continue  # noqa: BLE001 - per-item error logging, continue
                logger.error(str(e))
                logger.error(f"Could not create a class for {prim_datatype.name}")

    @staticmethod
    def get_model_name_from_directory_path(directory):
        if directory.name == 'TestClasses':
            return f'{directory.parent.name}.{directory.name}'
        else:
            return directory.name

    @staticmethod
    def create_complex_datatypes(directory, oslo_collector, complex_datatype_validation_rules):
        creator = OTLComplexDatatypeCreator(oslo_collector)

        for complex_datatype in tqdm(oslo_collector.complex_datatypes):
            try:
                data_to_write = creator.create_block_to_write_from_complex_types(
                    complex_datatype, complex_datatype_validation_rules=complex_datatype_validation_rules,
                    model_location=OTLModelCreator.get_model_name_from_directory_path(directory))
                OTLModelCreator._write_the_datatype(complex_datatype.name, data_to_write, directory)
            except BaseException as e:  # noqa: BLE001 - per-item error logging, continue
                logger.error(str(e))
                logger.error(f"Could not create a class for {complex_datatype.name}")

    @staticmethod
    def create_union_datatypes(directory, oslo_collector, union_datatype_validation_rules):
        creator = OTLUnionDatatypeCreator(oslo_collector)

        for union_datatype in tqdm(oslo_collector.union_datatypes):
            try:
                data_to_write = creator.create_block_to_write_from_union_types(
                    union_datatype, model_location=OTLModelCreator.get_model_name_from_directory_path(directory),
                    union_datatype_validation_rules=union_datatype_validation_rules)
                OTLModelCreator._write_the_datatype(union_datatype.name, data_to_write, directory)
            except BaseException as e:  # noqa: BLE001 - per-item error logging, continue
                logger.error(str(e))
                logger.error(f"Could not create a class for {union_datatype.name}")

    @staticmethod
    def _write_the_datatype(name, data_to_write, directory, log=logger.info):
        """Write a datatype, and report it when there is nothing to write."""
        if data_to_write is None:
            log(f"Could not create a class for {name}")
        if len(data_to_write) == 0:
            log(f"Could not create a class for {name}")
        write_to_file(name, 'Datatypes', data_to_write, relative_path=directory)

    @staticmethod
    def create_enumerations(directory, oslo_collector, enumeration_validation_rules,
                            enumeration_locations_by_environment: dict[str, list[str]],
                            include_kl_test_keuzelijst: bool = False, environment: str = 'prd'):
        with OTLEnumerationCreator(oslo_collector, env=environment,
                                   enumeration_locations_by_environment=enumeration_locations_by_environment,
                                   include_kl_test_keuzelijst=include_kl_test_keuzelijst) as creator:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {executor.submit(OTLModelCreator.create_enumeration, creator=creator, directory=directory,
                                           enumeration=enumeration, environment=environment,
                                           enumeration_validation_rules=enumeration_validation_rules): enumeration for
                           enumeration in oslo_collector.enumerations}
                with tqdm(total=len(futures)) as pbar:
                    while futures:
                        futures = OTLModelCreator._wait_for_the_enumerations(
                            executor, futures, creator, directory, environment, enumeration_validation_rules, pbar)

    @staticmethod
    def _wait_for_the_enumerations(executor, futures, creator, directory, environment,
                                   enumeration_validation_rules, pbar):
        """Wait for the enumerations that are created, and retry the ones that failed."""
        new_futures = {}
        done, pending = concurrent.futures.wait(futures, return_when=FIRST_COMPLETED, timeout=60)
        for fut in done:
            enumeration = futures[fut]
            if fut.exception():
                new_futures[executor.submit(
                    OTLModelCreator.create_enumeration, creator=creator, directory=directory,
                    enumeration=enumeration, environment=environment,
                    enumeration_validation_rules=enumeration_validation_rules)
                ] = enumeration
            else:
                pbar.update()
        for fut in pending:
            new_futures[fut] = futures[fut]
        return new_futures

    @staticmethod
    def create_enumeration(creator, directory, enumeration, environment, enumeration_validation_rules):
        try:
            data_to_write = creator.create_block_to_write_from_enumerations(
                enumeration, environment=environment, enumeration_validation_rules=enumeration_validation_rules)
            OTLModelCreator._write_the_datatype(enumeration.name, data_to_write, directory, log=logger.error)
        except BaseException as e:  # noqa: BLE001 - per-item error logging, continue
            logger.error(str(e))
            logger.error(f"Could not create a class for {enumeration.name}")

    @staticmethod
    def create_classes(directory, oslo_collector, geo_artefact_collector, class_validation_rules):
        creator = OTLClassCreator(oslo_collector, geo_artefact_collector)

        for oslo_class in tqdm(oslo_collector.classes):
            OTLModelCreator._create_the_class(oslo_class, creator, directory, class_validation_rules)

        OTLModelCreator._write_the_all_classes_helper(oslo_collector, directory, class_validation_rules)

    @staticmethod
    def _create_the_class(oslo_class, creator, directory, class_validation_rules):
        """Write the class of one OTL class."""
        try:
            if oslo_class.label == IGNORED_CLASS_LABEL:
                return
            data_to_write = creator.create_blocks_to_write_from_classes(
                oslo_class, model_location=OTLModelCreator.get_model_name_from_directory_path(directory),
                class_validation_rules=class_validation_rules)
            OTLModelCreator._write_the_class(oslo_class.name, data_to_write,
                                            OTLModelCreator._class_directory_of(oslo_class), directory)
        except Exception as e:  # noqa: BLE001 - per-item error logging, continue
            logger.error(str(e))
            logger.error(f"Could not create a class for {oslo_class.name}")

    @staticmethod
    def _class_directory_of(oslo_class):
        """The directory of a class, based on the namespace of its uri."""
        if oslo_class.objectUri == AGENT_URI:
            return 'Classes'
        ns, _ = get_ns_and_name_from_uri(oslo_class.objectUri)
        if ns is None:
            return 'Classes'
        return get_class_directory_from_ns(ns)

    @staticmethod
    def _write_the_class(name, data_to_write, class_directory, directory):
        """Write a class, and report it when there is nothing to write."""
        if data_to_write is None:
            logger.info(f"Could not create a class for {name}")
        if len(data_to_write) == 0:
            logger.info(f"Could not create a class for {name}")
        write_to_file(name, class_directory, data_to_write, relative_path=directory)

    @staticmethod
    def _write_the_all_classes_helper(oslo_collector, directory, class_validation_rules):
        """Write the helper that imports every class of the model."""
        data_to_write = []
        for oslo_class in oslo_collector.classes:
            if oslo_class.abstract:
                continue
            data_to_write.append(OTLModelCreator._import_statement_of(oslo_class, class_validation_rules))
        write_to_file('all_classes', 'Helpers', data_to_write, relative_path=directory)

    @staticmethod
    def _import_statement_of(oslo_class, class_validation_rules):
        """The import statement of a class, in the helper that imports every class."""
        valid_uri_and_types = class_validation_rules['valid_uri_and_types']
        if oslo_class.objectUri in valid_uri_and_types:
            ns = None
            name = valid_uri_and_types[oslo_class.objectUri]
        else:
            ns, name = get_ns_and_name_from_uri(oslo_class.objectUri)
        if ns is not None:
            return f'from ..Classes.{get_titlecase_from_ns(ns)}.{name} import {name}'
        return f'from ..Classes.{name} import {name}'

    @staticmethod
    def check_and_create_subdirectories(directory: Path):
        if not path.exists(directory):
            os.makedirs(directory)
        if not path.exists(directory):
            raise OSError(f'The directory {directory} does not exist. Please create it first.')
        if not path.isdir(directory):
            raise NotADirectoryError(f'{directory} is not a directory.')

        if not path.exists(directory / 'OtlmowModel'):
            os.mkdir(directory / 'OtlmowModel')

        model_directory = directory / 'OtlmowModel'

        OTLModelCreator.clean_directory(model_directory)
        OTLModelCreator.copy_fixed_classes_from_otlmow_model(model_directory)

        OTLModelCreator._create_the_class_directories(model_directory)

    @staticmethod
    def _create_the_class_directories(model_directory: Path) -> None:
        """Create the directories the classes and the datatypes are written to."""
        for class_directory in ['Classes', 'Datatypes'] + CLASS_DIRECTORIES:
            if not path.exists(model_directory / class_directory):
                os.mkdir(model_directory / class_directory)

    @staticmethod
    def clean_directory(directory):
        for root, dirs, files in os.walk(directory):
            for direc in dirs:
                shutil.rmtree(os.path.join(root, direc))
            for file in files:
                os.remove(os.path.join(root, file))

    @staticmethod
    def check_for_nested_attributes_in_classes(collector: OSLOCollector, exceptions=None,
                                               known_attribute_uris: list[str] | None = None):
        if known_attribute_uris is None:
            known_attribute_uris = []
        if exceptions is None:
            exceptions = DEFAULT_NESTED_LIST_EXCEPTIONS
        for cl in collector.classes:
            if cl.abstract:
                continue
            OTLModelCreator._check_the_class_for_nested_attributes(cl, collector, exceptions, known_attribute_uris)

    @staticmethod
    def _check_the_class_for_nested_attributes(cl, collector, exceptions, known_attribute_uris) -> None:
        """Check the attributes of one class for a list inside a list."""
        for attr in collector.find_attributes_by_class(cl):
            if attr.objectUri in exceptions:
                # exception for test classes
                continue
            nested_attrs = OTLModelCreator._find_the_nested_attributes(collector, attr)
            if len(nested_attrs) > 1:
                list_found = attr.kardinaliteit_max != '1'
                try:
                    OTLModelCreator.check_for_nested_attributes_in_attributes(list_found, nested_attrs, collector)
                except NestedListAttributeError as exc:
                    if attr.objectUri not in known_attribute_uris:
                        raise NestedListAttributeError(f'found in {cl.objectUri} {attr.objectUri}') from exc

    @staticmethod
    def _find_the_nested_attributes(collector, attr) -> list:
        """The attributes of the datatype of an attribute."""
        nested_attrs = collector.find_complex_datatype_attributes_by_class_uri(attr.type)
        if len(nested_attrs) == 0:
            nested_attrs = collector.find_primitive_datatype_attributes_by_class_uri(attr.type)
        if len(nested_attrs) == 0:
            nested_attrs = collector.find_union_datatype_attributes_by_class_uri(attr.type)
        return nested_attrs

    @staticmethod
    def check_for_nested_attributes_in_attributes(list_already_found, attributes, collector):
        for attr in attributes:
            list_found = attr.kardinaliteit_max != '1'

            if list_found and list_already_found:
                raise NestedListAttributeError(f'Found nested list attributes: {attr.objectUri}')
            nested_attrs = OTLModelCreator._find_the_nested_attributes(collector, attr)

            if len(nested_attrs) > 1:
                OTLModelCreator.check_for_nested_attributes_in_attributes(
                    list_found or list_already_found, nested_attrs, collector)

    @classmethod
    def check_for_attributes_with_different_case(cls, oslo_collector, attributes_with_different_cases_uris: list[str]):
        problems = cls._find_the_attributes_with_a_different_case(oslo_collector)
        problems = cls._remove_the_ignored_attributes(problems, attributes_with_different_cases_uris)

        if problems:
            raise NotImplementedError(f'Found attributes with different case:\n{json.dumps(problems, indent=4)}')

    @classmethod
    def _find_the_attributes_with_a_different_case(cls, oslo_collector) -> dict[str, list]:
        """The attributes that only differ in case, per name."""
        problems: dict = defaultdict(set)
        for lower_case_name in {attribute.name.lower() for attribute in oslo_collector.attributes}:
            attributes = cls._active_attributes_with_name(oslo_collector, lower_case_name)
            if len(attributes) < 2:
                continue
            cls._register_the_conflicting_uris(problems, attributes)
        return {name: list(uris) for name, uris in problems.items()}

    @staticmethod
    def _active_attributes_with_name(oslo_collector, lower_case_name) -> list:
        """The attributes with the given name that are not deprecated."""
        return [attribute for attribute in oslo_collector.attributes
                if attribute.name.lower() == lower_case_name and attribute.deprecated_version == '']

    @staticmethod
    def _register_the_conflicting_uris(problems, attributes) -> None:
        """Register the uris of the attributes that only differ in case."""
        first_attr = attributes[0].name
        for attr in attributes[1:]:
            if attr.name != first_attr:
                problems[first_attr.lower()].add(attributes[0].objectUri)
                problems[first_attr.lower()].add(attr.objectUri)

    @staticmethod
    def _remove_the_ignored_attributes(problems, ignored_uris) -> dict[str, list]:
        """Remove the attributes that are on the ignore list."""
        for name, uri_list in problems.items():
            for uri in tuple(uri_list):
                if uri in ignored_uris:
                    uri_list.remove(uri)

        for name in list(problems.keys()):
            if len(problems[name]) == 0:
                del problems[name]

        return problems

    @classmethod
    def copy_fixed_classes_from_otlmow_model(cls, model_directory: Path):
        otlmow_model_github_dir = Path(__file__).parent / 'OTLMOW-Model'
        if otlmow_model_github_dir.exists():
            shutil.rmtree(otlmow_model_github_dir)
        subprocess.call([
            "git", "clone", "--depth=1", "--filter=blob:none", "--sparse",
            "https://github.com/davidvlaminck/OTLMOW-Model/",
            str(otlmow_model_github_dir.absolute())
        ], cwd=str(Path(__file__).parent))
        subprocess.call([
            "git", "sparse-checkout", "set",
            "otlmow_model/OtlmowModel/BaseClasses",
            "otlmow_model/OtlmowModel/Exceptions",
            "otlmow_model/OtlmowModel/GeometrieTypes",
            "otlmow_model/OtlmowModel/Helpers",
            "otlmow_model/OtlmowModel/warnings",
        ], cwd=str(otlmow_model_github_dir.absolute()))

        otlmow_model_dir = otlmow_model_github_dir / 'otlmow_model' / 'OtlmowModel'
        if not otlmow_model_dir.exists():
            raise ModuleNotFoundError("Could not find otlmow-model directory")

        shutil.copytree(otlmow_model_dir / 'BaseClasses', model_directory / 'BaseClasses')
        shutil.copytree(otlmow_model_dir / 'Exceptions', model_directory / 'Exceptions')
        shutil.copytree(otlmow_model_dir / 'GeometrieTypes', model_directory / 'GeometrieTypes')
        shutil.copytree(otlmow_model_dir / 'Helpers', model_directory / 'Helpers')
        shutil.copytree(otlmow_model_dir / 'warnings', model_directory / 'warnings')

        try:
            shutil.rmtree(otlmow_model_github_dir)
        except PermissionError:
            print(f"Could not remove {otlmow_model_github_dir}")

    @classmethod
    def add_generated_info(cls, directory: Path, oslo_collector: OSLOCollector) -> None:
        relation_dict = cls.generate_relation_dict(oslo_collector)
        class_dict = cls.generate_class_dict(oslo_collector)
        class_dict = {k: v for k, v in class_dict.items() if v['label'] != IGNORED_CLASS_LABEL}
        with open(directory / 'generated_info.json', mode='w') as generated_info_file:
            json.dump({'relations': relation_dict, 'classes': class_dict}, generated_info_file, indent=4)

    @classmethod
    def generate_relation_dict(cls, oslo_collector: OSLOCollector) -> dict:
        relation_dict = {}
        for inheritance in oslo_collector.inheritances:
            if inheritance.base_uri == ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#'
                                        'DirectioneleRelatie'):
                relation_dict[inheritance.class_uri] = {'directional': True}
            elif inheritance.base_uri == ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#'
                                          'NietDirectioneleRelatie'):
                relation_dict[inheritance.class_uri] = {'directional': False}
        return relation_dict

    @classmethod
    def generate_class_dict(cls, oslo_collector: OSLOCollector) -> dict:
        return {uri: {
                'abstract': oslo_class.abstract == 1,
                'ns': get_ns_and_name_from_uri(oslo_class.objectUri)[0],
                'name': oslo_class.name,
                'label': oslo_class.label,
                'deprecated_version': oslo_class.deprecated_version,
                'direct_subclasses': list(oslo_collector.find_subclasses_uri_by_class_uri(oslo_class.objectUri))
            } for uri, oslo_class in oslo_collector.class_dict.items()}

    @classmethod
    def create_legacy_classes(cls, oslo_collector: OSLOCollector, directory: Path, legacy_types_path: Path):
        creator = LegacyClassCreator()

        lgc_type_data: list = []
        with open(legacy_types_path) as legacy_types_file:
            lgc_type_data.extend(iter(csv.reader(legacy_types_file, delimiter='\t')))

        cls._add_the_legacy_base_classes(oslo_collector)

        for lgc_type_row in tqdm(lgc_type_data):
            cls._create_the_legacy_class(lgc_type_row, oslo_collector, creator, directory)

        cls._add_the_legacy_classes_to_the_helper(lgc_type_data, directory)

        return oslo_collector

    @staticmethod
    def _add_the_legacy_base_classes(oslo_collector: OSLOCollector) -> None:
        """Add the legacy object class and the base classes it inherits from."""
        for base_name in LEGACY_BASE_CLASS_NAMES:
            oslo_collector.inheritances.append(Inheritance(
                base_name=base_name,
                base_uri=f'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#{base_name}',
                class_name='LegacyObject',
                class_uri=LEGACY_OBJECT_URI
            ))

        lgc_class = OSLOClass(
            label='Legacy Object',
            name='LegacyObject',
            objectUri=LEGACY_OBJECT_URI,
            deprecated_version='',
            definition='Abstracte voor een Legacy object',
            abstract=1
        )
        oslo_collector.classes.append(lgc_class)
        oslo_collector.class_dict[LEGACY_OBJECT_URI] = lgc_class

    @classmethod
    def _create_the_legacy_class(cls, lgc_type_row, oslo_collector, creator, directory) -> None:
        """Add one legacy type to the model and write its class."""
        class_uri = lgc_type_row[0]
        class_name = cls.alter_legacy_class_name(lgc_type_row[2])

        oslo_class = OSLOClass(
            objectUri=class_uri,
            name=class_name,
            label=lgc_type_row[1],
            deprecated_version='',
            abstract=False)
        oslo_collector.classes.append(oslo_class)
        oslo_collector.inheritances.append(Inheritance(
            base_name='LegacyObject',
            base_uri=LEGACY_OBJECT_URI,
            class_name=class_name,
            class_uri=class_uri
        ))
        oslo_collector.class_dict[class_uri] = oslo_class
        try:
            data_to_write = creator.create_blocks_to_write_from_rows(
                lgc_type_row=lgc_type_row, model_location=OTLModelCreator.get_model_name_from_directory_path(directory))
            if data_to_write is None:
                logger.info(f"Could not create a class for {class_name}")
            if len(data_to_write) == 0:
                logger.info(f"Could not create a class for {class_name}")
            class_directory = 'Classes/Legacy'

            write_to_file(class_name, class_directory, data_to_write, relative_path=directory)
        except Exception as e:  # noqa: BLE001 - per-item error logging, continue
            logger.error(str(e))
            logger.error(f"Could not create a class for {class_name}")

    @classmethod
    def _add_the_legacy_classes_to_the_helper(cls, lgc_type_data, directory) -> None:
        """Add the imports of the legacy classes to the helper that imports every class."""
        data_to_write = []
        for lgc_type_row in lgc_type_data:
            uri = lgc_type_row[0]
            _, name = get_ns_and_name_from_uri(uri)
            name = cls.alter_legacy_class_name(name)
            data_to_write.append(f'from ..Classes.Legacy.{name} import {name}')

        write_to_file('all_classes', 'Helpers', data_to_write, relative_path=directory, write_mode='a')

    @classmethod
    def alter_legacy_class_name(cls, class_name):
        class_name = class_name.replace('.', '_').replace('-', '_')
        return LEGACY_CLASS_NAME_ALIASES.get(class_name, class_name)

    @classmethod
    def add_inheritances(cls, oslo_collector: OSLOCollector, additional_inheritances: list[dict]):
        for inh in additional_inheritances:
            oslo_collector.inheritances.append(
                Inheritance(base_name=inh['base_name'], base_uri=inh['base_uri'], class_name=inh['class_name'],
                            class_uri=inh['class_uri'], deprecated_version=''))
            cls._add_the_placeholder_class(oslo_collector, inh['class_uri'], inh['class_name'])
            # same for base class, if not present
            cls._add_the_placeholder_class(oslo_collector, inh['base_uri'], inh['base_name'])

    @staticmethod
    def _add_the_placeholder_class(oslo_collector: OSLOCollector, uri: str, name: str) -> None:
        """Add a class that is not generated, but that is needed by the model."""
        if uri in oslo_collector.class_dict:
            return
        placeholder = OSLOClass(
            label=IGNORED_CLASS_LABEL,
            name=name,
            objectUri=uri,
            deprecated_version='',
            definition='',
            abstract=1
        )
        oslo_collector.class_dict[uri] = placeholder
        oslo_collector.classes.append(placeholder)
