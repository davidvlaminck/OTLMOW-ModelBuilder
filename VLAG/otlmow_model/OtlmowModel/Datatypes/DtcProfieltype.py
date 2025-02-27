# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlProfielhoogtemaat import KlProfielhoogtemaat
from ..Datatypes.KlProfielsoort import KlProfielsoort


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfieltypeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._profielhoogtemaat = OTLAttribuut(field=KlProfielhoogtemaat,
                                               naam='profielhoogtemaat',
                                               label='profielhoogtemaat',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype.profielhoogtemaat',
                                               definition='Voorgedefinieerde hoogtemaat van een profiel.',
                                               owner=self)

        self._profielsoort = OTLAttribuut(field=KlProfielsoort,
                                          naam='profielsoort',
                                          label='profielsoort',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype.profielsoort',
                                          definition='Het type profiel (de meest genormeerde types).',
                                          owner=self)

    @property
    def profielhoogtemaat(self) -> str:
        """Voorgedefinieerde hoogtemaat van een profiel."""
        return self._profielhoogtemaat.get_waarde()

    @profielhoogtemaat.setter
    def profielhoogtemaat(self, value):
        self._profielhoogtemaat.set_waarde(value, owner=self._parent)

    @property
    def profielsoort(self) -> str:
        """Het type profiel (de meest genormeerde types)."""
        return self._profielsoort.get_waarde()

    @profielsoort.setter
    def profielsoort(self, value):
        self._profielsoort.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfieltype(ComplexField):
    """Complex datatype om de hoogtemaat en de soort van het profiel in te geven."""
    naam = 'DtcProfieltype'
    label = 'Profieltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype'
    definition = 'Complex datatype om de hoogtemaat en de soort van het profiel in te geven.'
    waardeObject = DtcProfieltypeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

