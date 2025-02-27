# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCorrosiebelastingscategorie(KeuzelijstField):
    """De mogelijke codes om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven."""
    naam = 'KlCorrosiebelastingscategorie'
    label = 'Corrosiebelastingscategorie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlCorrosiebelastingscategorie'
    definition = 'De mogelijke codes om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCorrosiebelastingscategorie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

