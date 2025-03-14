# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonetype(KeuzelijstField):
    """TODO"""
    naam = 'KlZonetype'
    label = 'Zonetype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlZonetype'
    definition = 'TODO'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonetype'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

