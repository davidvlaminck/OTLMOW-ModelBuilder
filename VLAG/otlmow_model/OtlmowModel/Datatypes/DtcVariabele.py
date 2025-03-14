# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcCodelijst import DtcCodelijst, DtcCodelijstWaarden
from ..Datatypes.DtcTemplate1 import DtcTemplate1, DtcTemplate1Waarden
from ..Datatypes.KlVariabeleType import KlVariabeleType
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabeleWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._codelijst = OTLAttribuut(field=DtcCodelijst,
                                       naam='codelijst',
                                       label='codelijst',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.codelijst',
                                       definition='',
                                       owner=self)

        self._label = OTLAttribuut(field=StringField,
                                   naam='label',
                                   label='',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.label',
                                   definition='',
                                   owner=self)

        self._standaardwaarde = OTLAttribuut(field=StringField,
                                             naam='standaardwaarde',
                                             label='',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.standaardwaarde',
                                             definition='',
                                             owner=self)

        self._template = OTLAttribuut(field=DtcTemplate1,
                                      naam='template',
                                      label='',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.template',
                                      definition='',
                                      owner=self)

        self._type = OTLAttribuut(field=KlVariabeleType,
                                  naam='type',
                                  label='',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.type',
                                  definition='',
                                  owner=self)

        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele.waarde',
                                    definition='',
                                    owner=self)

    @property
    def codelijst(self) -> DtcCodelijstWaarden:
        """"""
        return self._codelijst.get_waarde()

    @codelijst.setter
    def codelijst(self, value):
        self._codelijst.set_waarde(value, owner=self._parent)

    @property
    def label(self) -> str:
        """"""
        return self._label.get_waarde()

    @label.setter
    def label(self, value):
        self._label.set_waarde(value, owner=self._parent)

    @property
    def standaardwaarde(self) -> str:
        """"""
        return self._standaardwaarde.get_waarde()

    @standaardwaarde.setter
    def standaardwaarde(self, value):
        self._standaardwaarde.set_waarde(value, owner=self._parent)

    @property
    def template(self) -> DtcTemplate1Waarden:
        """"""
        return self._template.get_waarde()

    @template.setter
    def template(self, value):
        self._template.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """"""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)

    @property
    def waarde(self) -> str:
        """"""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabele(ComplexField):
    """"""
    naam = 'DtcVariabele'
    label = 'Variabele'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele'
    definition = ''
    waardeObject = DtcVariabeleWaarden

    def __str__(self):
        return ComplexField.__str__(self)

