# coding=utf-8
from typing import List
from datetime import date, date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcContactinfo import DtcContactinfo, DtcContactinfoWaarden
from ...Datatypes.KlBetrokkenheidRol import KlBetrokkenheidRol


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftBetrokkene(DirectioneleRelatie):
    """Koppelt een natuurlijk persoon,rechtspersoon of een hoedanigheid (een functie eerder dan de persoon die de functie uitoefent) aan een object in een bepaalde rol."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._datumAanvang = OTLAttribuut(field=DateField,
                                          naam='datumAanvang',
                                          label='datum aanvang',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.datumAanvang',
                                          definition='De datum waarop de betrokkenheid effectief geworden is of zal worden.',
                                          owner=self)

        self._datumEinde = OTLAttribuut(field=DateField,
                                        naam='datumEinde',
                                        label='datum einde',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.datumEinde',
                                        definition='De datum waarop de betrokkenheid beëindigd is of moet beëindigd worden.',
                                        owner=self)

        self._rol = OTLAttribuut(field=KlBetrokkenheidRol,
                                 naam='rol',
                                 label='rol',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.rol',
                                 definition='Type voor de manier waarop een agent betrokken is bij een object.',
                                 owner=self)

        self._specifiekeContactinfo = OTLAttribuut(field=DtcContactinfo,
                                                   naam='specifiekeContactinfo',
                                                   label='specifieke contactinfo',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene.specifiekeContactinfo',
                                                   kardinaliteit_min='0',
                                                   kardinaliteit_max='*',
                                                   definition='Specifieke contactgegevens van de betrokken agent met betrekking tot het gekoppelde object.',
                                                   owner=self)

    @property
    def datumAanvang(self) -> date:
        """De datum waarop de betrokkenheid effectief geworden is of zal worden."""
        return self._datumAanvang.get_waarde()

    @datumAanvang.setter
    def datumAanvang(self, value):
        self._datumAanvang.set_waarde(value, owner=self)

    @property
    def datumEinde(self) -> date:
        """De datum waarop de betrokkenheid beëindigd is of moet beëindigd worden."""
        return self._datumEinde.get_waarde()

    @datumEinde.setter
    def datumEinde(self, value):
        self._datumEinde.set_waarde(value, owner=self)

    @property
    def rol(self) -> str:
        """Type voor de manier waarop een agent betrokken is bij een object."""
        return self._rol.get_waarde()

    @rol.setter
    def rol(self, value):
        self._rol.set_waarde(value, owner=self)

    @property
    def specifiekeContactinfo(self) -> List[DtcContactinfoWaarden]:
        """Specifieke contactgegevens van de betrokken agent met betrekking tot het gekoppelde object."""
        return self._specifiekeContactinfo.get_waarde()

    @specifiekeContactinfo.setter
    def specifiekeContactinfo(self, value):
        self._specifiekeContactinfo.set_waarde(value, owner=self)
