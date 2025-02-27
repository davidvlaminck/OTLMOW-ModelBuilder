# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlBVLaagtype import KlBVLaagtype
from ..Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfileerlaagWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.gewicht',
                                     definition='Het gewicht van de profileerlaag in ton.',
                                     owner=self)

        self._laagtype = OTLAttribuut(field=KlBVLaagtype,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.laagtype',
                                      definition='Het type van de bitumineuze verharding.',
                                      owner=self)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van de profileerlaag in ton."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self._parent)

    @property
    def laagtype(self) -> str:
        """Het type van de bitumineuze verharding."""
        return self._laagtype.get_waarde()

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfileerlaag(ComplexField):
    """Complex datatype om extra informatie te capteren van de profilerende laag."""
    naam = 'DtcProfileerlaag'
    label = 'Profileerlaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag'
    definition = 'Complex datatype om extra informatie te capteren van de profilerende laag.'
    waardeObject = DtcProfileerlaagWaarden

    def __str__(self):
        return ComplexField.__str__(self)

