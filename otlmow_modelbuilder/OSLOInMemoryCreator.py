import os
import sqlite3
from pathlib import Path
from sqlite3 import Connection

from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplex import OSLODatatypeComplex
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import OSLODatatypePrimitive
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnion import OSLODatatypeUnion
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOEnumeration import OSLOEnumeration
from otlmow_modelbuilder.SQLDataClasses.OSLORelatie import OSLORelatie
from otlmow_modelbuilder.SQLDataClasses.OSLOTypeLink import OSLOTypeLink


class OSLOInMemoryCreator:
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

    def get_otl_version(self) -> str:
        data = self.perform_read_query("SELECT Waarde FROM GeneralInfo WHERE Parameter = 'Version'")

        if len(data) == 0:
            return None

        return data[0][0]

    def get_all_primitive_datatype_attributes(self) -> [OSLODatatypePrimitiveAttribuut]:
        data = self.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, "
            "overerving, constraints, readonly, usagenote_nl, deprecated_version "
            "FROM OSLODatatypePrimitiveAttributen "
            "ORDER BY uri")

        return [OSLODatatypePrimitiveAttribuut(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            for row in data]

    def get_all_primitive_datatypes(self) -> [OSLODatatypePrimitive]:
        data = self.perform_read_query(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version "
            "FROM OSLODatatypePrimitive "
            "ORDER BY uri")

        return [OSLODatatypePrimitive(row[0], row[1], row[2], row[3], row[4], row[5]) for row in data]

    def get_all_classes(self) -> [OSLOClass]:
        data = self.perform_read_query(
            "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version "
            "FROM OSLOClass "
            "ORDER BY uri")

        return [OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in data]

    def get_class_by_uri(self, class_uri: str) -> OSLOClass:
        data = self.perform_read_query(
            query="SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version "
                  "FROM OSLOClass "
                  "WHERE uri=:uriclass",
            params={"uriclass": class_uri})

        class_results = [OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in data]

        if len(class_results) > 1:
            raise ValueError(f'There should only be 1 class with this uri: {class_uri}')

        if len(class_results) == 1:
            return class_results[0]

    def get_attributes_by_class_uri(self, class_uri, include_abstract=False) -> [OSLOAttribuut]:
        overerving_in_query = ''
        if not include_abstract:
            overerving_in_query = 'overerving = 0 AND '
        data = self.perform_read_query(
            query="SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, "
                  "overerving, constraints, readonly, usagenote_nl, deprecated_version "
                  f"FROM OSLOAttributen WHERE class_uri=:uriclass AND {overerving_in_query}name <> 'typeURI' "
                  "ORDER BY uri",
            params={"uriclass": class_uri})

        return [OSLOAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12]) for row in data]

    def get_all_attributes(self, include_abstract=False) -> [OSLOAttribuut]:
        overerving_in_query = ''
        if not include_abstract:
            overerving_in_query = 'overerving = 0 AND '
        data = self.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, "
            "overerving, constraints, readonly, usagenote_nl, deprecated_version "
            f"FROM OSLOAttributen WHERE {overerving_in_query}name <> 'typeURI' "
            f"ORDER BY uri")

        return [OSLOAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12]) for row in data]

    def get_all_inheritances(self) -> [Inheritance]:
        data = self.perform_read_query(
            "SELECT base_name, base_uri, class_uri, class_name, deprecated_version "
            "FROM InternalBaseClass "
            "ORDER BY base_uri, class_uri")

        return [Inheritance(row[0], row[1], row[2], row[3], row[4]) for row in data]

    def get_all_complex_datatypes(self) -> [OSLODatatypeComplex]:
        data = self.perform_read_query(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version "
            "FROM OSLODatatypeComplex "
            "ORDER BY uri")

        return [OSLODatatypeComplex(row[0], row[1], row[2], row[3], row[4], row[5]) for row in data]

    def get_all_complex_datatype_attributes(self) -> [OSLODatatypeComplexAttribuut]:
        data = self.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, "
            "overerving, constraints, readonly, usagenote_nl, deprecated_version "
            "FROM OSLODatatypeComplexAttributen "
            "ORDER BY uri")

        return [OSLODatatypeComplexAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                             row[9], row[10], row[11], row[12]) for row in data]

    def get_all_union_datatypes(self) -> [OSLODatatypeUnion]:
        data = self.perform_read_query(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version "
            "FROM OSLODatatypeUnion "
            "ORDER BY uri")

        return [OSLODatatypeUnion(row[0], row[1], row[2], row[3], row[4], row[5]) for row in data]

    def get_all_union_datatype_attributes(self) -> [OSLODatatypeUnionAttribuut]:
        data = self.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, "
            "overerving, constraints, readonly, usagenote_nl, deprecated_version "
            "FROM OSLODatatypeUnionAttributen "
            "ORDER BY uri")

        return [OSLODatatypeUnionAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                           row[9], row[10], row[11], row[12]) for row in data]

    def get_all_enumerations(self) -> [OSLOEnumeration]:
        data = self.perform_read_query(
            "SELECT name, uri, usagenote_nl, definition_nl, label_nl, codelist, deprecated_version "
            "FROM OSLOEnumeration "
            "ORDER BY uri")

        return [OSLOEnumeration(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in data]

    def get_all_typelinks(self) -> [OSLOTypeLink]:
        data = self.perform_read_query(
            "SELECT item_uri, item_tabel, deprecated_version "
            "FROM TypeLinkTabel "
            "ORDER BY item_uri")

        return [OSLOTypeLink(row[0], row[1], row[2]) for row in data]

    def get_all_relations(self) -> [OSLORelatie]:
        data = self.perform_read_query(
            "SELECT * "
            "FROM OSLORelaties "
            "ORDER BY uri, bron_uri, doel_uri")

        return [OSLORelatie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in data]

    def check_on_base_classes(self):
        data = self.perform_read_query(
            """
WITH valid_base_classes AS (
	VALUES ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'),
		('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject'),
        ('http://purl.org/dc/terms/Agent'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject')),    
concrete_classes AS (
	SELECT uri AS concrete_uri
	FROM OSLOClass o
	WHERE abstract = 0 AND concrete_uri NOT IN valid_base_classes),
inheritance_checks AS (
	SELECT concrete_uri, 
		 CASE WHEN inh7.base_uri IS NOT NULL AND inh7.base_uri IN valid_base_classes THEN 1
		 	WHEN inh6.base_uri IS NOT NULL AND inh6.base_uri IN valid_base_classes THEN 1
		 	WHEN inh5.base_uri IS NOT NULL AND inh5.base_uri IN valid_base_classes THEN 1
		 	WHEN inh4.base_uri IS NOT NULL AND inh4.base_uri IN valid_base_classes THEN 1
		 	WHEN inh3.base_uri IS NOT NULL AND inh3.base_uri IN valid_base_classes THEN 1
		 	WHEN inh2.base_uri IS NOT NULL AND inh2.base_uri IN valid_base_classes THEN 1
		 	WHEN inh1.base_uri IS NOT NULL AND inh1.base_uri IN valid_base_classes THEN 1
		 	ELSE 0 END has_valid_base
	FROM concrete_classes
		LEFT JOIN InternalBaseClass inh1 ON concrete_classes.concrete_uri = inh1.class_uri
		LEFT JOIN InternalBaseClass inh2 ON inh1.base_uri = inh2.class_uri
		LEFT JOIN InternalBaseClass inh3 ON inh2.base_uri = inh3.class_uri
		LEFT JOIN InternalBaseClass inh4 ON inh3.base_uri = inh4.class_uri
		LEFT JOIN InternalBaseClass inh5 ON inh4.base_uri = inh5.class_uri
		LEFT JOIN InternalBaseClass inh6 ON inh5.base_uri = inh6.class_uri
		LEFT JOIN InternalBaseClass inh7 ON inh6.base_uri = inh7.class_uri)
SELECT concrete_uri -- concrete_uri to view the list of classes that do not have a valid base class 
FROM inheritance_checks GROUP BY 1 HAVING sum(has_valid_base) = 0;""")
        if len(data) == 0:
            return []

        return data[0][0]
