# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlCorrosiebelastingscategorie import KlCorrosiebelastingscategorie
from ..Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBeschermendeLaagWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._beschermlaag = OTLAttribuut(field=KlDraagConstrBeschermlaag,
                                          naam='beschermlaag',
                                          label='beschermlaag',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBeschermendeLaag.beschermlaag',
                                          definition='Type bescherming van de constructie of steun, bv. geschilderd of gegalvaniseerd.',
                                          owner=self)

        self._corrosieklasse = OTLAttribuut(field=KlCorrosiebelastingscategorie,
                                            naam='corrosieklasse',
                                            label='corrosieklasse',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBeschermendeLaag.corrosieklasse',
                                            definition='Een code om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven, volgens ISO-12944-2.',
                                            owner=self)

    @property
    def beschermlaag(self) -> str:
        """Type bescherming van de constructie of steun, bv. geschilderd of gegalvaniseerd."""
        return self._beschermlaag.get_waarde()

    @beschermlaag.setter
    def beschermlaag(self, value):
        self._beschermlaag.set_waarde(value, owner=self._parent)

    @property
    def corrosieklasse(self) -> str:
        """Een code om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven, volgens ISO-12944-2."""
        return self._corrosieklasse.get_waarde()

    @corrosieklasse.setter
    def corrosieklasse(self, value):
        self._corrosieklasse.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBeschermendeLaag(ComplexField):
    """Complex datatype voor de inventarisatie van het type beschermlaag en de corrosiebelastingscategorie."""
    naam = 'DtcBeschermendeLaag'
    label = 'Beschermende laag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBeschermendeLaag'
    definition = 'Complex datatype voor de inventarisatie van het type beschermlaag en de corrosiebelastingscategorie.'
    waardeObject = DtcBeschermendeLaagWaarden

    def __str__(self):
        return ComplexField.__str__(self)

