# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBereikInKgWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._maximum = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='maximum',
                                     label='maximum',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBereikInKg.maximum',
                                     definition='Bovengrens van het bereik uitgedrukt in kilogram.',
                                     owner=self)

        self._minimium = OTLAttribuut(field=KwantWrdInKilogram,
                                      naam='minimium',
                                      label='minimum',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBereikInKg.minimium',
                                      definition='Ondergrens van het bereik uitgedrukt in kilogram.',
                                      owner=self)

    @property
    def maximum(self) -> KwantWrdInKilogramWaarden:
        """Bovengrens van het bereik uitgedrukt in kilogram."""
        return self._maximum.get_waarde()

    @maximum.setter
    def maximum(self, value):
        self._maximum.set_waarde(value, owner=self._parent)

    @property
    def minimium(self) -> KwantWrdInKilogramWaarden:
        """Ondergrens van het bereik uitgedrukt in kilogram."""
        return self._minimium.get_waarde()

    @minimium.setter
    def minimium(self, value):
        self._minimium.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBereikInKg(ComplexField):
    """Complex datatype om een bereik uit te drukken met een minimium en maximum in kilogram."""
    naam = 'DtcBereikInKg'
    label = 'Bereik in kg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBereikInKg'
    definition = 'Complex datatype om een bereik uit te drukken met een minimium en maximum in kilogram.'
    waardeObject = DtcBereikInKgWaarden

    def __str__(self):
        return ComplexField.__str__(self)

