# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerstekenconceptStatus(KeuzelijstField):
    """TODO"""
    naam = 'KlVerkeerstekenconceptStatus'
    label = 'Verkeerstekenconcept status'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlVerkeerstekenconceptStatus'
    definition = 'TODO'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerstekenconceptStatus'
    options = {
        'test-status': KeuzelijstWaarde(invulwaarde='test-status',
                                        label='test status',
                                        status='ingebruik',
                                        definitie='test status',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerstekenconceptStatus/test-status')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

