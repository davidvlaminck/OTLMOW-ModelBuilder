# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlConstructiestaalsoort import KlConstructiestaalsoort
from ..Datatypes.KlWalsmethode import KlWalsmethode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcConstructiestaalspecificatiesWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._staalsoort = OTLAttribuut(field=KlConstructiestaalsoort,
                                        naam='staalsoort',
                                        label='staalsoort',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties.staalsoort',
                                        definition='Staalkwaliteit die wordt gebruikt volgens Europese normen.',
                                        owner=self)

        self._walsmethode = OTLAttribuut(field=KlWalsmethode,
                                         naam='walsmethode',
                                         label='walsmethode',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties.walsmethode',
                                         definition='Op welke manier het staal gewalst is.',
                                         owner=self)

    @property
    def staalsoort(self) -> str:
        """Staalkwaliteit die wordt gebruikt volgens Europese normen."""
        return self._staalsoort.get_waarde()

    @staalsoort.setter
    def staalsoort(self, value):
        self._staalsoort.set_waarde(value, owner=self._parent)

    @property
    def walsmethode(self) -> str:
        """Op welke manier het staal gewalst is."""
        return self._walsmethode.get_waarde()

    @walsmethode.setter
    def walsmethode(self, value):
        self._walsmethode.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcConstructiestaalspecificaties(ComplexField):
    """Complex datatype om de eigenschappen van constructiestaal te bundelen."""
    naam = 'DtcConstructiestaalspecificaties'
    label = 'Constructiestaalspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties'
    definition = 'Complex datatype om de eigenschappen van constructiestaal te bundelen.'
    waardeObject = DtcConstructiestaalspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

