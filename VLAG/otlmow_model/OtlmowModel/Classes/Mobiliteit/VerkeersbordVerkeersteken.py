# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Mobiliteit.Verkeersteken import Verkeersteken
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersbordVerkeersteken(Verkeersteken):
    """Verkeersteken dat gerealiseerd wordt met een verkeersbord."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#heeftGerelateerdVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftOnderbord', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsGebaseerdOp', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersbordconcept', direction='o')  # o = direction: outgoing

        self._isBeginZone = OTLAttribuut(field=BooleanField,
                                         naam='isBeginZone',
                                         label='is begin zone',
                                         objectUri='https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken.isBeginZone',
                                         kardinaliteit_min='0',
                                         definition='Duidt aan of het verkeersbord-verkeersteken het begin van een zone aanduidt.',
                                         owner=self)

        self._isEindeZone = OTLAttribuut(field=BooleanField,
                                         naam='isEindeZone',
                                         label='is einde zone',
                                         objectUri='https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken.isEindeZone',
                                         kardinaliteit_min='0',
                                         definition='Duidt aan of het verkeerbord-verkeersteken het einde van een zone aanduidt.',
                                         owner=self)

    @property
    def isBeginZone(self) -> bool:
        """Duidt aan of het verkeersbord-verkeersteken het begin van een zone aanduidt."""
        return self._isBeginZone.get_waarde()

    @isBeginZone.setter
    def isBeginZone(self, value):
        self._isBeginZone.set_waarde(value, owner=self)

    @property
    def isEindeZone(self) -> bool:
        """Duidt aan of het verkeerbord-verkeersteken het einde van een zone aanduidt."""
        return self._isEindeZone.get_waarde()

    @isEindeZone.setter
    def isEindeZone(self, value):
        self._isEindeZone.set_waarde(value, owner=self)
