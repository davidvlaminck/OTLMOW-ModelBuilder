# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeterPerSecondeWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterPerSeconde.standaardEenheid',
                                              usagenote='"kg/m3"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"m/s"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in in kg per kubieke meter',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterPerSeconde.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self) -> str:
        """De standaard eenheid bij dit datatype is uitgedrukt in in kg per kubieke meter"""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self) -> float:
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeterPerSeconde(OTLField):
    """Een kwantitatieve waarde die een getal in kg per kubieke meter uitdrukt."""
    naam = 'KwantWrdInMeterPerSeconde'
    label = 'Kwantitatieve waarde in kg per kubieke meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterPerSeconde'
    definition = 'Een kwantitatieve waarde die een getal in kg per kubieke meter uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInMeterPerSecondeWaarden

    def __str__(self):
        return OTLField.__str__(self)

