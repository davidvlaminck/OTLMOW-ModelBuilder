# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastBevsToestel(KeuzelijstField):
    """De standaard bevestigingen van verlichtingstoestellen aan lichtmasten."""
    naam = 'KlWvLichtmastBevsToestel'
    label = 'Bevestiging voor wegverlichtingstoestellen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastBevsToestel'
    definition = 'De standaard bevestigingen van verlichtingstoestellen aan lichtmasten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastBevsToestel'
    options = {
        'kroon': KeuzelijstWaarde(invulwaarde='kroon',
                                  label='kroon',
                                  status='ingebruik',
                                  definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/kroon'),
        'mediaanbalk-h': KeuzelijstWaarde(invulwaarde='mediaanbalk-h',
                                          label='mediaanbalk H',
                                          status='ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-h'),
        'mediaanbalk-i': KeuzelijstWaarde(invulwaarde='mediaanbalk-i',
                                          label='mediaanbalk I',
                                          status='ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-i'),
        'mediaanbalk-u': KeuzelijstWaarde(invulwaarde='mediaanbalk-u',
                                          label='mediaanbalk U',
                                          status='ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-u'),
        'ossenkop': KeuzelijstWaarde(invulwaarde='ossenkop',
                                     label='ossenkop',
                                     status='ingebruik',
                                     definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/ossenkop'),
        'paaltop-108mm': KeuzelijstWaarde(invulwaarde='paaltop-108mm',
                                          label='paaltop 108mm',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-108mm'),
        'paaltop-60mm': KeuzelijstWaarde(invulwaarde='paaltop-60mm',
                                         label='paaltop 60mm',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-60mm'),
        'paaltop-76mm': KeuzelijstWaarde(invulwaarde='paaltop-76mm',
                                         label='paaltop 76mm',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-76mm'),
        'plaat': KeuzelijstWaarde(invulwaarde='plaat',
                                  label='plaat',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/plaat'),
        't-stuk': KeuzelijstWaarde(invulwaarde='t-stuk',
                                   label='t-stuk',
                                   status='ingebruik',
                                   definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/t-stuk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

