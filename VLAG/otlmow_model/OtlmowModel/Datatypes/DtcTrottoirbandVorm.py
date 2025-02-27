# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlLETrottoirbandVorm import KlLETrottoirbandVorm
from ..Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTrottoirbandVormWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.breedte',
                                     definition='De breedte van de trottoirband.',
                                     owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.dikte',
                                   definition='De dikte, ook aanzien als hoogte, van de trottoirband.',
                                   owner=self)

        self._vorm = OTLAttribuut(field=KlLETrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.vorm',
                                  definition='De vorm van de trottoirband.',
                                  owner=self)

    @property
    def breedte(self) -> KwantWrdInCentimeterWaarden:
        """De breedte van de trottoirband."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De dikte, ook aanzien als hoogte, van de trottoirband."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self._parent)

    @property
    def vorm(self) -> str:
        """De vorm van de trottoirband."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTrottoirbandVorm(ComplexField):
    """Complex datatype voor de vorm van een trotoirband."""
    naam = 'DtcTrottoirbandVorm'
    label = 'Trottoirband vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm'
    definition = 'Complex datatype voor de vorm van een trotoirband.'
    waardeObject = DtcTrottoirbandVormWaarden

    def __str__(self):
        return ComplexField.__str__(self)

