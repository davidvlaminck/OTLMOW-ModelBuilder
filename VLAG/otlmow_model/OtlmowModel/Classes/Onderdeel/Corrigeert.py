# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Corrigeert(DirectioneleRelatie):
    """Duidt aan dat deze rechtsgrond of legale verschijningsvorm tekstuele veranderingen zonder legale impact aanbrengt in een andere rechtsgrond of legale verschijningsvorm."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Corrigeert'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
