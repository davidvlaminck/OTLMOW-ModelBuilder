# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteKleurRALWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde',
                                    usagenote='De waarde moet voldoen aan volgende regex: [1-9]\\d{3}',
                                    definition='Beschrijft een kleur volgens het RAL classificatiesysteem.',
                                    owner=self)

    @property
    def waarde(self) -> str:
        """Beschrijft een kleur volgens het RAL classificatiesysteem."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteKleurRAL(OTLField):
    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""
    naam = 'DteKleurRAL'
    label = 'RAL-kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL'
    definition = 'Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.'
    waarde_shortcut_applicable = True
    waardeObject = DteKleurRALWaarden

    def __str__(self):
        return OTLField.__str__(self)

