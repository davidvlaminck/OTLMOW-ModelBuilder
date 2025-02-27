# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBeschermingVraatschadeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._materiaal = OTLAttribuut(field=KlMateriaalBeschermingVraatschade,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBeschermingVraatschade.materiaal',
                                       definition='De middelen als bescherming tegen vraatschade.',
                                       owner=self)

        self._tegenMaaischade = OTLAttribuut(field=BooleanField,
                                             naam='tegenMaaischade',
                                             label='tegen maaischade',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBeschermingVraatschade.tegenMaaischade',
                                             definition='Aanduiding of er bescherming tegen maaischade aanwezig is.',
                                             owner=self)

    @property
    def materiaal(self) -> str:
        """De middelen als bescherming tegen vraatschade."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self._parent)

    @property
    def tegenMaaischade(self) -> bool:
        """Aanduiding of er bescherming tegen maaischade aanwezig is."""
        return self._tegenMaaischade.get_waarde()

    @tegenMaaischade.setter
    def tegenMaaischade(self, value):
        self._tegenMaaischade.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBeschermingVraatschade(ComplexField):
    """Complex datatype voor bescherming van de stam tegen knaagdieren."""
    naam = 'DtcBeschermingVraatschade'
    label = 'Bescherming vraatschade'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBeschermingVraatschade'
    definition = 'Complex datatype voor bescherming van de stam tegen knaagdieren.'
    waardeObject = DtcBeschermingVraatschadeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

