# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Besluit(OTLAsset):
    """De authentieke schriftelijke neerslag van een beslissing van een bestuursorgaan. Deze beslissing houdt een rechtshandeling in waarbij sprake is van een beoogd rechtsgevolg."""

    typeURI = 'https://data.vlaanderen.be/ns/besluit#Besluit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/besluit#heeftVoorwaarde', target='http://data.vlaanderen.be/ns/besluit#Voorwaarde', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOnderdeelVan', target='https://data.vlaanderen.be/ns/besluit#Artikel', direction='i')  # i = direction: incoming

        self._beschrijving = OTLAttribuut(field=StringField,
                                          naam='beschrijving',
                                          label='beschrijving',
                                          objectUri='https://data.vlaanderen.be/ns/besluit#Besluit.beschrijving',
                                          definition='',
                                          owner=self)

        self._citeeropschrift = OTLAttribuut(field=StringField,
                                             naam='citeeropschrift',
                                             label='korte titel',
                                             objectUri='https://data.vlaanderen.be/ns/besluit#Besluit.citeeropschrift',
                                             definition='',
                                             owner=self)

        self._motivering = OTLAttribuut(field=StringField,
                                        naam='motivering',
                                        label='motivering',
                                        objectUri='https://data.vlaanderen.be/ns/besluit#Besluit.motivering',
                                        definition='Beschrijving van de juridische en feitelijke motivering achter de beslissing die wordt uitgedrukt in het besluit.',
                                        owner=self)

        self._publicatiedatum = OTLAttribuut(field=DateField,
                                             naam='publicatiedatum',
                                             label='datum publicatie',
                                             objectUri='https://data.vlaanderen.be/ns/besluit#Besluit.publicatiedatum',
                                             definition='',
                                             owner=self)

    @property
    def beschrijving(self) -> str:
        """"""
        return self._beschrijving.get_waarde()

    @beschrijving.setter
    def beschrijving(self, value):
        self._beschrijving.set_waarde(value, owner=self)

    @property
    def citeeropschrift(self) -> str:
        """"""
        return self._citeeropschrift.get_waarde()

    @citeeropschrift.setter
    def citeeropschrift(self, value):
        self._citeeropschrift.set_waarde(value, owner=self)

    @property
    def motivering(self) -> str:
        """Beschrijving van de juridische en feitelijke motivering achter de beslissing die wordt uitgedrukt in het besluit."""
        return self._motivering.get_waarde()

    @motivering.setter
    def motivering(self, value):
        self._motivering.set_waarde(value, owner=self)

    @property
    def publicatiedatum(self) -> date:
        """"""
        return self._publicatiedatum.get_waarde()

    @publicatiedatum.setter
    def publicatiedatum(self, value):
        self._publicatiedatum.set_waarde(value, owner=self)
