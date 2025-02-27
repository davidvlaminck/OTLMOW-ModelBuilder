# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftNetwerkProtectie(DirectioneleRelatie):
    """Deze relatie geeft aan wat de redundante paden/linken zijn van elkaar, dit is enkel in gebruik binnen het netwerk domein. Deze relatie heeft geen richting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerkProtectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
