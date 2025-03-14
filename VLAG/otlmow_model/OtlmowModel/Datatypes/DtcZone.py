# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcGeometrie import DtcGeometrie, DtcGeometrieWaarden
from ..Datatypes.KlZonetype import KlZonetype


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcZoneWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._geometrie = OTLAttribuut(field=DtcGeometrie,
                                       naam='geometrie',
                                       label='geometrie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcZone.geometrie',
                                       definition='2D weergave van de zone.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlZonetype,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcZone.type',
                                  usagenote='Bijvoorbeeld: corridor, evenementzone',
                                  definition='type zone',
                                  owner=self)

    @property
    def geometrie(self) -> DtcGeometrieWaarden:
        """2D weergave van de zone."""
        return self._geometrie.get_waarde()

    @geometrie.setter
    def geometrie(self, value):
        self._geometrie.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """type zone"""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcZone(ComplexField):
    """Ruimtelijk gebied"""
    naam = 'DtcZone'
    label = 'Zone'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcZone'
    definition = 'Ruimtelijk gebied'
    waardeObject = DtcZoneWaarden

    def __str__(self):
        return ComplexField.__str__(self)

