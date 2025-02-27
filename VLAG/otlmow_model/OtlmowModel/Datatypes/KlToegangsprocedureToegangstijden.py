# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangsprocedureToegangstijden(KeuzelijstField):
    """De mogelijke toegangstijden bij een toegangsprocedure."""
    naam = 'KlToegangsprocedureToegangstijden'
    label = 'Toegangsprocedure toegangstijden'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToegangsprocedureToegangstijden'
    definition = 'De mogelijke toegangstijden bij een toegangsprocedure.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangsprocedureToegangstijden'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

