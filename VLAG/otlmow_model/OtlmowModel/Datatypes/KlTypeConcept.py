# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeConcept(KeuzelijstField):
    """De mogelijke types van concepten van een beweegbare waterkerende constructie."""
    naam = 'KlTypeConcept'
    label = 'type beweging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeConcept'
    definition = 'De mogelijke types van concepten van een beweegbare waterkerende constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeConcept'
    options = {
        'cilinder': KeuzelijstWaarde(invulwaarde='cilinder',
                                     label='cilinder',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/cilinder'),
        'draai': KeuzelijstWaarde(invulwaarde='draai',
                                  label='draai',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/draai'),
        'glij': KeuzelijstWaarde(invulwaarde='glij',
                                 label='glij',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/glij'),
        'hef': KeuzelijstWaarde(invulwaarde='hef',
                                label='hef',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/hef'),
        'jaloezieofspiegel': KeuzelijstWaarde(invulwaarde='jaloezieofspiegel',
                                              label='jaloezieOfSpiegel',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/jaloezieofspiegel'),
        'klep': KeuzelijstWaarde(invulwaarde='klep',
                                 label='klep',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/klep'),
        'punt': KeuzelijstWaarde(invulwaarde='punt',
                                 label='punt',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/punt'),
        'rol': KeuzelijstWaarde(invulwaarde='rol',
                                label='rol',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/rol'),
        'sector': KeuzelijstWaarde(invulwaarde='sector',
                                   label='sector',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/sector'),
        'segment': KeuzelijstWaarde(invulwaarde='segment',
                                    label='segment',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/segment'),
        'vlinder': KeuzelijstWaarde(invulwaarde='vlinder',
                                    label='vlinder',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/vlinder'),
        'waaier': KeuzelijstWaarde(invulwaarde='waaier',
                                   label='waaier',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/waaier'),
        'wiel': KeuzelijstWaarde(invulwaarde='wiel',
                                 label='wiel',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/wiel'),
        'zink': KeuzelijstWaarde(invulwaarde='zink',
                                 label='zink',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeConcept/zink')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

