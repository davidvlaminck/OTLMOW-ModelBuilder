# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Winter(LegacyObject):
    """Winter (Legacy)
	Specifiek meldingstype wegen winterdienst : aangepaste voorspelling meteo - DRINGENDE INFO WINTERDIENST VOORSPELLING METEO"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Winter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
