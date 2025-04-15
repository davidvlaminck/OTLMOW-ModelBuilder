# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Turbine(LegacyObject):
    """Pompturbine (Legacy)
	Pompturbine"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Turbine'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
