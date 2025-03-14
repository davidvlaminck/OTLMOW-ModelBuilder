# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcCodelijst import DtcCodelijst, DtcCodelijstWaarden
from ..Datatypes.DtcTemplate2 import DtcTemplate2, DtcTemplate2Waarden
from ..Datatypes.KlVariabeleType import KlVariabeleType
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabele1Waarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._codelijst = OTLAttribuut(field=DtcCodelijst,
                                       naam='codelijst',
                                       label='codelijst',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.codelijst',
                                       definition='',
                                       owner=self)

        self._label = OTLAttribuut(field=StringField,
                                   naam='label',
                                   label='',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.label',
                                   definition='',
                                   owner=self)

        self._standaardwaarde = OTLAttribuut(field=StringField,
                                             naam='standaardwaarde',
                                             label='',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.standaardwaarde',
                                             definition='',
                                             owner=self)

        self._template = OTLAttribuut(field=DtcTemplate2,
                                      naam='template',
                                      label='',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.template',
                                      definition='',
                                      owner=self)

        self._type = OTLAttribuut(field=KlVariabeleType,
                                  naam='type',
                                  label='',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.type',
                                  definition='',
                                  owner=self)

        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.waarde',
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
    def template(self) -> DtcTemplate2Waarden:
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
class DtcVariabele1(ComplexField):
    """"""
    naam = 'DtcVariabele1'
    label = 'Variabele'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1'
    definition = ''
    waardeObject = DtcVariabele1Waarden

    def __str__(self):
        return ComplexField.__str__(self)

