from pathlib import Path

import pytest

from otlmow_modelbuilder.ModelBuilder import ModelBuilder

OTL_DB = Path(__file__).parent / 'OTL_AllCasesTestClass.db'
GEO_DB = Path(__file__).parent / 'GeometrieArtefact_AllCasesTestClass.db'


def test_build_otl_datamodel_creates_output_directory(tmp_path):
    ModelBuilder.build_otl_datamodel(
        otl_subset_location=OTL_DB,
        directory=tmp_path,
        environment='prd',
        geometry_artefact_location=GEO_DB,
        include_legacy=False,
        include_kl_test_keuzelijst=True,
    )

    assert (tmp_path / 'OtlmowModel').exists()


def test_build_otl_datamodel_defaults_directory_to_package_parent(tmp_path, monkeypatch):
    # directory=None falls back to the package parent directory; monkeypatch
    # create_full_model to avoid writing to the real package location.
    captured = {}

    def fake_create_full_model(directory, environment, settings, oslo_collector,
                               geo_artefact_collector, include_kl_test_keuzelijst, include_legacy):
        captured['directory'] = directory
        captured['environment'] = environment

    monkeypatch.setattr(
        'otlmow_modelbuilder.ModelBuilder.OTLModelCreator.create_full_model', fake_create_full_model)

    ModelBuilder.build_otl_datamodel(
        otl_subset_location=OTL_DB,
        directory=None,
        environment='tei',
        include_legacy=False,
    )

    assert captured['directory'] == Path(__file__).parent.parent / 'otlmow_modelbuilder'
    assert captured['environment'] == 'tei'
