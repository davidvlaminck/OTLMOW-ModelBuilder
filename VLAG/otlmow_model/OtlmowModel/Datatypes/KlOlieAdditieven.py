# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOlieAdditieven(KeuzelijstField):
    """Keuzelijst voor de verschillende additieven die men kan toevoegen aan olie."""
    naam = 'KlOlieAdditieven'
    label = 'Olie additieven'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOlieAdditieven'
    definition = 'Keuzelijst voor de verschillende additieven die men kan toevoegen aan olie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOlieAdditieven'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

