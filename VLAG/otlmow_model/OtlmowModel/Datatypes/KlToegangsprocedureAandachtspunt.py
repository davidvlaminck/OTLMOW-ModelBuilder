# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangsprocedureAandachtspunt(KeuzelijstField):
    """De soorten aandachtspunten voor toegang tot een object."""
    naam = 'KlToegangsprocedureAandachtspunt'
    label = 'Toegangsprocedure aandachtspunt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToegangsprocedureAandachtspunt'
    definition = 'De soorten aandachtspunten voor toegang tot een object.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangsprocedureAandachtspunt'
    options = {
        'botser-nodig': KeuzelijstWaarde(invulwaarde='botser-nodig',
                                         label='Botser nodig',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureAandachtspunt/botser-nodig'),
        'hoogtewerker-nodig': KeuzelijstWaarde(invulwaarde='hoogtewerker-nodig',
                                               label='Hoogtewerker nodig',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureAandachtspunt/hoogtewerker-nodig'),
        'niet-machinaal-bereikbaar': KeuzelijstWaarde(invulwaarde='niet-machinaal-bereikbaar',
                                                      label='niet machinaal bereikbaar',
                                                      status='ingebruik',
                                                      definitie='Het object kan niet bereikt worden met een machine voor bijvoorbeeld reiniging, onderhoud of vervanging.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureAandachtspunt/niet-machinaal-bereikbaar'),
        'onveilig': KeuzelijstWaarde(invulwaarde='onveilig',
                                     label='Onveilig',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureAandachtspunt/onveilig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

