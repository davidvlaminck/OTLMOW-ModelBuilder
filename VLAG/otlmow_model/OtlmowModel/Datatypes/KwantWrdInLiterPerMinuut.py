# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInLiterPerMinuutWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInLiterPerMinuut.standaardEenheid',
                                              usagenote='"l/min"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"l/min"^^cdt:ucumunit',
                                              definition='De staandaard eenheid bij dit datatype is uitgedrukt in liter per minuut.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInLiterPerMinuut.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self) -> str:
        """De staandaard eenheid bij dit datatype is uitgedrukt in liter per minuut."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self) -> float:
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInLiterPerMinuut(OTLField):
    """Een kwantitatieve waarde die een getal in liter per minuut uitdrukt."""
    naam = 'KwantWrdInLiterPerMinuut'
    label = 'Kwantitatieve waarde in liter per minuut'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInLiterPerMinuut'
    definition = 'Een kwantitatieve waarde die een getal in liter per minuut uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInLiterPerMinuutWaarden

    def __str__(self):
        return OTLField.__str__(self)

