# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcTemplate import DtcTemplate, DtcTemplateWaarden
from ...Datatypes.KlVerkeerstekenconceptStatus import KlVerkeerstekenconceptStatus
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeerstekenconcept(AIMLinkObject):
    """Inhoudelijke definitie van de betekenis van een verkeersteken zoals opgenomen in de wegcode."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftMaatregelconcept', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept', direction='o')  # o = direction: outgoing

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.afbeelding',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='TODO',
                                        owner=self)

        self._betekenis = OTLAttribuut(field=StringField,
                                       naam='betekenis',
                                       label='betekenis',
                                       objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.betekenis',
                                       definition='TODO',
                                       owner=self)

        self._heeftInstructie = OTLAttribuut(field=DtcTemplate,
                                             naam='heeftInstructie',
                                             label='instructie',
                                             objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.heeftInstructie',
                                             kardinaliteit_min='0',
                                             kardinaliteit_max='*',
                                             definition='TODO',
                                             owner=self)

        self._status = OTLAttribuut(field=KlVerkeerstekenconceptStatus,
                                    naam='status',
                                    label='status',
                                    objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.status',
                                    definition='TODO',
                                    owner=self)

        self._verkeersbordcode = OTLAttribuut(field=StringField,
                                              naam='verkeersbordcode',
                                              label='verkeersbordcode',
                                              objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.verkeersbordcode',
                                              definition='TODO',
                                              owner=self)

    @property
    def afbeelding(self) -> List[DtcDocumentWaarden]:
        """TODO"""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def betekenis(self) -> str:
        """TODO"""
        return self._betekenis.get_waarde()

    @betekenis.setter
    def betekenis(self, value):
        self._betekenis.set_waarde(value, owner=self)

    @property
    def heeftInstructie(self) -> List[DtcTemplateWaarden]:
        """TODO"""
        return self._heeftInstructie.get_waarde()

    @heeftInstructie.setter
    def heeftInstructie(self, value):
        self._heeftInstructie.set_waarde(value, owner=self)

    @property
    def status(self) -> str:
        """TODO"""
        return self._status.get_waarde()

    @status.setter
    def status(self, value):
        self._status.set_waarde(value, owner=self)

    @property
    def verkeersbordcode(self) -> str:
        """TODO"""
        return self._verkeersbordcode.get_waarde()

    @verkeersbordcode.setter
    def verkeersbordcode(self, value):
        self._verkeersbordcode.set_waarde(value, owner=self)
