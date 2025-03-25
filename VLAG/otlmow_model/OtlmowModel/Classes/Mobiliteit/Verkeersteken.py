# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from ...Datatypes.DtcAdres import DtcAdres, DtcAdresWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcTijdschema import DtcTijdschema, DtcTijdschemaWaarden
from ...Datatypes.KlVerkeerstekenWettelijkeStatus import KlVerkeerstekenWettelijkeStatus
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersteken(AIMLinkObject):
    """De voorstelling van een aanwijzing ten behoeve van de weggebruikers die verbonden wordt aan het aankondigen of opleggen van een bepaalde verkeersmaatregel zoals bepaald in de wegcode."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#heeftGerelateerdVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#heeftGerelateerdVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeerslichtVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#heeftGerelateerdVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#heeftGerelateerdVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#WegmarkeringVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Realiseert', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Realiseert', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WordtAangeduidDoor', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='i')  # i = direction: incoming

        self._adresVoorstelling = OTLAttribuut(field=DtcAdres,
                                               naam='adresVoorstelling',
                                               label='adresvoorstelling',
                                               objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.adresVoorstelling',
                                               usagenote='Ter hoogte van welk adres het verkeersteken geplaatst wordt. De preciese locatie komt op de opstelling.',
                                               kardinaliteit_min='0',
                                               definition='Adresvoorstelling van het verkeersteken.',
                                               owner=self)

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.afbeelding',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='TODO',
                                        owner=self)

        self._buitenwerkingtreding = OTLAttribuut(field=DtcTijdschema,
                                                  naam='buitenwerkingtreding',
                                                  label='buitenwerkingtreding',
                                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.buitenwerkingtreding',
                                                  kardinaliteit_min='0',
                                                  kardinaliteit_max='*',
                                                  definition='Periode waarbinnen het verkeersteken niet geldig is.',
                                                  owner=self)

        self._inwerkingstijd = OTLAttribuut(field=DtcTijdschema,
                                            naam='inwerkingstijd',
                                            label='inwerkingtreding',
                                            objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.inwerkingstijd',
                                            kardinaliteit_min='0',
                                            kardinaliteit_max='*',
                                            definition='TODO',
                                            owner=self)

        self._locatie = OTLAttribuut(field=StringField,
                                     naam='locatie',
                                     label='locatie',
                                     objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.locatie',
                                     definition='TODO',
                                     owner=self)

        self._plaatsbepaling = OTLAttribuut(field=StringField,
                                            naam='plaatsbepaling',
                                            label='plaatsbepaling',
                                            objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.plaatsbepaling',
                                            kardinaliteit_min='0',
                                            definition='TODO',
                                            owner=self)

        self._variabele = OTLAttribuut(field=StringField,
                                       naam='variabele',
                                       label='variabele',
                                       objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.variabele',
                                       kardinaliteit_min='0',
                                       kardinaliteit_max='*',
                                       definition='TODO',
                                       owner=self)

        self._wettelijkeStatus = OTLAttribuut(field=KlVerkeerstekenWettelijkeStatus,
                                              naam='wettelijkeStatus',
                                              label='wettelijke status',
                                              objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.wettelijkeStatus',
                                              definition='Wettelijke status van het verkeersteken.',
                                              owner=self)

    @property
    def adresVoorstelling(self) -> DtcAdresWaarden:
        """Adresvoorstelling van het verkeersteken."""
        return self._adresVoorstelling.get_waarde()

    @adresVoorstelling.setter
    def adresVoorstelling(self, value):
        self._adresVoorstelling.set_waarde(value, owner=self)

    @property
    def afbeelding(self) -> List[DtcDocumentWaarden]:
        """TODO"""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def buitenwerkingtreding(self) -> List[DtcTijdschemaWaarden]:
        """Periode waarbinnen het verkeersteken niet geldig is."""
        return self._buitenwerkingtreding.get_waarde()

    @buitenwerkingtreding.setter
    def buitenwerkingtreding(self, value):
        self._buitenwerkingtreding.set_waarde(value, owner=self)

    @property
    def inwerkingstijd(self) -> List[DtcTijdschemaWaarden]:
        """TODO"""
        return self._inwerkingstijd.get_waarde()

    @inwerkingstijd.setter
    def inwerkingstijd(self, value):
        self._inwerkingstijd.set_waarde(value, owner=self)

    @property
    def locatie(self) -> str:
        """TODO"""
        return self._locatie.get_waarde()

    @locatie.setter
    def locatie(self, value):
        self._locatie.set_waarde(value, owner=self)

    @property
    def plaatsbepaling(self) -> str:
        """TODO"""
        return self._plaatsbepaling.get_waarde()

    @plaatsbepaling.setter
    def plaatsbepaling(self, value):
        self._plaatsbepaling.set_waarde(value, owner=self)

    @property
    def variabele(self) -> List[str]:
        """TODO"""
        return self._variabele.get_waarde()

    @variabele.setter
    def variabele(self, value):
        self._variabele.set_waarde(value, owner=self)

    @property
    def wettelijkeStatus(self) -> str:
        """Wettelijke status van het verkeersteken."""
        return self._wettelijkeStatus.get_waarde()

    @wettelijkeStatus.setter
    def wettelijkeStatus(self, value):
        self._wettelijkeStatus.set_waarde(value, owner=self)
