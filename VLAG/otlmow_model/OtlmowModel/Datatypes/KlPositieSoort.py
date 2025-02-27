# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPositieSoort(KeuzelijstField):
    """Posities van het wegdek."""
    naam = 'KlPositieSoort'
    label = 'Positie soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPositieSoort'
    definition = 'Posities van het wegdek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPositieSoort'
    options = {
        'linkerrand': KeuzelijstWaarde(invulwaarde='linkerrand',
                                       label='linkerrand',
                                       status='ingebruik',
                                       definitie='linkerrand',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/linkerrand'),
        'midden': KeuzelijstWaarde(invulwaarde='midden',
                                   label='midden',
                                   status='ingebruik',
                                   definitie='midden',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/midden'),
        'rechterrand': KeuzelijstWaarde(invulwaarde='rechterrand',
                                        label='rechterrand',
                                        status='ingebruik',
                                        definitie='rechterrand',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/rechterrand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

