# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AIMLinkObject import AIMLinkObject
from ...Datatypes.KlVerkeersbordcategorie import KlVerkeersbordcategorie


# Generated with OTLClassCreator. To modify: extend, do not edit
class OntwerpVerkeersteken(AIMLinkObject):
    """Associatieklasse tussen het AR ontwerp en een verkeersteken."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#OntwerpVerkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BevatVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp', direction='i')  # i = direction: incoming

        self._status = OTLAttribuut(field=KlVerkeersbordcategorie,
                                    naam='status',
                                    label='status',
                                    objectUri='http://www.w3.org/ns/adms#status',
                                    definition='TODO',
                                    owner=self)

    @property
    def status(self) -> str:
        """TODO"""
        return self._status.get_waarde()

    @status.setter
    def status(self, value):
        self._status.set_waarde(value, owner=self)
