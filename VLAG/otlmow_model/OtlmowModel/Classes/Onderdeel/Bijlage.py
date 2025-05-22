# coding=utf-8
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bijlage(AbstracteAanvullendeGeometrie, GeenGeometrie):
    """Een bestand (document,afbeelding,...) dat behoort tot 1 of meerdere assets."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bijlage'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBijlage', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBijlage', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#VLAGAIMObject', direction='i')  # i = direction: incoming
