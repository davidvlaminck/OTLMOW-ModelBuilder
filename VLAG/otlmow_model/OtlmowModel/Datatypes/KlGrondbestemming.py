# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondbestemming(KeuzelijstField):
    """De bestemmingen of doelen van de grond."""
    naam = 'KlGrondbestemming'
    label = 'Grondbestemming'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrondbestemming'
    definition = 'De bestemmingen of doelen van de grond.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondbestemming'
    options = {
        'buiten-werfzone-of-top': KeuzelijstWaarde(invulwaarde='buiten-werfzone-of-top',
                                                   label='buiten werfzone of TOP',
                                                   status='ingebruik',
                                                   definitie='Grond met verwijdering voor gebruik buiten de werf of voor afvoer naar een tussentijdse opslagplaats (TOP).',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbestemming/buiten-werfzone-of-top'),
        'hergebruik': KeuzelijstWaarde(invulwaarde='hergebruik',
                                       label='hergebruik',
                                       status='ingebruik',
                                       definitie='Grond voor hergebruik.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbestemming/hergebruik'),
        'reiniging': KeuzelijstWaarde(invulwaarde='reiniging',
                                      label='reiniging',
                                      status='ingebruik',
                                      definitie='Te reinigen grond.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbestemming/reiniging'),
        'storten': KeuzelijstWaarde(invulwaarde='storten',
                                    label='storten',
                                    status='ingebruik',
                                    definitie='Grond met verwijdering naar een vergunde stortplaats.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbestemming/storten'),
        'tijdelijke-opslagplaats-(top)': KeuzelijstWaarde(invulwaarde='tijdelijke-opslagplaats-(top)',
                                                          label='tijdelijke opslagplaats (TOP)',
                                                          status='verwijderd',
                                                          definitie='Grond voor tijdelijke opslag.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbestemming/tijdelijke-opslagplaats-(top)'),
        'tijdelijke-werfopslagplaats': KeuzelijstWaarde(invulwaarde='tijdelijke-werfopslagplaats',
                                                        label='tijdelijke werfopslagplaats',
                                                        status='ingebruik',
                                                        definitie='Grond voor tijdelijke opslag in de werfzone.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbestemming/tijdelijke-werfopslagplaats')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

