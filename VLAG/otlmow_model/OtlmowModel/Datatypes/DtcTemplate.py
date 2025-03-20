# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcVariabele import DtcVariabele, DtcVariabeleWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTemplateWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._variabele = OTLAttribuut(field=DtcVariabele,
                                       naam='variabele',
                                       label='variabele',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTemplate.variabele',
                                       kardinaliteit_min='0',
                                       kardinaliteit_max='*',
                                       definition='TODO',
                                       owner=self)

        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTemplate.waarde',
                                    definition='De inhoud van de template als HTML of gewone string.',
                                    owner=self)

    @property
    def variabele(self) -> List[DtcVariabeleWaarden]:
        """TODO"""
        return self._variabele.get_waarde()

    @variabele.setter
    def variabele(self, value):
        self._variabele.set_waarde(value, owner=self._parent)

    @property
    def waarde(self) -> str:
        """De inhoud van de template als HTML of gewone string."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTemplate(ComplexField):
    """TODO"""
    naam = 'DtcTemplate'
    label = 'Template'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTemplate'
    definition = 'TODO'
    waardeObject = DtcTemplateWaarden

    def __str__(self):
        return ComplexField.__str__(self)

