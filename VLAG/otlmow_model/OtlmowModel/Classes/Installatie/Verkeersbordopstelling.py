# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Signalisatie import Signalisatie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcExterneReferentie import DtcExterneReferentie, DtcExterneReferentieWaarden
from ...Datatypes.KlPositieSoort import KlPositieSoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordopstelling(Signalisatie, AIMObject):
    """Het geheel van verticale verkeerssignalisatie die bevestigd is aan één of meerdere draagconstructies op éénzelfde geolocatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanzicht', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#AanzichtVerkeersbordopstelling', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOntwerpVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling', direction='o')  # o = direction: outgoing

        self._positieTovRijweg = OTLAttribuut(field=KlPositieSoort,
                                              naam='positieTovRijweg',
                                              label='positie ten opzichte van de rijweg',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.positieTovRijweg',
                                              usagenote='Bijvoorbeeld: boven, rechts, links',
                                              definition='De plaatsing van de opstelling ten aanzien van de rijbaan.',
                                              owner=self)

        self._wegSegment = OTLAttribuut(field=DtcExterneReferentie,
                                        naam='wegSegment',
                                        label='wegsegment',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.wegSegment',
                                        usagenote='Dit is niet noodzakelijk het wegsegment waarop het verkeersbord van toepassing is.',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Wegsegment waarbij de verkeersbordopstelling geplaatst is.',
                                        owner=self)

    @property
    def positieTovRijweg(self) -> str:
        """De plaatsing van de opstelling ten aanzien van de rijbaan."""
        return self._positieTovRijweg.get_waarde()

    @positieTovRijweg.setter
    def positieTovRijweg(self, value):
        self._positieTovRijweg.set_waarde(value, owner=self)

    @property
    def wegSegment(self) -> List[DtcExterneReferentieWaarden]:
        """Wegsegment waarbij de verkeersbordopstelling geplaatst is."""
        return self._wegSegment.get_waarde()

    @wegSegment.setter
    def wegSegment(self, value):
        self._wegSegment.set_waarde(value, owner=self)
