# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInMmWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm.diameter',
                                      definition='De diameter in millimeter.',
                                      owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter in millimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInMm(ComplexField):
    """Complex datatype voor de afmeting van een diameter in millimeter."""
    naam = 'DtcAfmetingDiameterInMm'
    label = 'Afmeting diameter in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm'
    definition = 'Complex datatype voor de afmeting van een diameter in millimeter.'
    waardeObject = DtcAfmetingDiameterInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

