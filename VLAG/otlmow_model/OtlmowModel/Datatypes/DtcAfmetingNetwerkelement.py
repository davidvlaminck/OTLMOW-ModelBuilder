# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ..Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingNetwerkelementWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfmetingNetwerkelement.breedte',
                                     definition='De breedte van het netwerkelement in centimeter.',
                                     owner=self)

        self._diepte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfmetingNetwerkelement.diepte',
                                    definition='De diepte van het netwerkelement in centimeter.',
                                    owner=self)

        self._hoogteInRU = OTLAttribuut(field=IntegerField,
                                        naam='hoogteInRU',
                                        label='hoogte in RU',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfmetingNetwerkelement.hoogteInRU',
                                        definition='De hoogte die door het netwerkelement wordt ingenomen, uitgedrukt in RU (rack units).',
                                        owner=self)

    @property
    def breedte(self) -> KwantWrdInCentimeterWaarden:
        """De breedte van het netwerkelement in centimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def diepte(self) -> KwantWrdInCentimeterWaarden:
        """De diepte van het netwerkelement in centimeter."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self._parent)

    @property
    def hoogteInRU(self) -> int:
        """De hoogte die door het netwerkelement wordt ingenomen, uitgedrukt in RU (rack units)."""
        return self._hoogteInRU.get_waarde()

    @hoogteInRU.setter
    def hoogteInRU(self, value):
        self._hoogteInRU.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingNetwerkelement(ComplexField):
    """Complex datatype voor de afmetingen van een netwerktelement."""
    naam = 'DtcAfmetingNetwerkelement'
    label = 'Afmeting netwerkelement'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfmetingNetwerkelement'
    definition = 'Complex datatype voor de afmetingen van een netwerktelement.'
    waardeObject = DtcAfmetingNetwerkelementWaarden

    def __str__(self):
        return ComplexField.__str__(self)

