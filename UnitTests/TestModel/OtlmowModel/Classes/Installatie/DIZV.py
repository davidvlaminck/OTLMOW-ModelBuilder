# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class DIZV(LegacyObject):
    """Detectie inbreuken zwaar verkeer (Legacy)
	VHS handhaving : Deze installaties meten de tussenafstand van vrachtwagens en verzamelen opnames en gegevens voor politie die eventueel een vaststelling kan opmaken."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#DIZV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
