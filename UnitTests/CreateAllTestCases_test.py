import os
import warnings
from pathlib import Path

import pytest

from otlmow_modelbuilder.ModelBuilder import ModelBuilder


def test_init_AllCasesTestClass_using_modelbuilder(subtests, caplog):
    current_file_path = Path(__file__)
    base_dir = current_file_path.parent
    otl_subset_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    ga_location = Path(f'{base_dir}/GeometrieArtefact_AllCasesTestClass.db')

    paths_to_create_test_class = [Path(f'{base_dir}/TestClasses'),
                                  Path(f'{base_dir}/../../OTLMOW-Model/UnitTests/TestClasses'),
                                  Path(f'{base_dir}/../../OTLMOW-Converter/UnitTests/TestClasses'),
                                  Path(f'{base_dir}/../../OTLMOW-Template/UnitTests/TestClasses')]

    for path in paths_to_create_test_class:
        with subtests.test(msg=f'Creating testclasses for {path}'):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=DeprecationWarning)  # supress deprecation warnings from tqdm
                ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_location,
                                                 geometry_artefact_location=ga_location,
                                                 directory=path)

        all_cases_class_location = Path(path / 'Classes/Onderdeel/AllCasesTestClass.py')
        assert os.path.isfile(all_cases_class_location)

    assert len(caplog.records) == 0
