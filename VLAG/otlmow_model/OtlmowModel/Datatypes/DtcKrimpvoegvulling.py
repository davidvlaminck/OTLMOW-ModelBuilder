# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlKrimpvoegvulling import KlKrimpvoegvulling


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoegvullingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._krimpvoegvulling = OTLAttribuut(field=KlKrimpvoegvulling,
                                              naam='krimpvoegvulling',
                                              label='krimvoegvulling',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKrimpvoegvulling.krimpvoegvulling',
                                              definition='De gebruikte vulling van de krimpvoeg.',
                                              owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKrimpvoegvulling.technischeFiche',
                                             definition='De technische fiche van het product waarmee de krimpvoeg is gevuld.',
                                             owner=self)

    @property
    def krimpvoegvulling(self) -> str:
        """De gebruikte vulling van de krimpvoeg."""
        return self._krimpvoegvulling.get_waarde()

    @krimpvoegvulling.setter
    def krimpvoegvulling(self, value):
        self._krimpvoegvulling.set_waarde(value, owner=self._parent)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het product waarmee de krimpvoeg is gevuld."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoegvulling(ComplexField):
    """Complex datatype om de vulling voor de krimpvoeg aan te duiden met zijn technische fiche."""
    naam = 'DtcKrimpvoegvulling'
    label = 'Krimvoegvulling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKrimpvoegvulling'
    definition = 'Complex datatype om de vulling voor de krimpvoeg aan te duiden met zijn technische fiche.'
    waardeObject = DtcKrimpvoegvullingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

