# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class WIM(LegacyObject):
    """Weigh-In-Motion (Legacy)
	Weigh-In-Motion installatie (meet en detecteert rijdende vrachtwagens die overladen zijn)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#WIM'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
