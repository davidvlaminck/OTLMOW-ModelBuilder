# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsDeelVan(DirectioneleRelatie):
    """De rechtsgrond waar deze rechtsgrond onderdeel van uitmaakt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsDeelVan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
