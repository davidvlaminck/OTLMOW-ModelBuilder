# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlDuurzaamheidsklasseHout import KlDuurzaamheidsklasseHout
from ..Datatypes.KlKwaliteitsklasseHout import KlKwaliteitsklasseHout
from ..Datatypes.KlSterkteklasseHout import KlSterkteklasseHout


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutspecificatiesWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._fscCertificaat = OTLAttribuut(field=DtcDocument,
                                            naam='fscCertificaat',
                                            label='FSC-certificaat',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.fscCertificaat',
                                            definition='Een attest of een bewijs dat voor elke boom die gebruikt wordt er een andere in de plaats is geplant.',
                                            owner=self)

        self._houtduurzaamheidsklasse = OTLAttribuut(field=KlDuurzaamheidsklasseHout,
                                                     naam='houtduurzaamheidsklasse',
                                                     label='houtduurzaamheidsklasse',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtduurzaamheidsklasse',
                                                     definition='De verwachte levensduur van het hout. De klasse geeft de resistentie aan van het kernhout tegen ongunstige omstandigheden.',
                                                     owner=self)

        self._houtkwaliteitsklasse = OTLAttribuut(field=KlKwaliteitsklasseHout,
                                                  naam='houtkwaliteitsklasse',
                                                  label='houtkwaliteitsklasse',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtkwaliteitsklasse',
                                                  definition='Kwaliteitsindeling van de houtsoort met betrekking op vervormingen, scheuren en kwasten.',
                                                  owner=self)

        self._houtsterkteklasse = OTLAttribuut(field=KlSterkteklasseHout,
                                               naam='houtsterkteklasse',
                                               label='houtsterkteklasse',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtsterkteklasse',
                                               definition='De maximale belasting van het hout. Deze klasse geeft aan hoe sterk en voor welke constructies de houtsoort geschikt is.',
                                               owner=self)

        self._isResistentTegenMarieneBoorders = OTLAttribuut(field=BooleanField,
                                                             naam='isResistentTegenMarieneBoorders',
                                                             label='is resistent tegen mariene boorders',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.isResistentTegenMarieneBoorders',
                                                             definition='Geeft aan of het hout resistent is bij toepassingen in contact met zout of brak water.',
                                                             owner=self)

    @property
    def fscCertificaat(self) -> DtcDocumentWaarden:
        """Een attest of een bewijs dat voor elke boom die gebruikt wordt er een andere in de plaats is geplant."""
        return self._fscCertificaat.get_waarde()

    @fscCertificaat.setter
    def fscCertificaat(self, value):
        self._fscCertificaat.set_waarde(value, owner=self._parent)

    @property
    def houtduurzaamheidsklasse(self) -> str:
        """De verwachte levensduur van het hout. De klasse geeft de resistentie aan van het kernhout tegen ongunstige omstandigheden."""
        return self._houtduurzaamheidsklasse.get_waarde()

    @houtduurzaamheidsklasse.setter
    def houtduurzaamheidsklasse(self, value):
        self._houtduurzaamheidsklasse.set_waarde(value, owner=self._parent)

    @property
    def houtkwaliteitsklasse(self) -> str:
        """Kwaliteitsindeling van de houtsoort met betrekking op vervormingen, scheuren en kwasten."""
        return self._houtkwaliteitsklasse.get_waarde()

    @houtkwaliteitsklasse.setter
    def houtkwaliteitsklasse(self, value):
        self._houtkwaliteitsklasse.set_waarde(value, owner=self._parent)

    @property
    def houtsterkteklasse(self) -> str:
        """De maximale belasting van het hout. Deze klasse geeft aan hoe sterk en voor welke constructies de houtsoort geschikt is."""
        return self._houtsterkteklasse.get_waarde()

    @houtsterkteklasse.setter
    def houtsterkteklasse(self, value):
        self._houtsterkteklasse.set_waarde(value, owner=self._parent)

    @property
    def isResistentTegenMarieneBoorders(self) -> bool:
        """Geeft aan of het hout resistent is bij toepassingen in contact met zout of brak water."""
        return self._isResistentTegenMarieneBoorders.get_waarde()

    @isResistentTegenMarieneBoorders.setter
    def isResistentTegenMarieneBoorders(self, value):
        self._isResistentTegenMarieneBoorders.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutspecificaties(ComplexField):
    """Complex datatype om de eigenschappen van hout te bundelen."""
    naam = 'DtcHoutspecificaties'
    label = 'Houtspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties'
    definition = 'Complex datatype om de eigenschappen van hout te bundelen.'
    waardeObject = DtcHoutspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

