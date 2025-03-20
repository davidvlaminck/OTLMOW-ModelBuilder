# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCTestType(KeuzelijstField):
    """Het test type van het geluidswerend scherm."""
    naam = 'KlLEGCTestType'
    label = 'Test type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCTestType'
    definition = 'Het test type van het geluidswerend scherm.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCTestType'
    options = {
        'fqs': KeuzelijstWaarde(invulwaarde='fqs',
                                label='fqs',
                                status='ingebruik',
                                definitie='fsdf',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/fqs'),
        'geluidsabsorptie': KeuzelijstWaarde(invulwaarde='geluidsabsorptie',
                                             label='geluidsabsorptie',
                                             status='ingebruik',
                                             definitie='Proef : De ÃƒÂ©ÃƒÂ©ngetalsaanduiding als waarde voor de geluidsabsorptie',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/geluidsabsorptie'),
        'luchtgeluidsisolatie': KeuzelijstWaarde(invulwaarde='luchtgeluidsisolatie',
                                                 label='luchtgeluidsisolatie',
                                                 status='ingebruik',
                                                 definitie='Proef : De ÃƒÂ©ÃƒÂ©ngetalsaanduiding voor luchtgeluidsisolatie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/luchtgeluidsisolatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

