# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Encoder(LegacyObject):
    """Encoder (Legacy)
	Camera-uitrusting : Het betreft hier een video-encoder. Deze vormt een analoog videosignaal om tot een digitale datastroom"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Encoder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
