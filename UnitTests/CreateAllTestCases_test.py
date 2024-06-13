import logging
import os
import site
import warnings
from pathlib import Path

import pytest

from otlmow_modelbuilder.ModelBuilder import ModelBuilder


def test_init_AllCasesTestClass_using_modelbuilder(subtests, caplog):
    current_file_path = Path(__file__)
    base_dir = current_file_path.parent
    otl_subset_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    ga_location = Path(f'{base_dir}/GeometrieArtefact_AllCasesTestClass.db')

    paths_to_create_test_class = [base_dir / 'TestModel',
                                  base_dir.parent.parent / 'OTLMOW-Model/UnitTests/TestModel',
                                  base_dir.parent.parent / 'OTLMOW-Converter/UnitTests/TestModel',
                                  base_dir.parent.parent / 'OTLMOW-Template/UnitTests/TestModel']

    for path in paths_to_create_test_class:
        with subtests.test(msg=f'Creating testclasses for {path}'):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=DeprecationWarning)  # supress deprecation warnings from tqdm
                try:
                    ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_location,
                                                     geometry_artefact_location=ga_location,
                                                     directory=path)
                except PermissionError:
                    logging.info(f'PermissionError for {path}, skipping this test because it is not applicable')
                    continue

        all_cases_class_location = path / 'OtlmowModel' / 'Classes' / 'Onderdeel' / 'AllCasesTestClass.py'
        assert os.path.isfile(all_cases_class_location)


    otl_subset_location_no_double_kard = base_dir / 'OTL_AllCasesTestClass_no_double_kard.db'
    paths_to_create_test_class_no_double_kard = [base_dir.parent.parent / 'OTLMOW-Template/UnitTests/TestModel']

    for path in paths_to_create_test_class_no_double_kard:
        with subtests.test(msg=f'Creating testclasses for {path}'):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=DeprecationWarning)  # supress deprecation warnings from tqdm
                try:
                    ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_location_no_double_kard,
                                                     geometry_artefact_location=ga_location,
                                                     directory=path)
                except PermissionError:
                    logging.info(f'PermissionError for {path}, skipping this test because it is not applicable')
                    continue

        all_cases_class_location = path / 'OtlmowModel' / 'Classes' / 'Onderdeel' / 'AllCasesTestClass.py'
        assert os.path.isfile(all_cases_class_location)

    assert len(caplog.records) == 0
