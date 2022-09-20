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


def _init_otl_model_creator(otl_file_location: Path = None, geo_a_file_location: Path = None) -> OTLModelCreator:
    sql_reader = SQLDbReader(otl_file_location)
    oslo_creator = OSLOInMemoryCreator(sql_reader)
    collector = OSLOCollector(oslo_creator)
    geo_artefact_collector = None
    if geo_a_file_location is not None:
        sql_reader_ga = SQLDbReader(geo_a_file_location)
        geo_memory_creator = GeometrieInMemoryCreator(sql_reader_ga)
        geo_artefact_collector = GeometrieArtefactCollector(geo_memory_creator)
    return OTLModelCreator(collector, geo_artefact_collector)


def _create_otl_datamodel(model_creator: OTLModelCreator, directory: Path = None, environment: str = ''):
    model_creator.oslo_collector.collect()
    if model_creator.geo_artefact_collector is not None:
        model_creator.geo_artefact_collector.collect()
    if directory is None:
        this_file_path = Path(__file__)
        directory = this_file_path.parents[1]
    model_creator.create_full_model(directory=directory, environment=environment)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.handlers = [
        logging.FileHandler(r'logs.txt'),
        logging.StreamHandler(sys.stdout)
    ]

    current_file_path = Path(__file__)
    base_dir = current_file_path.parents[0]
    settings_file_location = Path(f'{base_dir}/settings_OTLMOW.json')
    otl_file_path = Path(f'{base_dir}/InputFiles/OTL 2.4.db')
    GA_file_path = Path(f'{base_dir}/InputFiles/Geometrie_Artefact_2.4.db')

    model_creator_instance = _init_otl_model_creator(otl_file_location=otl_file_path, geo_a_file_location=GA_file_path)
    _create_otl_datamodel(directory=Path(f'{base_dir}/../../OTLMOW-Model/otlmow_model'),
                          model_creator=model_creator_instance, environment='prd')
