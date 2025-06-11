# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
        '24-7': KeuzelijstWaarde(invulwaarde='24-7',
                                 label='24/7',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureToegangstijden/24-7'),
        'op-afspraak': KeuzelijstWaarde(invulwaarde='op-afspraak',
                                        label='Op afspraak',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureToegangstijden/op-afspraak'),
        'tijdens-kantooruren': KeuzelijstWaarde(invulwaarde='tijdens-kantooruren',
                                                label='Tijdens kantooruren',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureToegangstijden/tijdens-kantooruren')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

