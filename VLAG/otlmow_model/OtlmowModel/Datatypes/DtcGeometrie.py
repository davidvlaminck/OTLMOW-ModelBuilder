# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGeometrieWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._gml = OTLAttribuut(field=StringField,
                                 naam='gml',
                                 label='als GML',
                                 objectUri='http://www.w3.org/ns/locn#Geometry.gml',
                                 definition='',
                                 owner=self)

        self._wkt = OTLAttribuut(field=StringField,
                                 naam='wkt',
                                 label='als WKT',
                                 objectUri='http://www.w3.org/ns/locn#Geometry.wkt',
                                 definition='',
                                 owner=self)

    @property
    def gml(self) -> str:
        """"""
        return self._gml.get_waarde()

    @gml.setter
    def gml(self, value):
        self._gml.set_waarde(value, owner=self._parent)

    @property
    def wkt(self) -> str:
        """"""
        return self._wkt.get_waarde()

    @wkt.setter
    def wkt(self, value):
        self._wkt.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGeometrie(ComplexField):
    """"""
    naam = 'DtcGeometrie'
    label = 'Geometrie'
    objectUri = 'http://www.w3.org/ns/locn#Geometry'
    definition = ''
    waardeObject = DtcGeometrieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

