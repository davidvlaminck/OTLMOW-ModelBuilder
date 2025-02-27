# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInCmWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._diameter = OTLAttribuut(field=KwantWrdInCentimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInCm.diameter',
                                      definition='De diameter in centimeter.',
                                      owner=self)

    @property
    def diameter(self) -> KwantWrdInCentimeterWaarden:
        """De diameter in centimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInCm(ComplexField):
    """Complex datatype voor de afmeting van een diameter in centimeter."""
    naam = 'DtcAfmetingDiameterInCm'
    label = 'Afmeting diameter in centimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInCm'
    definition = 'Complex datatype voor de afmeting van een diameter in centimeter.'
    waardeObject = DtcAfmetingDiameterInCmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

