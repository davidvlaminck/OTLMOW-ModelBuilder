# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAanplantingswijzeSierbeplanting(KeuzelijstField):
    """De mogelijke manieren van aanplanten van sierbeplanting."""
    naam = 'KlAanplantingswijzeSierbeplanting'
    label = 'aanplantingswijze sierbeplanting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAanplantingswijzeSierbeplanting'
    definition = 'De mogelijke manieren van aanplanten van sierbeplanting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAanplantingswijzeSierbeplanting'
    options = {
        'aanplanting-bol--en-knolgewassen': KeuzelijstWaarde(invulwaarde='aanplanting-bol--en-knolgewassen',
                                                             label='aanplanting bol- en knolgewassen',
                                                             status='ingebruik',
                                                             definitie='Aanplanting via bol- en knolgewassen',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-bol--en-knolgewassen'),
        'aanplanting-helm': KeuzelijstWaarde(invulwaarde='aanplanting-helm',
                                             label='aanplanting helm',
                                             status='ingebruik',
                                             definitie='Aanplanting via helm',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-helm'),
        'aanplanting-test': KeuzelijstWaarde(invulwaarde='aanplanting-test',
                                             label='aanplanting test',
                                             status='verwijderd',
                                             definitie='Aanplanting via test2',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-test'),
        'aanplanting-zonder-helm': KeuzelijstWaarde(invulwaarde='aanplanting-zonder-helm',
                                                    label='aanplanting zonder helm',
                                                    status='uitgebruik',
                                                    definitie='Aanplanting zonder helmtest',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-zonder-helm'),
        'application-pdf': KeuzelijstWaarde(invulwaarde='application-pdf',
                                            label='application/pdf',
                                            status='ingebruik',
                                            definitie='application/pdf',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/application-pdf'),
        'application-pdf-2': KeuzelijstWaarde(invulwaarde='application-pdf-2',
                                              label='application-pdf',
                                              status='ingebruik',
                                              definitie='application/pdf',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/application-pdf-2'),
        'k-2': KeuzelijstWaarde(invulwaarde='k-2',
                                label='K',
                                status='uitgebruik',
                                definitie="test op 'K'je",
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/k-2'),
        'test': KeuzelijstWaarde(invulwaarde='test',
                                 label='test',
                                 status='ingebruik',
                                 definitie='test - test',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/test'),
        'test-1': KeuzelijstWaarde(invulwaarde='test-1',
                                   label='test/1',
                                   status='ingebruik',
                                   definitie='test/1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/test-1'),
        'test-1-2': KeuzelijstWaarde(invulwaarde='test-1-2',
                                     label='test-1',
                                     status='ingebruik',
                                     definitie='die van test/1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/test-1-2'),
        'test-test2': KeuzelijstWaarde(invulwaarde='test-test2',
                                       label='Test+test2',
                                       status='ingebruik',
                                       definitie='Test+test2.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/test-test2'),
        'test-test2-2': KeuzelijstWaarde(invulwaarde='test-test2-2',
                                         label='Test-test2',
                                         status='ingebruik',
                                         definitie='Test-test2',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/test-test2-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

