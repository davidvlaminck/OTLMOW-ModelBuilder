# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardingAardingsstelsel(KeuzelijstField):
    """Lijst van mogelijke aardinggsstelsels."""
    naam = 'KlAardingAardingsstelsel'
    label = 'Aardingsinstallatie aardingsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAardingAardingsstelsel'
    definition = 'Lijst van mogelijke aardinggsstelsels.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardingAardingsstelsel'
    options = {
        'gemeenschappelijk': KeuzelijstWaarde(invulwaarde='gemeenschappelijk',
                                              label='gemeenschappelijk',
                                              status='ingebruik',
                                              definitie='gemeenschappelijk',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gemeenschappelijk'),
        'gemeenschappelijk---globaal': KeuzelijstWaarde(invulwaarde='gemeenschappelijk---globaal',
                                                        label='gemeenschappelijk + globaal',
                                                        status='ingebruik',
                                                        definitie='Een aardingsstelsel waarin alle aardingen (LS, N, HS) met elkaar verbonden zijn en waarvoor bovendien de distributienetbeheerder aan de hand van een attest garandeert dat de aardingen verbonden zijn met ten minste x andere aardingsinstallaties van andere installaties. Voor een globaal stelsel moet altijd het attest toegevoegd worden. Zonder dergelijk attest kan er enkel sprake zijn van een gemeenschappelijk stelsel en moet die optie gekozen worden.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gemeenschappelijk---globaal'),
        'gemeenschappelijk-globaal': KeuzelijstWaarde(invulwaarde='gemeenschappelijk-globaal',
                                                      label='gemeenschappelijk + globaal',
                                                      status='ingebruik',
                                                      definitie='gemeenschappelijk + globaal',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gemeenschappelijk-globaal'),
        'gescheiden': KeuzelijstWaarde(invulwaarde='gescheiden',
                                       label='gescheiden',
                                       status='ingebruik',
                                       definitie='gescheiden',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gescheiden')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

