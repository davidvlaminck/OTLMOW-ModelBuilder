# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoorzetconstructieBevestigingsmateriaalDiameter(KeuzelijstField):
    """De mogelijke diameters van het bevestigingsmateriaal gebruikt bij een voorzetconstructie."""
    naam = 'KlVoorzetconstructieBevestigingsmateriaalDiameter'
    label = 'Voorzetconstructie bevestigingsmateriaal diameter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoorzetconstructieBevestigingsmateriaalDiameter'
    definition = 'De mogelijke diameters van het bevestigingsmateriaal gebruikt bij een voorzetconstructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoorzetconstructieBevestigingsmateriaalDiameter'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

