# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Z30(LegacyObject):
    """Zone30 (Legacy)
	Dynamische borden : automatische zone 30 installatie (omvat alle infrastructuur horend bij 1 sturingskast met inbegrip van één of meerdere borden)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Z30'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
