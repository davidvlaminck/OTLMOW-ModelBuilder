# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoegtIn(DirectioneleRelatie):
    """Deze rechtsgrond of legale verschijningsvorm voegt een verandering met legale impact in bij een andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoegtIn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
