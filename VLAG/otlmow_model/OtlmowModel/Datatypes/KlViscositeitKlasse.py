# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlViscositeitKlasse(KeuzelijstField):
    """Keuzelijst voor de Viscosity Grade (VG) classificatie volgens ISO 3448."""
    naam = 'KlViscositeitKlasse'
    label = 'Viscositeit klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlViscositeitKlasse'
    definition = 'Keuzelijst voor de Viscosity Grade (VG) classificatie volgens ISO 3448.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlViscositeitKlasse'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

