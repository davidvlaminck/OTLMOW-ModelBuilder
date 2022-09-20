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
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class OSLOInMemoryCreator:
    def __init__(self, sql_db_reader: SQLDbReader):
        self.sqlDbReader = sql_db_reader

    def get_all_primitive_datatype_attributes(self) -> [OSLODatatypePrimitiveAttribuut]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, "
            "constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypePrimitiveAttributen ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLODatatypePrimitiveAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                               row[10], row[11], row[12])
            lijst.append(c)

        return lijst

    def get_all_primitive_datatypes(self) -> [OSLODatatypePrimitive]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypePrimitive ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLODatatypePrimitive(row[0], row[1], row[2], row[3], row[4], row[5])
            lijst.append(c)

        return lijst

    def get_all_classes(self) -> [OSLOClass]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            lijst.append(c)

        return lijst

    def get_class_by_uri(self, class_uri: str) -> OSLOClass:
        data = self.sqlDbReader.perform_read_query(
            "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version "
            "FROM OSLOClass WHERE uri=:uriclass",
            {"uriclass": class_uri})

        lijst = []
        for row in data:
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            lijst.append(c)

        if len(lijst) > 1:
            raise NotImplementedError(f'There should only be 1 class with this uri: {class_uri}')

        if len(lijst) == 1:
            return lijst[0]

    def get_attributes_by_class_uri(self, class_uri) -> [OSLOAttribuut]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version "
            "FROM OSLOAttributen WHERE class_uri=:uriclass AND overerving = 0 and name <> 'typeURI' "
            "ORDER BY uri",
            {"uriclass": class_uri})

        lijst = []
        for row in data:
            c = OSLOAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12])
            lijst.append(c)

        return lijst

    def get_all_attributes(self) -> [OSLOAttribuut]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version "
            "FROM OSLOAttributen WHERE overerving = 0 and name <> 'typeURI' ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLOAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12])
            lijst.append(c)

        return lijst

    def get_all_inheritances(self) -> [Inheritance]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT base_name, base_uri, class_uri, class_name, deprecated_version "
            "FROM InternalBaseClass ORDER BY base_uri, class_uri",
            {})

        lijst = []
        for row in data:
            c = Inheritance(row[0], row[1], row[2], row[3], row[4])
            lijst.append(c)

        return lijst

    def get_all_complex_datatypes(self) -> [OSLODatatypeComplex]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypeComplex ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLODatatypeComplex(row[0], row[1], row[2], row[3], row[4], row[5])
            lijst.append(c)

        return lijst

    def get_all_complex_datatype_attributes(self) -> [OSLODatatypeComplexAttribuut]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, "
            "constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypeComplexAttributen ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLODatatypeComplexAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                             row[10], row[11], row[12])
            lijst.append(c)

        return lijst

    def get_all_union_datatypes(self) -> [OSLODatatypeUnion]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypeUnion ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLODatatypeUnion(row[0], row[1], row[2], row[3], row[4], row[5])
            lijst.append(c)

        return lijst

    def get_all_union_datatype_attributes(self) -> [OSLODatatypeUnionAttribuut]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, "
            "constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypeUnionAttributen ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLODatatypeUnionAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                           row[10], row[11], row[12])
            lijst.append(c)

        return lijst

    def get_all_enumerations(self) -> [OSLOEnumeration]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT name, uri, usagenote_nl, definition_nl, label_nl, codelist, deprecated_version "
            "FROM OSLOEnumeration ORDER BY uri",
            {})

        lijst = []
        for row in data:
            c = OSLOEnumeration(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            lijst.append(c)

        return lijst

    def get_all_typelinks(self) -> [OSLOTypeLink]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT item_uri, item_tabel, deprecated_version FROM TypeLinkTabel ORDER BY item_uri",
            {})

        lijst = []
        for row in data:
            c = OSLOTypeLink(row[0], row[1], row[2])
            lijst.append(c)

        return lijst

    def get_all_relations(self) -> [OSLORelatie]:
        data = self.sqlDbReader.perform_read_query(
            "SELECT * FROM OSLORelaties ORDER BY uri, bron_uri, doel_uri",
            {})

        lijst = []
        for row in data:
            c = OSLORelatie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            lijst.append(c)

        return lijst

    def check_on_base_classes(self):
        data = self.sqlDbReader.perform_read_query(
            """WITH inh1 AS ( SELECT uri AS org_class_uri, CASE WHEN base_uri IS NULL THEN uri ELSE base_uri END AS 
            inheritsfrom FROM OSLOClass LEFT JOIN InternalBaseClass ON OSLOClass.uri = InternalBaseClass.class_uri WHERE 
            abstract = 0), inh2 AS ( SELECT org_class_uri, CASE WHEN base_uri IS NULL THEN inheritsfrom ELSE base_uri END AS 
            inheritsfrom FROM inh1 LEFT JOIN InternalBaseClass ON inh1.inheritsfrom = InternalBaseClass.class_uri), 
            inh3 AS ( SELECT org_class_uri, CASE WHEN base_uri IS NULL THEN inheritsfrom ELSE base_uri END AS inheritsfrom FROM 
            inh2 LEFT JOIN InternalBaseClass ON inh2.inheritsfrom = InternalBaseClass.class_uri), inh4 AS ( SELECT 
            org_class_uri, CASE WHEN base_uri IS NULL THEN inheritsfrom ELSE base_uri END AS inheritsfrom FROM inh3 LEFT JOIN 
            InternalBaseClass ON inh3.inheritsfrom = InternalBaseClass.class_uri), inh5 AS ( SELECT org_class_uri, 
            CASE WHEN base_uri IS NULL THEN inheritsfrom ELSE base_uri END AS inheritsfrom FROM inh4 LEFT JOIN 
            InternalBaseClass ON inh4.inheritsfrom = InternalBaseClass.class_uri), distinct_bases AS (SELECT DISTINCT 
            inheritsfrom AS uri FROM inh5), selected_bases AS (SELECT * FROM distinct_bases WHERE uri IN (
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject', 
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject','http://purl.org/dc/terms/Agent',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject')), check1 AS ( SELECT 
            distinct_bases.*, CASE WHEN class_uri IS NULL THEN uri ELSE class_uri END AS class_uri FROM distinct_bases LEFT 
            JOIN InternalBaseClass bases_1_up ON distinct_bases.uri = bases_1_up.base_uri WHERE distinct_bases.uri NOT IN (
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', 
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand')), check2 AS ( SELECT check1.uri, 
            base_uri AS class_uri FROM check1 LEFT JOIN InternalBaseClass inh_down ON check1.class_uri = inh_down.class_uri AND 
            check1.uri <> inh_down.base_uri AND base_uri NOT IN (
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', 
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand') WHERE base_uri IS NOT NULL AND 
            base_uri NOT IN (SELECT * FROM selected_bases)), check3 AS ( SELECT check2.uri, base_uri AS class_uri FROM check2 
            LEFT JOIN InternalBaseClass inh_down ON check2.class_uri = inh_down.class_uri AND check2.uri <> inh_down.base_uri 
            AND base_uri NOT IN ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', 
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand') WHERE base_uri IS NOT NULL AND 
            base_uri NOT IN (SELECT * FROM selected_bases)), check4 AS ( SELECT check3.uri, base_uri AS class_uri FROM check3 
            LEFT JOIN InternalBaseClass inh_down ON check3.class_uri = inh_down.class_uri AND check3.uri <> inh_down.base_uri 
            AND base_uri NOT IN ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', 
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand') WHERE base_uri IS NOT NULL AND 
            base_uri NOT IN (SELECT * FROM selected_bases)), check5 AS ( SELECT check4.uri, base_uri AS class_uri, 
            * FROM check4 LEFT JOIN InternalBaseClass inh_down ON check4.class_uri = inh_down.class_uri AND check4.uri <> 
            inh_down.base_uri AND base_uri NOT IN (
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', 
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand') WHERE base_uri IS NOT NULL AND 
            base_uri NOT IN (SELECT * FROM selected_bases)) SELECT count(*) FROM check5;""",
            {})

        return data[0][0]
