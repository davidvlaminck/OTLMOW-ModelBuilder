from otlmow_modelbuilder.GeometrieType import GeometrieType
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class GeometrieInMemoryCreator:
    def __init__(self, sQLDbReader: SQLDbReader):
        self.sqlDbReader = sQLDbReader

    def get_all_geometrie_types(self) -> [GeometrieType]:
        data = self.sqlDbReader.performReadQuery(
            'SELECT * FROM GeometrieType', {})

        lijst = []
        for row in data:
            c = GeometrieType(row[0].replace('-test', ''), row[1], row[2], row[3], row[4], row[5], row[6])
            lijst.append(c)

        return lijst

