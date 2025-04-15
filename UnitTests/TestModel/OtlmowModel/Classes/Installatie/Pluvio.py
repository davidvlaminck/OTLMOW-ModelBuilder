# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Pluvio(LegacyObject):
    """Neerslagmeetinstallatie (Legacy)
	Water : Neerslagmeetinstallatie (omvat één of meerdere pluviometers en alle locaal opgestelde apparatuur mee te onderhouden door aannemer neerslagmeetinstallatie)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Pluvio'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
