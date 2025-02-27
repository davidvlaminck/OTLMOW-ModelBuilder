# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsOnderdeelVan(DirectioneleRelatie):
    """Het besluit waarvan het artikel een onderdeel is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOnderdeelVan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
