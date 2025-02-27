# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerstekenWettelijkeStatus(KeuzelijstField):
    """Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven."""
    naam = 'KlVerkeerstekenWettelijkeStatus'
    label = 'VerkeerstekenWettelijkeStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeerstekenWettelijkeStatus'
    definition = 'Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerstekenWettelijkeStatus'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

