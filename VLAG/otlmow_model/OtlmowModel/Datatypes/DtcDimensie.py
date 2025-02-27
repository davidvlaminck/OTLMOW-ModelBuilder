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
                                              label='',
                                              objectUri='http://www.cidoc-crm.org/cidoc-crm/E54_Dimension.standaardeenheid',
                                              definition='',
                                              owner=self)

        self._type = OTLAttribuut(field=KlTypeGrootheid,
                                  naam='type',
                                  label='',
                                  objectUri='http://www.cidoc-crm.org/cidoc-crm/E54_Dimension.type',
                                  definition='',
                                  owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='',
                                    objectUri='http://www.cidoc-crm.org/cidoc-crm/E54_Dimension.waarde',
                                    definition='',
                                    owner=self)

    @property
    def standaardeenheid(self) -> str:
        """"""
        return self._standaardeenheid.get_waarde()

    @standaardeenheid.setter
    def standaardeenheid(self, value):
        self._standaardeenheid.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """"""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)

    @property
    def waarde(self) -> float:
        """"""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDimensie(ComplexField):
    """"""
    naam = 'DtcDimensie'
    label = ''
    objectUri = 'http://www.cidoc-crm.org/cidoc-crm/E54_Dimension'
    definition = ''
    waardeObject = DtcDimensieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

