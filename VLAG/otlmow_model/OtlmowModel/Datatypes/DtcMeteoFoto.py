# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlMeteoFotoBeschrijving import KlMeteoFotoBeschrijving


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMeteoFotoWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._beschrijving = OTLAttribuut(field=KlMeteoFotoBeschrijving,
                                          naam='beschrijving',
                                          label='beschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMeteoFoto.beschrijving',
                                          definition="De beschrijving of categorie waarbij de foto's behoren.",
                                          owner=self)

        self._fotobestand = OTLAttribuut(field=DtcDocument,
                                         naam='fotobestand',
                                         label='fotobestand',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMeteoFoto.fotobestand',
                                         definition='Het bestand dat de foto bevat.',
                                         owner=self)

    @property
    def beschrijving(self) -> str:
        """De beschrijving of categorie waarbij de foto's behoren."""
        return self._beschrijving.get_waarde()

    @beschrijving.setter
    def beschrijving(self, value):
        self._beschrijving.set_waarde(value, owner=self._parent)

    @property
    def fotobestand(self) -> DtcDocumentWaarden:
        """Het bestand dat de foto bevat."""
        return self._fotobestand.get_waarde()

    @fotobestand.setter
    def fotobestand(self, value):
        self._fotobestand.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMeteoFoto(ComplexField):
    """Complex datatype voor meteo gerelateerde foto's."""
    naam = 'DtcMeteoFoto'
    label = 'Meteo foto'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMeteoFoto'
    definition = "Complex datatype voor meteo gerelateerde foto's."
    waardeObject = DtcMeteoFotoWaarden

    def __str__(self):
        return ComplexField.__str__(self)

