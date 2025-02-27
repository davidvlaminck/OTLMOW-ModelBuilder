# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlantmaatOmtrek(KeuzelijstField):
    """De stamomtrek in centimeter (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""
    naam = 'KlPlantmaatOmtrek'
    label = 'Plantmaat omtrek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlantmaatOmtrek'
    definition = 'De stamomtrek in centimeter (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantmaatOmtrek'
    options = {
        '10-12': KeuzelijstWaarde(invulwaarde='10-12',
                                  label='10/12',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 10 en 12 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/10-12'),
        '12-14': KeuzelijstWaarde(invulwaarde='12-14',
                                  label='12/14',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 12 en 14 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/12-14'),
        '14-16': KeuzelijstWaarde(invulwaarde='14-16',
                                  label='14/16',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 14 en 16 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/14-16'),
        '16-18': KeuzelijstWaarde(invulwaarde='16-18',
                                  label='16/18',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 16 en 18 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/16-18'),
        '18-20': KeuzelijstWaarde(invulwaarde='18-20',
                                  label='18/20',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 18 en 20 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/18-20'),
        '20-25': KeuzelijstWaarde(invulwaarde='20-25',
                                  label='20/25',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 20 en 25 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/20-25'),
        '25-30': KeuzelijstWaarde(invulwaarde='25-30',
                                  label='25/30',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 25 en 30 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/25-30'),
        '30-35': KeuzelijstWaarde(invulwaarde='30-35',
                                  label='30/35',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 30 en 35 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/30-35'),
        '30-40': KeuzelijstWaarde(invulwaarde='30-40',
                                  label='30/40',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 30 en 40 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/30-40'),
        '35-40': KeuzelijstWaarde(invulwaarde='35-40',
                                  label='35/40',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 35 en 40 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/35-40'),
        '40-50': KeuzelijstWaarde(invulwaarde='40-50',
                                  label='40/50',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 40 en 50 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/40-50'),
        '50-60': KeuzelijstWaarde(invulwaarde='50-60',
                                  label='50/60',
                                  status='ingebruik',
                                  definitie='Houtige vegetatie met stamomtrek tussen 50 en 60 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/50-60'),
        '6-8': KeuzelijstWaarde(invulwaarde='6-8',
                                label='6/8',
                                status='ingebruik',
                                definitie='Houtige vegetatie met stamomtrek tussen 6 en 8 cm.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/6-8'),
        '8-10': KeuzelijstWaarde(invulwaarde='8-10',
                                 label='8/10',
                                 status='ingebruik',
                                 definitie='Houtige vegetatie met stamomtrek tussen 8 en 10 cm.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/8-10')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

