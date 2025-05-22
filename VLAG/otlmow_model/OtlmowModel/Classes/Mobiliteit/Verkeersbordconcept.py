# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Mobiliteit.Verkeerstekenconcept import Verkeerstekenconcept
from ...Datatypes.DtcVorm import DtcVorm, DtcVormWaarden
from ...Datatypes.KlVerkeersbordcategorie import KlVerkeersbordcategorie
from ...Datatypes.KlZonaliteit import KlZonaliteit


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordconcept(Verkeerstekenconcept):
    """Inhoudelijke definitie van de betekenis van een verkeersbord zoals opgenomen in de wegcode."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Verkeersbordconcept'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftMogelijkOnderbord', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersbordconcept', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsGebaseerdOp', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken', direction='i')  # i = direction: incoming

        self._classificatie = OTLAttribuut(field=KlVerkeersbordcategorie,
                                           naam='classificatie',
                                           label='classificatie',
                                           objectUri='http://purl.org/dc/terms/type',
                                           definition='TODO',
                                           owner=self)

        self._mogelijkeVorm = OTLAttribuut(field=DtcVorm,
                                           naam='mogelijkeVorm',
                                           label='mogelijke vorm',
                                           objectUri='https://w3id.org/isCharacterisedBy#isCharacterisedBy',
                                           kardinaliteit_min='0',
                                           kardinaliteit_max='*',
                                           definition='TODO',
                                           owner=self)

        self._zonaliteit = OTLAttribuut(field=KlZonaliteit,
                                        naam='zonaliteit',
                                        label='zonaliteit',
                                        objectUri='https://data.vlaanderen.be/ns/mobiliteit#Verkeersbordconcept.zonaliteit',
                                        kardinaliteit_min='0',
                                        definition='TODO',
                                        owner=self)

    @property
    def classificatie(self) -> str:
        """TODO"""
        return self._classificatie.get_waarde()

    @classificatie.setter
    def classificatie(self, value):
        self._classificatie.set_waarde(value, owner=self)

    @property
    def mogelijkeVorm(self) -> List[DtcVormWaarden]:
        """TODO"""
        return self._mogelijkeVorm.get_waarde()

    @mogelijkeVorm.setter
    def mogelijkeVorm(self, value):
        self._mogelijkeVorm.set_waarde(value, owner=self)

    @property
    def zonaliteit(self) -> str:
        """TODO"""
        return self._zonaliteit.get_waarde()

    @zonaliteit.setter
    def zonaliteit(self, value):
        self._zonaliteit.set_waarde(value, owner=self)
