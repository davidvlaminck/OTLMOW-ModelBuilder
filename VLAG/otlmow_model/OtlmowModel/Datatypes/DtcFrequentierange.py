# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInHerz import KwantWrdInHerz, KwantWrdInHerzWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcFrequentierangeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bovengrens = OTLAttribuut(field=KwantWrdInHerz,
                                        naam='bovengrens',
                                        label='bovengrens',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcFrequentierange.bovengrens',
                                        definition='De bovengrens van de frequentierange van het toestel.',
                                        owner=self)

        self._ondergrens = OTLAttribuut(field=KwantWrdInHerz,
                                        naam='ondergrens',
                                        label='ondergrens',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcFrequentierange.ondergrens',
                                        definition='De ondergrens van de frequentierange van het toestel.',
                                        owner=self)

    @property
    def bovengrens(self) -> KwantWrdInHerzWaarden:
        """De bovengrens van de frequentierange van het toestel."""
        return self._bovengrens.get_waarde()

    @bovengrens.setter
    def bovengrens(self, value):
        self._bovengrens.set_waarde(value, owner=self._parent)

    @property
    def ondergrens(self) -> KwantWrdInHerzWaarden:
        """De ondergrens van de frequentierange van het toestel."""
        return self._ondergrens.get_waarde()

    @ondergrens.setter
    def ondergrens(self, value):
        self._ondergrens.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcFrequentierange(ComplexField):
    """Complex datatype voor de frequentierange van een toestel."""
    naam = 'DtcFrequentierange'
    label = 'frequentierange'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcFrequentierange'
    definition = 'Complex datatype voor de frequentierange van een toestel.'
    waardeObject = DtcFrequentierangeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

