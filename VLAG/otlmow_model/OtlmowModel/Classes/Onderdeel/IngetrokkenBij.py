# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IngetrokkenBij(DirectioneleRelatie):
    """Geeft aan dat deze rechtsgrond of legale verschijningsvorm ingetrokken is bij een ander."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IngetrokkenBij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
