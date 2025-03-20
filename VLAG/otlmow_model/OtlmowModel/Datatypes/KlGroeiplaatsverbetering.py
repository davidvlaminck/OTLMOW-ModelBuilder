# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGroeiplaatsverbetering(KeuzelijstField):
    """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""
    naam = 'KlGroeiplaatsverbetering'
    label = 'Groeiplaatsverbetering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGroeiplaatsverbetering'
    definition = 'De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGroeiplaatsverbetering'
    options = {
        'bodembeluchting-luchtinjectie': KeuzelijstWaarde(invulwaarde='bodembeluchting-luchtinjectie',
                                                          label='bodembeluchting-luchtinjectie',
                                                          status='ingebruik',
                                                          definitie='Groeiplaatsverbetering dmv bodembeluchting-luchtinjectie.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/bodembeluchting-luchtinjectie'),
        'horizontale-drainage': KeuzelijstWaarde(invulwaarde='horizontale-drainage',
                                                 label='horizontale drainage',
                                                 status='ingebruik',
                                                 definitie='Groeiplaatsverbetering dmv horizontale drainage.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/horizontale-drainage'),
        'irrgatie-drainagebuis': KeuzelijstWaarde(invulwaarde='irrgatie-drainagebuis',
                                                  label='irrgatie drainagebuis',
                                                  status='ingebruik',
                                                  definitie='Groeiplaatsverbetering dmv irrigatie met een drainagebuis.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrgatie-drainagebuis'),
        'irrigatie-gietrand-overtollige-grond': KeuzelijstWaarde(invulwaarde='irrigatie-gietrand-overtollige-grond',
                                                                 label='irrigatie gietrand overtollige grond',
                                                                 status='ingebruik',
                                                                 definitie='Groeiplaatsverbetering dmv irrigatie met een overtollige grond.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrigatie-gietrand-overtollige-grond'),
        'irrigatie-kunstmatige-gietrand': KeuzelijstWaarde(invulwaarde='irrigatie-kunstmatige-gietrand',
                                                           label='irrigatie kunstmatige gietrand',
                                                           status='ingebruik',
                                                           definitie='Groeiplaatsverbetering dmv irrigatie met een kunstmatige gietrand.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrigatie-kunstmatige-gietrand'),
        'verticale-drainage': KeuzelijstWaarde(invulwaarde='verticale-drainage',
                                               label='verticale drainage',
                                               status='ingebruik',
                                               definitie='Groeiplaatsverbetering dmv verticale drainage.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/verticale-drainage')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

