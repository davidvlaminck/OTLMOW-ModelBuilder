# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCompacteBatterijModelnaam(KeuzelijstField):
    """De modelnaam van de compacte batterij."""
    naam = 'KlCompacteBatterijModelnaam'
    label = 'Compacte batterij modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCompacteBatterijModelnaam'
    definition = 'De modelnaam van de compacte batterij.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCompacteBatterijModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

