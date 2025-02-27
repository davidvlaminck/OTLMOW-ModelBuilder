# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgWeekdagen(KeuzelijstField):
    """Lijst van de verschillende weekdagen."""
    naam = 'KlAlgWeekdagen'
    label = 'Weekdagen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgWeekdagen'
    definition = 'Lijst van de verschillende weekdagen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgWeekdagen'
    options = {
        'dinsdag': KeuzelijstWaarde(invulwaarde='dinsdag',
                                    label='dinsdag',
                                    status='ingebruik',
                                    definitie='De dag van een week tussen maandag en woensdag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/dinsdag'),
        'donderdag': KeuzelijstWaarde(invulwaarde='donderdag',
                                      label='donderdag',
                                      status='ingebruik',
                                      definitie='De dag van een week tussen woensdag en vrijdag.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/donderdag'),
        'feestdag': KeuzelijstWaarde(invulwaarde='feestdag',
                                     label='feestdag',
                                     status='ingebruik',
                                     definitie='Een wettelijke nationale vrije dag.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/feestdag'),
        'maandag': KeuzelijstWaarde(invulwaarde='maandag',
                                    label='maandag',
                                    status='ingebruik',
                                    definitie='De dag van een week tussen zondag en dinsdag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/maandag'),
        'vrijdag': KeuzelijstWaarde(invulwaarde='vrijdag',
                                    label='vrijdag',
                                    status='ingebruik',
                                    definitie='De dag van een week tussen donderdag en zaterdag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/vrijdag'),
        'woensdag': KeuzelijstWaarde(invulwaarde='woensdag',
                                     label='woensdag',
                                     status='ingebruik',
                                     definitie='De dag van een week tussen dinsdag en donderdag.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/woensdag'),
        'zaterdag': KeuzelijstWaarde(invulwaarde='zaterdag',
                                     label='zaterdag',
                                     status='ingebruik',
                                     definitie='De dag van een week tussen vrijdag en zondag.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/zaterdag'),
        'zondag': KeuzelijstWaarde(invulwaarde='zondag',
                                   label='zondag',
                                   status='ingebruik',
                                   definitie='De dag van een week tussen zaterdag en maandag.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/zondag')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

