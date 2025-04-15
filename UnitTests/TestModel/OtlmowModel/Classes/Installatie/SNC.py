# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class SNC(LegacyObject):
    """Snelheidscamera installatie (Legacy)
	VHS flitspalen : Installatie snelheidscamera's : dit type flitspaal registreert snelheidsovertredingen, wordt opgesteld langs de weg"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SNC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
