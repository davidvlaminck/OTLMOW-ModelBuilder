from pathlib import Path
from typing import List

from otlmow_modelbuilder.NewOTLBaseClassNotImplemented import NewOTLBaseClassNotImplemented
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnion import OSLODatatypeUnion
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplex import OSLODatatypeComplex
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import OSLODatatypePrimitive
from otlmow_modelbuilder.SQLDataClasses.OSLOEnumeration import OSLOEnumeration
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLORelatie import OSLORelatie
from otlmow_modelbuilder.SQLDataClasses.OSLOTypeLink import OSLOTypeLink


class OSLOCollector:
    def __init__(self, path: Path):
        self.path = path

        self.inheritances: [Inheritance] = None
        self.attributes: [OSLOAttribuut] = None
        self.classes: [OSLOClass] = None
        self.primitive_datatypes: [OSLODatatypePrimitive] = None
        self.primitive_datatype_attributen: [OSLODatatypePrimitiveAttribuut] = None
        self.complex_datatypes: [OSLODatatypeComplex] = None
        self.complex_datatype_attributen: [OSLODatatypeComplexAttribuut] = None
        self.union_datatypes: [OSLODatatypeUnion] = None
        self.union_datatype_attributen: [OSLODatatypeUnionAttribuut] = None
        self.enumerations: [OSLOEnumeration] = None
        self.typeLinks: [OSLOTypeLink] = None
        self.relations: [OSLORelatie] = None

    def collect_all(self, include_abstract: bool = False) -> None:
        with OSLOInMemoryCreator(self.path) as memory_creator:
            self.classes = memory_creator.get_all_classes()
            self.attributes = memory_creator.get_all_attributes(include_abstract=include_abstract)
            self.inheritances = memory_creator.get_all_inheritances()
            self.primitive_datatypes = memory_creator.get_all_primitive_datatypes()
            self.primitive_datatype_attributen = memory_creator.get_all_primitive_datatype_attributes()
            self.complex_datatypes = memory_creator.get_all_complex_datatypes()
            self.complex_datatype_attributen = memory_creator.get_all_complex_datatype_attributes()
            self.union_datatypes = memory_creator.get_all_union_datatypes()
            self.union_datatype_attributen = memory_creator.get_all_union_datatype_attributes()
            self.enumerations = memory_creator.get_all_enumerations()
            self.typeLinks = memory_creator.get_all_typelinks()
            self.relations = memory_creator.get_all_relations()

    def find_attributes_by_class(self, oslo_class: OSLOClass) -> [OSLOAttribuut]:
        if oslo_class is None:
            return []
        return sorted(list(filter(lambda c: c.class_uri == oslo_class.objectUri, self.attributes)),
                      key=lambda a: a.objectUri)

    def find_inheritances_by_class(self, oslo_class: OSLOClass) -> [Inheritance]:
        if oslo_class is None:
            return []
        return self.find_inheritances_by_class_uri(oslo_class.objectUri)

    def find_inheritances_by_class_uri(self, oslo_class_uri: str) -> [Inheritance]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []
        return sorted(list(filter(lambda c: c.class_uri == oslo_class_uri, self.inheritances)),
                      key=lambda c: c.base_uri)

    def find_all_indirect_inheritances_by_class_uri(self, oslo_class_uri: str) -> [Inheritance]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []

        inheritance_list = []
        direct_inheritances = self.find_inheritances_by_class_uri(oslo_class_uri)
        if len(direct_inheritances) == 0:
            return inheritance_list

        inheritance_list.extend(direct_inheritances)
        for direct in direct_inheritances:
            inheritance_list.extend(self.find_all_indirect_inheritances_by_class_uri(direct.class_uri))

        return sorted(inheritance_list, key=lambda c: c.base_uri)

    def find_superclasses_uri_by_class_uri(self, oslo_class_uri: str) -> [str]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []

        inheritances = list(filter(lambda i: i.base_uri == oslo_class_uri, self.inheritances))
        return sorted(list(map(lambda c: c.class_uri, inheritances)))

    def find_indirect_superclasses_uri_by_class_uri(self, oslo_class_uri: str) -> [str]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []

        superclass_list = []
        direct_superclasses = self.find_superclasses_uri_by_class_uri(oslo_class_uri)
        if len(direct_superclasses) == 0:
            return superclass_list

        superclass_list.extend(direct_superclasses)
        for direct in direct_superclasses:
            superclass_list.extend(self.find_indirect_superclasses_uri_by_class_uri(direct))

        return sorted(superclass_list)

    def find_class_by_uri(self, uri: str) -> OSLOClass:
        return next((p for p in self.classes if p.objectUri == uri), None)

    def find_primitive_datatype_by_uri(self, uri: str) -> OSLODatatypePrimitive:
        return next((p for p in self.primitive_datatypes if p.objectUri == uri), None)

    def find_primitive_datatype_attributes_by_class_uri(self, class_uri: str) -> List[OSLODatatypePrimitiveAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.primitive_datatype_attributen)),
                      key=lambda p: p.objectUri)

    def find_complex_datatype_by_uri(self, uri) -> OSLODatatypeComplex:
        return next((p for p in self.complex_datatypes if p.objectUri == uri), None)

    def find_complex_datatype_attributes_by_class_uri(self, class_uri: str) -> List[OSLODatatypeComplexAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.complex_datatype_attributen)),
                      key=lambda p: p.objectUri)

    def find_union_datatype_by_uri(self, uri) -> OSLODatatypeUnion:
        return next((p for p in self.union_datatypes if p.objectUri == uri), None)

    def find_union_datatype_attributes_by_class_uri(self, class_uri: str) -> List[OSLODatatypeUnionAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.union_datatype_attributen)),
                      key=lambda p: p.objectUri)

    def find_enumeration_by_uri(self, uri) -> OSLOEnumeration:
        return next((p for p in self.enumerations if p.objectUri == uri), None)

    def find_type_link_by_uri(self, type_uri: str) -> OSLOTypeLink:
        return next((p for p in self.typeLinks if p.item_uri == type_uri), None)

    def find_outgoing_relations(self, objectUri: str) -> [OSLORelatie]:
        return sorted(list(filter(lambda r: r.bron_uri == objectUri and r.bron_overerving == ''
                                            and r.doel_overerving == '', self.relations)), key=lambda r: r.objectUri)

    def query_correct_base_classes(self) -> None:
        with OSLOInMemoryCreator(self.path) as memory_creator:
            result_uris = memory_creator.check_on_base_classes()
            if len(result_uris) != 0:
                raise NewOTLBaseClassNotImplemented()
