# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomVerankeringtype(KeuzelijstField):
    """De verschillende types van verankering van een boom."""
    naam = 'KlBoomVerankeringtype'
    label = 'Boom verankeringtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomVerankeringtype'
    definition = 'De verschillende types van verankering van een boom.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomVerankeringtype'
    options = {
        'biologisch-afbreekbare-grondankers': KeuzelijstWaarde(invulwaarde='biologisch-afbreekbare-grondankers',
                                                               label='biologisch afbreekbare grondankers',
                                                               status='ingebruik',
                                                               definitie='Een constructie van 100% biologisch afbreekbare grondankers en verankeringstouwen die de stabilietit van de boom waarborgt',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/biologisch-afbreekbare-grondankers'),
        'boompaalconstructie': KeuzelijstWaarde(invulwaarde='boompaalconstructie',
                                                label='boompaalconstructie',
                                                status='ingebruik',
                                                definitie='Een constructie uit houten palen en dwarslatten die de stabiliteit van de boom waarborgt',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/boompaalconstructie'),
        'niet-afbreekbare-grondankers': KeuzelijstWaarde(invulwaarde='niet-afbreekbare-grondankers',
                                                         label='niet-afbreekbare grondankers',
                                                         status='ingebruik',
                                                         definitie='Een constructie van stalen grondankers en kunststofverankeringsbanden die de stabilietit van de boom waarborgt',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/niet-afbreekbare-grondankers')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

