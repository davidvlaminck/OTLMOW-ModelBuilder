# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlantwijze(KeuzelijstField):
    """De mogelijke (aanplant)plantmanieren."""
    naam = 'KlPlantwijze'
    label = 'Plantwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPlantwijze'
    definition = 'De mogelijke (aanplant)plantmanieren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantwijze'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

