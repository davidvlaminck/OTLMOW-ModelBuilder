# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondHoofdnaamCode(KeuzelijstField):
    """De hoofdnaamcode van de grond.Namespace :http://interpretatie.kern.schemas.dov.vlaanderen.be/GecodeerdHoofdnaamCodesEnumType."""
    naam = 'KlGrondHoofdnaamCode'
    label = 'Grond hoofdnaamcode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrondHoofdnaamCode'
    definition = 'De hoofdnaamcode van de grond.Namespace :http://interpretatie.kern.schemas.dov.vlaanderen.be/GecodeerdHoofdnaamCodesEnumType.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondHoofdnaamCode'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

