# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ..Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm, DtcAfmetingBxlInCmWaarden
from ..Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm, DtcAfmetingDiameterInCmWaarden
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.BaseClasses.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlakWaarden(UnionWaarden):
    def __init__(self):
        UnionWaarden.__init__(self)
        self._rechthoekig = OTLAttribuut(field=DtcAfmetingBxlInCm,
                                         naam='rechthoekig',
                                         label='rechthoekig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rechthoekig',
                                         kardinaliteit_min='0',
                                         definition='Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter.',
                                         owner=self)

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInCm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rond',
                                  kardinaliteit_min='0',
                                  definition='Afmeting van de diameter in centimeter van een rond (grond)vlak.',
                                  owner=self)

    @property
    def rechthoekig(self) -> DtcAfmetingBxlInCmWaarden:
        """Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter."""
        return self._rechthoekig.get_waarde()

    @rechthoekig.setter
    def rechthoekig(self, value):
        self._rechthoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rechthoekig')

    @property
    def rond(self) -> DtcAfmetingDiameterInCmWaarden:
        """Afmeting van de diameter in centimeter van een rond (grond)vlak."""
        return self._rond.get_waarde()

    @rond.setter
    def rond(self, value):
        self._rond.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rond')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlak(UnionTypeField):
    """Datatype voor de afmeting van een (grond)vlak volgens zijn vorm."""
    naam = 'DtuAfmetingGrondvlak'
    label = 'afmeting grondvlak'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak'
    definition = 'Datatype voor de afmeting van een (grond)vlak volgens zijn vorm.'
    waardeObject = DtuAfmetingGrondvlakWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

