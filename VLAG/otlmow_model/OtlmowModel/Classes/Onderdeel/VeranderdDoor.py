# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VeranderdDoor(DirectioneleRelatie):
    """Duidt aan dat deze rechtsgrond een verandering met legale gevolgen heeft ondergaan door een andere rechtsgrond. Dit omvat amendementen, vervangingen, herroepingen en andere types verandering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VeranderdDoor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
