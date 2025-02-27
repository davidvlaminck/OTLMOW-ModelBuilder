# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlAardingAardingsstelsel import KlAardingAardingsstelsel


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAardingsstelselWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._attestDNB = OTLAttribuut(field=DtcDocument,
                                       naam='attestDNB',
                                       label='attest distributienetbeheerder',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcAardingsstelsel.attestDNB',
                                       usagenote='Voor een globaal aardingsstelsel moet een attest voorzien worden zoniet moet er van uitgegaan worden dat het om een gescheiden stelsel gaat ',
                                       definition='Een bestandsbijlage met het attest volgens het aardingsstelsel voorzien door de distributienetbeheerder .',
                                       owner=self)

        self._type = OTLAttribuut(field=KlAardingAardingsstelsel,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcAardingsstelsel.type',
                                  definition='Geeft het type aan van het aardingsstelsel volgens een keuzelijst.',
                                  owner=self)

    @property
    def attestDNB(self) -> DtcDocumentWaarden:
        """Een bestandsbijlage met het attest volgens het aardingsstelsel voorzien door de distributienetbeheerder ."""
        return self._attestDNB.get_waarde()

    @attestDNB.setter
    def attestDNB(self, value):
        self._attestDNB.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """Geeft het type aan van het aardingsstelsel volgens een keuzelijst."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAardingsstelsel(ComplexField):
    """Complex datatype dat het mogelijk maakt om het attest van de distributienetbeheerder toe te voegen in het geval van een globaal aardingsstelsel."""
    naam = 'DtcAardingsstelsel'
    label = 'Aardingsstelsel details.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcAardingsstelsel'
    definition = 'Complex datatype dat het mogelijk maakt om het attest van de distributienetbeheerder toe te voegen in het geval van een globaal aardingsstelsel.'
    usagenote = 'Het attest is enkel vereist voor globale aardingsstelsels. Voor gescheiden aardinsstelsel kanhet attribuut attestDNB leeg blijven.'
    waardeObject = DtcAardingsstelselWaarden

    def __str__(self):
        return ComplexField.__str__(self)

