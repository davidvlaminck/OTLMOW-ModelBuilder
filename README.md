# OTLMOW-ModelBuilder
[![PyPI](https://img.shields.io/pypi/v/otlmow-modelbuilder?label=latest%20release)](https://pypi.org/project/otlmow-modelbuilder/)
[![otlmow-modelbuilder-downloads](https://img.shields.io/pypi/dm/otlmow-modelbuilder)](https://pypi.org/project/otlmow-modelbuilder/)
[![Unittests](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/actions/workflows/unittest.yml/badge.svg)](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/actions/workflows/unittest.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otlmow-modelbuilder)
[![GitHub issues](https://img.shields.io/github/issues/davidvlaminck/OTLMOW-ModelBuilder)](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/issues)
[![coverage](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/blob/master/UnitTests/coverage.svg)](https://htmlpreview.github.io/?https://github.com/davidvlaminck/OTLMOW-ModelBuilder/blob/master/UnitTests/htmlcov/index.html)

## Summary
The main use case of otlmow-modelbuilder is to provide create the class model of otlmow_model, by reading in a OTL SQLite or subset.

## Code examples and usage
See the [Readme notebook](https://github.com/davidvlaminck/OTLMOW-ModelBuilder/blob/master/Readme.ipynb). This notebook contains an example on how to generate a model given an OTL SQLite.

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

## Installation
I recommend working with uv. Install this first:
``` 
pip install uv
```
Then install this package by using the uv pip install command:
``` 
uv pip install otlmow-modelbuilder
```
If you are a developer, use this command to install the dependencies, including those needed to run the test suite.
``` 
uv pip install -r pyproject.toml --extra test
``` 