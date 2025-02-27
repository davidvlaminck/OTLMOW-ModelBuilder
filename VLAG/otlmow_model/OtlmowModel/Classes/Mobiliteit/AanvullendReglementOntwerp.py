# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanvullendReglementOntwerp(OTLAsset):
    """"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BevatOntwerp', target='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BevatOntwerpVoor', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOntwerpVoor', target='http://data.vlaanderen.be/ns/besluit#AanvullendReglement', direction='o')  # o = direction: outgoing

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp.naam',
                                  definition='',
                                  owner=self)

    @property
    def naam(self) -> str:
        """"""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
