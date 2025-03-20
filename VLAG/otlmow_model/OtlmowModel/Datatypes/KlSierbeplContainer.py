# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplContainer(KeuzelijstField):
    """Verschillende mogeliike pot- en containermaten voor de sierbeplanting."""
    naam = 'KlSierbeplContainer'
    label = 'Sierbeplanting container'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplContainer'
    definition = 'Verschillende mogeliike pot- en containermaten voor de sierbeplanting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplContainer'
    options = {
        'c10': KeuzelijstWaarde(invulwaarde='c10',
                                label='C10',
                                status='ingebruik',
                                definitie='C10',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/c10'),
        'c5': KeuzelijstWaarde(invulwaarde='c5',
                               label='C5',
                               status='ingebruik',
                               definitie='C5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/c5'),
        'c7.5': KeuzelijstWaarde(invulwaarde='c7.5',
                                 label='C7.5',
                                 status='ingebruik',
                                 definitie='C7,5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/c7.5'),
        'p10.5-c1': KeuzelijstWaarde(invulwaarde='p10.5-c1',
                                     label='P10.5-C1',
                                     status='ingebruik',
                                     definitie='P10,5/C1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p10.5-c1'),
        'p13-c1.2': KeuzelijstWaarde(invulwaarde='p13-c1.2',
                                     label='P13-C1.2',
                                     status='ingebruik',
                                     definitie='P13/C1,2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p13-c1.2'),
        'p14-c1.5': KeuzelijstWaarde(invulwaarde='p14-c1.5',
                                     label='P14-C1.5',
                                     status='ingebruik',
                                     definitie='P14/C1,5',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p14-c1.5'),
        'p15-c2': KeuzelijstWaarde(invulwaarde='p15-c2',
                                   label='P15-C2',
                                   status='ingebruik',
                                   definitie='P15/C2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p15-c2'),
        'p17-c3': KeuzelijstWaarde(invulwaarde='p17-c3',
                                   label='P17-C3',
                                   status='ingebruik',
                                   definitie='P17/C3',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p17-c3'),
        'p19-c4': KeuzelijstWaarde(invulwaarde='p19-c4',
                                   label='P19-C4',
                                   status='ingebruik',
                                   definitie='P19/C4',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p19-c4'),
        'p7': KeuzelijstWaarde(invulwaarde='p7',
                               label='P7',
                               status='ingebruik',
                               definitie='P7',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p7'),
        'p9': KeuzelijstWaarde(invulwaarde='p9',
                               label='P9',
                               status='ingebruik',
                               definitie='P9',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/p9')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

