import os
import sqlite3
from pathlib import Path


class SQLDbReader:
    """SQLDbReader performs read query's. It first checks if the provided path has a file. Provides an easy way to
    override querying for testing purposes. """

    def __init__(self, path: Path = None):
        if path is None or path == '':
            self.file_exists = False
        else:
            self.path = path.resolve()
            self.file_exists = os.path.isfile(self.path)
            if not self.file_exists:
                raise FileNotFoundError(str(self.path) + " is not a valid path. File does not exist.")

    def perform_read_query(self, query: str, params=None):
        if params is None:
            params = {}
        self.file_exists = os.path.isfile(self.path)
        if not self.file_exists:
            raise FileNotFoundError(str(self.path) + " is not a valid path. File does not exist.")

        with sqlite3.connect(self.path) as con:
            cur = con.cursor()
            data = [row for row in cur.execute(query, params)]
        return data
