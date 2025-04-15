# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Wilddet(LegacyObject):
    """Wilddetectiesysteem (Legacy)
	Een wilddetectiesysteem zal de weggebruikers waarschuwen bij de aanwezigheid van eventueel overstekend wild"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Wilddet'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
