# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ..Datatypes.KlStandaardeenheid import KlStandaardeenheid
from ..Datatypes.KlTypeGrootheid import KlTypeGrootheid


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDimensieWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardeenheid = OTLAttribuut(field=KlStandaardeenheid,
                                              naam='standaardeenheid',
                                              label='standaardeenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDimensie.standaardeenheid',
                                              usagenote='Het is aangeraden gebruik te maken van op het web gepubliceerde eenheden, bij voorkeur deze van qudt. bv http://qudt.org/vocab/unit/M voor meten. http://www.cidoc-crm.org/cidoc-crm/P91_has_unit',
                                              definition='Het type eenheid waarin de dimensie werd uitgedrukt.',
                                              owner=self)

        self._type = OTLAttribuut(field=KlTypeGrootheid,
                                  naam='type',
                                  label='type grootheid',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDimensie.type',
                                  usagenote='Het wordt aangeraden QUDT te gebruiken, bv https://qudt.org/vocab/quantitykind/Height. http://www.cidoc-crm.org/cidoc-crm/P2_has_type',
                                  definition='Grootheid van de Dimensie. bv hoogte, lengte, breedte, diameter,...',
                                  owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDimensie.waarde',
                                    usagenote='http://www.cidoc-crm.org/cidoc-crm/P90_has_value',
                                    definition='Getal waarmee de kwantiteit van het kenmerk kan worden uitgedrukt.',
                                    owner=self)

    @property
    def standaardeenheid(self) -> str:
        """Het type eenheid waarin de dimensie werd uitgedrukt."""
        return self._standaardeenheid.get_waarde()

    @standaardeenheid.setter
    def standaardeenheid(self, value):
        self._standaardeenheid.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """Grootheid van de Dimensie. bv hoogte, lengte, breedte, diameter,..."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)

    @property
    def waarde(self) -> float:
        """Getal waarmee de kwantiteit van het kenmerk kan worden uitgedrukt."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDimensie(ComplexField):
    """TODO"""
    naam = 'DtcDimensie'
    label = 'Dimensie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDimensie'
    definition = 'TODO'
    usagenote = 'http://www.cidoc-crm.org/cidoc-crm/E54_Dimension'
    waardeObject = DtcDimensieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

