# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject


# Generated with LegacyClassCreator. To modify: extend, do not edit
class Decoder(LegacyObject):
    """Decoder camerabeelden (Legacy)
	Camera-uitrusting : Het betreft hier een video-decoder. Deze vormt eendigitale datastroom om tot een analoog videosignaal"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Decoder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
