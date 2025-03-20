# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondwerksoorten(KeuzelijstField):
    """Soorten van grondwerk."""
    naam = 'KlGrondwerksoorten'
    label = 'Grondwerksoorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrondwerksoorten'
    definition = 'Soorten van grondwerk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondwerksoorten'
    options = {
        'afdekking': KeuzelijstWaarde(invulwaarde='afdekking',
                                      label='afdekking',
                                      status='ingebruik',
                                      definitie='Grond voor afdekking.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondwerksoorten/afdekking'),
        'afgraving': KeuzelijstWaarde(invulwaarde='afgraving',
                                      label='afgraving',
                                      status='ingebruik',
                                      definitie='Grond van afgraving.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondwerksoorten/afgraving'),
        'ophoging': KeuzelijstWaarde(invulwaarde='ophoging',
                                     label='ophoging',
                                     status='ingebruik',
                                     definitie='Grond voor ophoging.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondwerksoorten/ophoging'),
        'uitgraving': KeuzelijstWaarde(invulwaarde='uitgraving',
                                       label='uitgraving',
                                       status='ingebruik',
                                       definitie='Grond van uitgraving.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondwerksoorten/uitgraving')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

