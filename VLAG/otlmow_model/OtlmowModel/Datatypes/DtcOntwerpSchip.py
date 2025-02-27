# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ..Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOntwerpSchipWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcOntwerpSchip.breedte',
                                     definition='De breedte van het ontwerpschip.',
                                     owner=self)

        self._diepgang = OTLAttribuut(field=KwantWrdInMeter,
                                      naam='diepgang',
                                      label='diepgang',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcOntwerpSchip.diepgang',
                                      definition='De diepgang van het ontwerpschip.',
                                      owner=self)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcOntwerpSchip.gewicht',
                                     definition='Het gewicht van het ontwerpschip.',
                                     owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcOntwerpSchip.lengte',
                                    definition='De lengte van het ontwerpschip.',
                                    owner=self)

    @property
    def breedte(self) -> KwantWrdInMeterWaarden:
        """De breedte van het ontwerpschip."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def diepgang(self) -> KwantWrdInMeterWaarden:
        """De diepgang van het ontwerpschip."""
        return self._diepgang.get_waarde()

    @diepgang.setter
    def diepgang(self, value):
        self._diepgang.set_waarde(value, owner=self._parent)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van het ontwerpschip."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self._parent)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van het ontwerpschip."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOntwerpSchip(ComplexField):
    """Complexe datatype om de afmetingen van het ontwerpschip bij te houden."""
    naam = 'DtcOntwerpSchip'
    label = 'Ontwerp schip'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcOntwerpSchip'
    definition = 'Complexe datatype om de afmetingen van het ontwerpschip bij te houden.'
    waardeObject = DtcOntwerpSchipWaarden

    def __str__(self):
        return ComplexField.__str__(self)

