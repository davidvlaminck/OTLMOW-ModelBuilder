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
                                       definition='TODO',
                                       owner=self)

        self._label = OTLAttribuut(field=StringField,
                                   naam='label',
                                   label='label',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.label',
                                   usagenote='http://purl.org/dc/terms/title',
                                   definition='TODO',
                                   owner=self)

        self._standaardwaarde = OTLAttribuut(field=StringField,
                                             naam='standaardwaarde',
                                             label='standaardwaarde',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.standaardwaarde',
                                             definition='TODO',
                                             owner=self)

        self._template = OTLAttribuut(field=DtcTemplate2,
                                      naam='template',
                                      label='template',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.template',
                                      definition='TODO',
                                      owner=self)

        self._type = OTLAttribuut(field=KlVariabeleType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.type',
                                  usagenote='http://purl.org/dc/terms/type',
                                  definition='TODO',
                                  owner=self)

        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1.waarde',
                                    usagenote='http://www.w3.org/2000/01/rdf-schema#value',
                                    definition='TODO',
                                    owner=self)

    @property
    def codelijst(self) -> DtcCodelijstWaarden:
        """TODO"""
        return self._codelijst.get_waarde()

    @codelijst.setter
    def codelijst(self, value):
        self._codelijst.set_waarde(value, owner=self._parent)

    @property
    def label(self) -> str:
        """TODO"""
        return self._label.get_waarde()

    @label.setter
    def label(self, value):
        self._label.set_waarde(value, owner=self._parent)

    @property
    def standaardwaarde(self) -> str:
        """TODO"""
        return self._standaardwaarde.get_waarde()

    @standaardwaarde.setter
    def standaardwaarde(self, value):
        self._standaardwaarde.set_waarde(value, owner=self._parent)

    @property
    def template(self) -> DtcTemplate2Waarden:
        """TODO"""
        return self._template.get_waarde()

    @template.setter
    def template(self, value):
        self._template.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """TODO"""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)

    @property
    def waarde(self) -> str:
        """TODO"""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabele1(ComplexField):
    """"""
    naam = 'DtcVariabele1'
    label = 'Variabele1'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabele1'
    definition = ''
    waardeObject = DtcVariabele1Waarden

    def __str__(self):
        return ComplexField.__str__(self)

