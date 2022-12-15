# OTLMOW-ModelBuilder
[![PyPI](https://img.shields.io/pypi/v/otlmow-modelbuilder?label=latest%20release)](https://pypi.org/project/otlmow-modelbuilder/)
[![otlmow-modelbuilder-downloads](https://img.shields.io/pypi/dm/otlmow-modelbuilder)](https://pypi.org/project/otlmow-modelbuilder/)
[![Unittests](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/actions/workflows/unittest.yml/badge.svg)](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/actions/workflows/unittest.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otlmow-modelbuilder)
[![GitHub issues](https://img.shields.io/github/issues/davidvlaminck/OTLMOW-ModelBuilder)](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/issues)

## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- otlmow_model
- otlmow_modelbuilder (you are currently looking at this package)
- otlmow_converter 
- otlmow-template
- otlmow-postenmapping

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
#TODO