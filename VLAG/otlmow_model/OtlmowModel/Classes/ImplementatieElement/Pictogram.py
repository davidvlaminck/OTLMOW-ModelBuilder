# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Concept import Concept
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pictogram(Concept):
    """"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pictogram.afbeelding',
                                        definition='',
                                        owner=self)

    @property
    def afbeelding(self) -> DtcDocumentWaarden:
        """"""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)
