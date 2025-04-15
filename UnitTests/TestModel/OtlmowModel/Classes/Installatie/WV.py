# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class WV(LegacyObject):
    """Wegverlichtingsinstallatie (Legacy)
	Wegverlichtingsinstallatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#WV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
