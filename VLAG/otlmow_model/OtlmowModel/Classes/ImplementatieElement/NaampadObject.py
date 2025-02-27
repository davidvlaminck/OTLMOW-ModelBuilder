# coding=utf-8
import re

from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject, NaamField


class NaampadField(NaamField):
    def __init__(self, naam: str, label: str, objectUri: str, definition: str, owner):
        super().__init__(naam, label, objectUri, definition, owner)

    @classmethod
    def validate(cls, value, attribuut) -> bool:
        if re.match(r'^[\w.\-]+[/[\w.\-]+]*$', value) is None:
            return False
        if attribuut.owner.naam is not None:
            return value.split('/')[-1] == attribuut.owner.naam
        return True

    @classmethod
    def create_dummy_data(cls) -> str:
        return 'dummy/dummy'

# Generated with OTLClassCreator. To modify: extend, do not edit
class NaampadObject(AIMNaamObject):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._naampad = OTLAttribuut(field=NaampadField,
                                     naam='naampad',
                                     label='naampad',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
                                     definition='Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).',
                                     owner=self)

    @property
    def naampad(self) -> str:
        """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""
        return self._naampad.get_waarde()

    @naampad.setter
    def naampad(self, value):
        self._naampad.set_waarde(value, owner=self)
