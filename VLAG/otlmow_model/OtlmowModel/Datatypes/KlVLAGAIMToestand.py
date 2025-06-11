# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVLAGAIMToestand(KeuzelijstField):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""
    naam = 'KlVLAGAIMToestand'
    label = 'VLAG AIM toestand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlVLAGAIMToestand'
    definition = 'Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVLAGAIMToestand'
    options = {
        'in-gebruik': KeuzelijstWaarde(invulwaarde='in-gebruik',
                                       label='in gebruik',
                                       status='ingebruik',
                                       definitie='in gebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVLAGAIMToestand/in-gebruik'),
        'uit-gebruik': KeuzelijstWaarde(invulwaarde='uit-gebruik',
                                        label='uit gebruik',
                                        status='ingebruik',
                                        definitie='uit gebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVLAGAIMToestand/uit-gebruik')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

