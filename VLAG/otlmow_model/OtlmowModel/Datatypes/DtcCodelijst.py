# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlCodelijstType import KlCodelijstType
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCodelijstWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._codelijstType = OTLAttribuut(field=KlCodelijstType,
                                           naam='codelijstType',
                                           label='codelijst type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCodelijst.codelijstType',
                                           definition='TODO',
                                           owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCodelijst.naam',
                                  definition='TODO',
                                  owner=self)

    @property
    def codelijstType(self) -> str:
        """TODO"""
        return self._codelijstType.get_waarde()

    @codelijstType.setter
    def codelijstType(self, value):
        self._codelijstType.set_waarde(value, owner=self._parent)

    @property
    def naam(self) -> str:
        """TODO"""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCodelijst(ComplexField):
    """TODO"""
    naam = 'DtcCodelijst'
    label = 'Codelijst'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCodelijst'
    definition = 'TODO'
    waardeObject = DtcCodelijstWaarden

    def __str__(self):
        return ComplexField.__str__(self)

