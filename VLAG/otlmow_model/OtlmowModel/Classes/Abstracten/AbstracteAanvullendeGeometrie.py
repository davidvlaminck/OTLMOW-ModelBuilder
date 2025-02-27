# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from ...Classes.ImplementatieElement.AIMToestand import AIMToestand
from ...Classes.ImplementatieElement.AIMVersie import AIMVersie
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AbstracteAanvullendeGeometrie(AIMDBStatus, AIMToestand, AIMVersie, OTLObject, RelationInteractor):
    """Abstracte om de eigenschappen en relaties van AanvullendeGeometrie te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.assetId',
                                     definition='Unieke identificatie van de aanvullende geometrie zoals toegekend door de beheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._bijlage = OTLAttribuut(field=DtcDocument,
                                     naam='bijlage',
                                     label='bijlage',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.bijlage',
                                     definition='Het document of artefact dat een geometrie heeft of een bijlage is.',
                                     owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.naam',
                                  definition='De mensleesbare naam van een aanvullende geometrie of bijlage. De beheerder kent deze naam toe of geeft de opdracht om deze toe te kennen.',
                                  owner=self)

        self._notitie = OTLAttribuut(field=StringField,
                                     naam='notitie',
                                     label='notitie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie.notitie',
                                     definition='Extra notitie voor het object.',
                                     owner=self)

    @property
    def assetId(self) -> DtcIdentificatorWaarden:
        """Unieke identificatie van de aanvullende geometrie zoals toegekend door de beheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def bijlage(self) -> DtcDocumentWaarden:
        """Het document of artefact dat een geometrie heeft of een bijlage is."""
        return self._bijlage.get_waarde()

    @bijlage.setter
    def bijlage(self, value):
        self._bijlage.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """De mensleesbare naam van een aanvullende geometrie of bijlage. De beheerder kent deze naam toe of geeft de opdracht om deze toe te kennen."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)

    @property
    def notitie(self) -> str:
        """Extra notitie voor het object."""
        return self._notitie.get_waarde()

    @notitie.setter
    def notitie(self, value):
        self._notitie.set_waarde(value, owner=self)
