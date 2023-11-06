from pathlib import Path

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SettingsManager import load_settings


class ModelBuilder:
    @staticmethod
    def build_otl_datamodel(otl_subset_location: Path,
                            directory: Path,
                            environment: str = 'prd',
                            geometry_artefact_location: Path = None,
                            settings_path: Path = None):
        if directory is None:
            this_file_path = Path(__file__)
            directory = this_file_path.parent

        subset_collector = OSLOCollector(otl_subset_location)
        subset_collector.collect_all()

        geo_artefact_collector = None
        if geometry_artefact_location is not None:
            geo_artefact_collector = GeometrieArtefactCollector(geometry_artefact_location)

        if geo_artefact_collector is not None:
            geo_artefact_collector.collect_all()

        settings = load_settings(settings_path)

        OTLModelCreator.create_full_model(directory=directory, environment=environment, settings=settings,
                                          oslo_collector=subset_collector,
                                          geo_artefact_collector=geo_artefact_collector)
