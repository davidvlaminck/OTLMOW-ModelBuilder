# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBurgerlijkeKlasseBrugWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._astype = OTLAttribuut(field=KwantWrdInKiloNewton,
                                    naam='astype',
                                    label='astype',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcBurgerlijkeKlasseBrug.astype',
                                    definition='Maximale aslast van een uitzonderlijk voertuig dat zonder bijkomend advies over de brug mag rijden, uitgedrukt in kiloNewton.',
                                    owner=self)

        self._totaleLast = OTLAttribuut(field=KwantWrdInKiloNewton,
                                        naam='totaleLast',
                                        label='totale last',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcBurgerlijkeKlasseBrug.totaleLast',
                                        definition='Maximale totale last van een uitzonderlijk voertuig dat zonder bijkomend advies over de brug mag rijden, uitgedrukt in kiloNewton.',
                                        owner=self)

        self._voorwaarden = OTLAttribuut(field=StringField,
                                         naam='voorwaarden',
                                         label='voorwaarden',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcBurgerlijkeKlasseBrug.voorwaarden',
                                         definition='De randvoorwaarden van toepassing op de brug.',
                                         owner=self)

    @property
    def astype(self) -> KwantWrdInKiloNewtonWaarden:
        """Maximale aslast van een uitzonderlijk voertuig dat zonder bijkomend advies over de brug mag rijden, uitgedrukt in kiloNewton."""
        return self._astype.get_waarde()

    @astype.setter
    def astype(self, value):
        self._astype.set_waarde(value, owner=self._parent)

    @property
    def totaleLast(self) -> KwantWrdInKiloNewtonWaarden:
        """Maximale totale last van een uitzonderlijk voertuig dat zonder bijkomend advies over de brug mag rijden, uitgedrukt in kiloNewton."""
        return self._totaleLast.get_waarde()

    @totaleLast.setter
    def totaleLast(self, value):
        self._totaleLast.set_waarde(value, owner=self._parent)

    @property
    def voorwaarden(self) -> str:
        """De randvoorwaarden van toepassing op de brug."""
        return self._voorwaarden.get_waarde()

    @voorwaarden.setter
    def voorwaarden(self, value):
        self._voorwaarden.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBurgerlijkeKlasseBrug(ComplexField):
    """Complex datatype om de burgerlijke klasse van een brug te bepalen."""
    naam = 'DtcBurgerlijkeKlasseBrug'
    label = 'Burgerlijke klasse brug'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcBurgerlijkeKlasseBrug'
    definition = 'Complex datatype om de burgerlijke klasse van een brug te bepalen.'
    waardeObject = DtcBurgerlijkeKlasseBrugWaarden

    def __str__(self):
        return ComplexField.__str__(self)

