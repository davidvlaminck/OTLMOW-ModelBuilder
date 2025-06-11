# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBadge(KeuzelijstField):
    """De verschillende badgetypes."""
    naam = 'KlTypeBadge'
    label = 'Type badge'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTypeBadge'
    definition = 'De verschillende badgetypes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBadge'
    options = {
        'extern': KeuzelijstWaarde(invulwaarde='extern',
                                   label='extern',
                                   status='ingebruik',
                                   definitie='extern',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBadge/extern'),
        'facilitair-bedrijf': KeuzelijstWaarde(invulwaarde='facilitair-bedrijf',
                                               label='Facilitair bedrijf',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBadge/facilitair-bedrijf'),
        'specifiek': KeuzelijstWaarde(invulwaarde='specifiek',
                                      label='specifiek',
                                      status='ingebruik',
                                      definitie='specifiek',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBadge/specifiek'),
        'tunnels-antwerpen': KeuzelijstWaarde(invulwaarde='tunnels-antwerpen',
                                              label='tunnels Antwerpen',
                                              status='ingebruik',
                                              definitie='tunnels Antwerpen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBadge/tunnels-antwerpen'),
        'vwt-net': KeuzelijstWaarde(invulwaarde='vwt-net',
                                    label='VWT-NET',
                                    status='ingebruik',
                                    definitie='VWT-NET',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBadge/vwt-net')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

