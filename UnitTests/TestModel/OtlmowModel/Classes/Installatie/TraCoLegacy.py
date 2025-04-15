# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class TraCoLegacy(LegacyObject):
    """Trajectcontrole (Legacy)
	Trajectcontrole (meet gemiddelde snelheid van voertuigen over een bepaald traject)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#TraCoLegacy'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
