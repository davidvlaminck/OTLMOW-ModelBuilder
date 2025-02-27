# coding=utf-8
from ...Classes.Mobiliteit.Verkeersteken import Verkeersteken


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegmarkering-Verkeersteken(Verkeersteken):
    """Verkeersteken dat gerealiseerd wordt met een wegmarkering"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#WegmarkeringVerkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#heeftGerelateerdVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsGebaseerdOp', target='https://data.vlaanderen.be/ns/mobiliteit#Wegmarkeringsconcept', direction='o')  # o = direction: outgoing
