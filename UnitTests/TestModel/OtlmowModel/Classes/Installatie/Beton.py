# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Beton(LegacyObject):
    """Betonstructuur (Legacy)
	Dit is voor als een techniek aan een tunnel, een tunnelwand of en brug gemonteerd is"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Beton'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
