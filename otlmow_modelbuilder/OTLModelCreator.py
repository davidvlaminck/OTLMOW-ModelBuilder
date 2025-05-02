import concurrent.futures
import csv
import json
import logging
import os
import shutil
import subprocess
from collections import defaultdict
from concurrent.futures import FIRST_COMPLETED
from datetime import datetime
from os import path
from pathlib import Path
from typing import Dict

from tqdm import tqdm

from otlmow_modelbuilder.GenericBuilderFunctions import write_to_file
from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns, \
    get_titlecase_from_ns
from otlmow_modelbuilder.LegacyClassCreator import LegacyClassCreator
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator
from otlmow_modelbuilder.OTLExtraChecker import OTLExtraChecker
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass


class OTLModelCreator:
    def __init__(self):
        pass

    @staticmethod
    def create_full_model(directory: Path, oslo_collector: OSLOCollector,
                          geo_artefact_collector: GeometrieArtefactCollector, settings: Dict, include_legacy: bool,
                          environment: str = '', include_kl_test_keuzelijst: bool = False):
        logging.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        OTLModelCreator.check_and_create_subdirectories(directory)
        oslo_collector.query_correct_base_classes()

        OTLModelCreator.check_for_attributes_with_different_case(oslo_collector)
        OTLModelCreator.check_for_nested_attributes_in_classes(collector=oslo_collector,
                                                               known_classes_uris=settings['nested_list_class_uris'])
        OTLModelCreator.create_primitive_datatypes(
            directory=directory / 'OtlmowModel', oslo_collector=oslo_collector,
            primitive_datatype_validation_rules=settings['primitive_datatype_validation_rules'])
        OTLModelCreator.create_complex_datatypes(
            directory=directory / 'OtlmowModel', oslo_collector=oslo_collector,
            complex_datatype_validation_rules=settings['complex_datatype_validation_rules'])
        OTLModelCreator.create_union_datatypes(
            directory=directory / 'OtlmowModel', oslo_collector=oslo_collector,
            union_datatype_validation_rules=settings['union_datatype_validation_rules'])
        OTLModelCreator.create_enumerations(
            directory=directory / 'OtlmowModel', environment=environment, oslo_collector=oslo_collector,
            enumeration_validation_rules=settings['enumeration_validation_rules'],
            include_kl_test_keuzelijst=include_kl_test_keuzelijst)
        OTLModelCreator.create_classes(
            directory=directory / 'OtlmowModel', oslo_collector=oslo_collector,
            geo_artefact_collector=geo_artefact_collector,
            valid_uri_and_types=settings['complex_datatype_validation_rules']['valid_uri_and_types'])
        if include_legacy:
            oslo_collector = OTLModelCreator.create_legacy_classes(oslo_collector=oslo_collector,
                directory=directory / 'OtlmowModel', legacy_types_path=Path(__file__).parent / 'legacy_types.csv')
        OTLExtraChecker.modify_for_extra_checks(directory=directory / 'OtlmowModel')
        OTLModelCreator.add_generated_info(
            directory=directory / 'OtlmowModel', oslo_collector=oslo_collector)
        logging.info(f'finished creating model in {directory} at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    @staticmethod
    def create_primitive_datatypes(directory, oslo_collector, primitive_datatype_validation_rules):
        creator = OTLPrimitiveDatatypeCreator(oslo_collector)

        for prim_datatype in tqdm(oslo_collector.primitive_datatypes):
            if prim_datatype.objectUri in ['http://www.w3.org/2000/01/rdf-schema#Literal',
                                           'http://www.w3.org/2001/XMLSchema#dateTime',
                                           'http://www.w3.org/2001/XMLSchema#integer',
                                           'http://www.w3.org/2001/XMLSchema#decimal',
                                           'http://www.w3.org/2001/XMLSchema#time',
                                           'http://www.w3.org/2001/XMLSchema#date',
                                           'http://www.w3.org/2001/XMLSchema#nonNegativeInteger',
                                           'http://www.w3.org/2001/XMLSchema#string',
                                           'http://www.w3.org/2001/XMLSchema#boolean',
                                           'http://www.w3.org/2001/XMLSchema#anyURI']:
                logging.info(f"Skip creating class for {prim_datatype.name}")
                continue

            try:
                model_name = OTLModelCreator.get_model_name_from_directory_path(directory)
                data_to_write = creator.create_block_to_write_from_primitive_types(
                    prim_datatype, model_location=model_name,
                    primitive_datatype_validation_rules=primitive_datatype_validation_rules)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {prim_datatype.name}")
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {prim_datatype.name}")
                write_to_file(prim_datatype.name, 'Datatypes', data_to_write, relative_path=directory)
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {prim_datatype.name}")

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
                model_name = OTLModelCreator.get_model_name_from_directory_path(directory)
                data_to_write = creator.create_block_to_write_from_complex_types(
                    complex_datatype, complex_datatype_validation_rules=complex_datatype_validation_rules,
                    model_location=model_name)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {complex_datatype.name}")
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {complex_datatype.name}")
                write_to_file(complex_datatype.name, 'Datatypes', data_to_write, relative_path=directory)
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {complex_datatype.name}")

    @staticmethod
    def create_union_datatypes(directory, oslo_collector, union_datatype_validation_rules):
        creator = OTLUnionDatatypeCreator(oslo_collector)

        for union_datatype in tqdm(oslo_collector.union_datatypes):
            try:
                model_name = OTLModelCreator.get_model_name_from_directory_path(directory)
                data_to_write = creator.create_block_to_write_from_union_types(
                    union_datatype, model_location=model_name,
                    union_datatype_validation_rules=union_datatype_validation_rules)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {union_datatype.name}")
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {union_datatype.name}")
                write_to_file(union_datatype.name, 'Datatypes', data_to_write, relative_path=directory)
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {union_datatype.name}")

    @staticmethod
    def create_enumerations(directory, oslo_collector, enumeration_validation_rules, environment: str = '',
                            include_kl_test_keuzelijst: bool = False):
        with OTLEnumerationCreator(oslo_collector, env=environment,
                                        include_kl_test_keuzelijst=include_kl_test_keuzelijst) as creator:

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {executor.submit(OTLModelCreator.create_enumeration, creator=creator, directory=directory,
                                           enumeration=enumeration, environment=environment,
                                           enumeration_validation_rules=enumeration_validation_rules): enumeration for
                           enumeration in oslo_collector.enumerations}
                with tqdm(total=len(futures)) as pbar:
                    while futures:
                        new_futures = {}
                        done, pending = concurrent.futures.wait(futures, return_when=FIRST_COMPLETED, timeout=60)
                        for fut in done:
                            if fut.exception():
                                enumeration = futures[fut]
                                new_futures[executor.submit(
                                    OTLModelCreator.create_enumeration, creator=creator, directory=directory,
                                    enumeration=enumeration, environment=environment,
                                    enumeration_validation_rules=enumeration_validation_rules)
                                ] = job
                            else:
                                pbar.update()
                        for fut in pending:
                            job = futures[fut]
                            new_futures[fut] = job
                        futures = new_futures

    @staticmethod
    def create_enumeration(creator, directory, enumeration, environment, enumeration_validation_rules):
        try:
            data_to_write = creator.create_block_to_write_from_enumerations(
                enumeration, environment=environment, enumeration_validation_rules=enumeration_validation_rules)
            if data_to_write is None:
                logging.error(f"Could not create a class for {enumeration.name}")
            if len(data_to_write) == 0:
                logging.error(f"Could not create a class for {enumeration.name}")
            write_to_file(enumeration.name, 'Datatypes', data_to_write, relative_path=directory)
        except BaseException as e:
            logging.error(str(e))
            logging.error(f"Could not create a class for {enumeration.name}")

    @staticmethod
    def create_classes(directory, oslo_collector, geo_artefact_collector, valid_uri_and_types):
        creator = OTLClassCreator(oslo_collector, geo_artefact_collector)

        for oslo_class in tqdm(oslo_collector.classes):
            try:
                model_name = OTLModelCreator.get_model_name_from_directory_path(directory)
                data_to_write = creator.create_blocks_to_write_from_classes(oslo_class, model_location=model_name,
                                                                            valid_uri_and_types=valid_uri_and_types)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {oslo_class.name}")
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {oslo_class.name}")
                class_directory = 'Classes'
                ns = None
                if oslo_class.objectUri != 'http://purl.org/dc/terms/Agent':
                    ns, _ = get_ns_and_name_from_uri(oslo_class.objectUri)
                if ns is not None:
                    class_directory = get_class_directory_from_ns(ns)

                write_to_file(oslo_class.name, class_directory, data_to_write, relative_path=directory)
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {oslo_class.name}")

        data_to_write = []
        for oslo_class in oslo_collector.classes:
            if oslo_class.abstract:
                continue
            ns = None
            if oslo_class.objectUri != 'http://purl.org/dc/terms/Agent':
                ns, name = get_ns_and_name_from_uri(oslo_class.objectUri)
            else:
                name = 'Agent'

            if ns is not None:
                data_to_write.append(f'from ..Classes.{get_titlecase_from_ns(ns)}.{name} import {name}')
            else:
                data_to_write.append(f'from ..Classes.{name} import {name}')

        write_to_file('all_classes', 'Helpers', data_to_write, relative_path=directory)


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

        if not path.exists(model_directory / 'Classes'):
            os.mkdir(model_directory / 'Classes')
        if not path.exists(model_directory / 'Datatypes'):
            os.mkdir(model_directory / 'Datatypes')

        if not path.exists(model_directory / 'Classes/Abstracten'):
            os.mkdir(model_directory / 'Classes/Abstracten')
        if not path.exists(model_directory / 'Classes/ImplementatieElement'):
            os.mkdir(model_directory / 'Classes/ImplementatieElement')
        if not path.exists(model_directory / 'Classes/Installatie'):
            os.mkdir(model_directory / 'Classes/Installatie')
        if not path.exists(model_directory / 'Classes/Legacy'):
            os.mkdir(model_directory / 'Classes/Legacy')
        if not path.exists(model_directory / 'Classes/Levenscyclus'):
            os.mkdir(model_directory / 'Classes/Levenscyclus')
        if not path.exists(model_directory / 'Classes/Onderdeel'):
            os.mkdir(model_directory / 'Classes/Onderdeel')
        if not path.exists(model_directory / 'Classes/ProefEnMeting'):
            os.mkdir(model_directory / 'Classes/ProefEnMeting')

    @staticmethod
    def clean_directory(directory):
        for root, dirs, files in os.walk(directory):
            for direc in dirs:
                shutil.rmtree(os.path.join(root, direc))
            for file in files:
                os.remove(os.path.join(root, file))

    @staticmethod
    def check_for_nested_attributes_in_classes(collector: OSLOCollector, exceptions=None,
                                               known_classes_uris: [str] = None):
        if known_classes_uris is None:
            known_classes_uris = []
        if exceptions is None:
            exceptions = [
                'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard']
        for cl in collector.classes:
            if cl.abstract:
                continue

            attributes = collector.find_attributes_by_class(cl)
            for attr in attributes:
                if attr.objectUri in exceptions:
                    # exception for test classes
                    continue
                list_found = False
                if attr.kardinaliteit_max != '1':
                    list_found = True
                nested_attrs = collector.find_complex_datatype_attributes_by_class_uri(attr.type)
                if len(nested_attrs) == 0:
                    nested_attrs = collector.find_primitive_datatype_attributes_by_class_uri(attr.type)
                if len(nested_attrs) == 0:
                    nested_attrs = collector.find_union_datatype_attributes_by_class_uri(attr.type)

                if len(nested_attrs) > 1:
                    try:
                        OTLModelCreator.check_for_nested_attributes_in_attributes(list_found, nested_attrs, collector)
                    except NotImplementedError as exc:
                        if cl.objectUri not in known_classes_uris:
                            raise NotImplementedError(f'found in {cl.objectUri} {attr.objectUri}') from exc

    @staticmethod
    def check_for_nested_attributes_in_attributes(list_already_found, attributes, collector):
        for attr in attributes:
            list_found = False
            if attr.kardinaliteit_max != '1':
                list_found = True

            if list_found and list_already_found:
                raise NotImplementedError(f'Found nested list attributes: {attr.objectUri}')
            nested_attrs = collector.find_complex_datatype_attributes_by_class_uri(attr.type)
            if len(nested_attrs) == 0:
                nested_attrs = collector.find_primitive_datatype_attributes_by_class_uri(attr.type)
            if len(nested_attrs) == 0:
                nested_attrs = collector.find_union_datatype_attributes_by_class_uri(attr.type)

            if len(nested_attrs) > 1:
                list_found = list_found or list_already_found
                OTLModelCreator.check_for_nested_attributes_in_attributes(list_found, nested_attrs, collector)

    @classmethod
    def check_for_attributes_with_different_case(cls, oslo_collector):
        lower_case_names = [d.name.lower() for d in oslo_collector.attributes]
        # find names that are identical when case-insensitive
        unique_lower_case_names = set(lower_case_names)
        problems = defaultdict(set)
        for lower_case_name in unique_lower_case_names:
            attrs = [d for d in oslo_collector.attributes if
                     d.name.lower() == lower_case_name and d.deprecated_version == '']
            if len(attrs) < 2:
                continue
            first_attr = attrs[0].name
            for attr in attrs[1:]:
                if attr.name != first_attr:
                    problems[first_attr.lower()].add(attrs[0].objectUri)
                    problems[first_attr.lower()].add(attr.objectUri)

        problems = {k: list(v) for k, v in problems.items()}

        # remove attributes that are known to be different
        known_list = ['basisoppervlakte', 'ipadres', 'risicoanalyse', 'technischefiche', 'opstelhoogte',
                      'buitendiameter', 'dnsnaam', 'funderingsaanzetonderdebodemvandewaterweg', 'binnendiameter',
                      'netwerktype', 'beschoeiingslengte', 'softwareversie', 'folietype', 'lamptype']
        for known in known_list:
            if known in problems:
                del problems[known]

        if problems:
            raise NotImplementedError(f'Found attributes with different case:\n{json.dumps(problems, indent=4)}')

    @classmethod
    def copy_fixed_classes_from_otlmow_model(cls, model_directory: Path):
        otlmow_model_github_dir = Path(__file__).parent / 'OTLMOW-Model'
        subprocess.call(["git", "clone", "--depth=1", "https://github.com/davidvlaminck/OTLMOW-Model/",
                         str(otlmow_model_github_dir.absolute())])

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
                'name': oslo_class.name,
                'label': oslo_class.label,
                'deprecated_version': oslo_class.deprecated_version,
                'direct_subclasses': list(oslo_collector.find_subclasses_uri_by_class_uri(oslo_class.objectUri))
            } for uri, oslo_class in oslo_collector.class_dict.items()}

    @classmethod
    def create_legacy_classes(cls, oslo_collector: OSLOCollector, directory: Path, legacy_types_path: Path):
        creator = LegacyClassCreator()

        lgc_type_data = []
        with open(legacy_types_path) as legacy_types_file:
            lgc_type_data.extend(iter(csv.reader(legacy_types_file, delimiter='\t')))

        oslo_collector.inheritances.append(Inheritance(
            base_name='AIMDBStatus',
            base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus',
            class_name='LegacyObject',
            class_uri='https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject'
        ))
        oslo_collector.inheritances.append(Inheritance(
            base_name='AIMToestand',
            base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand',
            class_name='LegacyObject',
            class_uri='https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject'
        ))
        oslo_collector.inheritances.append(Inheritance(
            base_name='AIMVersie',
            base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMVersie',
            class_name='LegacyObject',
            class_uri='https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject'
        ))

        lgc_class = OSLOClass(
            label='Legacy Object',
            name='LegacyObject',
            objectUri='https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject',
            deprecated_version='',
            definition='Abstracte voor een Legacy object',
            abstract=1
        )
        oslo_collector.classes.append(lgc_class)
        oslo_collector.class_dict['https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject'] = lgc_class


        for lgc_type_row in tqdm(lgc_type_data):
            class_name = lgc_type_row[2]
            class_uri = lgc_type_row[0]
            if '.' in class_name:
                class_name = class_name.replace('.', '_')
            if '-' in class_name:
                class_name = class_name.replace('-', '_')
            if class_name == "RIS":
                class_name = "RISLegacy"
            elif class_name == 'Fietstel':
                class_name = 'FietstelLegacy'
            elif class_name == 'Brug':
                class_name = 'BeweegbareBrug'
            elif class_name == 'Voedingskeuzeschakelaar':
                class_name = 'VKS'

            oslo_class = OSLOClass(
                objectUri=class_uri,
                name=class_name,
                label=lgc_type_row[1],
                deprecated_version='',
                abstract=False)
            oslo_collector.classes.append(oslo_class)
            oslo_collector.inheritances.append(Inheritance(
                base_name='LegacyObject',
                base_uri='https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject',
                class_name=class_name,
                class_uri=class_uri
            ))
            oslo_collector.class_dict[class_uri] = oslo_class
            try:
                model_name = OTLModelCreator.get_model_name_from_directory_path(directory)
                data_to_write = creator.create_blocks_to_write_from_rows(lgc_type_row=lgc_type_row, model_location=model_name)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {class_name}")
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {class_name}")
                class_directory = 'Classes/Legacy'

                write_to_file(class_name, class_directory, data_to_write, relative_path=directory)
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {class_name}")

        data_to_write = []
        for lgc_type_row in lgc_type_data:
            uri = lgc_type_row[0]
            ns, name = get_ns_and_name_from_uri(uri)
            data_to_write.append(f'from ..Classes.{get_titlecase_from_ns(ns)}.{name} import {name}')

        write_to_file('all_classes', 'Helpers', data_to_write, relative_path=directory, write_mode='a')

        return oslo_collector

