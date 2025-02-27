# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlVervuilingSoorten import KlVervuilingSoorten
from ..Datatypes.KwantWrdInMicrogramPerKilogram import KwantWrdInMicrogramPerKilogram, KwantWrdInMicrogramPerKilogramWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSoortVervuilingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._microgramPerKilogram = OTLAttribuut(field=KwantWrdInMicrogramPerKilogram,
                                                  naam='microgramPerKilogram',
                                                  label='microgram per kilogram',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoortVervuiling.microgramPerKilogram',
                                                  kardinaliteit_max='3',
                                                  definition='De concentratie van de vervuiling kan in µg/kg bepaalt worden.',
                                                  owner=self)

        self._soortVervuiling = OTLAttribuut(field=KlVervuilingSoorten,
                                             naam='soortVervuiling',
                                             label='soort vervuiling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoortVervuiling.soortVervuiling',
                                             definition='Het soort vervuiling kan hiermee bepaalt worden.',
                                             owner=self)

    @property
    def microgramPerKilogram(self) -> List[KwantWrdInMicrogramPerKilogramWaarden]:
        """De concentratie van de vervuiling kan in µg/kg bepaalt worden."""
        return self._microgramPerKilogram.get_waarde()

    @microgramPerKilogram.setter
    def microgramPerKilogram(self, value):
        self._microgramPerKilogram.set_waarde(value, owner=self._parent)

    @property
    def soortVervuiling(self) -> str:
        """Het soort vervuiling kan hiermee bepaalt worden."""
        return self._soortVervuiling.get_waarde()

    @soortVervuiling.setter
    def soortVervuiling(self, value):
        self._soortVervuiling.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSoortVervuiling(ComplexField):
    """Complex datatype om het soort vervuiling te bepalen."""
    naam = 'DtcSoortVervuiling'
    label = 'soort vervuiling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoortVervuiling'
    definition = 'Complex datatype om het soort vervuiling te bepalen.'
    waardeObject = DtcSoortVervuilingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

