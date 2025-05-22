# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from ...Datatypes.DtcAdres import DtcAdres, DtcAdresWaarden
from ...Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden
from ...Datatypes.DtcPeriode import DtcPeriode, DtcPeriodeWaarden
from ...Datatypes.DtcTijdschema import DtcTijdschema, DtcTijdschemaWaarden
from ...Datatypes.DtcZone import DtcZone, DtcZoneWaarden
from ...Datatypes.KlCode import KlCode
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Mobiliteitsmaatregel(AIMLinkObject):
    """Maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BevatOntwerpVoor', target='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftMobiliteitsmaatregel', target='https://data.vlaanderen.be/ns/besluit#Artikel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsGebaseerdOp', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WordtAangeduidDoor', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='o')  # o = direction: outgoing

        self._adresVoorstelling = OTLAttribuut(field=DtcAdres,
                                               naam='adresVoorstelling',
                                               label='adresvoorstelling',
                                               objectUri='http://www.w3.org/ns/locn#address',
                                               kardinaliteit_min='0',
                                               kardinaliteit_max='*',
                                               definition='TODO',
                                               owner=self)

        self._beschrijving = OTLAttribuut(field=StringField,
                                          naam='beschrijving',
                                          label='beschrijving',
                                          objectUri='http://purl.org/dc/terms/description',
                                          definition='TODO',
                                          owner=self)

        self._doelgroep = OTLAttribuut(field=KlCode,
                                       naam='doelgroep',
                                       label='doelgroep',
                                       objectUri='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel.doelgroep',
                                       usagenote='Bijvoorbeeld: alle bewoners uit een bepaalde straat',
                                       kardinaliteit_min='0',
                                       kardinaliteit_max='*',
                                       definition='Groep of categorie die belang hebben bij de mobiliteitsmaatregel.',
                                       owner=self)

        self._identificator = OTLAttribuut(field=DtcIdentificator,
                                           naam='identificator',
                                           label='identificator',
                                           objectUri='http://www.w3.org/ns/adms#identifier',
                                           kardinaliteit_min='0',
                                           definition='TODO',
                                           owner=self)

        self._periode = OTLAttribuut(field=DtcPeriode,
                                     naam='periode',
                                     label='periode',
                                     objectUri='https://data.vlaanderen.be/ns/mobiliteit#periode',
                                     kardinaliteit_max='*',
                                     definition='TODO',
                                     owner=self)

        self._plaatsbepaling = OTLAttribuut(field=StringField,
                                            naam='plaatsbepaling',
                                            label='plaatsbepaling',
                                            objectUri='https://data.vlaanderen.be/ns/mobiliteit#plaatsbepaling',
                                            definition='TODO',
                                            owner=self)

        self._tijdschema = OTLAttribuut(field=DtcTijdschema,
                                        naam='tijdschema',
                                        label='tijdschema',
                                        objectUri='http://schema.org/eventSchedule',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Wanneer de mobiliteitsmaatregel plaatsvindt volgens een tijdschema.',
                                        owner=self)

        self._type = OTLAttribuut(field=KlCode,
                                  naam='type',
                                  label='type',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel.type',
                                  usagenote='Voorbeelden: straat afzetten, trager rijden, extra fietsstallingen, shuttledienst etc.',
                                  definition='Type mobiliteitsmaatregel.',
                                  owner=self)

        self._zone = OTLAttribuut(field=DtcZone,
                                  naam='zone',
                                  label='zone',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#zone',
                                  kardinaliteit_max='*',
                                  definition='TODO',
                                  owner=self)

    @property
    def adresVoorstelling(self) -> List[DtcAdresWaarden]:
        """TODO"""
        return self._adresVoorstelling.get_waarde()

    @adresVoorstelling.setter
    def adresVoorstelling(self, value):
        self._adresVoorstelling.set_waarde(value, owner=self)

    @property
    def beschrijving(self) -> str:
        """TODO"""
        return self._beschrijving.get_waarde()

    @beschrijving.setter
    def beschrijving(self, value):
        self._beschrijving.set_waarde(value, owner=self)

    @property
    def doelgroep(self) -> List[str]:
        """Groep of categorie die belang hebben bij de mobiliteitsmaatregel."""
        return self._doelgroep.get_waarde()

    @doelgroep.setter
    def doelgroep(self, value):
        self._doelgroep.set_waarde(value, owner=self)

    @property
    def identificator(self) -> DtcIdentificatorWaarden:
        """TODO"""
        return self._identificator.get_waarde()

    @identificator.setter
    def identificator(self, value):
        self._identificator.set_waarde(value, owner=self)

    @property
    def periode(self) -> List[DtcPeriodeWaarden]:
        """TODO"""
        return self._periode.get_waarde()

    @periode.setter
    def periode(self, value):
        self._periode.set_waarde(value, owner=self)

    @property
    def plaatsbepaling(self) -> str:
        """TODO"""
        return self._plaatsbepaling.get_waarde()

    @plaatsbepaling.setter
    def plaatsbepaling(self, value):
        self._plaatsbepaling.set_waarde(value, owner=self)

    @property
    def tijdschema(self) -> List[DtcTijdschemaWaarden]:
        """Wanneer de mobiliteitsmaatregel plaatsvindt volgens een tijdschema."""
        return self._tijdschema.get_waarde()

    @tijdschema.setter
    def tijdschema(self, value):
        self._tijdschema.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Type mobiliteitsmaatregel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def zone(self) -> List[DtcZoneWaarden]:
        """TODO"""
        return self._zone.get_waarde()

    @zone.setter
    def zone(self, value):
        self._zone.set_waarde(value, owner=self)
