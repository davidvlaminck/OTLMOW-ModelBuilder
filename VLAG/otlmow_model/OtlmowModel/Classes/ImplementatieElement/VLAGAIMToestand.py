# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from ...Datatypes.KlVLAGAIMToestand import KlVLAGAIMToestand


# Generated with OTLClassCreator. To modify: extend, do not edit
class VLAGAIMToestand(ABC):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#VLAGAIMToestand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._toestand = OTLAttribuut(field=KlVLAGAIMToestand,
                                      naam='toestand',
                                      label='AIM-toestand',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#VLAGAIMToestand.toestand',
                                      definition='Geeft de actuele stand in de levenscyclus van het VLAG object.',
                                      owner=self)

    @property
    def toestand(self) -> str:
        """Geeft de actuele stand in de levenscyclus van het VLAG object."""
        return self._toestand.get_waarde()

    @toestand.setter
    def toestand(self, value):
        self._toestand.set_waarde(value, owner=self)
