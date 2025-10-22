import itertools
from collections import defaultdict, deque
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

        self.inheritances: list[Inheritance] = None
        self.attributes: list[OSLOAttribuut] = None
        self.classes: list[OSLOClass] = None
        self.primitive_datatypes: list[OSLODatatypePrimitive] = None
        self.primitive_datatype_attributen: list[OSLODatatypePrimitiveAttribuut] = None
        self.complex_datatypes: list[OSLODatatypeComplex] = None
        self.complex_datatype_attributen: list[OSLODatatypeComplexAttribuut] = None
        self.union_datatypes: list[OSLODatatypeUnion] = None
        self.union_datatype_attributen: list[OSLODatatypeUnionAttribuut] = None
        self.enumerations: list[OSLOEnumeration] = None
        self.typeLinks: list[OSLOTypeLink] = None
        self.relations: list[OSLORelatie] = None
        self.general_info: list[GeneralInfoRecord] = None

        self.class_dict: Optional[dict] = None
        self.inheritance_map: Optional[dict] = None

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

    def find_attributes_by_class(self, oslo_class: OSLOClass, sort_by_uri: bool = True) -> list[OSLOAttribuut]:
        if oslo_class is None:
            return []
        
        if sort_by_uri:
            return sorted((a for a in self.attributes if a.class_uri == oslo_class.objectUri),
                          key=lambda a: a.objectUri)
        return [a for a in self.attributes if a.class_uri == oslo_class.objectUri]

    def find_inheritances_by_class(self, oslo_class: OSLOClass, sort_by_uri: bool = True) -> list[Inheritance]:
        if oslo_class is None:
            return []
        return self.find_inheritances_by_class_uri(oslo_class.objectUri, sort_by_uri=sort_by_uri)

    def find_inheritances_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True) -> list[Inheritance]:
        if oslo_class_uri is None or not oslo_class_uri:
            return []

        if sort_by_uri:
            return sorted((i for i in self.inheritances if i.class_uri == oslo_class_uri),
                      key=lambda i: i.base_uri)
        return [i for i in self.inheritances if i.class_uri == oslo_class_uri]

    def find_all_indirect_inheritances_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True
                                                    ) -> list[Inheritance]:
        if oslo_class_uri is None or not oslo_class_uri:
            return []

        direct_inheritances = self.find_inheritances_by_class_uri(oslo_class_uri)
        if len(direct_inheritances) == 0:
            return []

        inheritance_list = []
        inheritance_list.extend(direct_inheritances)
        for direct in direct_inheritances:
            inheritance_list.extend(self.find_all_indirect_inheritances_by_class_uri(direct.class_uri))
        
        if sort_by_uri:
            return sorted(inheritance_list, key=lambda c: c.base_uri)
        return inheritance_list

    def find_subclasses_uri_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True) -> list[str]:
        if oslo_class_uri is None or not oslo_class_uri:
            return []

        if sort_by_uri:
            return sorted((i.class_uri for i in self.inheritances if i.base_uri == oslo_class_uri),
                          key=lambda uri: uri)

        return [i.class_uri for i in self.inheritances if i.base_uri == oslo_class_uri]

    def find_indirect_subclasses_uri_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True) -> list[str]:
        if oslo_class_uri is None or not oslo_class_uri:
            return []

        superclass_list = []
        direct_superclasses = self.find_subclasses_uri_by_class_uri(oslo_class_uri)
        if len(direct_superclasses) == 0:
            return superclass_list

        superclass_list.extend(direct_superclasses)
        for direct in direct_superclasses:
            superclass_list.extend(self.find_indirect_subclasses_uri_by_class_uri(direct))

        return sorted(superclass_list) if sort_by_uri else superclass_list

    def find_class_by_uri(self, uri: str) -> OSLOClass:
        return next((p for p in self.classes if p.objectUri == uri), None)

    def find_primitive_datatype_by_uri(self, uri: str) -> OSLODatatypePrimitive:
        return next((p for p in self.primitive_datatypes if p.objectUri == uri), None)

    def find_primitive_datatype_attributes_by_class_uri(self, class_uri: str, sort_by_uri: bool = True
                                                        ) -> List[OSLODatatypePrimitiveAttribuut]:
        if sort_by_uri:
            return sorted((p for p in self.primitive_datatype_attributen if p.class_uri == class_uri),
                          key=lambda p: p.objectUri)
        return [p for p in self.primitive_datatype_attributen if p.class_uri == class_uri]

    def find_complex_datatype_by_uri(self, uri) -> OSLODatatypeComplex:
        return next((p for p in self.complex_datatypes if p.objectUri == uri), None)

    def find_complex_datatype_attributes_by_class_uri(self, class_uri: str, sort_by_uri: bool = True
                                                      ) -> List[OSLODatatypeComplexAttribuut]:
        if sort_by_uri:
            return sorted((p for p in self.complex_datatype_attributen if p.class_uri == class_uri),
                          key=lambda p: p.objectUri)
        return [p for p in self.complex_datatype_attributen if p.class_uri == class_uri]

    def find_union_datatype_by_uri(self, uri) -> OSLODatatypeUnion:
        return next((p for p in self.union_datatypes if p.objectUri == uri), None)

    def find_union_datatype_attributes_by_class_uri(self, class_uri: str, sort_by_uri: bool = True
                                                    ) -> List[OSLODatatypeUnionAttribuut]:
        if sort_by_uri:
            return sorted((p for p in self.union_datatype_attributen if p.class_uri == class_uri),
                          key=lambda p: p.objectUri)
        return [p for p in self.union_datatype_attributen if p.class_uri == class_uri]

    def find_enumeration_by_uri(self, uri) -> OSLOEnumeration:
        return next((p for p in self.enumerations if p.objectUri == uri), None)

    def find_enumeration_by_codelist(self, uri) -> OSLOEnumeration:
        return next((p for p in self.enumerations if p.codelist == uri), None)

    def find_type_link_by_uri(self, type_uri: str) -> OSLOTypeLink:
        return next((p for p in self.typeLinks if p.item_uri == type_uri), None)

    def find_outgoing_relations(self, objectUri: str, sort_by_uri: bool = True) -> list[OSLORelatie]:
        if sort_by_uri:
            return sorted((r for r in self.relations if r.bron_uri == objectUri and r.bron_overerving == ''
                           and r.doel_overerving == ''), key=lambda r: r.objectUri)
        return [r for r in self.relations if r.bron_uri == objectUri and r.bron_overerving == ''
                and r.doel_overerving == '']

    def find_all_relations(self, objectUri: str, allow_duplicates: bool = False, sort_by_uri: bool = True
                           ) -> [OSLORelatie]:
        """finds all relations, given an objectUri, where the object is either the source or the target of the relation.
        allow_duplicates is relevant for unidirectional relations, as the relation would be included twice:
        once where objectUri is the source and once where objectUri is the target. If allow_duplicates is False,
        only the relation where objectUri is the source is returned."""
        all_relations = [r for r in self.relations if (r.bron_uri == objectUri or r.doel_uri == objectUri)
                         and r.bron_overerving == '' and r.doel_overerving == '']
        if allow_duplicates:
            return sorted(all_relations, key=lambda r: r.objectUri) if sort_by_uri else all_relations
        filtered = [
            r for r in all_relations
            if (r.richting == 'Unspecified' and r.bron_uri == objectUri) or r.richting != 'Unspecified'
        ]
        return sorted(filtered, key=lambda r: r.objectUri) if sort_by_uri else filtered

    def query_correct_base_classes(self, valid_base_class_uris: [str] = None) -> None:
        if valid_base_class_uris is None:
            valid_base_class_uris = []
        with OSLOInMemoryCreator(self.path) as memory_creator:
            result_uris = memory_creator.check_on_base_classes(valid_base_class_uris=valid_base_class_uris)
            if len(result_uris) != 0:
                print('The following classes are not using the correct base classes:')
                print(result_uris)
                raise NewOTLBaseClassNotImplemented()

    def find_all_concrete_relations(self, objectUri: str, allow_duplicates: bool = False, sort_by_uri: bool = True
                                    ) -> list[OSLORelatie]:
        class_ = self.find_class_by_uri(objectUri)
        if class_ is None:
            raise ValueError(f'Class with uri {objectUri} does not exist.')
        if class_.abstract == 1:
            raise ValueError(f'Class with uri {objectUri} is an abstract class.')

        all_relations = [r for r in self.relations if (r.bron_uri == objectUri or r.doel_uri == objectUri)
                         and self.class_dict[r.bron_uri].abstract == 0 and self.class_dict[r.doel_uri].abstract == 0]

        if allow_duplicates:
            return sorted(all_relations, key=lambda r: r.objectUri) if sort_by_uri else all_relations
        filtered = [
            r for r in all_relations
            if (r.richting == 'Unspecified' and (r.bron_uri == objectUri or r.bron_overerving == objectUri))
            or r.richting != 'Unspecified'
        ]
        return sorted(filtered, key=lambda r: r.objectUri) if sort_by_uri else filtered

    @classmethod
    def _c3_merge(cls, seqs: list[list[str]]) -> list[str]:
        """
        Perform C3 linearization merge on the given sequences.
        """
        result = []
        seqs = [list(s) for s in seqs if s]
        while seqs:
            for seq in seqs:
                candidate = seq[0]
                if all(candidate not in s[1:] for s in seqs):
                    break
            else:
                raise TypeError(f"Inconsistent hierarchy: {seqs!r}")
            result.append(candidate)
            # Remove candidate from all sequences (simplified)
            seqs = [s[1:] if s and s[0] == candidate else s for s in seqs if s and (s[0] != candidate or len(s) > 1)]
            seqs = [s for s in seqs if s]
        return result

    @classmethod
    def _find_valid_base_order_uris(cls, base_uris: list[str], mro_map: dict[str, list[str]]) -> list[str]:
        """
        Find a permutation of base_uris for which C3-merge succeeds.
        """
        for perm in itertools.permutations(base_uris):
            parent_mros = [mro_map[b] for b in perm]
            try:
                cls._c3_merge(parent_mros + [list(perm)])
                return list(perm)
            except TypeError:
                continue
        raise TypeError(f"No consistent base order for {base_uris!r}")

    @classmethod
    def _topo_sort(cls, class_uris: list[str], inheritances: list[Inheritance]) -> list[str]:
        """
        Topologically sort class_uris based on inheritances.
        """
        if not class_uris:
            return []
        indegree = {u: 0 for u in class_uris}
        children = defaultdict(list)
        for inh in inheritances:
            if inh.base_uri in indegree and inh.class_uri in indegree:
                indegree[inh.class_uri] += 1
                children[inh.base_uri].append(inh.class_uri)
        queue = deque(u for u, d in indegree.items() if d == 0)
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in children[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        if len(order) != len(class_uris):
            cyclic_classes = set(class_uris) - set(order)
            raise RuntimeError(
                f"Cirkels in inheritance gedetecteerd. Betrokken klassen: {', '.join(cyclic_classes)}"
            )
        return order

    @classmethod
    def _compute_mros(cls, oslo_classes: list[OSLOClass], inheritances: list[Inheritance]
                      ) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
        """
        Compute MROs and direct base order for each class.
        """
        class_uris = [c.objectUri for c in oslo_classes]
        direct_bases = defaultdict(list)
        for inh in inheritances:
            direct_bases[inh.class_uri].append(inh.base_uri)

        order = cls._topo_sort(class_uris, inheritances)
        mro_map = {}
        direct_order_map = {}

        for uri in order:
            bases = [b for b in direct_bases.get(uri, []) if b]
            if not bases:
                mro_map[uri] = [uri]
                direct_order_map[uri] = []
                continue

            valid_bases = cls._find_valid_base_order_uris(bases, mro_map)
            parent_mros = [mro_map[b] for b in valid_bases]
            merged = cls._c3_merge(parent_mros + [valid_bases])

            mro_map[uri] = [uri] + merged
            direct_order_map[uri] = valid_bases

        return mro_map, direct_order_map

    def get_inheritance_map(self):
        if self.inheritance_map is not None:
            return self.inheritance_map

        if self.classes is None or self.inheritances is None:
            raise ValueError('Classes and inheritances must be collected before computing the inheritance map.')

        _, self.inheritance_map = OSLOCollector._compute_mros(oslo_classes=self.classes, inheritances=self.inheritances)
        return self.inheritance_map

