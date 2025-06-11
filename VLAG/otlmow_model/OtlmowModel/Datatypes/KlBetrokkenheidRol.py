# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetrokkenheidRol(KeuzelijstField):
    """Keuzelijst met mogelijke waarden voor de rol waarmee een agent betrokken is bij een object."""
    naam = 'KlBetrokkenheidRol'
    label = 'Betrokkenheid rol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBetrokkenheidRol'
    definition = 'Keuzelijst met mogelijke waarden voor de rol waarmee een agent betrokken is bij een object.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetrokkenheidRol'
    options = {
        'beheerder': KeuzelijstWaarde(invulwaarde='beheerder',
                                      label='beheerder',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/beheerder'),
        'berekende-beheerder': KeuzelijstWaarde(invulwaarde='berekende-beheerder',
                                                label='berekende beheerder',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/berekende-beheerder'),
        'eigenaar': KeuzelijstWaarde(invulwaarde='eigenaar',
                                     label='eigenaar',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/eigenaar'),
        'installatieverantwoordelijke': KeuzelijstWaarde(invulwaarde='installatieverantwoordelijke',
                                                         label='Installatieverantwoordelijke',
                                                         status='ingebruik',
                                                         definitie='De installatieverantwoordelijke is de persoon, aangeduid door de werkgever, om de verantwoordelijkheid voor de exploitatie van de elektrische installatie op zich te nemen. Indien nodig kan hij die verantwoordelijkheid wel gedeeltelijk op andere personen overdragen. Concreet is hij op de hoogte van de eventuele afwijkende situaties en gaat, in overleg met de werkverantwoordelijke, na of de nodige maatregelen genomen worden om op een veilige manier te werken met een dergelijke installatie.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/installatieverantwoordelijke'),
        'keuringsinstantie': KeuzelijstWaarde(invulwaarde='keuringsinstantie',
                                              label='keuringsinstantie',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/keuringsinstantie'),
        'klant': KeuzelijstWaarde(invulwaarde='klant',
                                  label='klant',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/klant'),
        'leidinggevende': KeuzelijstWaarde(invulwaarde='leidinggevende',
                                           label='leidinggevende',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/leidinggevende'),
        'lid': KeuzelijstWaarde(invulwaarde='lid',
                                label='lid',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/lid'),
        'schadebeheerder': KeuzelijstWaarde(invulwaarde='schadebeheerder',
                                            label='schadebeheerder',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/schadebeheerder'),
        'suborganisatie-van': KeuzelijstWaarde(invulwaarde='suborganisatie-van',
                                               label='suborganisatie van',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/suborganisatie-van'),
        'toezicht-onderhoud': KeuzelijstWaarde(invulwaarde='toezicht-onderhoud',
                                               label='toezicht onderhoud',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezicht-onderhoud'),
        'toezichter': KeuzelijstWaarde(invulwaarde='toezichter',
                                       label='toezichter',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichter'),
        'toezichtsgroep': KeuzelijstWaarde(invulwaarde='toezichtsgroep',
                                           label='toezichtsgroep',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichtsgroep'),
        'verantwoordelijke-reiniging': KeuzelijstWaarde(invulwaarde='verantwoordelijke-reiniging',
                                                        label='verantwoordelijke reiniging',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/verantwoordelijke-reiniging')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

