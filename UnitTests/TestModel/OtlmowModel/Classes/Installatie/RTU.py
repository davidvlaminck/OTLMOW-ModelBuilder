# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class RTU(LegacyObject):
    """Remote terminal unit VMM (Legacy)
	VMM lucht : remote terminal unit meetstation luchtkwaliteit"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RTU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
