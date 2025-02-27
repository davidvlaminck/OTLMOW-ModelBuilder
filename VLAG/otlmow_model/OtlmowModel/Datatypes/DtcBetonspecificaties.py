# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlBetonmilieuklasse import KlBetonmilieuklasse
from ..Datatypes.KlBetonomgevingsklasse import KlBetonomgevingsklasse
from ..Datatypes.KlBetonsterkteklasse import KlBetonsterkteklasse
from ..Datatypes.KlGebruiksdomein import KlGebruiksdomein
from ..Datatypes.KlToeslagmiddelBeton import KlToeslagmiddelBeton
from ..Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBetonspecificatiesWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._betondekking = OTLAttribuut(field=KwantWrdInMillimeter,
                                          naam='betondekking',
                                          label='betondekking',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betondekking',
                                          definition='De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal.',
                                          owner=self)

        self._betonmilieuklassen = OTLAttribuut(field=KlBetonmilieuklasse,
                                                naam='betonmilieuklassen',
                                                label='betonmilieuklassen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonmilieuklassen',
                                                kardinaliteit_max='*',
                                                definition='Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn.',
                                                owner=self)

        self._betonomgevingsklassen = OTLAttribuut(field=KlBetonomgevingsklasse,
                                                   naam='betonomgevingsklassen',
                                                   label='betonomgevingsklassen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonomgevingsklassen',
                                                   kardinaliteit_max='*',
                                                   definition='De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn.',
                                                   owner=self)

        self._betonsterkteklasse = OTLAttribuut(field=KlBetonsterkteklasse,
                                                naam='betonsterkteklasse',
                                                label='betonsterkteklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonsterkteklasse',
                                                definition='De sterkteklasse is een maat voor de druksterkte van beton.',
                                                owner=self)

        self._gebruiksdomein = OTLAttribuut(field=KlGebruiksdomein,
                                            naam='gebruiksdomein',
                                            label='gebruiksdomein',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.gebruiksdomein',
                                            definition='De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte.',
                                            owner=self)

        self._grootsteKorrelafmetingDmax = OTLAttribuut(field=KwantWrdInMillimeter,
                                                        naam='grootsteKorrelafmetingDmax',
                                                        label='grootste korrelafmeting (Dmax)',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.grootsteKorrelafmetingDmax',
                                                        definition='De nominale grootste korrelafmeting (Dmax).',
                                                        owner=self)

        self._isCementMetBeperktAlkaligehalte = OTLAttribuut(field=BooleanField,
                                                             naam='isCementMetBeperktAlkaligehalte',
                                                             label='is cement met beperkt alkaligehalte',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetBeperktAlkaligehalte',
                                                             definition='Aanduiding of het cement een beperkt alkaligehalte heeft (LA).',
                                                             owner=self)

        self._isCementMetHogeAanvangssterkte = OTLAttribuut(field=BooleanField,
                                                            naam='isCementMetHogeAanvangssterkte',
                                                            label='is cement met hoge aanvangssterkte',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeAanvangssterkte',
                                                            definition='Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES).',
                                                            owner=self)

        self._isCementMetHogeBestandheidTegenSulfaten = OTLAttribuut(field=BooleanField,
                                                                     naam='isCementMetHogeBestandheidTegenSulfaten',
                                                                     label='is cement met hoge bestandheid tegen sulfaten',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeBestandheidTegenSulfaten',
                                                                     definition='Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR).',
                                                                     owner=self)

        self._isCementMetLageHydratatiewarmte = OTLAttribuut(field=BooleanField,
                                                             naam='isCementMetLageHydratatiewarmte',
                                                             label='is cement met lage hydratatiewarmte',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetLageHydratatiewarmte',
                                                             definition='Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH).',
                                                             owner=self)

        self._isColloidaalbeton = OTLAttribuut(field=BooleanField,
                                               naam='isColloidaalbeton',
                                               label='is colloïdaalbeton',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isColloidaalbeton',
                                               definition='Geeft aan of het beton zich niet ontmengt onder of in water.',
                                               owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                             usagenote='Attribuut uit gebruik sinds versie 2.5.0',
                                             deprecated_version='2.5.0',
                                             definition='De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                             owner=self)

        self._technischeFicheSpecificatiesBeton = OTLAttribuut(field=DtcDocument,
                                                               naam='technischeFicheSpecificatiesBeton',
                                                               label='technische fiche specificaties beton',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFicheSpecificatiesBeton',
                                                               definition='De technische fiche van de specificaties van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                                               owner=self)

        self._toeslagmiddelen = OTLAttribuut(field=KlToeslagmiddelBeton,
                                             naam='toeslagmiddelen',
                                             label='toeslagmiddelen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.toeslagmiddelen',
                                             kardinaliteit_max='*',
                                             definition='Materialen die aan het beton worden toegevoegd om vb.: een beter geheel te maken, holle ruimten te vullen waardoor de sterkte toeneemt, ruimten met minder massa te creëren,... Dit kunnen er meerdere zijn.',
                                             owner=self)

    @property
    def betondekking(self) -> KwantWrdInMillimeterWaarden:
        """De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal."""
        return self._betondekking.get_waarde()

    @betondekking.setter
    def betondekking(self, value):
        self._betondekking.set_waarde(value, owner=self._parent)

    @property
    def betonmilieuklassen(self) -> List[str]:
        """Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn."""
        return self._betonmilieuklassen.get_waarde()

    @betonmilieuklassen.setter
    def betonmilieuklassen(self, value):
        self._betonmilieuklassen.set_waarde(value, owner=self._parent)

    @property
    def betonomgevingsklassen(self) -> List[str]:
        """De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn."""
        return self._betonomgevingsklassen.get_waarde()

    @betonomgevingsklassen.setter
    def betonomgevingsklassen(self, value):
        self._betonomgevingsklassen.set_waarde(value, owner=self._parent)

    @property
    def betonsterkteklasse(self) -> str:
        """De sterkteklasse is een maat voor de druksterkte van beton."""
        return self._betonsterkteklasse.get_waarde()

    @betonsterkteklasse.setter
    def betonsterkteklasse(self, value):
        self._betonsterkteklasse.set_waarde(value, owner=self._parent)

    @property
    def gebruiksdomein(self) -> str:
        """De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte."""
        return self._gebruiksdomein.get_waarde()

    @gebruiksdomein.setter
    def gebruiksdomein(self, value):
        self._gebruiksdomein.set_waarde(value, owner=self._parent)

    @property
    def grootsteKorrelafmetingDmax(self) -> KwantWrdInMillimeterWaarden:
        """De nominale grootste korrelafmeting (Dmax)."""
        return self._grootsteKorrelafmetingDmax.get_waarde()

    @grootsteKorrelafmetingDmax.setter
    def grootsteKorrelafmetingDmax(self, value):
        self._grootsteKorrelafmetingDmax.set_waarde(value, owner=self._parent)

    @property
    def isCementMetBeperktAlkaligehalte(self) -> bool:
        """Aanduiding of het cement een beperkt alkaligehalte heeft (LA)."""
        return self._isCementMetBeperktAlkaligehalte.get_waarde()

    @isCementMetBeperktAlkaligehalte.setter
    def isCementMetBeperktAlkaligehalte(self, value):
        self._isCementMetBeperktAlkaligehalte.set_waarde(value, owner=self._parent)

    @property
    def isCementMetHogeAanvangssterkte(self) -> bool:
        """Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES)."""
        return self._isCementMetHogeAanvangssterkte.get_waarde()

    @isCementMetHogeAanvangssterkte.setter
    def isCementMetHogeAanvangssterkte(self, value):
        self._isCementMetHogeAanvangssterkte.set_waarde(value, owner=self._parent)

    @property
    def isCementMetHogeBestandheidTegenSulfaten(self) -> bool:
        """Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR)."""
        return self._isCementMetHogeBestandheidTegenSulfaten.get_waarde()

    @isCementMetHogeBestandheidTegenSulfaten.setter
    def isCementMetHogeBestandheidTegenSulfaten(self, value):
        self._isCementMetHogeBestandheidTegenSulfaten.set_waarde(value, owner=self._parent)

    @property
    def isCementMetLageHydratatiewarmte(self) -> bool:
        """Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH)."""
        return self._isCementMetLageHydratatiewarmte.get_waarde()

    @isCementMetLageHydratatiewarmte.setter
    def isCementMetLageHydratatiewarmte(self, value):
        self._isCementMetLageHydratatiewarmte.set_waarde(value, owner=self._parent)

    @property
    def isColloidaalbeton(self) -> bool:
        """Geeft aan of het beton zich niet ontmengt onder of in water."""
        return self._isColloidaalbeton.get_waarde()

    @isColloidaalbeton.setter
    def isColloidaalbeton(self, value):
        self._isColloidaalbeton.set_waarde(value, owner=self._parent)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,..."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self._parent)

    @property
    def technischeFicheSpecificatiesBeton(self) -> DtcDocumentWaarden:
        """De technische fiche van de specificaties van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,..."""
        return self._technischeFicheSpecificatiesBeton.get_waarde()

    @technischeFicheSpecificatiesBeton.setter
    def technischeFicheSpecificatiesBeton(self, value):
        self._technischeFicheSpecificatiesBeton.set_waarde(value, owner=self._parent)

    @property
    def toeslagmiddelen(self) -> List[str]:
        """Materialen die aan het beton worden toegevoegd om vb.: een beter geheel te maken, holle ruimten te vullen waardoor de sterkte toeneemt, ruimten met minder massa te creëren,... Dit kunnen er meerdere zijn."""
        return self._toeslagmiddelen.get_waarde()

    @toeslagmiddelen.setter
    def toeslagmiddelen(self, value):
        self._toeslagmiddelen.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBetonspecificaties(ComplexField):
    """Complex datatype om de eigenschappen van beton te bundelen. Deze omvat onder andere de verschillende betonklassen,hoe het beton gebruikt wordt,eigenschappen van het cement,een technische fiche van het beton,..."""
    naam = 'DtcBetonspecificaties'
    label = 'Betonspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties'
    definition = 'Complex datatype om de eigenschappen van beton te bundelen. Deze omvat onder andere de verschillende betonklassen,hoe het beton gebruikt wordt,eigenschappen van het cement,een technische fiche van het beton,...'
    waardeObject = DtcBetonspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

