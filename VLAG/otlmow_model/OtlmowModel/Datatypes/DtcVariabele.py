# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcVariabeleWaarden import DtcVariabeleWaarden, DtcVariabeleWaardenWaarden
from otlmow_model.OtlmowModel.BaseClasses.URIField import URIField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabeleWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._uri = OTLAttribuut(field=URIField,
                                 naam='uri',
                                 label='uri',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.uri',
                                 definition='TODO',
                                 owner=self)

        self._waarde = OTLAttribuut(field=DtcVariabeleWaarden,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.waarde',
                                    kardinaliteit_max='*',
                                    definition='De waarde van de variabele (getal, tekst, optie uit codelijst of datum).',
                                    owner=self)

    @property
    def uri(self) -> str:
        """TODO"""
        return self._uri.get_waarde()

    @uri.setter
    def uri(self, value):
        self._uri.set_waarde(value, owner=self._parent)

    @property
    def waarde(self) -> List[DtcVariabeleWaardenWaarden]:
        """De waarde van de variabele (getal, tekst, optie uit codelijst of datum)."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabele(ComplexField):
    """Complex datatype die de variabele bevat."""
    naam = 'DtcVariabele'
    label = 'Variabele'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele'
    definition = 'Complex datatype die de variabele bevat.'
    waardeObject = DtcVariabeleWaarden

    def __str__(self):
        return ComplexField.__str__(self)

