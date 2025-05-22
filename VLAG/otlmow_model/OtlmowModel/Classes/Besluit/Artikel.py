# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Artikel(AIMLinkObject):
    """Formeel afgebakend onderdeel van een besluit,dat een of meer van de beoogde rechtsgevolgen beschrijft."""

    typeURI = 'https://data.vlaanderen.be/ns/besluit#Artikel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/besluit#heeftVoorwaarde', target='https://data.vlaanderen.be/ns/besluit#Voorwaarde', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftMobiliteitsmaatregel', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOnderdeelVan', target='https://data.vlaanderen.be/ns/besluit#Besluit', direction='o')  # o = direction: outgoing

        self._nummer = OTLAttribuut(field=StringField,
                                    naam='nummer',
                                    label='nummer',
                                    objectUri='http://data.europa.eu/eli/ontology#number',
                                    definition='TODO',
                                    owner=self)

    @property
    def nummer(self) -> str:
        """TODO"""
        return self._nummer.get_waarde()

    @nummer.setter
    def nummer(self, value):
        self._nummer.set_waarde(value, owner=self)
