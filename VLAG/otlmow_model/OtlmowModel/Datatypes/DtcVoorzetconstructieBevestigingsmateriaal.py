# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlVoorzetconstructieBevestigingsmateriaal import KlVoorzetconstructieBevestigingsmateriaal
from ..Datatypes.KlVoorzetconstructieBevestigingsmateriaalDiameter import KlVoorzetconstructieBevestigingsmateriaalDiameter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVoorzetconstructieBevestigingsmateriaalWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._diameter = OTLAttribuut(field=KlVoorzetconstructieBevestigingsmateriaalDiameter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieBevestigingsmateriaal.diameter',
                                      definition='De diameter van de voorzetconstructie.',
                                      owner=self)

        self._materiaal = OTLAttribuut(field=KlVoorzetconstructieBevestigingsmateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieBevestigingsmateriaal.materiaal',
                                       definition='Het materiaal gebruikt bij de bevestiging van de voorzetconstructie.',
                                       owner=self)

    @property
    def diameter(self) -> str:
        """De diameter van de voorzetconstructie."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self._parent)

    @property
    def materiaal(self) -> str:
        """Het materiaal gebruikt bij de bevestiging van de voorzetconstructie."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVoorzetconstructieBevestigingsmateriaal(ComplexField):
    """Complex datatype voor de bevestigingsmaterialen van een voorzetconstructie."""
    naam = 'DtcVoorzetconstructieBevestigingsmateriaal'
    label = 'Voorzetconstructie bevestigingsmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieBevestigingsmateriaal'
    definition = 'Complex datatype voor de bevestigingsmaterialen van een voorzetconstructie.'
    waardeObject = DtcVoorzetconstructieBevestigingsmateriaalWaarden

    def __str__(self):
        return ComplexField.__str__(self)

