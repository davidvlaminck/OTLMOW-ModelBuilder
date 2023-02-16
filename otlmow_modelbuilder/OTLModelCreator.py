import concurrent.futures
import logging
import os
import shutil
from concurrent.futures import FIRST_COMPLETED
from datetime import datetime
from os import path
from pathlib import Path
from typing import Dict

from tqdm import tqdm

from otlmow_modelbuilder.GenericBuilderFunctions import write_to_file
from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector


class OTLModelCreator:
    def __init__(self, oslo_collector: OSLOCollector, geo_artefact_collector: GeometrieArtefactCollector = None):
        self.oslo_collector = oslo_collector
        self.geo_artefact_collector = geo_artefact_collector

    @staticmethod
    def create_full_model(directory: Path, oslo_collector, geo_artefact_collector, settings: Dict, environment: str = ''):
        logging.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        OTLModelCreator.check_and_create_subdirectories(directory)
        oslo_collector.query_correct_base_classes()
        OTLModelCreator.check_for_nested_attributes_in_classes(collector=oslo_collector,
                                                               known_classes_uris=settings['nested_list_class_uris'])
        OTLModelCreator.create_primitive_datatypes(
            directory=directory, oslo_collector=oslo_collector,
            primitive_datatype_validation_rules=settings['primitive_datatype_validation_rules'])
        OTLModelCreator.create_complex_datatypes(
            directory=directory, oslo_collector=oslo_collector,
            complex_datatype_validation_rules=settings['complex_datatype_validation_rules'])
        OTLModelCreator.create_union_datatypes(
            directory=directory, oslo_collector=oslo_collector,
            union_datatype_validation_rules=settings['union_datatype_validation_rules'])
        OTLModelCreator.create_enumerations(
            directory=directory, environment=environment, oslo_collector=oslo_collector,
            enumeration_validation_rules=settings['enumeration_validation_rules'])
        OTLModelCreator.create_classes(
            directory=directory, oslo_collector=oslo_collector, geo_artefact_collector=geo_artefact_collector,
            valid_uri_and_types=settings['complex_datatype_validation_rules']['valid_uri_and_types'])
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
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {prim_datatype.name}")
                    pass
                write_to_file(prim_datatype, 'Datatypes', data_to_write, relative_path=directory)
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {prim_datatype.name}")

    @staticmethod
    def get_model_name_from_directory_path(directory):
        if directory.name == 'TestClasses':
            return directory.parent.name + '.' + directory.name
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
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {complex_datatype.name}")
                    pass
                write_to_file(complex_datatype, 'Datatypes', data_to_write, relative_path=directory)
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
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {union_datatype.name}")
                    pass
                write_to_file(union_datatype, 'Datatypes', data_to_write, relative_path=directory)
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {union_datatype.name}")

    @staticmethod
    def create_enumerations(directory, oslo_collector, enumeration_validation_rules, environment: str = ''):
        creator = OTLEnumerationCreator(oslo_collector)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(OTLModelCreator.create_enumeration, creator=creator, directory=directory,
                                       enumeration=enumeration, environment=environment,
                                       enumeration_validation_rules=enumeration_validation_rules): enumeration for
                       enumeration in oslo_collector.enumerations}
            with tqdm(total=len(futures)) as pbar:
                while len(futures) > 0:
                    new_futures = {}
                    done, pending = concurrent.futures.wait(futures, return_when=FIRST_COMPLETED, timeout=60)
                    for fut in done:
                        if fut.exception():
                            enumeration = futures[fut]
                            new_futures[executor.submit(OTLModelCreator.create_enumeration, creator=creator,
                                                        directory=directory, enumeration=enumeration,
                                                        environment=environment,
                                                        enumeration_validation_rules=enumeration_validation_rules)] = job
                        else:
                            pbar.update()
                    for fut in pending:
                        job = futures[fut]
                        new_futures[fut] = job
                    futures = new_futures

    @staticmethod
    def create_enumeration(creator, directory, enumeration, environment, enumeration_validation_rules):
        try:
            model_name = OTLModelCreator.get_model_name_from_directory_path(directory)
            data_to_write = creator.create_block_to_write_from_enumerations(
                enumeration, environment=environment, enumeration_validation_rules=enumeration_validation_rules)
            if data_to_write is None:
                logging.error(f"Could not create a class for {enumeration.name}")
                pass
            if len(data_to_write) == 0:
                logging.error(f"Could not create a class for {enumeration.name}")
                pass
            write_to_file(enumeration, 'Datatypes', data_to_write, relative_path=directory)
            # logging.info(f"Created a class for {enumeration.name}")
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
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {oslo_class.name}")
                    pass

                class_directory = 'Classes'
                ns = None
                if oslo_class.objectUri != 'http://purl.org/dc/terms/Agent':
                    ns, name = get_ns_and_name_from_uri(oslo_class.objectUri)
                if ns is not None:
                    class_directory = get_class_directory_from_ns(ns)

                write_to_file(oslo_class, class_directory, data_to_write, relative_path=directory)
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {oslo_class.name}")

    @staticmethod
    def check_and_create_subdirectories(directory: Path):
        if not path.exists(directory):
            os.makedirs(directory)
        if not path.exists(directory):
            raise OSError(f'The directory {directory} does not exist. Please create it first.')
        if not path.isdir(directory):
            raise NotADirectoryError(f'{directory} is not a directory.')

        OTLModelCreator.clean_directory(directory)

        if not path.exists(directory / 'Classes'):
            os.mkdir(directory / 'Classes')
        if not path.exists(directory / 'Datatypes'):
            os.mkdir(directory / 'Datatypes')

        if not path.exists(directory / 'Classes/Abstracten'):
            os.mkdir(directory / 'Classes/Abstracten')
        if not path.exists(directory / 'Classes/ImplementatieElement'):
            os.mkdir(directory / 'Classes/ImplementatieElement')
        if not path.exists(directory / 'Classes/Installatie'):
            os.mkdir(directory / 'Classes/Installatie')
        if not path.exists(directory / 'Classes/Levenscyclus'):
            os.mkdir(directory / 'Classes/Levenscyclus')
        if not path.exists(directory / 'Classes/Onderdeel'):
            os.mkdir(directory / 'Classes/Onderdeel')
        if not path.exists(directory / 'Classes/ProefEnMeting'):
            os.mkdir(directory / 'Classes/ProefEnMeting')

    @staticmethod
    def clean_directory(directory):
        for subdir in ['Classes', 'Datatypes']:
            if not path.exists(subdir):
                continue
            dir_path = os.path.join(directory, subdir)
            try:
                shutil.rmtree(dir_path)
            except Exception as e:
                print(f'Failed to delete {subdir}. Reason: {e}')

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
