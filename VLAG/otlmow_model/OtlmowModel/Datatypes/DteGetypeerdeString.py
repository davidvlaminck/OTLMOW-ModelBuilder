# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteGetypeerdeStringWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._string = OTLAttribuut(field=StringField,
                                    naam='string',
                                    label='',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteGetypeerdeString.string',
                                    definition='De string.',
                                    owner=self)

    @property
    def string(self) -> str:
        """De string."""
        return self._string.get_waarde()

    @string.setter
    def string(self, value):
        self._string.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteGetypeerdeString(OTLField):
    """"""
    naam = 'DteGetypeerdeString'
    label = 'Getypeerde string'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteGetypeerdeString'
    definition = ''
    waarde_shortcut_applicable = True
    waardeObject = DteGetypeerdeStringWaarden

    def __str__(self):
        return OTLField.__str__(self)

