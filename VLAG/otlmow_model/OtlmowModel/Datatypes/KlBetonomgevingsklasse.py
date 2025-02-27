# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetonomgevingsklasse(KeuzelijstField):
    """Omgevingsklasse waaraan het beton wordt blootgesteld."""
    naam = 'KlBetonomgevingsklasse'
    label = 'Betonomgevingsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBetonomgevingsklasse'
    definition = 'Omgevingsklasse waaraan het beton wordt blootgesteld.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetonomgevingsklasse'
    options = {
        'e-0': KeuzelijstWaarde(invulwaarde='e-0',
                                label='E0',
                                status='ingebruik',
                                definitie='Niet schadelijk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-0'),
        'e-a-1': KeuzelijstWaarde(invulwaarde='e-a-1',
                                  label='EA1',
                                  status='ingebruik',
                                  definitie='Zwak agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-1'),
        'e-a-2': KeuzelijstWaarde(invulwaarde='e-a-2',
                                  label='EA2',
                                  status='ingebruik',
                                  definitie='Middelmatig agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-2'),
        'e-a-3': KeuzelijstWaarde(invulwaarde='e-a-3',
                                  label='EA3',
                                  status='ingebruik',
                                  definitie='Sterk agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-3'),
        'e-e-1': KeuzelijstWaarde(invulwaarde='e-e-1',
                                  label='EE1',
                                  status='ingebruik',
                                  definitie='Buitenomgeving : geen vorst.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-1'),
        'e-e-2': KeuzelijstWaarde(invulwaarde='e-e-2',
                                  label='EE2',
                                  status='ingebruik',
                                  definitie='Buitenomgeving : vorst, geen contact met regen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-2'),
        'e-e-3': KeuzelijstWaarde(invulwaarde='e-e-3',
                                  label='EE3',
                                  status='ingebruik',
                                  definitie='Buitenomgeving : vorst, contact met regen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-3'),
        'e-e-4': KeuzelijstWaarde(invulwaarde='e-e-4',
                                  label='EE4',
                                  status='ingebruik',
                                  definitie='Buitenomgeving : vorst en dooizouten (aanwezigheid van ter plaatse ontdooid of opspattend of aflopend dooizouthoudend water).',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-4'),
        'e-s-1': KeuzelijstWaarde(invulwaarde='e-s-1',
                                  label='ES1',
                                  status='ingebruik',
                                  definitie='Zeeomgeving : geen contact met zeewater, wel contact met zeelucht (tot 3 km van de kust) en/of brak water, en geen contact met vorst.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-1'),
        'e-s-2': KeuzelijstWaarde(invulwaarde='e-s-2',
                                  label='ES2',
                                  status='ingebruik',
                                  definitie='Zeeomgeving : geen contact met zeewater, wel contact met zeelucht (tot 3 km van de kust) en/of brak water, en wel contact met vorst.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-2'),
        'e-s-3': KeuzelijstWaarde(invulwaarde='e-s-3',
                                  label='ES3',
                                  status='ingebruik',
                                  definitie='Zeeomgeving : contact met zeewater en ondergedompeld.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-3'),
        'e-s-4': KeuzelijstWaarde(invulwaarde='e-s-4',
                                  label='ES4',
                                  status='ingebruik',
                                  definitie='Zeeomgeving : contact met zeewater en getijden- en spatzone.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-4'),
        'ei': KeuzelijstWaarde(invulwaarde='ei',
                               label='EI',
                               status='ingebruik',
                               definitie='Binnenomgeving.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/ei'),
        'xf3': KeuzelijstWaarde(invulwaarde='xf3',
                                label='XF3',
                                status='ingebruik',
                                definitie='Verzadigd met water, zonder dooizouten.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/xf3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

