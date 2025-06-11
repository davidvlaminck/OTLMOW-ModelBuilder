# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSuppCBV(KeuzelijstField):
    """Keuzelijst om het type van de toegevoegde supplementen van de CBV te bepalen."""
    naam = 'KlTypeSuppCBV'
    label = 'Type supplementen CBV'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSuppCBV'
    definition = 'Keuzelijst om het type van de toegevoegde supplementen van de CBV te bepalen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSuppCBV'
    options = {
        'figureren-betonoppervlak-in-de-massa-gekleurd': KeuzelijstWaarde(invulwaarde='figureren-betonoppervlak-in-de-massa-gekleurd',
                                                                          label='figureren betonoppervlak in de massa gekleurd',
                                                                          status='ingebruik',
                                                                          definitie='Supplementen voor het bekomen van een in de massa gekleurde CBV.',
                                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSuppCBV/figureren-betonoppervlak-in-de-massa-gekleurd'),
        'figureren-betonoppervlak-met-kleurverharder': KeuzelijstWaarde(invulwaarde='figureren-betonoppervlak-met-kleurverharder',
                                                                        label='figureren betonoppervlak met kleurverharder',
                                                                        status='ingebruik',
                                                                        definitie='Supplementen voor het bekomen van een gekleurde 2 laagse deklaag van CBV.',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSuppCBV/figureren-betonoppervlak-met-kleurverharder')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

