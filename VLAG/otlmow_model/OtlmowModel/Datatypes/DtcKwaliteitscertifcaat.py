# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKwaliteitscertifcaatWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._datumOndertekening = OTLAttribuut(field=DateField,
                                                naam='datumOndertekening',
                                                label='datum ondertekening',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKwaliteitscertifcaat.datumOndertekening',
                                                definition='De datum waarop het kwalitetiscertificaat ondertekend is door de administrateur-generaal.',
                                                owner=self)

        self._document = OTLAttribuut(field=DtcDocument,
                                      naam='document',
                                      label='document',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKwaliteitscertifcaat.document',
                                      definition='Documentbijlage met de vergunning.',
                                      owner=self)

        self._identificator = OTLAttribuut(field=StringField,
                                           naam='identificator',
                                           label='identificator',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKwaliteitscertifcaat.identificator',
                                           definition='De identificator van de vergunning.',
                                           owner=self)

    @property
    def datumOndertekening(self) -> date:
        """De datum waarop het kwalitetiscertificaat ondertekend is door de administrateur-generaal."""
        return self._datumOndertekening.get_waarde()

    @datumOndertekening.setter
    def datumOndertekening(self, value):
        self._datumOndertekening.set_waarde(value, owner=self._parent)

    @property
    def document(self) -> DtcDocumentWaarden:
        """Documentbijlage met de vergunning."""
        return self._document.get_waarde()

    @document.setter
    def document(self, value):
        self._document.set_waarde(value, owner=self._parent)

    @property
    def identificator(self) -> str:
        """De identificator van de vergunning."""
        return self._identificator.get_waarde()

    @identificator.setter
    def identificator(self, value):
        self._identificator.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKwaliteitscertifcaat(ComplexField):
    """Complex datatype voor een rapport waarin vastgelegd wordt dat een apparaat of installatie voldoet aan vooropgestelde kwaliteitseisen. Kan vereist zijn voor de tegenstelbaarheid van het gebruik van het toestel of de installatie in kwestie"""
    naam = 'DtcKwaliteitscertifcaat'
    label = 'kwaliteitscertificaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcKwaliteitscertifcaat'
    definition = 'Complex datatype voor een rapport waarin vastgelegd wordt dat een apparaat of installatie voldoet aan vooropgestelde kwaliteitseisen. Kan vereist zijn voor de tegenstelbaarheid van het gebruik van het toestel of de installatie in kwestie'
    waardeObject = DtcKwaliteitscertifcaatWaarden

    def __str__(self):
        return ComplexField.__str__(self)

