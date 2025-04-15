# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class RLC(LegacyObject):
    """Roodlichtcamera installatie (Legacy)
	VHS flitspalen : Installatie Roodlichtcamera - Dit type flitspaal registreert zowel roodlichtnegaties als snelheidsovertredingen. Zij worden opgesteld op kruispunten met verkeerslichten."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RLC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
