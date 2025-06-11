# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlViscositeitKlasse(KeuzelijstField):
    """Keuzelijst voor de Viscosity Grade (VG) classificatie volgens ISO 3448."""
    naam = 'KlViscositeitKlasse'
    label = 'Viscositeit klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlViscositeitKlasse'
    definition = 'Keuzelijst voor de Viscosity Grade (VG) classificatie volgens ISO 3448.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlViscositeitKlasse'
    options = {
        'iso-vg-10': KeuzelijstWaarde(invulwaarde='iso-vg-10',
                                      label='ISO VG 10',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-10'),
        'iso-vg-100': KeuzelijstWaarde(invulwaarde='iso-vg-100',
                                       label='ISO VG 100',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-100'),
        'iso-vg-1000': KeuzelijstWaarde(invulwaarde='iso-vg-1000',
                                        label='ISO VG 1000',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-1000'),
        'iso-vg-15': KeuzelijstWaarde(invulwaarde='iso-vg-15',
                                      label='ISO VG 15',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-15'),
        'iso-vg-150': KeuzelijstWaarde(invulwaarde='iso-vg-150',
                                       label='ISO VG 150',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-150'),
        'iso-vg-1500': KeuzelijstWaarde(invulwaarde='iso-vg-1500',
                                        label='ISO VG 1500',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-1500'),
        'iso-vg-2': KeuzelijstWaarde(invulwaarde='iso-vg-2',
                                     label='ISO VG 2',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-2'),
        'iso-vg-22': KeuzelijstWaarde(invulwaarde='iso-vg-22',
                                      label='ISO VG 22',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-22'),
        'iso-vg-220': KeuzelijstWaarde(invulwaarde='iso-vg-220',
                                       label='ISO VG 220',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-220'),
        'iso-vg-3': KeuzelijstWaarde(invulwaarde='iso-vg-3',
                                     label='ISO VG 3',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-3'),
        'iso-vg-32': KeuzelijstWaarde(invulwaarde='iso-vg-32',
                                      label='ISO VG 32',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-32'),
        'iso-vg-320': KeuzelijstWaarde(invulwaarde='iso-vg-320',
                                       label='ISO VG 320',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-320'),
        'iso-vg-46': KeuzelijstWaarde(invulwaarde='iso-vg-46',
                                      label='ISO VG 46',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-46'),
        'iso-vg-460': KeuzelijstWaarde(invulwaarde='iso-vg-460',
                                       label='ISO VG 460',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-460'),
        'iso-vg-5': KeuzelijstWaarde(invulwaarde='iso-vg-5',
                                     label='ISO VG 5',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-5'),
        'iso-vg-68': KeuzelijstWaarde(invulwaarde='iso-vg-68',
                                      label='ISO VG 68',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-68'),
        'iso-vg-680': KeuzelijstWaarde(invulwaarde='iso-vg-680',
                                       label='ISO VG 680',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-680'),
        'iso-vg-7': KeuzelijstWaarde(invulwaarde='iso-vg-7',
                                     label='ISO VG 7',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlViscositeitKlasse/iso-vg-7')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

