import logging
from pathlib import Path

from otlmow_modelbuilder.ModelBuilder import ModelBuilder

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    current_dir = Path(__file__).parent
    otl_subset_path = Path(current_dir / 'InputFiles' / 'OTL 2.11.db')
    GA_file_path = Path(current_dir / 'InputFiles' / 'Geometrie_Artefact_2.11.db')
    model_directory = Path(current_dir.parent.parent / 'OTLMOW-Model/otlmow_model')
    settings_path = Path(current_dir / 'settings_otlmow_modelbuilder.json')

    ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_path, geometry_artefact_location=GA_file_path,
                                     directory=model_directory, settings_path=settings_path,
                                     environment='prd')
