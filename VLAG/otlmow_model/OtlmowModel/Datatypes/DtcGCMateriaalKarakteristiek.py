# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlLEGCGeluidskarakteristiek import KlLEGCGeluidskarakteristiek
from ..Datatypes.KlLEGCMateriaal import KlLEGCMateriaal


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGCMateriaalKarakteristiekWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._geluidskarakteristiek = OTLAttribuut(field=KlLEGCGeluidskarakteristiek,
                                                   naam='geluidskarakteristiek',
                                                   label='geluidskarakteristiek',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek.geluidskarakteristiek',
                                                   definition='Het kenmerkend gedrag inzake geluid van de geluidswerende constructie.',
                                                   owner=self)

        self._materiaal = OTLAttribuut(field=KlLEGCMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek.materiaal',
                                       definition='Het materiaal van de geluidswerende constructie.',
                                       owner=self)

    @property
    def geluidskarakteristiek(self) -> str:
        """Het kenmerkend gedrag inzake geluid van de geluidswerende constructie."""
        return self._geluidskarakteristiek.get_waarde()

    @geluidskarakteristiek.setter
    def geluidskarakteristiek(self, value):
        self._geluidskarakteristiek.set_waarde(value, owner=self._parent)

    @property
    def materiaal(self) -> str:
        """Het materiaal van de geluidswerende constructie."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGCMateriaalKarakteristiek(ComplexField):
    """Complex datatype voor het materiaal en zijn geluidskarakteristiek van de geluidswerende constructie."""
    naam = 'DtcGCMateriaalKarakteristiek'
    label = 'Materiaal karakteristiek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek'
    definition = 'Complex datatype voor het materiaal en zijn geluidskarakteristiek van de geluidswerende constructie.'
    waardeObject = DtcGCMateriaalKarakteristiekWaarden

    def __str__(self):
        return ComplexField.__str__(self)

