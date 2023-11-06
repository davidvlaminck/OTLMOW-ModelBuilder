from pathlib import Path
from typing import Type, Union

from otlmow_modelbuilder.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from otlmow_modelbuilder.GeometrieType import GeometrieType


class GeometrieArtefactCollector:
    def __init__(self, path: Path):
        self.path = path

        self.geometrie_types: [GeometrieType] = None

    def collect_all(self):
        with GeometrieInMemoryCreator(self.path) as memory_creator:
            self.geometrie_types = memory_creator.get_all_geometrie_types()

    def find_by_objectUri(self, objectUri: str) -> Union[Type[GeometrieType], None]:
        result = list(filter(lambda g: g.objectUri == objectUri, self.geometrie_types))
        if len(result) == 0:
            return None
        return result[0]

