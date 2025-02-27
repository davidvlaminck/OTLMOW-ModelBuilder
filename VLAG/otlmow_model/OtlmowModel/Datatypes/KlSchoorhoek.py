# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchoorhoek(KeuzelijstField):
    """De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4)."""
    naam = 'KlSchoorhoek'
    label = 'Schoorhoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSchoorhoek'
    definition = 'De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchoorhoek'
    options = {
        '1-3': KeuzelijstWaarde(invulwaarde='1-3',
                                label='1/3',
                                status='ingebruik',
                                definitie='Een schoorhoek van 1 op 3.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-3'),
        '1-4': KeuzelijstWaarde(invulwaarde='1-4',
                                label='1/4',
                                status='ingebruik',
                                definitie='Een schoorhoek van 1 op 4.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-4'),
        '1-5': KeuzelijstWaarde(invulwaarde='1-5',
                                label='1/5',
                                status='ingebruik',
                                definitie='Een schoorhoek van 1 op 5.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

