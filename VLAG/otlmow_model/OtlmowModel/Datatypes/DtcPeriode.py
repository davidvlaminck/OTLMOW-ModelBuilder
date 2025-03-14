# coding=utf-8
from datetime import datetime, datetime
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcPeriodeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._begin = OTLAttribuut(field=DateTimeField,
                                   naam='begin',
                                   label='begin',
                                   objectUri='http://data.europa.eu/m8g/PeriodOfTime.begin',
                                   definition='Moment waarop de periode begint.',
                                   owner=self)

        self._einde = OTLAttribuut(field=DateTimeField,
                                   naam='einde',
                                   label='einde',
                                   objectUri='http://data.europa.eu/m8g/PeriodOfTime.einde',
                                   definition='Moment waarop de periode eindigt.',
                                   owner=self)

    @property
    def begin(self) -> datetime:
        """Moment waarop de periode begint."""
        return self._begin.get_waarde()

    @begin.setter
    def begin(self, value):
        self._begin.set_waarde(value, owner=self._parent)

    @property
    def einde(self) -> datetime:
        """Moment waarop de periode eindigt."""
        return self._einde.get_waarde()

    @einde.setter
    def einde(self, value):
        self._einde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcPeriode(ComplexField):
    """De tijdsperiode tussen twee momenten in de tijd."""
    naam = 'DtcPeriode'
    label = 'Periode'
    objectUri = 'http://data.europa.eu/m8g/PeriodOfTime'
    definition = 'De tijdsperiode tussen twee momenten in de tijd.'
    waardeObject = DtcPeriodeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

