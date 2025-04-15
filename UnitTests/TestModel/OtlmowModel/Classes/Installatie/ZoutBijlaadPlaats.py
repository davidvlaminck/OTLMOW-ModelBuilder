# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class ZoutBijlaadPlaats(LegacyObject):
    """ZBP (Legacy)
	Bewaakt terrein om zout en pekel te stockeren en te laden."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#ZoutBijlaadPlaats'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
