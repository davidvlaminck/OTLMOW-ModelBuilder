# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcBeschermingVraatschade import DtcBeschermingVraatschade, DtcBeschermingVraatschadeWaarden
from ..Datatypes.KlBeschermingMaaischade import KlBeschermingMaaischade
from ..Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade
from ..Datatypes.KlPlantmaatHoogte import KlPlantmaatHoogte
from ..Datatypes.KlPlantmaatOmtrek import KlPlantmaatOmtrek
from ..Datatypes.KlVegetatiePlantverband import KlVegetatiePlantverband
from ..Datatypes.KlVegetatieWortel import KlVegetatieWortel
from ..Datatypes.KlVormAanleveringHoutigeVegetatie import KlVormAanleveringHoutigeVegetatie
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutigeAanlegWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._beschermingVraatschade = OTLAttribuut(field=DtcBeschermingVraatschade,
                                                    naam='beschermingVraatschade',
                                                    label='bescherming vraatschade',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.beschermingVraatschade',
                                                    usagenote='Attribuut uit gebruik sinds versie 2.0.0',
                                                    deprecated_version='2.0.0',
                                                    definition='Bescherming van de stam tegen knaagdieren.',
                                                    owner=self)

        self._heeftBoomplaat = OTLAttribuut(field=BooleanField,
                                            naam='heeftBoomplaat',
                                            label='heeft boomplaat',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftBoomplaat',
                                            definition='Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden.',
                                            owner=self)

        self._heeftHaagsteun = OTLAttribuut(field=BooleanField,
                                            naam='heeftHaagsteun',
                                            label='heeft haagsteun',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftHaagsteun',
                                            definition='Duidt op de aanezigheid van een constructie van palen en bedrading die haagbeplanting ondersteunt.',
                                            owner=self)

        self._heeftWortelgeleidingwortelwering = OTLAttribuut(field=BooleanField,
                                                              naam='heeftWortelgeleidingwortelwering',
                                                              label='heeft wortelgeleiding-wortelwering',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftWortelgeleidingwortelwering',
                                                              definition='Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen. Het heeft als doel om boomwortels naar beneden te leiden, waar ze onder een obstakel verder kunnen groeien.',
                                                              owner=self)

        self._maaischadeBescherming = OTLAttribuut(field=KlBeschermingMaaischade,
                                                   naam='maaischadeBescherming',
                                                   label='maaischade bescherming',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.maaischadeBescherming',
                                                   definition='Bescherming van de stam tegen maaimachines.',
                                                   owner=self)

        self._plantafstand = OTLAttribuut(field=NonNegIntegerField,
                                          naam='plantafstand',
                                          label='plantafstand',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantafstand',
                                          definition='Aantal planten per lopende meter.',
                                          owner=self)

        self._plantdichtheid = OTLAttribuut(field=NonNegIntegerField,
                                            naam='plantdichtheid',
                                            label='plantdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantdichtheid',
                                            definition='Aantal planten per vierkante meter.',
                                            owner=self)

        self._plantmaatHoogte = OTLAttribuut(field=KlPlantmaatHoogte,
                                             naam='plantmaatHoogte',
                                             label='plantmaat hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantmaatHoogte',
                                             definition='De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde.',
                                             owner=self)

        self._plantmaatOmtrek = OTLAttribuut(field=KlPlantmaatOmtrek,
                                             naam='plantmaatOmtrek',
                                             label='plantmaat omtrek',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantmaatOmtrek',
                                             definition='De stamomtrek in centimeter (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.',
                                             owner=self)

        self._plantverband = OTLAttribuut(field=KlVegetatiePlantverband,
                                          naam='plantverband',
                                          label='plantverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantverband',
                                          definition='De wijze waarop de planten zijn geschikt.',
                                          owner=self)

        self._vormAanlevering = OTLAttribuut(field=KlVormAanleveringHoutigeVegetatie,
                                             naam='vormAanlevering',
                                             label='vorm aanlevering',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.vormAanlevering',
                                             definition='De wijze waarop het plantgoed wordt aangeleverd.',
                                             owner=self)

        self._vraatschadeBescherming = OTLAttribuut(field=KlMateriaalBeschermingVraatschade,
                                                    naam='vraatschadeBescherming',
                                                    label='vraatschade bescherming',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.vraatschadeBescherming',
                                                    definition='Bescherming van de stam tegen knaagdieren.',
                                                    owner=self)

        self._wortel = OTLAttribuut(field=KlVegetatieWortel,
                                    naam='wortel',
                                    label='wortel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.wortel',
                                    definition='De manier van levering en aanplanting van het wortelgestel van de boom of plant.',
                                    owner=self)

    @property
    def beschermingVraatschade(self) -> DtcBeschermingVraatschadeWaarden:
        """Bescherming van de stam tegen knaagdieren."""
        return self._beschermingVraatschade.get_waarde()

    @beschermingVraatschade.setter
    def beschermingVraatschade(self, value):
        self._beschermingVraatschade.set_waarde(value, owner=self._parent)

    @property
    def heeftBoomplaat(self) -> bool:
        """Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden."""
        return self._heeftBoomplaat.get_waarde()

    @heeftBoomplaat.setter
    def heeftBoomplaat(self, value):
        self._heeftBoomplaat.set_waarde(value, owner=self._parent)

    @property
    def heeftHaagsteun(self) -> bool:
        """Duidt op de aanezigheid van een constructie van palen en bedrading die haagbeplanting ondersteunt."""
        return self._heeftHaagsteun.get_waarde()

    @heeftHaagsteun.setter
    def heeftHaagsteun(self, value):
        self._heeftHaagsteun.set_waarde(value, owner=self._parent)

    @property
    def heeftWortelgeleidingwortelwering(self) -> bool:
        """Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen. Het heeft als doel om boomwortels naar beneden te leiden, waar ze onder een obstakel verder kunnen groeien."""
        return self._heeftWortelgeleidingwortelwering.get_waarde()

    @heeftWortelgeleidingwortelwering.setter
    def heeftWortelgeleidingwortelwering(self, value):
        self._heeftWortelgeleidingwortelwering.set_waarde(value, owner=self._parent)

    @property
    def maaischadeBescherming(self) -> str:
        """Bescherming van de stam tegen maaimachines."""
        return self._maaischadeBescherming.get_waarde()

    @maaischadeBescherming.setter
    def maaischadeBescherming(self, value):
        self._maaischadeBescherming.set_waarde(value, owner=self._parent)

    @property
    def plantafstand(self) -> int:
        """Aantal planten per lopende meter."""
        return self._plantafstand.get_waarde()

    @plantafstand.setter
    def plantafstand(self, value):
        self._plantafstand.set_waarde(value, owner=self._parent)

    @property
    def plantdichtheid(self) -> int:
        """Aantal planten per vierkante meter."""
        return self._plantdichtheid.get_waarde()

    @plantdichtheid.setter
    def plantdichtheid(self, value):
        self._plantdichtheid.set_waarde(value, owner=self._parent)

    @property
    def plantmaatHoogte(self) -> str:
        """De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde."""
        return self._plantmaatHoogte.get_waarde()

    @plantmaatHoogte.setter
    def plantmaatHoogte(self, value):
        self._plantmaatHoogte.set_waarde(value, owner=self._parent)

    @property
    def plantmaatOmtrek(self) -> str:
        """De stamomtrek in centimeter (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""
        return self._plantmaatOmtrek.get_waarde()

    @plantmaatOmtrek.setter
    def plantmaatOmtrek(self, value):
        self._plantmaatOmtrek.set_waarde(value, owner=self._parent)

    @property
    def plantverband(self) -> str:
        """De wijze waarop de planten zijn geschikt."""
        return self._plantverband.get_waarde()

    @plantverband.setter
    def plantverband(self, value):
        self._plantverband.set_waarde(value, owner=self._parent)

    @property
    def vormAanlevering(self) -> str:
        """De wijze waarop het plantgoed wordt aangeleverd."""
        return self._vormAanlevering.get_waarde()

    @vormAanlevering.setter
    def vormAanlevering(self, value):
        self._vormAanlevering.set_waarde(value, owner=self._parent)

    @property
    def vraatschadeBescherming(self) -> str:
        """Bescherming van de stam tegen knaagdieren."""
        return self._vraatschadeBescherming.get_waarde()

    @vraatschadeBescherming.setter
    def vraatschadeBescherming(self, value):
        self._vraatschadeBescherming.set_waarde(value, owner=self._parent)

    @property
    def wortel(self) -> str:
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""
        return self._wortel.get_waarde()

    @wortel.setter
    def wortel(self, value):
        self._wortel.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutigeAanleg(ComplexField):
    """Complex datatype dat de aanleg van houtige vegetatie beschrijft."""
    naam = 'DtcHoutigeAanleg'
    label = 'Houtige aanleg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg'
    definition = 'Complex datatype dat de aanleg van houtige vegetatie beschrijft.'
    waardeObject = DtcHoutigeAanlegWaarden

    def __str__(self):
        return ComplexField.__str__(self)

