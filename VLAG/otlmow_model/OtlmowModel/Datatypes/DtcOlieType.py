# coding=utf-8
from datetime import date
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ..Datatypes.KlOlieAdditieven import KlOlieAdditieven
from ..Datatypes.KlOlieMerk import KlOlieMerk
from ..Datatypes.KlOlieType import KlOlieType
from ..Datatypes.KlViscositeitKlasse import KlViscositeitKlasse
from ..Datatypes.KwantWrdInLiter import KwantWrdInLiter, KwantWrdInLiterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOlieTypeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._additievenOlie = OTLAttribuut(field=KlOlieAdditieven,
                                            naam='additievenOlie',
                                            label='additieven olie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.additievenOlie',
                                            kardinaliteit_max='*',
                                            definition='Geeft aan welke additieven er aan de olie zijn toegevoegd.',
                                            owner=self)

        self._datumLaatstVerverst = OTLAttribuut(field=DateField,
                                                 naam='datumLaatstVerverst',
                                                 label='datum laatst ververst',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.datumLaatstVerverst',
                                                 definition='Geeft aan wanneer de olie voor het laatst ververst is geweest.',
                                                 owner=self)

        self._isSynthetisch = OTLAttribuut(field=BooleanField,
                                           naam='isSynthetisch',
                                           label='is synthetisch',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.isSynthetisch',
                                           definition='Geeft aan of de olie synthetisch is. Zo niet, dan is de olie biologisch.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlOlieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.merk',
                                  definition='Het merk van de olie.',
                                  owner=self)

        self._typeOlie = OTLAttribuut(field=KlOlieType,
                                      naam='typeOlie',
                                      label='type olie',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.typeOlie',
                                      definition='De technische naam van de type olie dat gebruikt wordt.',
                                      owner=self)

        self._viscositeitOlie = OTLAttribuut(field=KlViscositeitKlasse,
                                             naam='viscositeitOlie',
                                             label='viscositeit olie',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.viscositeitOlie',
                                             definition='De viscositeit van de gebruikte olie. Dit wordt aangeduid aan de hand van de ISO 3448 Viscosity Grade (VG) classificatie.',
                                             owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInLiter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType.volume',
                                    definition='Geeft aan hoeveel olie in het systeem zit.',
                                    owner=self)

    @property
    def additievenOlie(self) -> List[str]:
        """Geeft aan welke additieven er aan de olie zijn toegevoegd."""
        return self._additievenOlie.get_waarde()

    @additievenOlie.setter
    def additievenOlie(self, value):
        self._additievenOlie.set_waarde(value, owner=self._parent)

    @property
    def datumLaatstVerverst(self) -> date:
        """Geeft aan wanneer de olie voor het laatst ververst is geweest."""
        return self._datumLaatstVerverst.get_waarde()

    @datumLaatstVerverst.setter
    def datumLaatstVerverst(self, value):
        self._datumLaatstVerverst.set_waarde(value, owner=self._parent)

    @property
    def isSynthetisch(self) -> bool:
        """Geeft aan of de olie synthetisch is. Zo niet, dan is de olie biologisch."""
        return self._isSynthetisch.get_waarde()

    @isSynthetisch.setter
    def isSynthetisch(self, value):
        self._isSynthetisch.set_waarde(value, owner=self._parent)

    @property
    def merk(self) -> str:
        """Het merk van de olie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self._parent)

    @property
    def typeOlie(self) -> str:
        """De technische naam van de type olie dat gebruikt wordt."""
        return self._typeOlie.get_waarde()

    @typeOlie.setter
    def typeOlie(self, value):
        self._typeOlie.set_waarde(value, owner=self._parent)

    @property
    def viscositeitOlie(self) -> str:
        """De viscositeit van de gebruikte olie. Dit wordt aangeduid aan de hand van de ISO 3448 Viscosity Grade (VG) classificatie."""
        return self._viscositeitOlie.get_waarde()

    @viscositeitOlie.setter
    def viscositeitOlie(self, value):
        self._viscositeitOlie.set_waarde(value, owner=self._parent)

    @property
    def volume(self) -> KwantWrdInLiterWaarden:
        """Geeft aan hoeveel olie in het systeem zit."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOlieType(ComplexField):
    """Complex datatype om het type olie te beschrijven."""
    naam = 'DtcOlieType'
    label = 'Olie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcOlieType'
    definition = 'Complex datatype om het type olie te beschrijven.'
    waardeObject = DtcOlieTypeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

