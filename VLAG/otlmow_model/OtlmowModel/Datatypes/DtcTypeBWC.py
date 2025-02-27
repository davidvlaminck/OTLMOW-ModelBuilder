# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlConstructie import KlConstructie
from ..Datatypes.KlTypeConcept import KlTypeConcept


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTypeBWCWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._typeConcept = OTLAttribuut(field=KlTypeConcept,
                                         naam='typeConcept',
                                         label='type concept',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcTypeBWC.typeConcept',
                                         definition='Het type concept van de beweegbare waterkerende constructie.',
                                         owner=self)

        self._typeConstructie = OTLAttribuut(field=KlConstructie,
                                             naam='typeConstructie',
                                             label='type constructie',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcTypeBWC.typeConstructie',
                                             definition='De type beweegbare waterkerende constructie.',
                                             owner=self)

    @property
    def typeConcept(self) -> str:
        """Het type concept van de beweegbare waterkerende constructie."""
        return self._typeConcept.get_waarde()

    @typeConcept.setter
    def typeConcept(self, value):
        self._typeConcept.set_waarde(value, owner=self._parent)

    @property
    def typeConstructie(self) -> str:
        """De type beweegbare waterkerende constructie."""
        return self._typeConstructie.get_waarde()

    @typeConstructie.setter
    def typeConstructie(self, value):
        self._typeConstructie.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTypeBWC(ComplexField):
    """Complex datatype om het type beweegbare waterkerende constructie aan te duiden"""
    naam = 'DtcTypeBWC'
    label = 'Type beweegbare waterkerende constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcTypeBWC'
    definition = 'Complex datatype om het type beweegbare waterkerende constructie aan te duiden'
    waardeObject = DtcTypeBWCWaarden

    def __str__(self):
        return ComplexField.__str__(self)

