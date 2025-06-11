# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ..Datatypes.KlVariabeleWaarden import KlVariabeleWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabeleWaardenWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._codelijst = OTLAttribuut(field=KlVariabeleWaarden,
                                       naam='codelijst',
                                       label='codelijst',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabeleWaarden.codelijst',
                                       definition='Bevat een optie uit de codelijst.',
                                       owner=self)

        self._datum = OTLAttribuut(field=DateField,
                                   naam='datum',
                                   label='datum',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabeleWaarden.datum',
                                   definition='Bevat de waarde als datum.',
                                   owner=self)

        self._getal = OTLAttribuut(field=FloatOrDecimalField,
                                   naam='getal',
                                   label='getal',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabeleWaarden.getal',
                                   definition='Bevat de waarde als getal.',
                                   owner=self)

        self._tekst = OTLAttribuut(field=StringField,
                                   naam='tekst',
                                   label='tekst',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabeleWaarden.tekst',
                                   definition='Bevat de waarde als tekst.',
                                   owner=self)

    @property
    def codelijst(self) -> str:
        """Bevat een optie uit de codelijst."""
        return self._codelijst.get_waarde()

    @codelijst.setter
    def codelijst(self, value):
        self._codelijst.set_waarde(value, owner=self._parent)

    @property
    def datum(self) -> date:
        """Bevat de waarde als datum."""
        return self._datum.get_waarde()

    @datum.setter
    def datum(self, value):
        self._datum.set_waarde(value, owner=self._parent)

    @property
    def getal(self) -> float:
        """Bevat de waarde als getal."""
        return self._getal.get_waarde()

    @getal.setter
    def getal(self, value):
        self._getal.set_waarde(value, owner=self._parent)

    @property
    def tekst(self) -> str:
        """Bevat de waarde als tekst."""
        return self._tekst.get_waarde()

    @tekst.setter
    def tekst(self, value):
        self._tekst.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVariabeleWaarden(ComplexField):
    """Complex datatype die de variabele waarden definieert."""
    naam = 'DtcVariabeleWaarden'
    label = 'Variabele waarden'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcVariabeleWaarden'
    definition = 'Complex datatype die de variabele waarden definieert.'
    waardeObject = DtcVariabeleWaardenWaarden

    def __str__(self):
        return ComplexField.__str__(self)

