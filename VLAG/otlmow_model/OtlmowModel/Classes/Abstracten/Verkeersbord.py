# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtuAfmetingVerkeersbord import DtuAfmetingVerkeersbord, DtuAfmetingVerkeersbordWaarden
from ...Datatypes.KlSoortSteun import KlSoortSteun
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbord(PuntGeometrie):
    """Abstracte klasse voor borden die een fysieke drager van verkeerstekens kunnen zijn waarvan de betekenis bepaald wordt door een verkeersbordconcept."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Realiseert', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='i')  # i = direction: incoming

        self._afmeting = OTLAttribuut(field=DtuAfmetingVerkeersbord,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afmeting',
                                      definition='De afmeting(en) van het verkeersbord.',
                                      owner=self)

        self._kaartVoorstelling = OTLAttribuut(field=DtcDocument,
                                               naam='kaartVoorstelling',
                                               label='kaart voorstelling',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.kaartVoorstelling',
                                               definition='TODO',
                                               owner=self)

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.opstelhoogte',
                                          definition='Afstand tussen het maaiveld en de onderrand van het bord.',
                                          owner=self)

        self._soortSteun = OTLAttribuut(field=KlSoortSteun,
                                        naam='soortSteun',
                                        label='soort steun',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.soortSteun',
                                        definition='Aanduiding welk type steun het verkeersbord draagt.',
                                        owner=self)

    @property
    def afmeting(self) -> DtuAfmetingVerkeersbordWaarden:
        """De afmeting(en) van het verkeersbord."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def kaartVoorstelling(self) -> DtcDocumentWaarden:
        """TODO"""
        return self._kaartVoorstelling.get_waarde()

    @kaartVoorstelling.setter
    def kaartVoorstelling(self, value):
        self._kaartVoorstelling.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """Afstand tussen het maaiveld en de onderrand van het bord."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)

    @property
    def soortSteun(self) -> str:
        """Aanduiding welk type steun het verkeersbord draagt."""
        return self._soortSteun.get_waarde()

    @soortSteun.setter
    def soortSteun(self, value):
        self._soortSteun.set_waarde(value, owner=self)
