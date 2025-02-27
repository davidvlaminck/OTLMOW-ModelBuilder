# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ..Datatypes.KlGCMeetMethode import KlGCMeetMethode
from ..Datatypes.KlLEGCNorm import KlLEGCNorm
from ..Datatypes.KlLEGCTestType import KlLEGCTestType


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGeluidstestRapportWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._geluidsabsorptieReflectie = OTLAttribuut(field=IntegerField,
                                                       naam='geluidsabsorptieReflectie',
                                                       label='geluidsabsorptie reflectie',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.geluidsabsorptieReflectie',
                                                       definition='De absorptie- of reflectiewaarde van het geluidsscherm als geheel getal.',
                                                       owner=self)

        self._gemetenWaarde = OTLAttribuut(field=IntegerField,
                                           naam='gemetenWaarde',
                                           label='gemeten waarde',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.gemetenWaarde',
                                           definition='De sterkte van het geluid in dB.',
                                           owner=self)

        self._locatieInSitulabo = OTLAttribuut(field=KlGCMeetMethode,
                                               naam='locatieInSitulabo',
                                               label='locatie in situlabo',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.locatieInSitulabo',
                                               definition='Locatie waar de geluidstest is uitgevoerd (terrein of labo).',
                                               owner=self)

        self._luchtgeluidsisolatie = OTLAttribuut(field=IntegerField,
                                                  naam='luchtgeluidsisolatie',
                                                  label='luchtgeluidsisolatie',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.luchtgeluidsisolatie',
                                                  definition='De gemeten waarde van het luchtgeluidsisiolatie van het geluidsscherm.',
                                                  owner=self)

        self._norm = OTLAttribuut(field=KlLEGCNorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.norm',
                                  definition='De proef volgens de beschreven standaard.',
                                  owner=self)

        self._testrapport = OTLAttribuut(field=DtcDocument,
                                         naam='testrapport',
                                         label='testrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.testrapport',
                                         usagenote='Bestanden van het type xlsx of pdf.',
                                         kardinaliteit_max='*',
                                         definition='Documentbijlage met de resultaten van de test.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlLEGCTestType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.type',
                                  definition='Het type van de test.',
                                  owner=self)

    @property
    def geluidsabsorptieReflectie(self) -> int:
        """De absorptie- of reflectiewaarde van het geluidsscherm als geheel getal."""
        return self._geluidsabsorptieReflectie.get_waarde()

    @geluidsabsorptieReflectie.setter
    def geluidsabsorptieReflectie(self, value):
        self._geluidsabsorptieReflectie.set_waarde(value, owner=self._parent)

    @property
    def gemetenWaarde(self) -> int:
        """De sterkte van het geluid in dB."""
        return self._gemetenWaarde.get_waarde()

    @gemetenWaarde.setter
    def gemetenWaarde(self, value):
        self._gemetenWaarde.set_waarde(value, owner=self._parent)

    @property
    def locatieInSitulabo(self) -> str:
        """Locatie waar de geluidstest is uitgevoerd (terrein of labo)."""
        return self._locatieInSitulabo.get_waarde()

    @locatieInSitulabo.setter
    def locatieInSitulabo(self, value):
        self._locatieInSitulabo.set_waarde(value, owner=self._parent)

    @property
    def luchtgeluidsisolatie(self) -> int:
        """De gemeten waarde van het luchtgeluidsisiolatie van het geluidsscherm."""
        return self._luchtgeluidsisolatie.get_waarde()

    @luchtgeluidsisolatie.setter
    def luchtgeluidsisolatie(self, value):
        self._luchtgeluidsisolatie.set_waarde(value, owner=self._parent)

    @property
    def norm(self) -> str:
        """De proef volgens de beschreven standaard."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self._parent)

    @property
    def testrapport(self) -> List[DtcDocumentWaarden]:
        """Documentbijlage met de resultaten van de test."""
        return self._testrapport.get_waarde()

    @testrapport.setter
    def testrapport(self, value):
        self._testrapport.set_waarde(value, owner=self._parent)

    @property
    def type(self) -> str:
        """Het type van de test."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGeluidstestRapport(ComplexField):
    """Complex datatype voor een verslag dat de resultaten van de geluidsmetingen weergeeft."""
    naam = 'DtcGeluidstestRapport'
    label = 'Geluidstest rapport'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport'
    definition = 'Complex datatype voor een verslag dat de resultaten van de geluidsmetingen weergeeft.'
    waardeObject = DtcGeluidstestRapportWaarden

    def __str__(self):
        return ComplexField.__str__(self)

