# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingZijdeInMmWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._zijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='zijde',
                                   label='zijde',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingZijdeInMm.zijde',
                                   definition='De afmeting van een zijde in millimeter.',
                                   owner=self)

    @property
    def zijde(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting van een zijde in millimeter."""
        return self._zijde.get_waarde()

    @zijde.setter
    def zijde(self, value):
        self._zijde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingZijdeInMm(ComplexField):
    """Complex datatype voor de afmeting van een zijde in millimeter."""
    naam = 'DtcAfmetingZijdeInMm'
    label = 'Afmeting zijde in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingZijdeInMm'
    definition = 'Complex datatype voor de afmeting van een zijde in millimeter.'
    waardeObject = DtcAfmetingZijdeInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

