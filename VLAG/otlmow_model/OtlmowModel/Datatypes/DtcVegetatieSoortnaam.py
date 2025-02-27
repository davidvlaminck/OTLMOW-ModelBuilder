# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlWetenschappelijkeSoortnaam import KlWetenschappelijkeSoortnaam
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVegetatieSoortnaamWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._code = OTLAttribuut(field=StringField,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.code',
                                  usagenote='De GBIF code is een unieke gestandaardiseerde code uitgegeven door het GBIF (the Global Biodiversity Information Facility - GBIF.org)',
                                  definition='De unieke identificator voor de soort van het vegetatie-element.',
                                  owner=self)

        self._soortnaamNederlands = OTLAttribuut(field=StringField,
                                                 naam='soortnaamNederlands',
                                                 label='soortnaam nederlands',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamNederlands',
                                                 definition='De Nederlandse soortnaam van de beplanting.',
                                                 owner=self)

        self._soortnaamWetenschappelijk = OTLAttribuut(field=StringField,
                                                       naam='soortnaamWetenschappelijk',
                                                       label='soortnaam wetenschappelijk',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamWetenschappelijk',
                                                       usagenote='Attribuut uit gebruik sinds versie 2.12.0',
                                                       deprecated_version='2.12.0',
                                                       definition='De wetenschappelijke soortnaam van de beplanting.',
                                                       owner=self)

        self._wetenschappelijkeSoortnaam = OTLAttribuut(field=KlWetenschappelijkeSoortnaam,
                                                        naam='wetenschappelijkeSoortnaam',
                                                        label='wetenschappelijke soortnaam',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.wetenschappelijkeSoortnaam',
                                                        definition='De wetenschappelijke soortnaam van de vegetatie.',
                                                        owner=self)

    @property
    def code(self) -> str:
        """De unieke identificator voor de soort van het vegetatie-element."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self._parent)

    @property
    def soortnaamNederlands(self) -> str:
        """De Nederlandse soortnaam van de beplanting."""
        return self._soortnaamNederlands.get_waarde()

    @soortnaamNederlands.setter
    def soortnaamNederlands(self, value):
        self._soortnaamNederlands.set_waarde(value, owner=self._parent)

    @property
    def soortnaamWetenschappelijk(self) -> str:
        """De wetenschappelijke soortnaam van de beplanting."""
        return self._soortnaamWetenschappelijk.get_waarde()

    @soortnaamWetenschappelijk.setter
    def soortnaamWetenschappelijk(self, value):
        self._soortnaamWetenschappelijk.set_waarde(value, owner=self._parent)

    @property
    def wetenschappelijkeSoortnaam(self) -> str:
        """De wetenschappelijke soortnaam van de vegetatie."""
        return self._wetenschappelijkeSoortnaam.get_waarde()

    @wetenschappelijkeSoortnaam.setter
    def wetenschappelijkeSoortnaam(self, value):
        self._wetenschappelijkeSoortnaam.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVegetatieSoortnaam(ComplexField):
    """Complex datatype voor de soortnaam en code van een begroeiing."""
    naam = 'DtcVegetatieSoortnaam'
    label = 'Vegetatie soortnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam'
    definition = 'Complex datatype voor de soortnaam en code van een begroeiing.'
    waardeObject = DtcVegetatieSoortnaamWaarden

    def __str__(self):
        return ComplexField.__str__(self)

