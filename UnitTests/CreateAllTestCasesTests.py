import logging
import os
import unittest
from pathlib import Path

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class CreateAllTestCasesTests(unittest.TestCase):
    def test_init_AllCasesTestClass(self):
        current_file_path = Path(__file__)
        base_dir = current_file_path.parents[0]
        settings_file_location = Path(f'{base_dir}/settings_OTLMOW.json')
        subset_file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')

        with self.assertLogs() as captured:
            model_creator = self._init_otl_model_creator(otl_file_location=subset_file_location)
            self._create_otl_datamodel(directory=Path(f'{base_dir}/TestClasses'), model_creator=model_creator)
            self._create_otl_datamodel(directory=Path(f'{base_dir}/../../OTLMOW-Model/UnitTests/TestClasses'), model_creator=model_creator)
            allcasesclass_location = Path(f'{base_dir}/TestClasses/Classes/Onderdeel/AllCasesTestClass.py')
            self.assertTrue(os.path.isfile(allcasesclass_location))

        errors = list(filter(lambda r: r.levelno >= logging.ERROR, list(captured.records)))
        self.assertListEqual([], errors)

    @unittest.skip
    def test_use_AllCasesTestClass(self):
        instance = AssetFactory.dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                                                                 directory='UnitTests.TestClasses.OTLModel.Classes')
        self.assertIsInstance(instance, AllCasesTestClass)

    @staticmethod
    def _init_otl_model_creator(otl_file_location: Path = None, geoA_file_location: Path = None) -> OTLModelCreator:
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        geo_artefact_collector = None
        if geoA_file_location != None:
            sql_reader_GA = SQLDbReader(geoA_file_location)
            geo_memory_creator = GeometrieInMemoryCreator(sql_reader_GA)
            geo_artefact_collector = GeometrieArtefactCollector(geo_memory_creator)
        return OTLModelCreator(collector, geo_artefact_collector)

    @staticmethod
    def _create_otl_datamodel(model_creator: OTLModelCreator, directory: Path = None, environment: str = ''):
        model_creator.oslo_collector.collect()
        if model_creator.geo_artefact_collector is not None:
            model_creator.geo_artefact_collector.collect()
        if directory == None:
            current_file_path = Path(__file__)
            directory = current_file_path.parents[1]
        model_creator.create_full_model(directory=directory, environment=environment)
