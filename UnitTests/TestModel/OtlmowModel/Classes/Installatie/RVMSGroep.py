# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class RVMSGroep(LegacyObject):
    """RVMS groep (Legacy)
	Groep van RVMS-borden (rijwegvariabele geografische route-informatiepanelen)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RVMSGroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
