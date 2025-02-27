# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondBijmengingHoeveelheidCode(KeuzelijstField):
    """De mogelijke waarden voor de hoeveelheid bijmenging (X staat voor de lithologie van de bijmenging)."""
    naam = 'KlGrondBijmengingHoeveelheidCode'
    label = 'Grondbijmenging hoeveelheidscode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrondBijmengingHoeveelheidCode'
    definition = 'De mogelijke waarden voor de hoeveelheid bijmenging (X staat voor de lithologie van de bijmenging).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondBijmengingHoeveelheidCode'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

