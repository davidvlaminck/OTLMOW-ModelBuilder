from pathlib import Path

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class ModelBuilder:
    @staticmethod
    def build_otl_datamodel(otl_subset_location: Path,
                            directory: Path,
                            environment: str = 'prd',
                            geometry_artefact_location: Path = None):
        if directory is None:
            this_file_path = Path(__file__)
            directory = this_file_path.parent

        sql_reader = SQLDbReader(otl_subset_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        subset_collector = OSLOCollector(oslo_creator)
        geo_artefact_collector = None
        if geometry_artefact_location is not None:
            sql_reader_ga = SQLDbReader(geometry_artefact_location)
            geo_memory_creator = GeometrieInMemoryCreator(sql_reader_ga)
            geo_artefact_collector = GeometrieArtefactCollector(geo_memory_creator)

        subset_collector.collect()
        if geo_artefact_collector is not None:
            geo_artefact_collector.collect()

        OTLModelCreator.create_full_model(directory=directory, environment=environment,
                                          oslo_collector=subset_collector,
                                          geo_artefact_collector=geo_artefact_collector)
