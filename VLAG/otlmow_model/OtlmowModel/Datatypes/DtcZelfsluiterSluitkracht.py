# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlZelfsluiterSluitkrachtnorm import KlZelfsluiterSluitkrachtnorm


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcZelfsluiterSluitkrachtWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bovengrens = OTLAttribuut(field=KlZelfsluiterSluitkrachtnorm,
                                        naam='bovengrens',
                                        label='bovengrens',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcZelfsluiterSluitkracht.bovengrens',
                                        usagenote='Gebruik dezelfde waarde voor onder- en bovengrens en ingestelde sluitkracht voor zelfsluiters zonder bereik, met slechts een mogelijke invulling van de sluitkracht.',
                                        definition='Hoogste sluitkracht van de zelfsluiter voor deuren, poorten etc. volgens de bestaande normering',
                                        owner=self)

        self._ingesteld = OTLAttribuut(field=KlZelfsluiterSluitkrachtnorm,
                                       naam='ingesteld',
                                       label='ingesteld',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcZelfsluiterSluitkracht.ingesteld',
                                       usagenote='Gebruik dezelfde waarde voor onder- en bovengrens en ingestelde sluitkracht voor zelfsluiters zonder bereik, met slechts een mogelijke invulling van de sluitkracht.',
                                       definition='De ingestelde sluitkracht van de zelfsluiter voor deuren, poorten etc. volgens de bestaande normering',
                                       owner=self)

        self._ondergrens = OTLAttribuut(field=KlZelfsluiterSluitkrachtnorm,
                                        naam='ondergrens',
                                        label='ondergrens',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcZelfsluiterSluitkracht.ondergrens',
                                        usagenote='Gebruik dezelfde waarde voor onder- en bovengrens en ingestelde sluitkracht voor zelfsluiters zonder bereik, met slechts een mogelijke invulling van de sluitkracht.',
                                        definition='Laagste sluitkracht van de zelfsluiter voor deuren, poorten etc. volgens de bestaande normering',
                                        owner=self)

    @property
    def bovengrens(self) -> str:
        """Hoogste sluitkracht van de zelfsluiter voor deuren, poorten etc. volgens de bestaande normering"""
        return self._bovengrens.get_waarde()

    @bovengrens.setter
    def bovengrens(self, value):
        self._bovengrens.set_waarde(value, owner=self._parent)

    @property
    def ingesteld(self) -> str:
        """De ingestelde sluitkracht van de zelfsluiter voor deuren, poorten etc. volgens de bestaande normering"""
        return self._ingesteld.get_waarde()

    @ingesteld.setter
    def ingesteld(self, value):
        self._ingesteld.set_waarde(value, owner=self._parent)

    @property
    def ondergrens(self) -> str:
        """Laagste sluitkracht van de zelfsluiter voor deuren, poorten etc. volgens de bestaande normering"""
        return self._ondergrens.get_waarde()

    @ondergrens.setter
    def ondergrens(self, value):
        self._ondergrens.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcZelfsluiterSluitkracht(ComplexField):
    """Datatype voor het bereik en de instelling van een zelfsluiter voor deuren, poorten etc."""
    naam = 'DtcZelfsluiterSluitkracht'
    label = 'Zelfsluiter sluitkracht'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcZelfsluiterSluitkracht'
    definition = 'Datatype voor het bereik en de instelling van een zelfsluiter voor deuren, poorten etc.'
    waardeObject = DtcZelfsluiterSluitkrachtWaarden

    def __str__(self):
        return ComplexField.__str__(self)

