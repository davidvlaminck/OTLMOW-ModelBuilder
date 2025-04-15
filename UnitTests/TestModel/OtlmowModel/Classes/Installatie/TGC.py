# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class TGC(LegacyObject):
    """Toegangscontrole aannemer (Legacy)
	Toegangscontrole (gedeelte waarvoor de onderhoudsaannemer dient tussen te komen)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#TGC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
