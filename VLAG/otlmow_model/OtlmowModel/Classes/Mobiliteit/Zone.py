# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from ...Datatypes.KlZonetype import KlZonetype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zone(OTLAsset):
    """Ruimtelijk gebied"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Zone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlZonetype,
                                  naam='type',
                                  label='type',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#Zone.type',
                                  usagenote='Bijvoorbeeld: corridor, evenementzone',
                                  kardinaliteit_min='0',
                                  kardinaliteit_max='*',
                                  definition='Soort zone.',
                                  owner=self)

    @property
    def type(self) -> List[str]:
        """Soort zone."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
