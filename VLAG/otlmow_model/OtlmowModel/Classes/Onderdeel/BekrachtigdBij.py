# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BekrachtigdBij(DirectioneleRelatie):
    """Een rechtsgrond of legale verschijningsvorm krijgt volledige rechtskracht door instemming onder opschortende voorwaarde van een andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BekrachtigdBij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
