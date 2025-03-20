# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondtoevoegsel(KeuzelijstField):
    """De eventuele toevoegsels bij de grond."""
    naam = 'KlGrondtoevoegsel'
    label = 'Grondtoevoegsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrondtoevoegsel'
    definition = 'De eventuele toevoegsels bij de grond.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondtoevoegsel'
    options = {
        'cement': KeuzelijstWaarde(invulwaarde='cement',
                                   label='cement',
                                   status='ingebruik',
                                   definitie='Cement als toevoegsel.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondtoevoegsel/cement'),
        'kalk': KeuzelijstWaarde(invulwaarde='kalk',
                                 label='kalk',
                                 status='ingebruik',
                                 definitie='Kalk als toevoegsel bij de grond.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondtoevoegsel/kalk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

