# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WordtAangeduidDoor(DirectioneleRelatie):
    """Een verkeersteken dat bijdraagt tot de aanduiding van een mobiliteitsmaatregel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WordtAangeduidDoor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
