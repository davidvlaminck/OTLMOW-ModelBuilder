# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class SeinbrugDVM(LegacyObject):
    """Seinbrug DVM (Legacy)
	Mechanische contructie DVM installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SeinbrugDVM'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
