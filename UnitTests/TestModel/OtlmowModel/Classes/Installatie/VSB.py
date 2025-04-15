# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class VSB(LegacyObject):
    """Veranderlijke signalisatie borden (Legacy)
	Dynamische borden : Soort van restgroep van allerlei dynamische borden die niet onder een meer specifiek type vallen. Exacte verschil met VGL is me niet duidelijk"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VSB'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
