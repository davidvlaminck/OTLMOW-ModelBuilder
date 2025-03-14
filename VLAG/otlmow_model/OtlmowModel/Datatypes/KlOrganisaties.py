# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOrganisaties(KeuzelijstField):
    """De mogelijke organisaties."""
    naam = 'KlOrganisaties'
    label = 'Organisaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlOrganisaties'
    definition = 'De mogelijke organisaties.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOrganisaties'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

