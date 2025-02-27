# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ..Datatypes.DtcAfmetingBxhInMm import DtcAfmetingBxhInMm, DtcAfmetingBxhInMmWaarden
from ..Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm, DtcAfmetingDiameterInMmWaarden
from ..Datatypes.DtcAfmetingZijdeInMm import DtcAfmetingZijdeInMm, DtcAfmetingZijdeInMmWaarden
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.BaseClasses.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbordWaarden(UnionWaarden):
    def __init__(self):
        UnionWaarden.__init__(self)
        self._achthoekig = OTLAttribuut(field=DtcAfmetingZijdeInMm,
                                        naam='achthoekig',
                                        label='achthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.achthoekig',
                                        kardinaliteit_min='0',
                                        definition='De afmeting voor een achthoekig verkeersbord (zijde in millimeter).',
                                        owner=self)

        self._driehoekig = OTLAttribuut(field=DtcAfmetingZijdeInMm,
                                        naam='driehoekig',
                                        label='driehoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.driehoekig',
                                        kardinaliteit_min='0',
                                        definition='De afmeting van een driehoekig verkeersbord (zijde in millimeter).',
                                        owner=self)

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInMm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.rond',
                                  kardinaliteit_min='0',
                                  definition='De afmeting voor een rond verkeersbord (diameter in millimeter).',
                                  owner=self)

        self._vierhoekig = OTLAttribuut(field=DtcAfmetingBxhInMm,
                                        naam='vierhoekig',
                                        label='vierhoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.vierhoekig',
                                        kardinaliteit_min='0',
                                        definition='De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter).',
                                        owner=self)

        self._zeshoekig = OTLAttribuut(field=DtcAfmetingZijdeInMm,
                                       naam='zeshoekig',
                                       label='zeshoekig',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.zeshoekig',
                                       kardinaliteit_min='0',
                                       definition='De afmeting voor een zeshoekig verkeersbord (zijde in millimeter).',
                                       owner=self)

    @property
    def achthoekig(self) -> DtcAfmetingZijdeInMmWaarden:
        """De afmeting voor een achthoekig verkeersbord (zijde in millimeter)."""
        return self._achthoekig.get_waarde()

    @achthoekig.setter
    def achthoekig(self, value):
        self._achthoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_achthoekig')

    @property
    def driehoekig(self) -> DtcAfmetingZijdeInMmWaarden:
        """De afmeting van een driehoekig verkeersbord (zijde in millimeter)."""
        return self._driehoekig.get_waarde()

    @driehoekig.setter
    def driehoekig(self, value):
        self._driehoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_driehoekig')

    @property
    def rond(self) -> DtcAfmetingDiameterInMmWaarden:
        """De afmeting voor een rond verkeersbord (diameter in millimeter)."""
        return self._rond.get_waarde()

    @rond.setter
    def rond(self, value):
        self._rond.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rond')

    @property
    def vierhoekig(self) -> DtcAfmetingBxhInMmWaarden:
        """De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter)."""
        return self._vierhoekig.get_waarde()

    @vierhoekig.setter
    def vierhoekig(self, value):
        self._vierhoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_vierhoekig')

    @property
    def zeshoekig(self) -> DtcAfmetingZijdeInMmWaarden:
        """De afmeting voor een zeshoekig verkeersbord (zijde in millimeter)."""
        return self._zeshoekig.get_waarde()

    @zeshoekig.setter
    def zeshoekig(self, value):
        self._zeshoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_zeshoekig')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbord(UnionTypeField):
    """Union datatype voor de afmeting van het verkeersbord."""
    naam = 'DtuAfmetingVerkeersbord'
    label = 'Afmeting verkeersbord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord'
    definition = 'Union datatype voor de afmeting van het verkeersbord.'
    waardeObject = DtuAfmetingVerkeersbordWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

