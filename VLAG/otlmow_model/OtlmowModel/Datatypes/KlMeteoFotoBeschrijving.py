# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeteoFotoBeschrijving(KeuzelijstField):
    """De mogelijke beschrijvingen voor meteo-gerelateerde foto's."""
    naam = 'KlMeteoFotoBeschrijving'
    label = 'Meteo foto beschrijving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMeteoFotoBeschrijving'
    definition = "De mogelijke beschrijvingen voor meteo-gerelateerde foto's."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeteoFotoBeschrijving'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

