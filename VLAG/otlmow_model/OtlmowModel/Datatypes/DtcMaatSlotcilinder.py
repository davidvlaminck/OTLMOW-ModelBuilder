# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMaatSlotcilinderWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._maatBinnenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                             naam='maatBinnenzijde',
                                             label='maat binnenzijde',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMaatSlotcilinder.maatBinnenzijde',
                                             definition='De maat van de slotcilinder aan de binnenkant.',
                                             owner=self)

        self._maatBuitenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                             naam='maatBuitenzijde',
                                             label='maat buitenzijde',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMaatSlotcilinder.maatBuitenzijde',
                                             definition='De maat van de cilinder aan de buitenkant.',
                                             owner=self)

    @property
    def maatBinnenzijde(self) -> KwantWrdInMillimeterWaarden:
        """De maat van de slotcilinder aan de binnenkant."""
        return self._maatBinnenzijde.get_waarde()

    @maatBinnenzijde.setter
    def maatBinnenzijde(self, value):
        self._maatBinnenzijde.set_waarde(value, owner=self._parent)

    @property
    def maatBuitenzijde(self) -> KwantWrdInMillimeterWaarden:
        """De maat van de cilinder aan de buitenkant."""
        return self._maatBuitenzijde.get_waarde()

    @maatBuitenzijde.setter
    def maatBuitenzijde(self, value):
        self._maatBuitenzijde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMaatSlotcilinder(ComplexField):
    """Complex datatype voor de maat van de slotcilinder."""
    naam = 'DtcMaatSlotcilinder'
    label = 'Maat van de slotcilinder'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMaatSlotcilinder'
    definition = 'Complex datatype voor de maat van de slotcilinder.'
    waardeObject = DtcMaatSlotcilinderWaarden

    def __str__(self):
        return ComplexField.__str__(self)

