# coding=utf-8
from datetime import datetime
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SignalisatieOntwerp(AIMLinkObject):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BevatOntwerp', target='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BevatVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#OntwerpVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing

        self._datum = OTLAttribuut(field=DateTimeField,
                                   naam='datum',
                                   label='datum',
                                   objectUri='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp.datum',
                                   definition='TODO',
                                   owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp.naam',
                                  definition='TODO',
                                  owner=self)

    @property
    def datum(self) -> datetime:
        """TODO"""
        return self._datum.get_waarde()

    @datum.setter
    def datum(self, value):
        self._datum.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """TODO"""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
