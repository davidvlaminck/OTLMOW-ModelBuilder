# coding=utf-8
from datetime import time, time
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlAlgWeekdagen import KlAlgWeekdagen
from otlmow_model.OtlmowModel.BaseClasses.TimeField import TimeField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOpeningsurenSpecificatieWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._openingstijd = OTLAttribuut(field=TimeField,
                                          naam='openingstijd',
                                          label='openingstijd',
                                          objectUri='https://schema.org/OpeningHoursSpecification.openingstijd',
                                          definition='Het tijdsstip waarop de opening plaatsvindt.',
                                          owner=self)

        self._sluitingstijd = OTLAttribuut(field=TimeField,
                                           naam='sluitingstijd',
                                           label='sluitingstijd',
                                           objectUri='https://schema.org/OpeningHoursSpecification.sluitingstijd',
                                           definition='Het tijdsstip waarop de sluiting plaatsvindt.',
                                           owner=self)

        self._weekdag = OTLAttribuut(field=KlAlgWeekdagen,
                                     naam='weekdag',
                                     label='weekdag',
                                     objectUri='https://schema.org/OpeningHoursSpecification.weekdag',
                                     definition='Een dag uit de week incl. weekenddagen.',
                                     owner=self)

    @property
    def openingstijd(self) -> time:
        """Het tijdsstip waarop de opening plaatsvindt."""
        return self._openingstijd.get_waarde()

    @openingstijd.setter
    def openingstijd(self, value):
        self._openingstijd.set_waarde(value, owner=self._parent)

    @property
    def sluitingstijd(self) -> time:
        """Het tijdsstip waarop de sluiting plaatsvindt."""
        return self._sluitingstijd.get_waarde()

    @sluitingstijd.setter
    def sluitingstijd(self, value):
        self._sluitingstijd.set_waarde(value, owner=self._parent)

    @property
    def weekdag(self) -> str:
        """Een dag uit de week incl. weekenddagen."""
        return self._weekdag.get_waarde()

    @weekdag.setter
    def weekdag(self, value):
        self._weekdag.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOpeningsurenSpecificatie(ComplexField):
    """Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert."""
    naam = 'DtcOpeningsurenSpecificatie'
    label = 'Openingsurenspecificatie'
    objectUri = 'https://schema.org/OpeningHoursSpecification'
    definition = 'Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert.'
    waardeObject = DtcOpeningsurenSpecificatieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

