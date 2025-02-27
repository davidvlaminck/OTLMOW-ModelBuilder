# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcExterneReferentieWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._externReferentienummer = OTLAttribuut(field=StringField,
                                                    naam='externReferentienummer',
                                                    label='extern referentienummer',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie.externReferentienummer',
                                                    definition='Referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ...',
                                                    owner=self)

        self._externePartij = OTLAttribuut(field=StringField,
                                           naam='externePartij',
                                           label='externe partij',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie.externePartij',
                                           definition='De naam van de externe partij waarvoor de referentie geldt. Dit kan een organisatie zijn maar ook een softwaretoepassing zoals bv. ABBA of VLCC.',
                                           owner=self)

    @property
    def externReferentienummer(self) -> str:
        """Referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ..."""
        return self._externReferentienummer.get_waarde()

    @externReferentienummer.setter
    def externReferentienummer(self, value):
        self._externReferentienummer.set_waarde(value, owner=self._parent)

    @property
    def externePartij(self) -> str:
        """De naam van de externe partij waarvoor de referentie geldt. Dit kan een organisatie zijn maar ook een softwaretoepassing zoals bv. ABBA of VLCC."""
        return self._externePartij.get_waarde()

    @externePartij.setter
    def externePartij(self, value):
        self._externePartij.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcExterneReferentie(ComplexField):
    """Complex datatype waarmee een referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ... kan toegevoegd worden aan object."""
    naam = 'DtcExterneReferentie'
    label = 'Externe referentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie'
    definition = 'Complex datatype waarmee een referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ... kan toegevoegd worden aan object.'
    waardeObject = DtcExterneReferentieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

