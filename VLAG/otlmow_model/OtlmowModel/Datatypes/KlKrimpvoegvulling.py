# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKrimpvoegvulling(KeuzelijstField):
    """De mogelijke vullingen voor een krimpvoeg."""
    naam = 'KlKrimpvoegvulling'
    label = 'Krimpvoegvulling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlKrimpvoegvulling'
    definition = 'De mogelijke vullingen voor een krimpvoeg.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKrimpvoegvulling'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

