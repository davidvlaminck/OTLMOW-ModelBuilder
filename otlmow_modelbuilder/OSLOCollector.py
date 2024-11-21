from pathlib import Path
from typing import List, Optional

from otlmow_modelbuilder.NewOTLBaseClassNotImplemented import NewOTLBaseClassNotImplemented
from otlmow_modelbuilder.SQLDataClasses.GeneralInfoRecord import GeneralInfoRecord
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
        self.general_info: [GeneralInfoRecord] = None

        self.class_dict: Optional[dict] = None

    def collect_all(self, include_abstract: bool = False) -> None:
        self.class_dict = {}
        with OSLOInMemoryCreator(self.path) as memory_creator:
            self.classes, self.class_dict = memory_creator.get_all_classes_and_class_dict()
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
            self.general_info = memory_creator.get_general_info()

    def find_attributes_by_class(self, oslo_class: OSLOClass) -> [OSLOAttribuut]:
        if oslo_class is None:
            return []

        return sorted((a for a in self.attributes if a.class_uri == oslo_class.objectUri),
                      key=lambda a: a.objectUri)

    def find_inheritances_by_class(self, oslo_class: OSLOClass) -> [Inheritance]:
        if oslo_class is None:
            return []
        return self.find_inheritances_by_class_uri(oslo_class.objectUri)

    def find_inheritances_by_class_uri(self, oslo_class_uri: str) -> [Inheritance]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []

        return sorted((i for i in self.inheritances if i.class_uri == oslo_class_uri),
                      key=lambda i: i.base_uri)

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

    def find_subclasses_uri_by_class_uri(self, oslo_class_uri: str) -> [str]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []

        return sorted((i.class_uri for i in self.inheritances if i.base_uri == oslo_class_uri))

    def find_indirect_subclasses_uri_by_class_uri(self, oslo_class_uri: str) -> [str]:
        if oslo_class_uri is None or oslo_class_uri == '':
            return []

        superclass_list = []
        direct_superclasses = self.find_subclasses_uri_by_class_uri(oslo_class_uri)
        if len(direct_superclasses) == 0:
            return superclass_list

        superclass_list.extend(direct_superclasses)
        for direct in direct_superclasses:
            superclass_list.extend(self.find_indirect_subclasses_uri_by_class_uri(direct))

        return sorted(superclass_list)

    def find_class_by_uri(self, uri: str) -> OSLOClass:
        return next((p for p in self.classes if p.objectUri == uri), None)

    def find_primitive_datatype_by_uri(self, uri: str) -> OSLODatatypePrimitive:
        return next((p for p in self.primitive_datatypes if p.objectUri == uri), None)

    def find_primitive_datatype_attributes_by_class_uri(self, class_uri: str) -> List[OSLODatatypePrimitiveAttribuut]:
        return sorted((p for p in self.primitive_datatype_attributen if p.class_uri == class_uri),
                      key=lambda p: p.objectUri)

    def find_complex_datatype_by_uri(self, uri) -> OSLODatatypeComplex:
        return next((p for p in self.complex_datatypes if p.objectUri == uri), None)

    def find_complex_datatype_attributes_by_class_uri(self, class_uri: str) -> List[OSLODatatypeComplexAttribuut]:
        return sorted((p for p in self.complex_datatype_attributen if p.class_uri == class_uri),
                      key=lambda p: p.objectUri)

    def find_union_datatype_by_uri(self, uri) -> OSLODatatypeUnion:
        return next((p for p in self.union_datatypes if p.objectUri == uri), None)

    def find_union_datatype_attributes_by_class_uri(self, class_uri: str) -> List[OSLODatatypeUnionAttribuut]:
        return sorted((p for p in self.union_datatype_attributen if p.class_uri == class_uri),
                      key=lambda p: p.objectUri)

    def find_enumeration_by_uri(self, uri) -> OSLOEnumeration:
        return next((p for p in self.enumerations if p.objectUri == uri), None)

    def find_type_link_by_uri(self, type_uri: str) -> OSLOTypeLink:
        return next((p for p in self.typeLinks if p.item_uri == type_uri), None)

    def find_outgoing_relations(self, objectUri: str) -> [OSLORelatie]:
        return sorted((r for r in self.relations if r.bron_uri == objectUri and r.bron_overerving == ''
                       and r.doel_overerving == ''), key=lambda r: r.objectUri)

    def find_all_relations(self, objectUri: str, allow_duplicates: bool = False) -> [OSLORelatie]:
        """finds all relations, given an objectUri, where the object is either the source or the target of the relation.
        allow_duplicates is relevant for unidirectional relations, as the relation would be included twice:
        once where objectUri is the source and once where objectUri is the target. If allow_duplicates is False,
        only the relation where objectUri is the source is returned."""
        all_relations = [r for r in self.relations if (r.bron_uri == objectUri or r.doel_uri == objectUri)
                         and r.bron_overerving == '' and r.doel_overerving == '']
        if allow_duplicates:
            return sorted(all_relations, key=lambda r: r.objectUri)
        else:
            return sorted((r for r in all_relations
                           if r.richting == 'Unspecified' and r.bron_uri == objectUri or r.richting != 'Unspecified'),
                          key=lambda r: r.objectUri)

    def query_correct_base_classes(self) -> None:
        with OSLOInMemoryCreator(self.path) as memory_creator:
            result_uris = memory_creator.check_on_base_classes()
            if len(result_uris) != 0:
                print('The following classes are not using the correct base classes:')
                print(result_uris)
                raise NewOTLBaseClassNotImplemented()

    def find_all_concrete_relations(self, objectUri: str, allow_duplicates: bool = False) -> [OSLORelatie]:
        class_ = self.find_class_by_uri(objectUri)
        if class_ is None:
            raise ValueError(f'Class with uri {objectUri} does not exist.')
        if class_.abstract == 1:
            raise ValueError(f'Class with uri {objectUri} is an abstract class.')

        all_relations = [r for r in self.relations if (r.bron_uri == objectUri or r.doel_uri == objectUri)
                         and self.class_dict[r.bron_uri].abstract == 0 and self.class_dict[r.doel_uri].abstract == 0]

        if allow_duplicates:
            return sorted(all_relations, key=lambda r: r.objectUri)
        else:
            return sorted((r for r in all_relations
                           if (r.richting == 'Unspecified' and
                               (r.bron_uri == objectUri or r.bron_overerving == objectUri))
                           or r.richting != 'Unspecified'),
                           key=lambda r: r.objectUri)
