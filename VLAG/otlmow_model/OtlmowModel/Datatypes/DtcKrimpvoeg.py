# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcKrimpvoegvulling import DtcKrimpvoegvulling, DtcKrimpvoegvullingWaarden
from ..Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoegWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._krimpvoegFrequentie = OTLAttribuut(field=KwantWrdInMeter,
                                                 naam='krimpvoegFrequentie',
                                                 label='krimpvoeg frequentie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.krimpvoegFrequentie',
                                                 definition='De afstand tussen de krimpvoegen in meter.',
                                                 owner=self)

        self._krimpvoegvulling = OTLAttribuut(field=DtcKrimpvoegvulling,
                                              naam='krimpvoegvulling',
                                              label='krimpvoegvulling',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.krimpvoegvulling',
                                              definition='Het gebruikte materiaal met zijn technische fiche als krimpvoegvulling.',
                                              owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.totaleLengte',
                                          definition='De totale lengte in meter.',
                                          owner=self)

    @property
    def krimpvoegFrequentie(self) -> KwantWrdInMeterWaarden:
        """De afstand tussen de krimpvoegen in meter."""
        return self._krimpvoegFrequentie.get_waarde()

    @krimpvoegFrequentie.setter
    def krimpvoegFrequentie(self, value):
        self._krimpvoegFrequentie.set_waarde(value, owner=self._parent)

    @property
    def krimpvoegvulling(self) -> DtcKrimpvoegvullingWaarden:
        """Het gebruikte materiaal met zijn technische fiche als krimpvoegvulling."""
        return self._krimpvoegvulling.get_waarde()

    @krimpvoegvulling.setter
    def krimpvoegvulling(self, value):
        self._krimpvoegvulling.set_waarde(value, owner=self._parent)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte in meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoeg(ComplexField):
    """Complex datatype voor de informatie van de krimpvoegen."""
    naam = 'DtcKrimpvoeg'
    label = 'Krimpvoeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg'
    definition = 'Complex datatype voor de informatie van de krimpvoegen.'
    waardeObject = DtcKrimpvoegWaarden

    def __str__(self):
        return ComplexField.__str__(self)

