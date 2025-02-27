# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcGrondbijmenging import DtcGrondbijmenging, DtcGrondbijmengingWaarden
from ..Datatypes.KlGrondHoofdnaamCode import KlGrondHoofdnaamCode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondsoortWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bijmenging = OTLAttribuut(field=DtcGrondbijmenging,
                                        naam='bijmenging',
                                        label='bijmenging',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondsoort.bijmenging',
                                        usagenote='https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdHoofdnaamCodesEnumType)',
                                        kardinaliteit_max='3',
                                        definition='Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                        owner=self)

        self._hoofdnaamcode = OTLAttribuut(field=KlGrondHoofdnaamCode,
                                           naam='hoofdnaamcode',
                                           label='hoofdnaamcode',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondsoort.hoofdnaamcode',
                                           usagenote='https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/interpretatie/GecodeerdeLithologieDataCodes.xsd  (GecodeerdHoofdnaamCodesEnumType)',
                                           definition='Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                           owner=self)

    @property
    def bijmenging(self) -> List[DtcGrondbijmengingWaarden]:
        """Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._bijmenging.get_waarde()

    @bijmenging.setter
    def bijmenging(self, value):
        self._bijmenging.set_waarde(value, owner=self._parent)

    @property
    def hoofdnaamcode(self) -> str:
        """Lithologisch hoofdbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._hoofdnaamcode.get_waarde()

    @hoofdnaamcode.setter
    def hoofdnaamcode(self, value):
        self._hoofdnaamcode.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondsoort(ComplexField):
    """Complex datatype om het soort grond te bepalen."""
    naam = 'DtcGrondsoort'
    label = 'Grondsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondsoort'
    definition = 'Complex datatype om het soort grond te bepalen.'
    waardeObject = DtcGrondsoortWaarden

    def __str__(self):
        return ComplexField.__str__(self)

