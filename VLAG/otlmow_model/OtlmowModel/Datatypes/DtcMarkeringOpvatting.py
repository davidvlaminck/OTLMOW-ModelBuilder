# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlMarkeringWaarborgperiode import KlMarkeringWaarborgperiode
from ..Datatypes.KlSignalisatieMarkeringOpvatting import KlSignalisatieMarkeringOpvatting


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMarkeringOpvattingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._opvatting = OTLAttribuut(field=KlSignalisatieMarkeringOpvatting,
                                       naam='opvatting',
                                       label='opvatting',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMarkeringOpvatting.opvatting',
                                       definition='De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis.',
                                       owner=self)

        self._waarborgperiode = OTLAttribuut(field=KlMarkeringWaarborgperiode,
                                             naam='waarborgperiode',
                                             label='waarborgperiode',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMarkeringOpvatting.waarborgperiode',
                                             definition='De periode waarin de markering moet voldoen aan de resultaatseisen.',
                                             owner=self)

    @property
    def opvatting(self) -> str:
        """De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis."""
        return self._opvatting.get_waarde()

    @opvatting.setter
    def opvatting(self, value):
        self._opvatting.set_waarde(value, owner=self._parent)

    @property
    def waarborgperiode(self) -> str:
        """De periode waarin de markering moet voldoen aan de resultaatseisen."""
        return self._waarborgperiode.get_waarde()

    @waarborgperiode.setter
    def waarborgperiode(self, value):
        self._waarborgperiode.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMarkeringOpvatting(ComplexField):
    """Complex datatype voor de opvatting van een markering."""
    naam = 'DtcMarkeringOpvatting'
    label = 'Markering opvatting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMarkeringOpvatting'
    definition = 'Complex datatype voor de opvatting van een markering.'
    waardeObject = DtcMarkeringOpvattingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

