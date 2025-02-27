# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GecorrigeerdDoor(DirectioneleRelatie):
    """Duidt een rechtsgrond aan die een tekstuele verandering zonder legale impact aan deze rechtsgrond aanbrengt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GecorrigeerdDoor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
