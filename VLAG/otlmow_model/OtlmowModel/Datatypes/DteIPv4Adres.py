# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteIPv4AdresWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres.waarde',
                                    usagenote='Het formaat is een decimale notatie bv. 91.198.174.232',
                                    definition='De string die het IPv4 adres representeert.',
                                    owner=self)

    @property
    def waarde(self) -> str:
        """De string die het IPv4 adres representeert."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteIPv4Adres(OTLField):
    """Beschrijft een ip-adres volgens de ipv4 specificatie."""
    naam = 'DteIPv4Adres'
    label = 'IPv4-adres'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres'
    definition = 'Beschrijft een ip-adres volgens de ipv4 specificatie.'
    waarde_shortcut_applicable = True
    waardeObject = DteIPv4AdresWaarden

    def __str__(self):
        return OTLField.__str__(self)

