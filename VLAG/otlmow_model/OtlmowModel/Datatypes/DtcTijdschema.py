# coding=utf-8
from typing import List
from datetime import date, time, date, time, date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.BaseClasses.TimeField import TimeField
from otlmow_model.OtlmowModel.BaseClasses.URIField import URIField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTijdschemaWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._aantal = OTLAttribuut(field=IntegerField,
                                    naam='aantal',
                                    label='aantal',
                                    objectUri='https://schema.org/Schedule.aantal',
                                    usagenote='Bv 10 keer vanaf de startdatum.',
                                    kardinaliteit_min='0',
                                    definition='Aantal keer dat het plaatsvindt.',
                                    owner=self)

        self._duur = OTLAttribuut(field=StringField,
                                  naam='duur',
                                  label='duur',
                                  objectUri='https://schema.org/Schedule.duur',
                                  usagenote='Uit te drukken als een interval volgens iso 8601, bv P1D 1 dag, P2H twee uur... ',
                                  kardinaliteit_min='0',
                                  definition='Duur van hetgeen plaatsvindt.',
                                  owner=self)

        self._einddatum = OTLAttribuut(field=DateField,
                                       naam='einddatum',
                                       label='einddatum',
                                       objectUri='https://schema.org/Schedule.einddatum',
                                       kardinaliteit_min='0',
                                       definition='Datum tot wanneer het plaatsvindt.',
                                       owner=self)

        self._eindtijd = OTLAttribuut(field=TimeField,
                                      naam='eindtijd',
                                      label='eindtijd',
                                      objectUri='https://schema.org/Schedule.eindtijd',
                                      kardinaliteit_min='0',
                                      definition='Tijdstip waarop het eindigt.',
                                      owner=self)

        self._frequentie = OTLAttribuut(field=StringField,
                                        naam='frequentie',
                                        label='frequentie',
                                        objectUri='https://schema.org/Schedule.frequentie',
                                        usagenote='Uit te drukken als een interval volgens iso 8601, bv P1W betekent wekelijks, P2W tweewekelijks, P1D dagelijks... ',
                                        definition='Frequentie waarmee het plaatsvindt.',
                                        owner=self)

        self._perDag = OTLAttribuut(field=URIField,
                                    naam='perDag',
                                    label='per dag',
                                    objectUri='https://schema.org/Schedule.perDag',
                                    usagenote="Gebruik de URI's van schema.org, bv https://schema.org/Monday voor maandag. Deze verwijzen door naar Wikidata waar ook de Nederlandse vertaling te vinden is, bv http://www.wikidata.org/entity/Q105 voor maandag.  ",
                                    kardinaliteit_min='0',
                                    kardinaliteit_max='*',
                                    definition='Dagen van de week waarop het plaatsvindt.',
                                    owner=self)

        self._perDagVanDeMaand = OTLAttribuut(field=IntegerField,
                                              naam='perDagVanDeMaand',
                                              label='per dag van de maand',
                                              objectUri='https://schema.org/Schedule.perDagVanDeMaand',
                                              kardinaliteit_min='0',
                                              kardinaliteit_max='*',
                                              definition='Dagen van de maand waarop het plaatsvindt.',
                                              owner=self)

        self._perMaand = OTLAttribuut(field=IntegerField,
                                      naam='perMaand',
                                      label='per maand',
                                      objectUri='https://schema.org/Schedule.perMaand',
                                      kardinaliteit_min='0',
                                      kardinaliteit_max='*',
                                      definition='Maanden van het jaar waarop het plaatsvindt.',
                                      owner=self)

        self._perSetPositie = OTLAttribuut(field=IntegerField,
                                           naam='perSetPositie',
                                           label='per setpositie',
                                           objectUri='https://schema.org/Schedule.perSetPositie',
                                           usagenote='Bv als iets maandelijks plaatsvindt op maandag om te zeggen dat het bv de eerste maandag is vd maand. Frequentie is dan maandelijks, perDag is Maandag en de perSetpositie is dan 1. Ook negatieve cijfers zijn mogelijk, bv -1 zou aangeven dat het op de laatste maandag vd maand plaatsvindt.',
                                           kardinaliteit_min='0',
                                           definition='N-de keer dat iets plaatsvindt uit de verzameling van mogelijke tijdstippen.',
                                           owner=self)

        self._startdatum = OTLAttribuut(field=DateField,
                                        naam='startdatum',
                                        label='startdatum',
                                        objectUri='https://schema.org/Schedule.startdatum',
                                        kardinaliteit_min='0',
                                        definition='Datum vanaf wanneer het plaatsvindt.',
                                        owner=self)

        self._starttijd = OTLAttribuut(field=TimeField,
                                       naam='starttijd',
                                       label='starttijd',
                                       objectUri='https://schema.org/Schedule.starttijd',
                                       kardinaliteit_min='0',
                                       definition='Tijdstip waarop het start.',
                                       owner=self)

        self._uitzonderingsdatum = OTLAttribuut(field=DateField,
                                                naam='uitzonderingsdatum',
                                                label='uitzonderingsdatum',
                                                objectUri='https://schema.org/Schedule.uitzonderingsdatum',
                                                kardinaliteit_min='0',
                                                kardinaliteit_max='*',
                                                definition='Datums waarop het uitzonderlijk niet plaatsvindt.',
                                                owner=self)

    @property
    def aantal(self) -> int:
        """Aantal keer dat het plaatsvindt."""
        return self._aantal.get_waarde()

    @aantal.setter
    def aantal(self, value):
        self._aantal.set_waarde(value, owner=self._parent)

    @property
    def duur(self) -> str:
        """Duur van hetgeen plaatsvindt."""
        return self._duur.get_waarde()

    @duur.setter
    def duur(self, value):
        self._duur.set_waarde(value, owner=self._parent)

    @property
    def einddatum(self) -> date:
        """Datum tot wanneer het plaatsvindt."""
        return self._einddatum.get_waarde()

    @einddatum.setter
    def einddatum(self, value):
        self._einddatum.set_waarde(value, owner=self._parent)

    @property
    def eindtijd(self) -> time:
        """Tijdstip waarop het eindigt."""
        return self._eindtijd.get_waarde()

    @eindtijd.setter
    def eindtijd(self, value):
        self._eindtijd.set_waarde(value, owner=self._parent)

    @property
    def frequentie(self) -> str:
        """Frequentie waarmee het plaatsvindt."""
        return self._frequentie.get_waarde()

    @frequentie.setter
    def frequentie(self, value):
        self._frequentie.set_waarde(value, owner=self._parent)

    @property
    def perDag(self) -> List[str]:
        """Dagen van de week waarop het plaatsvindt."""
        return self._perDag.get_waarde()

    @perDag.setter
    def perDag(self, value):
        self._perDag.set_waarde(value, owner=self._parent)

    @property
    def perDagVanDeMaand(self) -> List[int]:
        """Dagen van de maand waarop het plaatsvindt."""
        return self._perDagVanDeMaand.get_waarde()

    @perDagVanDeMaand.setter
    def perDagVanDeMaand(self, value):
        self._perDagVanDeMaand.set_waarde(value, owner=self._parent)

    @property
    def perMaand(self) -> List[int]:
        """Maanden van het jaar waarop het plaatsvindt."""
        return self._perMaand.get_waarde()

    @perMaand.setter
    def perMaand(self, value):
        self._perMaand.set_waarde(value, owner=self._parent)

    @property
    def perSetPositie(self) -> int:
        """N-de keer dat iets plaatsvindt uit de verzameling van mogelijke tijdstippen."""
        return self._perSetPositie.get_waarde()

    @perSetPositie.setter
    def perSetPositie(self, value):
        self._perSetPositie.set_waarde(value, owner=self._parent)

    @property
    def startdatum(self) -> date:
        """Datum vanaf wanneer het plaatsvindt."""
        return self._startdatum.get_waarde()

    @startdatum.setter
    def startdatum(self, value):
        self._startdatum.set_waarde(value, owner=self._parent)

    @property
    def starttijd(self) -> time:
        """Tijdstip waarop het start."""
        return self._starttijd.get_waarde()

    @starttijd.setter
    def starttijd(self, value):
        self._starttijd.set_waarde(value, owner=self._parent)

    @property
    def uitzonderingsdatum(self) -> List[date]:
        """Datums waarop het uitzonderlijk niet plaatsvindt."""
        return self._uitzonderingsdatum.get_waarde()

    @uitzonderingsdatum.setter
    def uitzonderingsdatum(self, value):
        self._uitzonderingsdatum.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTijdschema(ComplexField):
    """Overzicht van de tijdstippen waarop iets plaatsvindt."""
    naam = 'DtcTijdschema'
    label = 'Tijdschema'
    objectUri = 'https://schema.org/Schedule'
    definition = 'Overzicht van de tijdstippen waarop iets plaatsvindt.'
    usagenote = 'Tijdstippen (meervoud) ipv tijdstip (enkelvoud),het gaat maw over iets (bv vergadering,taak,gebeurtenis) dat herhaaldelijk plaatsvindt,typisch volgens een regelmatig patroon (bv repetitie elke vrijdag).'
    waardeObject = DtcTijdschemaWaarden

    def __str__(self):
        return ComplexField.__str__(self)

