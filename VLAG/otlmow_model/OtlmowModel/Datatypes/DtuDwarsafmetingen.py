# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ..Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm, DtcAfmetingBxlxhInMmWaarden
from ..Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm, DtcAfmetingDiameterInMmWaarden
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.BaseClasses.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingenWaarden(UnionWaarden):
    def __init__(self):
        UnionWaarden.__init__(self)
        self._rechthoekig = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                         naam='rechthoekig',
                                         label='rechthoekig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rechthoekig',
                                         kardinaliteit_min='0',
                                         definition='Afmetingen voor breedte, lengte en hoogte van een rechthoekig object.',
                                         owner=self)

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInMm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rond',
                                  kardinaliteit_min='0',
                                  definition='Afmeting van de diameter in milimeter van een rond object.',
                                  owner=self)

    @property
    def rechthoekig(self) -> DtcAfmetingBxlxhInMmWaarden:
        """Afmetingen voor breedte, lengte en hoogte van een rechthoekig object."""
        return self._rechthoekig.get_waarde()

    @rechthoekig.setter
    def rechthoekig(self, value):
        self._rechthoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rechthoekig')

    @property
    def rond(self) -> DtcAfmetingDiameterInMmWaarden:
        """Afmeting van de diameter in milimeter van een rond object."""
        return self._rond.get_waarde()

    @rond.setter
    def rond(self, value):
        self._rond.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rond')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingen(UnionTypeField):
    """Union datatype voor de dwarsafmetingen van een object volgens zijn vorm."""
    naam = 'DtuDwarsafmetingen'
    label = 'Dwarsafmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen'
    definition = 'Union datatype voor de dwarsafmetingen van een object volgens zijn vorm.'
    waardeObject = DtuDwarsafmetingenWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

