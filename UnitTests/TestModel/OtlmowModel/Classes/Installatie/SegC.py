# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class SegC(LegacyObject):
    """Segment controller (Legacy)
	Controller die zorgt voor de bewaking en bediening van verlichtingssegmenten per paal en aldus zorgt voor de communicatie tussen de cabine en de armatuurcontrollers."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SegC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
