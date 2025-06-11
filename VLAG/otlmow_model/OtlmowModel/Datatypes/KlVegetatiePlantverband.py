# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatiePlantverband(KeuzelijstField):
    """De verschillende opties voor het plantverband."""
    naam = 'KlVegetatiePlantverband'
    label = 'Vegetatie plantverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatiePlantverband'
    definition = 'De verschillende opties voor het plantverband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatiePlantverband'
    options = {
        'geschrankt': KeuzelijstWaarde(invulwaarde='geschrankt',
                                       label='geschrankt',
                                       status='ingebruik',
                                       definitie='De planten staan geschrankt',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/geschrankt'),
        'rijafstand': KeuzelijstWaarde(invulwaarde='rijafstand',
                                       label='rijafstand',
                                       status='ingebruik',
                                       definitie='De afstand tussen de rijen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/rijafstand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

