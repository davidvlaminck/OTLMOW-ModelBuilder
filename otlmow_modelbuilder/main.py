import logging
import sys
from pathlib import Path

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

logging.warning = print
logging.error = print


def _init_otl_model_creator(otl_file_location: Path = None, geo_a_file_location: Path = None) -> (
OSLOCollector, GeometrieArtefactCollector):
    sql_reader = SQLDbReader(otl_file_location)
    oslo_creator = OSLOInMemoryCreator(sql_reader)
    collector = OSLOCollector(oslo_creator)
    geo_artefact_collector = None
    if geo_a_file_location is not None:
        sql_reader_ga = SQLDbReader(geo_a_file_location)
        geo_memory_creator = GeometrieInMemoryCreator(sql_reader_ga)
        geo_artefact_collector = GeometrieArtefactCollector(geo_memory_creator)
    return collector, geo_artefact_collector


def _create_otl_datamodel(oslo_collector, geo_artefact_collector, directory: Path = None, environment: str = ''):
    oslo_collector.collect()
    if geo_artefact_collector is not None:
        geo_artefact_collector.collect()
    if directory is None:
        this_file_path = Path(__file__)
        directory = this_file_path.parents[1]
    OTLModelCreator.create_full_model(directory=directory, environment=environment, oslo_collector=oslo_collector,
                                      geo_artefact_collector=geo_artefact_collector)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.handlers = [
        logging.FileHandler(r'logs.txt'),
        logging.StreamHandler(sys.stdout)
    ]

    current_file_path = Path(__file__)
    base_dir = current_file_path.parents[0]
    settings_file_location = Path(f'{base_dir}/settings_OTLMOW.json')
    otl_file_path = Path(f'{base_dir}/InputFiles/OTL 2.5.db')
    GA_file_path = Path(f'{base_dir}/InputFiles/Geometrie_Artefact_2.5.db')

    oslo_collector, geo_artefact_collector = _init_otl_model_creator(otl_file_location=otl_file_path,
                                                                     geo_a_file_location=GA_file_path)
    _create_otl_datamodel(directory=Path(f'{base_dir}/../../OTLMOW-Model/otlmow_model'), environment='prd',
                          oslo_collector=oslo_collector, geo_artefact_collector=geo_artefact_collector)
