# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgProvincie(KeuzelijstField):
    """Lijst van provincies in Vlaanderen."""
    naam = 'KlAlgProvincie'
    label = 'Provincie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgProvincie'
    definition = 'Lijst van provincies in Vlaanderen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgProvincie'
    options = {
        'antwerpen': KeuzelijstWaarde(invulwaarde='antwerpen',
                                      label='antwerpen',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/antwerpen'),
        'limburg': KeuzelijstWaarde(invulwaarde='limburg',
                                    label='limburg',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/limburg'),
        'oost-Vlaanderen': KeuzelijstWaarde(invulwaarde='oost-Vlaanderen',
                                            label='oost-Vlaanderen',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/oost-Vlaanderen'),
        'vlaams-Brabant': KeuzelijstWaarde(invulwaarde='vlaams-Brabant',
                                           label='vlaams-Brabant',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/vlaams-Brabant'),
        'west-Vlaanderen': KeuzelijstWaarde(invulwaarde='west-Vlaanderen',
                                            label='west-Vlaanderen',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/west-Vlaanderen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

