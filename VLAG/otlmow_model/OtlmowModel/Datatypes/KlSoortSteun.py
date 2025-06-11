# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSoortSteun(KeuzelijstField):
    """TODO"""
    naam = 'KlSoortSteun'
    label = 'Soort steun'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSoortSteun'
    definition = 'TODO'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSoortSteun'
    options = {
        'rechte-steun': KeuzelijstWaarde(invulwaarde='rechte-steun',
                                         label='rechte steun',
                                         status='ingebruik',
                                         definitie='rechte steun of baar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoortSteun/rechte-steun')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

