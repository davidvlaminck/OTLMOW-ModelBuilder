# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ..Datatypes.KlSchoorhoek import KlSchoorhoek
from ..Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.BaseClasses.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuHellingsSchoorhoekWaarden(UnionWaarden):
    def __init__(self):
        UnionWaarden.__init__(self)
        self._hellingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek.hellingshoek',
                                          kardinaliteit_min='0',
                                          definition='Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in decimale graden.',
                                          owner=self)

        self._schoorhoek = OTLAttribuut(field=KlSchoorhoek,
                                        naam='schoorhoek',
                                        label='schoorhoek',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek.schoorhoek',
                                        kardinaliteit_min='0',
                                        definition='Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in 1 op x (vb.: 1/4).',
                                        owner=self)

    @property
    def hellingshoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in decimale graden."""
        return self._hellingshoek.get_waarde()

    @hellingshoek.setter
    def hellingshoek(self, value):
        self._hellingshoek.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_hellingshoek')

    @property
    def schoorhoek(self) -> str:
        """Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in 1 op x (vb.: 1/4)."""
        return self._schoorhoek.get_waarde()

    @schoorhoek.setter
    def schoorhoek(self, value):
        self._schoorhoek.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_schoorhoek')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuHellingsSchoorhoek(UnionTypeField):
    """Union datatype voor de hellings- of de schoorhoek."""
    naam = 'DtuHellingsSchoorhoek'
    label = 'Hellings- of schoorhoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek'
    definition = 'Union datatype voor de hellings- of de schoorhoek.'
    waardeObject = DtuHellingsSchoorhoekWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

