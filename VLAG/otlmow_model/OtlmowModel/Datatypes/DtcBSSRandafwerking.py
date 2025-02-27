# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlBSSRandafwerking import KlBSSRandafwerking
from ..Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBSSRandafwerkingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._lengteRandafwerking = OTLAttribuut(field=KwantWrdInMeter,
                                                 naam='lengteRandafwerking',
                                                 label='lengte randafwerking',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.lengteRandafwerking',
                                                 definition='De lengte in meter van de randafwerking.',
                                                 owner=self)

        self._randafwerking = OTLAttribuut(field=KlBSSRandafwerking,
                                           naam='randafwerking',
                                           label='randafwerking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.randafwerking',
                                           definition='De wijze waarop de rand van de bestrating is afgewerkt.',
                                           owner=self)

    @property
    def lengteRandafwerking(self) -> KwantWrdInMeterWaarden:
        """De lengte in meter van de randafwerking."""
        return self._lengteRandafwerking.get_waarde()

    @lengteRandafwerking.setter
    def lengteRandafwerking(self, value):
        self._lengteRandafwerking.set_waarde(value, owner=self._parent)

    @property
    def randafwerking(self) -> str:
        """De wijze waarop de rand van de bestrating is afgewerkt."""
        return self._randafwerking.get_waarde()

    @randafwerking.setter
    def randafwerking(self, value):
        self._randafwerking.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBSSRandafwerking(ComplexField):
    """Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding."""
    naam = 'DtcBSSRandafwerking'
    label = 'Betonstraatsteenafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking'
    definition = 'Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding.'
    waardeObject = DtcBSSRandafwerkingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

