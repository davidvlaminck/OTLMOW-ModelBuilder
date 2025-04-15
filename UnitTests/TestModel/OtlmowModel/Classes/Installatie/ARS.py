# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class ARS(LegacyObject):
    """Uitleesapparatuur camera (Legacy)
	VHS flitspalen : Set uitleesapparatuur  (viewer, scherm, printer, bedieningspaneel, voedingen en kabels) in gebruik bij lokale politie voor uitlezen beelden oudere generatie onbemande verkeerscameras (niet digitale)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#ARS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
