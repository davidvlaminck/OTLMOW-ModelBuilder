import logging
import os
import unittest
from pathlib import Path

from otlmow_modelbuilder.ModelBuilder import ModelBuilder


class CreateAllTestCasesTests(unittest.TestCase):
    def test_init_AllCasesTestClass_using_modelbuilder(self):
        current_file_path = Path(__file__)
        base_dir = current_file_path.parent
        otl_subset_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
        GA_location = Path(f'{base_dir}/GeometrieArtefact_AllCasesTestClass.db')

        with self.assertLogs() as captured:
            paths_to_create_test_class = [Path(f'{base_dir}/TestClasses'),
                                          Path(f'{base_dir}/../../OTLMOW-Model/UnitTests/TestClasses'),
                                          Path(f'{base_dir}/../../OTLMOW-Converter/UnitTests/TestClasses'),
                                          Path(f'{base_dir}/../../OTLMOW-Template/UnitTests/TestClasses')
                                          ]
            for path in paths_to_create_test_class:
                ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_location,
                                                 geometry_artefact_location=GA_location,
                                                 directory=path)

            all_cases_class_location = Path(f'{base_dir}/TestClasses/Classes/Onderdeel/AllCasesTestClass.py')
            self.assertTrue(os.path.isfile(all_cases_class_location))

        errors = list(filter(lambda r: r.levelno >= logging.ERROR, list(captured.records)))
        self.assertListEqual([], errors)
