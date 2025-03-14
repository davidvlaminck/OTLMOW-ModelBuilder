# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Besluit.Besluit import Besluit
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from ...Datatypes.DtcPeriode import DtcPeriode, DtcPeriodeWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanvullendReglement(Besluit, OTLAsset):
    """Een aanvullend reglement op de politie van het wegverkeer is een besluit met betrekking tot de aanpassing van de algemene wegcode aan plaatselijke omstandigheden met een blijvend of periodiek karakter."""

    typeURI = 'http://data.vlaanderen.be/ns/besluit#AanvullendReglement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOntwerpVoor', target='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp', direction='i')  # i = direction: incoming

        self._tijdsinterval = OTLAttribuut(field=DtcPeriode,
                                           naam='tijdsinterval',
                                           label='tijdsinterval',
                                           objectUri='http://data.vlaanderen.be/ns/besluit#AanvullendReglement.tijdsinterval',
                                           kardinaliteit_min='0',
                                           kardinaliteit_max='*',
                                           definition='TODO',
                                           owner=self)

    @property
    def tijdsinterval(self) -> List[DtcPeriodeWaarden]:
        """TODO"""
        return self._tijdsinterval.get_waarde()

    @tijdsinterval.setter
    def tijdsinterval(self, value):
        self._tijdsinterval.set_waarde(value, owner=self)
