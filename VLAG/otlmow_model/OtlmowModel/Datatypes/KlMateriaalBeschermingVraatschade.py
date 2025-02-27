# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalBeschermingVraatschade(KeuzelijstField):
    """De middelen als bescherming tegen vraatschade."""
    naam = 'KlMateriaalBeschermingVraatschade'
    label = 'Materiaal bescherming vraatschade'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalBeschermingVraatschade'
    definition = 'De middelen als bescherming tegen vraatschade.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBeschermingVraatschade'
    options = {
        'juteband': KeuzelijstWaarde(invulwaarde='juteband',
                                     label='juteband',
                                     status='ingebruik',
                                     definitie='Materiaal dat gebruikt wordt als bescherming vraatschade is een juteband.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBeschermingVraatschade/juteband'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='Materiaal dat gebruikt wordt als bescherming vraatschade is kunststof.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBeschermingVraatschade/kunststof'),
        'wildafwerend-product': KeuzelijstWaarde(invulwaarde='wildafwerend-product',
                                                 label='wildafwerend product',
                                                 status='ingebruik',
                                                 definitie='Wildafwerend product wordt gebruikt als bescherming tegen vraatschade.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBeschermingVraatschade/wildafwerend-product')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

