# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInMmWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInMm.breedte',
                                     definition='De breedte in millimeter.',
                                     owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInMm.lengte',
                                    definition='De lengte in millimeter.',
                                    owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De breedte in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte in millimeter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInMm(ComplexField):
    """Complex datatype voor de afmeting van de breedte en de lengte in millimeter."""
    naam = 'DtcAfmetingBxlInMm'
    label = 'Afmeting bxl in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInMm'
    definition = 'Complex datatype voor de afmeting van de breedte en de lengte in millimeter.'
    waardeObject = DtcAfmetingBxlInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

