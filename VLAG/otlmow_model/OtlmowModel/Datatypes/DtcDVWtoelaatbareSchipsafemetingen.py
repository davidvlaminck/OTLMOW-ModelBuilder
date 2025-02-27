# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDVWtoelaatbareSchipsafemetingenWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._maximaleBreedte = OTLAttribuut(field=KwantWrdInMeter,
                                             naam='maximaleBreedte',
                                             label='maximale breedte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcDVWtoelaatbareSchipsafemetingen.maximaleBreedte',
                                             definition='De maximale toelaatbare Breedte',
                                             owner=self)

        self._maximaleDiepgang = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='maximaleDiepgang',
                                              label='maximale diepgang',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcDVWtoelaatbareSchipsafemetingen.maximaleDiepgang',
                                              definition='De maximale toelaatbare diepgang.',
                                              owner=self)

        self._maximaleHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='maximaleHoogte',
                                            label='maximale hoogte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcDVWtoelaatbareSchipsafemetingen.maximaleHoogte',
                                            definition='De maximale toelaatbare hoogte.',
                                            owner=self)

        self._maximaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='maximaleLengte',
                                            label='maximale lengte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcDVWtoelaatbareSchipsafemetingen.maximaleLengte',
                                            definition='De maximale toelaatbare lengte.',
                                            owner=self)

    @property
    def maximaleBreedte(self) -> KwantWrdInMeterWaarden:
        """De maximale toelaatbare Breedte"""
        return self._maximaleBreedte.get_waarde()

    @maximaleBreedte.setter
    def maximaleBreedte(self, value):
        self._maximaleBreedte.set_waarde(value, owner=self._parent)

    @property
    def maximaleDiepgang(self) -> KwantWrdInMeterWaarden:
        """De maximale toelaatbare diepgang."""
        return self._maximaleDiepgang.get_waarde()

    @maximaleDiepgang.setter
    def maximaleDiepgang(self, value):
        self._maximaleDiepgang.set_waarde(value, owner=self._parent)

    @property
    def maximaleHoogte(self) -> KwantWrdInMeterWaarden:
        """De maximale toelaatbare hoogte."""
        return self._maximaleHoogte.get_waarde()

    @maximaleHoogte.setter
    def maximaleHoogte(self, value):
        self._maximaleHoogte.set_waarde(value, owner=self._parent)

    @property
    def maximaleLengte(self) -> KwantWrdInMeterWaarden:
        """De maximale toelaatbare lengte."""
        return self._maximaleLengte.get_waarde()

    @maximaleLengte.setter
    def maximaleLengte(self, value):
        self._maximaleLengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDVWtoelaatbareSchipsafemetingen(ComplexField):
    """Complexe datatype om de toelaatbare schipsafmetingen bij te houden."""
    naam = 'DtcDVWtoelaatbareSchipsafemetingen'
    label = 'Toelaatbare schipsafmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcDVWtoelaatbareSchipsafemetingen'
    definition = 'Complexe datatype om de toelaatbare schipsafmetingen bij te houden.'
    waardeObject = DtcDVWtoelaatbareSchipsafemetingenWaarden

    def __str__(self):
        return ComplexField.__str__(self)

