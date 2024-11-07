import cProfile
import logging
from pathlib import Path

from otlmow_modelbuilder.ModelBuilder import ModelBuilder


def create_model():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    current_dir = Path(__file__).parent
    otl_subset_path = Path(current_dir.parent / 'InputFiles' / 'latest' / 'OTL.db')
    GA_file_path = Path(current_dir.parent / 'InputFiles' / 'latest' / 'Geometrie_Artefact.db')
    model_directory = Path(current_dir.parent.parent / 'OTLMOW-Model/otlmow_model')

    ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_path, geometry_artefact_location=GA_file_path,
                                     directory=model_directory, environment='prd')


if __name__ == '__main__':
    #cProfile.run('create_model()')
    create_model()
