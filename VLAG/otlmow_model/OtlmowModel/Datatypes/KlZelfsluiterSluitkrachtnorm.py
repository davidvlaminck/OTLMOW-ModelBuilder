# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZelfsluiterSluitkrachtnorm(KeuzelijstField):
    """Codelijst met mogelijke waarden voor de sluitkracht van een zefsluiter voor deuren, poorten etc.volgens de bestaande normering."""
    naam = 'KlZelfsluiterSluitkrachtnorm'
    label = 'Zelfsluiter sluitkrachtnorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZelfsluiterSluitkrachtnorm'
    definition = 'Codelijst met mogelijke waarden voor de sluitkracht van een zefsluiter voor deuren, poorten etc.volgens de bestaande normering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZelfsluiterSluitkrachtnorm'
    options = {
        'en-2': KeuzelijstWaarde(invulwaarde='en-2',
                                 label='EN 2',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZelfsluiterSluitkrachtnorm/en-2'),
        'en-4': KeuzelijstWaarde(invulwaarde='en-4',
                                 label='EN 4',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZelfsluiterSluitkrachtnorm/en-4'),
        'en-6': KeuzelijstWaarde(invulwaarde='en-6',
                                 label='EN 6',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZelfsluiterSluitkrachtnorm/en-6')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

