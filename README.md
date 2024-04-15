# OTLMOW-ModelBuilder
[![PyPI](https://img.shields.io/pypi/v/otlmow-modelbuilder?label=latest%20release)](https://pypi.org/project/otlmow-modelbuilder/)
[![otlmow-modelbuilder-downloads](https://img.shields.io/pypi/dm/otlmow-modelbuilder)](https://pypi.org/project/otlmow-modelbuilder/)
[![Unittests](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/actions/workflows/unittest.yml/badge.svg)](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/actions/workflows/unittest.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otlmow-modelbuilder)
[![GitHub issues](https://img.shields.io/github/issues/davidvlaminck/OTLMOW-ModelBuilder)](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/issues)
[![coverage](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/blob/master/UnitTests/coverage.svg)](https://htmlpreview.github.io/?https://github.com/davidvlaminck/OTLMOW-ModelBuilder/blob/master/UnitTests/htmlcov/index.html)

## Summary
The main use case of otlmow-modelbuilder is to provide create the class model of otlmow_model, by reading in a OTL SQLite or subset.

## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- [otlmow_model](https://github.com/davidvlaminck/OTLMOW-Model)
- [otlmow_modelbuilder](https://github.com/davidvlaminck/OTLMOW-ModelBuilder) (you are currently looking at this package)
- [otlmow_converter](https://github.com/davidvlaminck/OTLMOW-Converter)
- [otlmow_template](https://github.com/davidvlaminck/OTLMOW-Template)
- [otlmow_postenmapping](https://github.com/davidvlaminck/OTLMOW-PostenMapping)
- [otlmow_davie](https://github.com/davidvlaminck/OTLMOW-DAVIE)
- [otlmow_visuals](https://github.com/davidvlaminck/OTLMOW-Visuals)
- [otlmow_gui](https://github.com/davidvlaminck/OTLMOW-GUI)


## Installation and requirements
OTLMOW-ModelBuilder has one dependency besides the standard Python libraries: rdflib. It will be automatically installed when installing this library. 
Currently, you need at least Python version 3.6 to use this library.

To install the OTL MOW project into your Python project, use pip to install it:
``` 
pip install otlmow_modelbuilder
```
To upgrade an existing installation use:
``` 
pip install otlmow_modelbuilder --upgrade
```

## Usage
In order to create a model, the ModelBuilder requires two Path parameters: 
- otl_subset_location: the location of OTL SQLite file that is used to build the model with (this can be a subset)
- directory: the location where the model will be created

Note that the given directory will be emptied if needed. 

Additionally, it is possible to also add the location of the Geometry Artefact. If used, the classes will inherit from the various geometry type classes to add validation to the property 'geometry'.
```
logging.basicConfig(level=logging.INFO, format='%(message)s')

current_dir = Path(__file__).parent
otl_subset_path = Path(current_dir / 'InputFiles' / 'OTL 2.11.db')
GA_file_path = Path(current_dir / 'InputFiles' / 'Geometrie_Artefact_2.11.db')
model_directory = Path(current_dir.parent.parent / 'OTLMOW-Model/otlmow_model')
settings_path = Path(current_dir / 'settings_otlmow_modelbuilder.json')

ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_path, geometry_artefact_location=GA_file_path,
                                 directory=model_directory, settings_path=settings_path,
                                 environment='prd')
```
