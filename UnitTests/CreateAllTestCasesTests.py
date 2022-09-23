import logging
import os
import unittest
from pathlib import Path

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
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
            oslo_collector, geo_artefact_collector = self._init_otl_model_creator(otl_file_location=subset_file_location)

            paths_to_create_test_class = [Path(f'{base_dir}/TestClasses'), Path(f'{base_dir}/../../OTLMOW-Model/UnitTests/TestClasses'), Path(f'{base_dir}/../../OTLMOW-Converter/UnitTests/TestClasses')]
            for path in paths_to_create_test_class:
                self._create_otl_datamodel(directory=path, oslo_collector=oslo_collector,
                                           geo_artefact_collector=geo_artefact_collector)
            all_cases_class_location = Path(f'{base_dir}/TestClasses/Classes/Onderdeel/AllCasesTestClass.py')
            self.assertTrue(os.path.isfile(all_cases_class_location))

        errors = list(filter(lambda r: r.levelno >= logging.ERROR, list(captured.records)))
        self.assertListEqual([], errors)

    @staticmethod
    def _init_otl_model_creator(otl_file_location: Path = None, geo_a_file_location: Path = None) -> (OSLOCollector, GeometrieArtefactCollector):
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        geo_artefact_collector = None
        if geo_a_file_location is not None:
            sql_reader_ga = SQLDbReader(geo_a_file_location)
            geo_memory_creator = GeometrieInMemoryCreator(sql_reader_ga)
            geo_artefact_collector = GeometrieArtefactCollector(geo_memory_creator)
        return collector, geo_artefact_collector

    @staticmethod
    def _create_otl_datamodel(oslo_collector, geo_artefact_collector, directory: Path = None, environment: str = ''):
        oslo_collector.collect()
        if geo_artefact_collector is not None:
            geo_artefact_collector.collect()
        if directory is None:
            this_file_path = Path(__file__)
            directory = this_file_path.parents[1]
        OTLModelCreator.create_full_model(directory=directory, environment=environment, oslo_collector=oslo_collector,
                                          geo_artefact_collector=geo_artefact_collector)
