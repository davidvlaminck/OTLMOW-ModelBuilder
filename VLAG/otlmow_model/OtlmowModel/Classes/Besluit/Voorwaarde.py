# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voorwaarde(OTLAsset):
    """Datgene waaraan moet voldaan worden om een geldig besluit te zijn."""

    typeURI = 'http://data.vlaanderen.be/ns/besluit#Voorwaarde'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/besluit#heeftVoorwaarde', target='https://data.vlaanderen.be/ns/besluit#Artikel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/besluit#heeftVoorwaarde', target='https://data.vlaanderen.be/ns/besluit#Besluit', direction='i')  # i = direction: incoming

        self._beschrijving = OTLAttribuut(field=StringField,
                                          naam='beschrijving',
                                          label='beschrijving',
                                          objectUri='http://data.vlaanderen.be/ns/besluit#Voorwaarde.beschrijving',
                                          definition='TODO',
                                          owner=self)

    @property
    def beschrijving(self) -> str:
        """TODO"""
        return self._beschrijving.get_waarde()

    @beschrijving.setter
    def beschrijving(self, value):
        self._beschrijving.set_waarde(value, owner=self)
