# coding=utf-8
from ...Classes.Mobiliteit.Verkeerstekenconcept import Verkeerstekenconcept


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeerslichtconcept(Verkeerstekenconcept):
    """Inhoudelijke definitie van de betekenis van een verkeerslicht zoals opgenomen in de wegcode."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Verkeerslichtconcept'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsGebaseerdOp', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeerslichtVerkeersteken', direction='i')  # i = direction: incoming
