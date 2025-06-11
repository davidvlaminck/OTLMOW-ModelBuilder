# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSleutel(KeuzelijstField):
    """De verschillende sleuteltypes."""
    naam = 'KlTypeSleutel'
    label = 'Type sleutel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTypeSleutel'
    definition = 'De verschillende sleuteltypes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSleutel'
    options = {
        'dom': KeuzelijstWaarde(invulwaarde='dom',
                                label='DOM',
                                status='ingebruik',
                                definitie='DOM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSleutel/dom'),
        'extern': KeuzelijstWaarde(invulwaarde='extern',
                                   label='extern',
                                   status='ingebruik',
                                   definitie='extern',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSleutel/extern'),
        'specifiek': KeuzelijstWaarde(invulwaarde='specifiek',
                                      label='specifiek',
                                      status='ingebruik',
                                      definitie='specifiek',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSleutel/specifiek'),
        'yale-5': KeuzelijstWaarde(invulwaarde='yale-5',
                                   label='Yale 5',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSleutel/yale-5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

