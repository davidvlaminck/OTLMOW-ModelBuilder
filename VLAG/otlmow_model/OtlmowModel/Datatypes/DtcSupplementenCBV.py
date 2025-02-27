# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlKleurSupp import KlKleurSupp
from ..Datatypes.KlTypeSuppCBV import KlTypeSuppCBV


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSupplementenCBVWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.kleur',
                                   definition='De kleur van de supplementen toegevoegd aan de verharding.',
                                   owner=self)

        self._type = OTLAttribuut(field=KlTypeSuppCBV,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.type',
                                  definition='Het type van de supplementen toegevoegd aan de verharding.',
                                  owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van de supplementen toegevoegd aan de verharding."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """Het type van de supplementen toegevoegd aan de verharding."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSupplementenCBV(ComplexField):
    """Complex datatype voor de supplementen van de CBV."""
    naam = 'DtcSupplementenCBV'
    label = 'Supplementen CBV'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV'
    definition = 'Complex datatype voor de supplementen van de CBV.'
    waardeObject = DtcSupplementenCBVWaarden

    def __str__(self):
        return ComplexField.__str__(self)

