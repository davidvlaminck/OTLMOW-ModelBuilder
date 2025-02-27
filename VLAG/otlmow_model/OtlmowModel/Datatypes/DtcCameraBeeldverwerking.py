# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlCameraBeeldverwerkingstype import KlCameraBeeldverwerkingstype


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCameraBeeldverwerkingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._configBestand = OTLAttribuut(field=DtcDocument,
                                           naam='configBestand',
                                           label='configuratiebestand beeldverwerking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCameraBeeldverwerking.configBestand',
                                           definition='Een bestand met de details van de configuratie voor het type beeldverwerking dat gekozen is in het type-attribuut van de instantie.',
                                           owner=self)

        self._typeBeeldverwerking = OTLAttribuut(field=KlCameraBeeldverwerkingstype,
                                                 naam='typeBeeldverwerking',
                                                 label='type beeldverwerking',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCameraBeeldverwerking.typeBeeldverwerking',
                                                 usagenote='Wanneer de camera de beeldverwerking niet zelf doet maar enkel beelden  verstuurt voor verwerking in een externe eenheid, moet die externe eenheid als aparte asset aangemaakt worden indien het specifieke type bestaat in de OTL of moet een instantie van Software gebruikt worden wanneer geen specifieke externe verwerkingseenheid voorzien is.',
                                                 definition='Geeft aan welk type beeldverwerking als onlosmakelijk deel van de camera geconfigureerd is.',
                                                 owner=self)

    @property
    def configBestand(self) -> DtcDocumentWaarden:
        """Een bestand met de details van de configuratie voor het type beeldverwerking dat gekozen is in het type-attribuut van de instantie."""
        return self._configBestand.get_waarde()

    @configBestand.setter
    def configBestand(self, value):
        self._configBestand.set_waarde(value, owner=self._parent)

    @property
    def typeBeeldverwerking(self) -> str:
        """Geeft aan welk type beeldverwerking als onlosmakelijk deel van de camera geconfigureerd is."""
        return self._typeBeeldverwerking.get_waarde()

    @typeBeeldverwerking.setter
    def typeBeeldverwerking(self, value):
        self._typeBeeldverwerking.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCameraBeeldverwerking(ComplexField):
    """Complex datatype waarmee een type beeldverwerking van een camera en het relevant configuratiebestand, bijgehouden worden."""
    naam = 'DtcCameraBeeldverwerking'
    label = 'Camera beeldverwerkingsinstellingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCameraBeeldverwerking'
    definition = 'Complex datatype waarmee een type beeldverwerking van een camera en het relevant configuratiebestand, bijgehouden worden.'
    waardeObject = DtcCameraBeeldverwerkingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

