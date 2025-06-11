# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVariabeleWaarden(KeuzelijstField):
    """"""
    naam = 'KlVariabeleWaarden'
    label = ''
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlVariabeleWaarden'
    definition = ''
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabeleWaarden'
    options = {
        'varoptie1': KeuzelijstWaarde(invulwaarde='varoptie1',
                                      label='varoptie1',
                                      status='ingebruik',
                                      definitie='varoptie1',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabeleWaarden/varoptie1'),
        'varoptie2': KeuzelijstWaarde(invulwaarde='varoptie2',
                                      label='varoptie2',
                                      status='ingebruik',
                                      definitie='varoptie2',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabeleWaarden/varoptie2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

