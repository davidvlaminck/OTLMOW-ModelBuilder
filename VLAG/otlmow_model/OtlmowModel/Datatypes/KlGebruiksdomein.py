# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGebruiksdomein(KeuzelijstField):
    """De omstandigheden waarin het beton gebruikt zal worden."""
    naam = 'KlGebruiksdomein'
    label = 'Gebruiksdomein'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlGebruiksdomein'
    definition = 'De omstandigheden waarin het beton gebruikt zal worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGebruiksdomein'
    options = {
        'gb-gewapend': KeuzelijstWaarde(invulwaarde='gb-gewapend',
                                        label='GB (gewapend)',
                                        status='ingebruik',
                                        definitie='Gewapend beton.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/gb-gewapend'),
        'gzb-gewapend-zichtbeton': KeuzelijstWaarde(invulwaarde='gzb-gewapend-zichtbeton',
                                                    label='GZB (gewapend zichtbeton) ',
                                                    status='ingebruik',
                                                    definitie='Gewapend zichtbeton.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/gzb-gewapend-zichtbeton'),
        'ob-ongewapend': KeuzelijstWaarde(invulwaarde='ob-ongewapend',
                                          label='OB (ongewapend)',
                                          status='ingebruik',
                                          definitie='Ongewapend beton.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/ob-ongewapend'),
        'vb-voorgespannen': KeuzelijstWaarde(invulwaarde='vb-voorgespannen',
                                             label='VB (voorgespannen)',
                                             status='ingebruik',
                                             definitie='Voorgespannen beton.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/vb-voorgespannen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

