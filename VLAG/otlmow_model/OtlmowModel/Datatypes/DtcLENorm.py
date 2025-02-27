# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlLEKantopsluitingBijkomendeParameter import KlLEKantopsluitingBijkomendeParameter
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcLENormWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bijkomendeParameter = OTLAttribuut(field=KlLEKantopsluitingBijkomendeParameter,
                                                 naam='bijkomendeParameter',
                                                 label='bijkomende parameter',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.bijkomendeParameter',
                                                 definition='Het gedetailleerder typeren van de kantopsluiting.',
                                                 owner=self)

        self._norm = OTLAttribuut(field=StringField,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.norm',
                                  definition='De opgelegde en beschreven standaard van de kantopsluiting.',
                                  owner=self)

    @property
    def bijkomendeParameter(self) -> str:
        """Het gedetailleerder typeren van de kantopsluiting."""
        return self._bijkomendeParameter.get_waarde()

    @bijkomendeParameter.setter
    def bijkomendeParameter(self, value):
        self._bijkomendeParameter.set_waarde(value, owner=self._parent)

    @property
    def norm(self) -> str:
        """De opgelegde en beschreven standaard van de kantopsluiting."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcLENorm(ComplexField):
    """Complex datatype voor de norm van het lijnvormig element."""
    naam = 'DtcLENorm'
    label = 'Norm van het lijnvormig element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm'
    definition = 'Complex datatype voor de norm van het lijnvormig element.'
    waardeObject = DtcLENormWaarden

    def __str__(self):
        return ComplexField.__str__(self)

