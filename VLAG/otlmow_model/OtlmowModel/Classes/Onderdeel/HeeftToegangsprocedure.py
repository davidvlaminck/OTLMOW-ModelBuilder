# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftToegangsprocedure(DirectioneleRelatie):
    """Deze relatie wordt gelegd tussen een klasse en de klasse Toegangsprocedure. De relatie vertrekt vanuit de klasse Toegangsprocedure en geeft aan dat er een toegangsprocedure van toepassing is voor een object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftToegangsprocedure'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
