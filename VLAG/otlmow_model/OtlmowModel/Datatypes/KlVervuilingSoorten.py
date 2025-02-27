# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVervuilingSoorten(KeuzelijstField):
    """De specificatie van de vastgestelde vervuiling van de grond."""
    naam = 'KlVervuilingSoorten'
    label = 'Vervuiling soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlVervuilingSoorten'
    definition = 'De specificatie van de vastgestelde vervuiling van de grond.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVervuilingSoorten'
    options = {
        'pfos': KeuzelijstWaarde(invulwaarde='pfos',
                                 label='PFOS',
                                 status='ingebruik',
                                 definitie='Perfluoroctaansulfonaten zijn chemische stoffen die behoren tot de bredere PFAS (perfluorinated alkylated substances), een grote familie van duizenden synthetische stoffen met meerdere fluoratomen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVervuilingSoorten/pfos')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

