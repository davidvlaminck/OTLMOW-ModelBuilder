import logging
import sys
from pathlib import Path

from otlmow_modelbuilder.ModelBuilder import ModelBuilder

logging.warning = print
logging.error = print


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.handlers = [
        logging.FileHandler(r'logs.txt'),
        logging.StreamHandler(sys.stdout)
    ]

    base_dir = Path(__file__).parent
    otl_subset_path = Path(f'{base_dir}/InputFiles/OTL 2.5.db')
    GA_file_path = Path(f'{base_dir}/InputFiles/Geometrie_Artefact_2.5.db')

    ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_path, geometry_artefact_location=GA_file_path,
                                     directory=Path(base_dir.parent.parent / "OTLMOW-Model/otlmow_model"))
