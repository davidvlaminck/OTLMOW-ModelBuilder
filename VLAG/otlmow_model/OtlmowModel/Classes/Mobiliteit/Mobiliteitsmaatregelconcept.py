# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcTemplate import DtcTemplate, DtcTemplateWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Mobiliteitsmaatregelconcept(OTLAsset):
    """Maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftMaatregelconcept', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsGebaseerdOp', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='i')  # i = direction: incoming

        self._label = OTLAttribuut(field=StringField,
                                   naam='label',
                                   label='label',
                                   objectUri='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept.label',
                                   definition='TODO',
                                   owner=self)

        self._template = OTLAttribuut(field=DtcTemplate,
                                      naam='template',
                                      label='template',
                                      objectUri='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept.template',
                                      definition='Gestructureerd sjabloon dat als basis gebruikt kan worden voor de mobiliteitsmaatregel.',
                                      owner=self)

        self._variabeleSignalisatie = OTLAttribuut(field=BooleanField,
                                                   naam='variabeleSignalisatie',
                                                   label='variabele signalisatie',
                                                   objectUri='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept.variabeleSignalisatie',
                                                   definition='TODO',
                                                   owner=self)

    @property
    def label(self) -> str:
        """TODO"""
        return self._label.get_waarde()

    @label.setter
    def label(self, value):
        self._label.set_waarde(value, owner=self)

    @property
    def template(self) -> DtcTemplateWaarden:
        """Gestructureerd sjabloon dat als basis gebruikt kan worden voor de mobiliteitsmaatregel."""
        return self._template.get_waarde()

    @template.setter
    def template(self, value):
        self._template.set_waarde(value, owner=self)

    @property
    def variabeleSignalisatie(self) -> bool:
        """TODO"""
        return self._variabeleSignalisatie.get_waarde()

    @variabeleSignalisatie.setter
    def variabeleSignalisatie(self, value):
        self._variabeleSignalisatie.set_waarde(value, owner=self)
