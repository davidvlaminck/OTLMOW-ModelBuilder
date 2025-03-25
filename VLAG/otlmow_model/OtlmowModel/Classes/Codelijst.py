# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Codelijst(AIMLinkObject):
    """TODO"""

    typeURI = 'http://www.w3.org/2004/02/skos/core#ConceptScheme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BehoortTot', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Concept', direction='u')  # u = unidirectional

        self._codelijstType = OTLAttribuut(field=StringField,
                                           naam='codelijstType',
                                           label='codelijstType',
                                           objectUri='http://www.w3.org/2004/02/skos/core#ConceptScheme.codelijstType',
                                           definition='TODO',
                                           owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='http://www.w3.org/2004/02/skos/core#ConceptScheme.naam',
                                  definition='TODO',
                                  owner=self)

    @property
    def codelijstType(self) -> str:
        """TODO"""
        return self._codelijstType.get_waarde()

    @codelijstType.setter
    def codelijstType(self, value):
        self._codelijstType.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """TODO"""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
