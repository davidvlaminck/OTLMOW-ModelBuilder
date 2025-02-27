# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlGrondBijmengingHoeveelheidCode import KlGrondBijmengingHoeveelheidCode
from ..Datatypes.KlGrondHoofdnaamCode import KlGrondHoofdnaamCode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondbijmengingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bijmengingshoofdnaamcode = OTLAttribuut(field=KlGrondHoofdnaamCode,
                                                      naam='bijmengingshoofdnaamcode',
                                                      label='bijmengingshoofdnaamcode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging.bijmengingshoofdnaamcode',
                                                      usagenote='https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdHoofdnaamCodesEnumType)',
                                                      definition='Lithologisch nevenbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                                      owner=self)

        self._hoeveelheidscode = OTLAttribuut(field=KlGrondBijmengingHoeveelheidCode,
                                              naam='hoeveelheidscode',
                                              label='hoeveelheidscode',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging.hoeveelheidscode',
                                              usagenote=' https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdBijmengingHoeveelheidEnumType)',
                                              definition='Aanduiding (als code) van de hoeveelheid bijmenging.',
                                              owner=self)

        self._isPlaatselijk = OTLAttribuut(field=BooleanField,
                                           naam='isPlaatselijk',
                                           label='is grondmenging plaatselijk',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging.isPlaatselijk',
                                           definition='Grondbijmenging plaatselijk of niet-plaatselijk.',
                                           owner=self)

    @property
    def bijmengingshoofdnaamcode(self) -> str:
        """Lithologisch nevenbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._bijmengingshoofdnaamcode.get_waarde()

    @bijmengingshoofdnaamcode.setter
    def bijmengingshoofdnaamcode(self, value):
        self._bijmengingshoofdnaamcode.set_waarde(value, owner=self._parent)

    @property
    def hoeveelheidscode(self) -> str:
        """Aanduiding (als code) van de hoeveelheid bijmenging."""
        return self._hoeveelheidscode.get_waarde()

    @hoeveelheidscode.setter
    def hoeveelheidscode(self, value):
        self._hoeveelheidscode.set_waarde(value, owner=self._parent)

    @property
    def isPlaatselijk(self) -> bool:
        """Grondbijmenging plaatselijk of niet-plaatselijk."""
        return self._isPlaatselijk.get_waarde()

    @isPlaatselijk.setter
    def isPlaatselijk(self, value):
        self._isPlaatselijk.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondbijmenging(ComplexField):
    """Complex datatype om extra informatie van de bijmenging van grond te capteren."""
    naam = 'DtcGrondbijmenging'
    label = 'Grondbijmenging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondbijmenging'
    definition = 'Complex datatype om extra informatie van de bijmenging van grond te capteren.'
    waardeObject = DtcGrondbijmengingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

