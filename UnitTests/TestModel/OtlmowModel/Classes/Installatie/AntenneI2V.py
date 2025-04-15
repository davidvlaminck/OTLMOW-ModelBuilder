# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class AntenneI2V(LegacyObject):
    """Antenne I2V (Legacy)
	Road side unit (RSU) voor ITS-G5 broadcasting. Deze antenne faciliteert in Infrastructuur-naar-Voertuig (I2V) communicatie."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AntenneI2V'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
