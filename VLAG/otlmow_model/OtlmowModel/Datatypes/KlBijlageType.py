# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBijlageType(KeuzelijstField):
    """De mogelijke types of categorieën van het document."""
    naam = 'KlBijlageType'
    label = 'Bijlage type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBijlageType'
    definition = 'De mogelijke types of categorieën van het document.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBijlageType'
    options = {
        'attest': KeuzelijstWaarde(invulwaarde='attest',
                                   label='attest',
                                   status='ingebruik',
                                   definitie='attest',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/attest'),
        'foto': KeuzelijstWaarde(invulwaarde='foto',
                                 label='foto',
                                 status='ingebruik',
                                 definitie='foto',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/foto'),
        'handleiding': KeuzelijstWaarde(invulwaarde='handleiding',
                                        label='handleiding',
                                        status='ingebruik',
                                        definitie='handleiding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/handleiding'),
        'plan': KeuzelijstWaarde(invulwaarde='plan',
                                 label='plan',
                                 status='ingebruik',
                                 definitie='plan',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/plan'),
        'technische-fiche': KeuzelijstWaarde(invulwaarde='technische-fiche',
                                             label='technische fiche',
                                             status='ingebruik',
                                             definitie='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/technische-fiche'),
        'verslag': KeuzelijstWaarde(invulwaarde='verslag',
                                    label='verslag',
                                    status='ingebruik',
                                    definitie='verslag',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/verslag')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

