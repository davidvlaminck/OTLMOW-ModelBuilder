# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSoortSteun(KeuzelijstField):
    """TODO"""
    naam = 'KlSoortSteun'
    label = 'Soort steun'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSoortSteun'
    definition = 'TODO'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSoortSteun'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

