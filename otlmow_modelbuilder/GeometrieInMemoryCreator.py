import os
import sqlite3
from pathlib import Path
from sqlite3 import Connection

from otlmow_modelbuilder.GeometrieType import GeometrieType


class GeometrieInMemoryCreator:
    def __init__(self, path: Path):
        self.connection: Connection
        self.path: Path = path
        if path is None or path == '':
            self.file_exists = False
        else:
            self.path = path.resolve()
            self.file_exists = os.path.isfile(self.path)
            if not self.file_exists:
                raise FileNotFoundError(str(self.path) + " is not a valid path. File does not exist.")

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

    def perform_read_query(self, query: str, params=None) -> [tuple]:
        if params is None:
            params = {}

        cur = self.connection.cursor()
        return [row for row in cur.execute(query, params)]

    def get_all_geometrie_types(self) -> [GeometrieType]:
        data = self.perform_read_query(query='SELECT * FROM GeometrieType')
        return [GeometrieType(row[0].replace('-test', ''), row[1], row[2], row[3], row[4], row[5], row[6])
                for row in data]


