# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlConstructie(KeuzelijstField):
    """De mogelijke beweegbare delen."""
    naam = 'KlConstructie'
    label = 'Beweegbaar deel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlConstructie'
    definition = 'De mogelijke beweegbare delen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlConstructie'
    options = {
        'deur': KeuzelijstWaarde(invulwaarde='deur',
                                 label='deur',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructie/deur'),
        'klep': KeuzelijstWaarde(invulwaarde='klep',
                                 label='klep',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructie/klep'),
        'schuif': KeuzelijstWaarde(invulwaarde='schuif',
                                   label='schuif',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructie/schuif')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

