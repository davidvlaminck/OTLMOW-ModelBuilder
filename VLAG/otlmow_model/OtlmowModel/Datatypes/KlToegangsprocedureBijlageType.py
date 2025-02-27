# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangsprocedureBijlageType(KeuzelijstField):
    """De bijlagetypes van een toegangsprocedure."""
    naam = 'KlToegangsprocedureBijlageType'
    label = 'Bijlagetype toegangsprocedure'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToegangsprocedureBijlageType'
    definition = 'De bijlagetypes van een toegangsprocedure.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangsprocedureBijlageType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

