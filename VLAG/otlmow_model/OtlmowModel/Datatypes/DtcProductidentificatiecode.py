# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.BaseClasses.URIField import URIField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProductidentificatiecodeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._keuringsverslag = OTLAttribuut(field=DtcDocument,
                                             naam='keuringsverslag',
                                             label='keuringsverslag',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.keuringsverslag',
                                             definition='Een rapport met de resultaten van de keuring.',
                                             owner=self)

        self._linkTechnischeFiche = OTLAttribuut(field=URIField,
                                                 naam='linkTechnischeFiche',
                                                 label='link technische fiche',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.linkTechnischeFiche',
                                                 definition='De link naar de technische fiche van het gerelateerd product.',
                                                 owner=self)

        self._producent = OTLAttribuut(field=StringField,
                                       naam='producent',
                                       label='producent',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.producent',
                                       definition='De gerelateerde fabrikant.',
                                       owner=self)

        self._productidentificatiecode = OTLAttribuut(field=StringField,
                                                      naam='productidentificatiecode',
                                                      label='productidentificatiecode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.productidentificatiecode',
                                                      definition='De code van het gebruikte product (COPRO/BENOR).',
                                                      owner=self)

    @property
    def keuringsverslag(self) -> DtcDocumentWaarden:
        """Een rapport met de resultaten van de keuring."""
        return self._keuringsverslag.get_waarde()

    @keuringsverslag.setter
    def keuringsverslag(self, value):
        self._keuringsverslag.set_waarde(value, owner=self._parent)

    @property
    def linkTechnischeFiche(self) -> str:
        """De link naar de technische fiche van het gerelateerd product."""
        return self._linkTechnischeFiche.get_waarde()

    @linkTechnischeFiche.setter
    def linkTechnischeFiche(self, value):
        self._linkTechnischeFiche.set_waarde(value, owner=self._parent)

    @property
    def producent(self) -> str:
        """De gerelateerde fabrikant."""
        return self._producent.get_waarde()

    @producent.setter
    def producent(self, value):
        self._producent.set_waarde(value, owner=self._parent)

    @property
    def productidentificatiecode(self) -> str:
        """De code van het gebruikte product (COPRO/BENOR)."""
        return self._productidentificatiecode.get_waarde()

    @productidentificatiecode.setter
    def productidentificatiecode(self, value):
        self._productidentificatiecode.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProductidentificatiecode(ComplexField):
    """Complex datatype dat alle nodige informatie van het product capteert."""
    naam = 'DtcProductidentificatiecode'
    label = 'Productidentificatiecode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode'
    definition = 'Complex datatype dat alle nodige informatie van het product capteert.'
    waardeObject = DtcProductidentificatiecodeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

