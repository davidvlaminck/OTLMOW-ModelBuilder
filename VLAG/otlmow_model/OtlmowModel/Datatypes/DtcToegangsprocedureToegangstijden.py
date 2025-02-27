# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DteTekstblok import DteTekstblok, DteTekstblokWaarden
from ..Datatypes.KlToegangsprocedureToegangstijden import KlToegangsprocedureToegangstijden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcToegangsprocedureToegangstijdenWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._opmerking = OTLAttribuut(field=DteTekstblok,
                                       naam='opmerking',
                                       label='opmerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureToegangstijden.opmerking',
                                       definition='Opmerking bij de toegangstijden van een object (bijv. kantooruren tussen 9 en 17u.)',
                                       owner=self)

        self._toegangstijden = OTLAttribuut(field=KlToegangsprocedureToegangstijden,
                                            naam='toegangstijden',
                                            label='toegangstijden',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureToegangstijden.toegangstijden',
                                            definition='Het moment waarop het object toegankelijk is.',
                                            owner=self)

    @property
    def opmerking(self) -> DteTekstblokWaarden:
        """Opmerking bij de toegangstijden van een object (bijv. kantooruren tussen 9 en 17u.)"""
        return self._opmerking.get_waarde()

    @opmerking.setter
    def opmerking(self, value):
        self._opmerking.set_waarde(value, owner=self._parent)

    @property
    def toegangstijden(self) -> str:
        """Het moment waarop het object toegankelijk is."""
        return self._toegangstijden.get_waarde()

    @toegangstijden.setter
    def toegangstijden(self, value):
        self._toegangstijden.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcToegangsprocedureToegangstijden(ComplexField):
    """Complex datatype om de toegangstijden bij een toegangsprocedure te specifieren."""
    naam = 'DtcToegangsprocedureToegangstijden'
    label = 'Toegangstijden'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureToegangstijden'
    definition = 'Complex datatype om de toegangstijden bij een toegangsprocedure te specifieren.'
    waardeObject = DtcToegangsprocedureToegangstijdenWaarden

    def __str__(self):
        return ComplexField.__str__(self)

