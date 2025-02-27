# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ..Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor
from ..Datatypes.DtcContactinfo import DtcContactinfo, DtcContactinfoWaarden
from ..Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Agent(AIMDBStatus, OTLObject, RelationInteractor):
    """Iemand die of iets dat kan handelen of een effect kan teweeg brengen."""

    typeURI = 'http://purl.org/dc/terms/Agent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure', direction='i')  # i = direction: incoming

        self._agentId = OTLAttribuut(field=DtcIdentificator,
                                     naam='agentId',
                                     label='agent identificatie',
                                     objectUri='http://purl.org/dc/terms/Agent.agentId',
                                     definition='Identificatie van de agent volgens een bepaalde bron.',
                                     owner=self)

        self._contactinfo = OTLAttribuut(field=DtcContactinfo,
                                         naam='contactinfo',
                                         label='contactinfo',
                                         objectUri='http://purl.org/dc/terms/Agent.contactinfo',
                                         kardinaliteit_max='*',
                                         definition='Algemene contactgegevens voor de agent.',
                                         owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='http://purl.org/dc/terms/Agent.naam',
                                  definition='De naam waarmee de agent doorgaans benoemd wordt.',
                                  owner=self)

    @property
    def agentId(self) -> DtcIdentificatorWaarden:
        """Identificatie van de agent volgens een bepaalde bron."""
        return self._agentId.get_waarde()

    @agentId.setter
    def agentId(self, value):
        self._agentId.set_waarde(value, owner=self)

    @property
    def contactinfo(self) -> List[DtcContactinfoWaarden]:
        """Algemene contactgegevens voor de agent."""
        return self._contactinfo.get_waarde()

    @contactinfo.setter
    def contactinfo(self, value):
        self._contactinfo.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """De naam waarmee de agent doorgaans benoemd wordt."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
