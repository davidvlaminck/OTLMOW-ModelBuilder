import logging
import os
from datetime import datetime
from os import path
from os.path import abspath

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator


class NewOTLBaseClassNotImplemented(NotImplementedError):
    pass


class OTLModelCreator:
    def __init__(self, oslo_collector: OSLOCollector, geo_artefact_collector: GeometrieArtefactCollector = None):
        self.oslo_collector = oslo_collector
        self.geo_artefact_collector = geo_artefact_collector
        logging.info("Created an instance of OTLModelCreator")

    def create_full_model(self, directory, environment: str = ''):
        logging.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        directory = abspath(directory)
        self.check_and_create_subdirectories(directory)
        self.query_correct_base_classes()
        self.create_primitive_datatypes(directory=directory)
        self.create_complex_datatypes(directory=directory)
        self.create_union_datatypes(directory=directory)
        self.create_enumerations(directory=directory, environment=environment)
        self.create_classes(model_directory=directory)
        logging.info('finished creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def create_primitive_datatypes(self, directory):
        creator = OTLPrimitiveDatatypeCreator(self.oslo_collector)

        for prim_datatype in self.oslo_collector.primitive_datatypes:
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
                data_to_write = creator.create_block_to_write_from_primitive_types(prim_datatype, model_location=directory)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {prim_datatype.name}")
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {prim_datatype.name}")
                    pass
                creator.write_to_file(prim_datatype, 'Datatypes', data_to_write, relative_path=directory)
                logging.info(f"Created a class for {prim_datatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {prim_datatype.name}")

    def create_complex_datatypes(self, directory):
        creator = OTLComplexDatatypeCreator(self.oslo_collector)

        for complex_datatype in self.oslo_collector.complex_datatypes:
            try:
                data_to_write = creator.CreateBlockToWriteFromComplexTypes(complex_datatype, model_location=directory)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {complex_datatype.name}")
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {complex_datatype.name}")
                    pass
                creator.write_to_file(complex_datatype, 'Datatypes', data_to_write, relative_path=directory)
                logging.info(f"Created a class for {complex_datatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {complex_datatype.name}")

    def create_union_datatypes(self, directory):
        creator = OTLUnionDatatypeCreator(self.oslo_collector)

        for union_datatype in self.oslo_collector.union_datatypes:
            try:
                data_to_write = creator.create_block_to_write_from_union_types(union_datatype, model_location=directory)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {union_datatype.name}")
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {union_datatype.name}")
                    pass
                creator.write_to_file(union_datatype, 'Datatypes', data_to_write, relative_path=directory)
                logging.info(f"Created a class for {union_datatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {union_datatype.name}")

    def create_enumerations(self, directory, environment: str = ''):
        creator = OTLEnumerationCreator(self.oslo_collector)

        for enumeration in self.oslo_collector.enumerations:

            try:
                data_to_write = creator.create_block_to_write_from_enumerations(enumeration, environment=environment)
                if data_to_write is None:
                    logging.info(f"Could not create a class for {enumeration.name}")
                    pass
                if len(data_to_write) == 0:
                    logging.info(f"Could not create a class for {enumeration.name}")
                    pass
                creator.write_to_file(enumeration, 'Datatypes', data_to_write, relative_path=directory)
                logging.info(f"Created a class for {enumeration.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {enumeration.name}")

    def create_classes(self, model_directory):
        creator = OTLClassCreator(self.oslo_collector, self.geo_artefact_collector)

        for oslo_class in self.oslo_collector.classes:
            try:
                data_to_write = creator.create_blocks_to_write_from_classes(oslo_class, model_location=model_directory)
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

                creator.write_to_file(oslo_class, class_directory, data_to_write, relative_path=model_directory)
                logging.info(f"Created a class for {oslo_class.name}")
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {oslo_class.name}")

    def query_correct_base_classes(self):
        result = self.oslo_collector.memory_creator.check_on_base_classes()
        if result != 0:
            raise NewOTLBaseClassNotImplemented()

    def check_and_create_subdirectories(self, directory):
        if not path.exists(directory):
            raise OSError(f'The directory {directory} does not exist. Please create it first.')
        if not path.isdir(directory):
            raise NotADirectoryError(f'{directory} is not a directory.')

        if not path.exists(directory + '/Classes'):
            os.mkdir(directory + '/Classes')
        if not path.exists(directory + '/Datatypes'):
            os.mkdir(directory + '/Datatypes')

        if not path.exists(directory + '/Classes/Abstracten'):
            os.mkdir(directory + '/Classes/Abstracten')
        if not path.exists(directory + '/Classes/ImplementatieElement'):
            os.mkdir(directory + '/Classes/ImplementatieElement')
        if not path.exists(directory + '/Classes/Installatie'):
            os.mkdir(directory + '/Classes/Installatie')
        if not path.exists(directory + '/Classes/Levenscyclus'):
            os.mkdir(directory + '/Classes/Levenscyclus')
        if not path.exists(directory + '/Classes/Onderdeel'):
            os.mkdir(directory + '/Classes/Onderdeel')
        if not path.exists(directory + '/Classes/ProefEnMeting'):
            os.mkdir(directory + '/Classes/ProefEnMeting')
