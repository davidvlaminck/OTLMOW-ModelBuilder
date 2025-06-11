# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlProfielsoort(KeuzelijstField):
    """Het type profiel (de meest genormeerde types)."""
    naam = 'KlProfielsoort'
    label = 'Profielsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlProfielsoort'
    definition = 'Het type profiel (de meest genormeerde types).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlProfielsoort'
    options = {
        'hd': KeuzelijstWaarde(invulwaarde='hd',
                               label='HD',
                               status='ingebruik',
                               definitie='Breedflensprofiel : een HD-profiel heeft dikkere flenzen en lijf. Dit profiel is speciaal voor kolommen.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hd'),
        'hea': KeuzelijstWaarde(invulwaarde='hea',
                                label='HEA',
                                status='ingebruik',
                                definitie='Meest voorkomende breedflensprofiel (een profiel met brede evenwijdige flenzen).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hea'),
        'heb': KeuzelijstWaarde(invulwaarde='heb',
                                label='HEB',
                                status='ingebruik',
                                definitie='Meest voorkomende breedflensprofiel (een profiel met brede evenwijdige flenzen). Het HEB-profiel heeft meer draagkracht dan het HEA-profiel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/heb'),
        'hem': KeuzelijstWaarde(invulwaarde='hem',
                                label='HEM',
                                status='ingebruik',
                                definitie='Breedflensprofiel : een HEM-profiel heeft dikkere flenzen en lijf dan HEA- en HEB-profielen.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hem'),
        'hp-bulbstaal': KeuzelijstWaarde(invulwaarde='hp-bulbstaal',
                                         label='HP (bulbstaal)',
                                         status='ingebruik',
                                         definitie='Een massief profiel : Hollandprofiel (afgekort HP).',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hp-bulbstaal'),
        'ipe': KeuzelijstWaarde(invulwaarde='ipe',
                                label='IPE',
                                status='ingebruik',
                                definitie='Een IPE-profiel (I Profiel Europees) heeft betrekkelijk korte, evenwijdige flenzen met een constante dikte.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/ipe'),
        'ipn': KeuzelijstWaarde(invulwaarde='ipn',
                                label='IPN',
                                status='ingebruik',
                                definitie='Een IPN-profiel (I Normaal Profiel, ook wel INP genoemd) heeft iets schuinere flenzen dan een IPE-profiel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/ipn'),
        'upe': KeuzelijstWaarde(invulwaarde='upe',
                                label='UPE',
                                status='ingebruik',
                                definitie='U-vormig profiel. Een UPE-profiel heeft rechte flenzen die overal even dik zijn en dikker zijn dan het lijf.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/upe'),
        'upn': KeuzelijstWaarde(invulwaarde='upn',
                                label='UPN',
                                status='ingebruik',
                                definitie='Het meest gebruikte U-vormig profiel. Een UPN-profiel (U Normaal Profiel, ook wel UNP genoemd) heeft schuine flenzen.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/upn')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

