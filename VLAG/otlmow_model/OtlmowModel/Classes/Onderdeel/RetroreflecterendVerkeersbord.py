# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Verkeersbord import Verkeersbord
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlFabricageTypeRetroreflecterendVerkeersbord import KlFabricageTypeRetroreflecterendVerkeersbord
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroreflecterendVerkeersbord(Verkeersbord, AIMNaamObject):
    """Verkeersbord met op het beeldvlak een tekening en/of tekst die worden weergegeven met een geëigend bekledingsmateriaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#AanzichtVerkeersbordopstelling', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Realiseert', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='i')  # i = direction: incoming

        self._fabricageDatum = OTLAttribuut(field=DateField,
                                            naam='fabricageDatum',
                                            label='fabricage datum',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.fabricageDatum',
                                            definition='De datum waarop het bord werd gebouwd.',
                                            owner=self)

        self._fabricageType = OTLAttribuut(field=KlFabricageTypeRetroreflecterendVerkeersbord,
                                           naam='fabricageType',
                                           label='fabricage type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.fabricageType',
                                           definition='Genormaliseerde referentie waaraan het verkeersbord voldoet.',
                                           owner=self)

        self._horizontaleVerschuiving = OTLAttribuut(field=KwantWrdInMillimeter,
                                                     naam='horizontaleVerschuiving',
                                                     label='horizontale verschuiving',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.horizontaleVerschuiving',
                                                     definition='De verschuiving van het bord, gemeten van het midden van het bord tot de centrale as van de opstelling. Een positieve waarde duidt op een verschuiving naar rechts, een negatieve waarde op een verschuiving naar links',
                                                     owner=self)

        self._kaartvoorstelling = OTLAttribuut(field=DtcDocument,
                                               naam='kaartvoorstelling',
                                               label='kaartvoorstelling',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.kaartvoorstelling',
                                               definition='TODO',
                                               owner=self)

    @property
    def fabricageDatum(self) -> date:
        """De datum waarop het bord werd gebouwd."""
        return self._fabricageDatum.get_waarde()

    @fabricageDatum.setter
    def fabricageDatum(self, value):
        self._fabricageDatum.set_waarde(value, owner=self)

    @property
    def fabricageType(self) -> str:
        """Genormaliseerde referentie waaraan het verkeersbord voldoet."""
        return self._fabricageType.get_waarde()

    @fabricageType.setter
    def fabricageType(self, value):
        self._fabricageType.set_waarde(value, owner=self)

    @property
    def horizontaleVerschuiving(self) -> KwantWrdInMillimeterWaarden:
        """De verschuiving van het bord, gemeten van het midden van het bord tot de centrale as van de opstelling. Een positieve waarde duidt op een verschuiving naar rechts, een negatieve waarde op een verschuiving naar links"""
        return self._horizontaleVerschuiving.get_waarde()

    @horizontaleVerschuiving.setter
    def horizontaleVerschuiving(self, value):
        self._horizontaleVerschuiving.set_waarde(value, owner=self)

    @property
    def kaartvoorstelling(self) -> DtcDocumentWaarden:
        """TODO"""
        return self._kaartvoorstelling.get_waarde()

    @kaartvoorstelling.setter
    def kaartvoorstelling(self, value):
        self._kaartvoorstelling.set_waarde(value, owner=self)
