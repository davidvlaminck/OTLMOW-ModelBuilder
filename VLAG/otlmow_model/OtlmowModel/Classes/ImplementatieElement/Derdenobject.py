# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from ...Classes.ImplementatieElement.AIMToestand import AIMToestand
from ...Classes.ImplementatieElement.AIMVersie import AIMVersie
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Derdenobject(AIMDBStatus, AIMToestand, AIMVersie, OTLAsset, RelationInteractor, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Object niet in eigendom van de assetbeheerder dat zonder verdere typering bewaard wordt om relaties met getypeerde assets te kunnen beheren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftToegangsprocedure', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='o')  # o = direction: outgoing

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._contactgegevens = OTLAttribuut(field=StringField,
                                             naam='contactgegevens',
                                             label='contactgegevens',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.contactgegevens',
                                             definition='Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon.',
                                             owner=self)

        self._foto = OTLAttribuut(field=DtcDocument,
                                  naam='foto',
                                  label='foto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.foto',
                                  usagenote='Enkel bestanden die een foto zijn.',
                                  kardinaliteit_max='*',
                                  definition='Een foto van het derdenobject die eventuele detailinformatie weergeeft.',
                                  owner=self)

        self._heeftAansluitkastGeintegreerd = OTLAttribuut(field=BooleanField,
                                                           naam='heeftAansluitkastGeintegreerd',
                                                           label='heeft aansluitkast geïntegreerd',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.heeftAansluitkastGeintegreerd',
                                                           definition='Aanduiding of de aansluitkast geïntegreerd is.',
                                                           owner=self)

        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.omschrijving',
                                          definition='Omschrijving van het derdenobject.',
                                          owner=self)

    @property
    def assetId(self) -> DtcIdentificatorWaarden:
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def contactgegevens(self) -> str:
        """Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon."""
        return self._contactgegevens.get_waarde()

    @contactgegevens.setter
    def contactgegevens(self, value):
        self._contactgegevens.set_waarde(value, owner=self)

    @property
    def foto(self) -> List[DtcDocumentWaarden]:
        """Een foto van het derdenobject die eventuele detailinformatie weergeeft."""
        return self._foto.get_waarde()

    @foto.setter
    def foto(self, value):
        self._foto.set_waarde(value, owner=self)

    @property
    def heeftAansluitkastGeintegreerd(self) -> bool:
        """Aanduiding of de aansluitkast geïntegreerd is."""
        return self._heeftAansluitkastGeintegreerd.get_waarde()

    @heeftAansluitkastGeintegreerd.setter
    def heeftAansluitkastGeintegreerd(self, value):
        self._heeftAansluitkastGeintegreerd.set_waarde(value, owner=self)

    @property
    def omschrijving(self) -> str:
        """Omschrijving van het derdenobject."""
        return self._omschrijving.get_waarde()

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self)
