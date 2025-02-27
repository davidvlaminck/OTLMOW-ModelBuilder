# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlDuurzaamheidsklasseHout import KlDuurzaamheidsklasseHout
from ..Datatypes.KwantWrdInMegaPascal import KwantWrdInMegaPascal, KwantWrdInMegaPascalWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKunststofspecificatiesWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._elasticiteitsmodulus = OTLAttribuut(field=KwantWrdInMegaPascal,
                                                  naam='elasticiteitsmodulus',
                                                  label='elasticiteitsmodulus',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKunststofspecificaties.elasticiteitsmodulus',
                                                  definition='Materiaaleigenschap die een maat is voor de stijfheid of starheid van het materiaal, uitgedrukt in N/m² of Pa.',
                                                  owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKunststofspecificaties.naam',
                                  definition='Naam of chemische formule van het kunststof of de samengestelde elementen.',
                                  owner=self)

        self._norm = OTLAttribuut(field=KlDuurzaamheidsklasseHout,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKunststofspecificaties.norm',
                                  definition='Toegepaste norm op het kunststof voor kwaliteit te testen.',
                                  owner=self)

        self._treksterkte = OTLAttribuut(field=KwantWrdInMegaPascal,
                                         naam='treksterkte',
                                         label='treksterkte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKunststofspecificaties.treksterkte',
                                         definition='Treksterkte van het kunststof door de volgens de norm uitgevoerde trekproef, uitgedrukt in N/m².',
                                         owner=self)

    @property
    def elasticiteitsmodulus(self) -> KwantWrdInMegaPascalWaarden:
        """Materiaaleigenschap die een maat is voor de stijfheid of starheid van het materiaal, uitgedrukt in N/m² of Pa."""
        return self._elasticiteitsmodulus.get_waarde()

    @elasticiteitsmodulus.setter
    def elasticiteitsmodulus(self, value):
        self._elasticiteitsmodulus.set_waarde(value, owner=self._parent)

    @property
    def naam(self) -> str:
        """Naam of chemische formule van het kunststof of de samengestelde elementen."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self._parent)

    @property
    def norm(self) -> str:
        """Toegepaste norm op het kunststof voor kwaliteit te testen."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self._parent)

    @property
    def treksterkte(self) -> KwantWrdInMegaPascalWaarden:
        """Treksterkte van het kunststof door de volgens de norm uitgevoerde trekproef, uitgedrukt in N/m²."""
        return self._treksterkte.get_waarde()

    @treksterkte.setter
    def treksterkte(self, value):
        self._treksterkte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKunststofspecificaties(ComplexField):
    """Complex datatype dat specifieke eigenschappen van de kunststof bevat."""
    naam = 'DtcKunststofspecificaties'
    label = 'Kunststofspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKunststofspecificaties'
    definition = 'Complex datatype dat specifieke eigenschappen van de kunststof bevat.'
    waardeObject = DtcKunststofspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

