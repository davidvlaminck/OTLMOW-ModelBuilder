# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWalsmethode(KeuzelijstField):
    """De manier waarop het staal is gewalst."""
    naam = 'KlWalsmethode'
    label = 'Walsmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlWalsmethode'
    definition = 'De manier waarop het staal is gewalst.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWalsmethode'
    options = {
        'koud': KeuzelijstWaarde(invulwaarde='koud',
                                 label='Koud',
                                 status='ingebruik',
                                 definitie='Staal die bij omgevingstemperatuur wordt gevormd (getrokken) uit warmgewalst staal.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWalsmethode/koud'),
        'warm': KeuzelijstWaarde(invulwaarde='warm',
                                 label='Warm',
                                 status='ingebruik',
                                 definitie='Heet staal wordt vervormd onder druk van persen en walsen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWalsmethode/warm')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

