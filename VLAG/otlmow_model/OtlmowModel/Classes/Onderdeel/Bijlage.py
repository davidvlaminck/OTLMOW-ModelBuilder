# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from ...Datatypes.KlBijlageType import KlBijlageType
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bijlage(AbstracteAanvullendeGeometrie, GeenGeometrie):
    """Een bestand (document,afbeelding,...) dat behoort tot 1 of meerdere assets."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bijlage'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBijlage', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming

        self._type = OTLAttribuut(field=KlBijlageType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bijlage.type',
                                  kardinaliteit_max='*',
                                  definition='De typering of categorie van de bijlage.',
                                  owner=self)

    @property
    def type(self) -> List[str]:
        """De typering of categorie van de bijlage."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
