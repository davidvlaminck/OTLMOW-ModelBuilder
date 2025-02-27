# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from ...Classes.ImplementatieElement.AIMToestand import AIMToestand
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor
from ...Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden
from ...Datatypes.DtcToegangsprocedureBijlage import DtcToegangsprocedureBijlage, DtcToegangsprocedureBijlageWaarden
from ...Datatypes.DtcToegangsprocedureToegangstijden import DtcToegangsprocedureToegangstijden, DtcToegangsprocedureToegangstijdenWaarden
from ...Datatypes.KlToegangsprocedureAandachtspunt import KlToegangsprocedureAandachtspunt
from ...Datatypes.KlTypeBadge import KlTypeBadge
from ...Datatypes.KlTypeSleutel import KlTypeSleutel
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangsprocedure(AIMDBStatus, AIMToestand, OTLObject, RelationInteractor, PuntGeometrie):
    """De procedure die gevolgd moet worden om toegang te verkrijgen tot een object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftToegangsprocedure', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftToegangsprocedure', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject', direction='i')  # i = direction: incoming

        self._aandachtspunt = OTLAttribuut(field=KlToegangsprocedureAandachtspunt,
                                           naam='aandachtspunt',
                                           label='aandachtspunt',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.aandachtspunt',
                                           kardinaliteit_max='*',
                                           definition='Aandachtspunten waar men rekening mee moet houden, die een impact hebben op de toegankelijkheid van een object.',
                                           owner=self)

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.assetId',
                                     definition='De unieke identificator van de toegangsprocedure.',
                                     owner=self)

        self._bijlage = OTLAttribuut(field=DtcToegangsprocedureBijlage,
                                     naam='bijlage',
                                     label='bijlage',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.bijlage',
                                     kardinaliteit_max='*',
                                     definition='Bijlages, onder de vorm van een beschrijving en/of een document en/of een URL, die aanvullende informatie bevatten over de toegangsprocedure.',
                                     owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.naam',
                                  definition='De naam van de toegangsprocedure.',
                                  owner=self)

        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.omschrijving',
                                          definition='Een uitgebreide toelichting die beschrijft hoe de toegangsprocedure gebruikt kan worden.',
                                          owner=self)

        self._toegangstijden = OTLAttribuut(field=DtcToegangsprocedureToegangstijden,
                                            naam='toegangstijden',
                                            label='toegangstijden',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.toegangstijden',
                                            kardinaliteit_max='*',
                                            definition='De dagen/uren van de dag waarop de procedure geldt.',
                                            owner=self)

        self._typeBadge = OTLAttribuut(field=KlTypeBadge,
                                       naam='typeBadge',
                                       label='type badge',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.typeBadge',
                                       kardinaliteit_max='*',
                                       definition='Het soort badge dat wordt gebruikt om toegang te verkijgen.',
                                       owner=self)

        self._typeSleutel = OTLAttribuut(field=KlTypeSleutel,
                                         naam='typeSleutel',
                                         label='type sleutel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure.typeSleutel',
                                         kardinaliteit_max='*',
                                         definition='Het soort sleutel dat wordt gebruikt om toegang te verkrijgen.',
                                         owner=self)

    @property
    def aandachtspunt(self) -> List[str]:
        """Aandachtspunten waar men rekening mee moet houden, die een impact hebben op de toegankelijkheid van een object."""
        return self._aandachtspunt.get_waarde()

    @aandachtspunt.setter
    def aandachtspunt(self, value):
        self._aandachtspunt.set_waarde(value, owner=self)

    @property
    def assetId(self) -> DtcIdentificatorWaarden:
        """De unieke identificator van de toegangsprocedure."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def bijlage(self) -> List[DtcToegangsprocedureBijlageWaarden]:
        """Bijlages, onder de vorm van een beschrijving en/of een document en/of een URL, die aanvullende informatie bevatten over de toegangsprocedure."""
        return self._bijlage.get_waarde()

    @bijlage.setter
    def bijlage(self, value):
        self._bijlage.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """De naam van de toegangsprocedure."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)

    @property
    def omschrijving(self) -> str:
        """Een uitgebreide toelichting die beschrijft hoe de toegangsprocedure gebruikt kan worden."""
        return self._omschrijving.get_waarde()

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self)

    @property
    def toegangstijden(self) -> List[DtcToegangsprocedureToegangstijdenWaarden]:
        """De dagen/uren van de dag waarop de procedure geldt."""
        return self._toegangstijden.get_waarde()

    @toegangstijden.setter
    def toegangstijden(self, value):
        self._toegangstijden.set_waarde(value, owner=self)

    @property
    def typeBadge(self) -> List[str]:
        """Het soort badge dat wordt gebruikt om toegang te verkijgen."""
        return self._typeBadge.get_waarde()

    @typeBadge.setter
    def typeBadge(self, value):
        self._typeBadge.set_waarde(value, owner=self)

    @property
    def typeSleutel(self) -> List[str]:
        """Het soort sleutel dat wordt gebruikt om toegang te verkrijgen."""
        return self._typeSleutel.get_waarde()

    @typeSleutel.setter
    def typeSleutel(self, value):
        self._typeSleutel.set_waarde(value, owner=self)
