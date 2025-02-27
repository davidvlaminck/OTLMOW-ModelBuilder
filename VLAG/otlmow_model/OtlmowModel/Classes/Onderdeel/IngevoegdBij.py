# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IngevoegdBij(DirectioneleRelatie):
    """Bij deze rechtsgrond of legale verschijningsvorm is een verandering met legale impact ingevoegd door een andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IngevoegdBij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
