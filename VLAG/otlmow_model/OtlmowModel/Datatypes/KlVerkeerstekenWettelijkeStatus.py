# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
        'test-wettelijke-status': KeuzelijstWaarde(invulwaarde='test-wettelijke-status',
                                                   label='test wettelijke status',
                                                   status='ingebruik',
                                                   definitie='test wettelijke status',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerstekenWettelijkeStatus/test-wettelijke-status')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

