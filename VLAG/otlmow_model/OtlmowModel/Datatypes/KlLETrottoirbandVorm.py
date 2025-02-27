# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLETrottoirbandVorm(KeuzelijstField):
    """De vormen van een trottoirband."""
    naam = 'KlLETrottoirbandVorm'
    label = 'Trottoirband vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandVorm'
    definition = 'De vormen van een trottoirband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandVorm'
    options = {
        'afgeschuind': KeuzelijstWaarde(invulwaarde='afgeschuind',
                                        label='afgeschuind',
                                        status='ingebruik',
                                        definitie='Afgeschuind',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandVorm/afgeschuind'),
        'niet-afgeschuind': KeuzelijstWaarde(invulwaarde='niet-afgeschuind',
                                             label='niet afgeschuind',
                                             status='ingebruik',
                                             definitie='niet afgeschuind',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandVorm/niet-afgeschuind')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

