# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoorzetconstructieBevestigingsmateriaal(KeuzelijstField):
    """De mogelijke materialen gebruikt voor de bevestiging van een voorzetconstructie."""
    naam = 'KlVoorzetconstructieBevestigingsmateriaal'
    label = 'Voorzetconstructie bevestigingsmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoorzetconstructieBevestigingsmateriaal'
    definition = 'De mogelijke materialen gebruikt voor de bevestiging van een voorzetconstructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoorzetconstructieBevestigingsmateriaal'
    options = {
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorzetconstructieBevestigingsmateriaal/rvs'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorzetconstructieBevestigingsmateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

