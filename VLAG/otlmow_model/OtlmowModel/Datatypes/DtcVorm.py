# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDimensie import DtcDimensie, DtcDimensieWaarden
from ..Datatypes.KlVormType import KlVormType


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVormWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._dimensie = OTLAttribuut(field=DtcDimensie,
                                      naam='dimensie',
                                      label='',
                                      objectUri='https://w3id.org/tribont/core#Shape.dimensie',
                                      kardinaliteit_max='*',
                                      definition='',
                                      owner=self)

        self._vormType = OTLAttribuut(field=KlVormType,
                                      naam='vormType',
                                      label='',
                                      objectUri='https://w3id.org/tribont/core#Shape.vormType',
                                      definition='',
                                      owner=self)

    @property
    def dimensie(self) -> List[DtcDimensieWaarden]:
        """"""
        return self._dimensie.get_waarde()

    @dimensie.setter
    def dimensie(self, value):
        self._dimensie.set_waarde(value, owner=self._parent)

    @property
    def vormType(self) -> str:
        """"""
        return self._vormType.get_waarde()

    @vormType.setter
    def vormType(self, value):
        self._vormType.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVorm(ComplexField):
    """"""
    naam = 'DtcVorm'
    label = ''
    objectUri = 'https://w3id.org/tribont/core#Shape'
    definition = ''
    waardeObject = DtcVormWaarden

    def __str__(self):
        return ComplexField.__str__(self)

