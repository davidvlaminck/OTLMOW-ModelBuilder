from __future__ import annotations

import itertools
import os
from collections import defaultdict, deque
from pathlib import Path

from otlmow_modelbuilder.NewOTLBaseClassNotImplemented import (
    NewOTLBaseClassNotImplemented,
)
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.GeneralInfoRecord import GeneralInfoRecord
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplex import OSLODatatypeComplex
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import (
    OSLODatatypeComplexAttribuut,
)
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import (
    OSLODatatypePrimitive,
)
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitiveAttribuut import (
    OSLODatatypePrimitiveAttribuut,
)
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnion import OSLODatatypeUnion
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnionAttribuut import (
    OSLODatatypeUnionAttribuut,
)
from otlmow_modelbuilder.SQLDataClasses.OSLOEnumeration import OSLOEnumeration
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

        self.class_dict: dict | None = None
        self.inheritance_map: dict | None = None
        self._relations_by_uri: dict | None = None
        self._attributes_by_class_uri: dict | None = None
        self._inheritances_by_class_uri: dict | None = None

        # Build fast lookup maps after data is loaded
        self._build_lookup_maps()

    def _build_lookup_maps(self) -> None:
        if not self.relations:
            return
        self._relations_by_uri = OSLOCollector._build_relations_by_uri_map(self.relations)
        self._attributes_by_class_uri = OSLOCollector._group_by_class_uri(self.attributes)
        self._inheritances_by_class_uri = OSLOCollector._group_by_class_uri(self.inheritances)

    @staticmethod
    def _group_by_class_uri(items: list) -> dict:
        """Group a list of objects by their class_uri into a dict of lists."""
        grouped = {}
        for item in items:
            grouped.setdefault(item.class_uri, []).append(item)
        return grouped

    @staticmethod
    def _build_relations_by_uri_map(relations: list) -> dict:
        """Build a map of relations by their bron_uri.

        A directional relation whose doel_uri differs from its bron_uri is also
        indexed under doel_uri. Unspecified relations are only indexed under
        bron_uri, because the caller filters them by bron_uri alone.
        """
        result = {}
        for r in relations:
            result.setdefault(r.bron_uri, []).append(r)
            if r.doel_uri != r.bron_uri and r.richting != 'Unspecified':
                result.setdefault(r.doel_uri, []).append(r)
        return result

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
        return self._find_by_class_uri(self.attributes, oslo_class.objectUri, sort_by_uri,
                                       key=lambda a: a.objectUri)

    def find_inheritances_by_class(self, oslo_class: OSLOClass, sort_by_uri: bool = True) -> list[Inheritance]:
        if oslo_class is None:
            return []
        return self.find_inheritances_by_class_uri(oslo_class.objectUri, sort_by_uri=sort_by_uri)

    def find_inheritances_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True) -> list[Inheritance]:
        if not oslo_class_uri:
            return []
        return self._find_by_class_uri(self.inheritances, oslo_class_uri, sort_by_uri,
                                       key=lambda i: i.base_uri)

    def _find_by_class_uri(self, items: list, class_uri: str, sort_by_uri: bool, key) -> list:
        """Filter items by class_uri and optionally sort them."""
        matches = [item for item in items if item.class_uri == class_uri]
        return sorted(matches, key=key) if sort_by_uri else matches

    def find_all_indirect_inheritances_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True
                                                    ) -> list[Inheritance]:
        if not oslo_class_uri:
            return []
        inheritance_list = self._collect_all_indirect_inheritances(oslo_class_uri)
        return sorted(inheritance_list, key=lambda c: c.base_uri) if sort_by_uri else inheritance_list

    def _collect_all_indirect_inheritances(self, oslo_class_uri: str) -> list[Inheritance]:
        direct = self.find_inheritances_by_class_uri(oslo_class_uri)
        result = list(direct)
        for inherit in direct:
            result.extend(self._collect_all_indirect_inheritances(inherit.base_uri))
        return result

    def find_subclasses_uri_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True) -> list[str]:
        if not oslo_class_uri:
            return []
        rust_result = self._try_rust_find_subclasses(oslo_class_uri, sort_by_uri)
        if rust_result is not None:
            return rust_result
        return self._python_find_subclasses(oslo_class_uri, sort_by_uri)

    def _try_rust_find_subclasses(self, oslo_class_uri: str, sort_by_uri: bool) -> list[str] | None:
        if not self._path_is_valid():
            return None
        try:
            from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
                find_subclasses_uri_by_class_uri as rust_find,
            )
            return rust_find(str(self.path.resolve()), oslo_class_uri, sort_by_uri)
        except ImportError:
            return None

    def _python_find_subclasses(self, oslo_class_uri: str, sort_by_uri: bool) -> list[str]:
        subclasses = [i.class_uri for i in self.inheritances if i.base_uri == oslo_class_uri]
        return sorted(subclasses) if sort_by_uri else subclasses

    def _path_is_valid(self) -> bool:
        path = self.path
        return path is not None and path != '' and os.path.isfile(str(path))

    def find_indirect_subclasses_uri_by_class_uri(self, oslo_class_uri: str, sort_by_uri: bool = True) -> list[str]:
        if not oslo_class_uri:
            return []
        superclass_list = self._collect_indirect_subclasses(oslo_class_uri)
        return sorted(superclass_list) if sort_by_uri else superclass_list

    def _collect_indirect_subclasses(self, oslo_class_uri: str) -> list[str]:
        direct = self.find_subclasses_uri_by_class_uri(oslo_class_uri)
        result = list(direct)
        for subclass in direct:
            result.extend(self._collect_indirect_subclasses(subclass))
        return result

    def find_class_by_uri(self, uri: str) -> OSLOClass:
        return next((p for p in self.classes if p.objectUri == uri), None)

    def find_primitive_datatype_by_uri(self, uri: str) -> OSLODatatypePrimitive:
        return next((p for p in self.primitive_datatypes if p.objectUri == uri), None)

    def find_primitive_datatype_attributes_by_class_uri(self, class_uri: str, sort_by_uri: bool = True
                                                        ) -> list[OSLODatatypePrimitiveAttribuut]:
        return self._find_by_class_uri(self.primitive_datatype_attributen, class_uri, sort_by_uri,
                                       key=lambda p: p.objectUri)

    def find_complex_datatype_by_uri(self, uri) -> OSLODatatypeComplex:
        return next((p for p in self.complex_datatypes if p.objectUri == uri), None)

    def find_complex_datatype_attributes_by_class_uri(self, class_uri: str, sort_by_uri: bool = True
                                                      ) -> list[OSLODatatypeComplexAttribuut]:
        return self._find_by_class_uri(self.complex_datatype_attributen, class_uri, sort_by_uri,
                                       key=lambda p: p.objectUri)

    def find_union_datatype_by_uri(self, uri) -> OSLODatatypeUnion:
        return next((p for p in self.union_datatypes if p.objectUri == uri), None)

    def find_union_datatype_attributes_by_class_uri(self, class_uri: str, sort_by_uri: bool = True
                                                     ) -> list[OSLODatatypeUnionAttribuut]:
        return self._find_by_class_uri(self.union_datatype_attributen, class_uri, sort_by_uri,
                                       key=lambda p: p.objectUri)

    def find_enumeration_by_uri(self, uri) -> OSLOEnumeration:
        return next((p for p in self.enumerations if p.objectUri == uri), None)

    def find_enumeration_by_codelist(self, uri) -> OSLOEnumeration:
        return next((p for p in self.enumerations if p.codelist == uri), None)

    def find_type_link_by_uri(self, type_uri: str) -> OSLOTypeLink:
        return next((p for p in self.typeLinks if p.item_uri == type_uri), None)

    def find_outgoing_relations(self, objectUri: str, sort_by_uri: bool = True) -> list[OSLORelatie]:
        outgoing = [r for r in self._relations_of(objectUri, include_inherited=True) if r.bron_uri == objectUri]
        return sorted(outgoing, key=lambda r: r.objectUri) if sort_by_uri else outgoing

    def find_all_relations(self, objectUri: str, allow_duplicates: bool = False, sort_by_uri: bool = True
                           ) -> [OSLORelatie]:
        """finds all relations, given an objectUri, where the object is either the source or the target of the relation.
        allow_duplicates is relevant for unidirectional relations, as the relation would be included twice:
        once where objectUri is the source and once where objectUri is the target. If allow_duplicates is False,
        only the relation where objectUri is the source is returned."""
        all_relations = self._relations_of(objectUri, include_inherited=True)
        return self._select_relations(all_relations, allow_duplicates, sort_by_uri,
                                      lambda r: r.bron_uri == objectUri)

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

        all_relations = self._relations_of(objectUri, include_inherited=False)
        return self._select_relations(all_relations, allow_duplicates, sort_by_uri,
                                      lambda r: r.bron_uri == objectUri or r.bron_overerving == objectUri)

    def _relations_of(self, objectUri: str, include_inherited: bool) -> list[OSLORelatie]:
        """The relations where the object is the source or the target.

        When include_inherited is True, inherited relations (bron_overerving or doel_overerving set)
        are included. When False, only direct relations of concrete classes are kept.
        """
        if include_inherited:
            return self._direct_relations_of(objectUri)
        return self._concrete_relations_of(objectUri)

    def _direct_relations_of(self, objectUri: str) -> list[OSLORelatie]:
        """The relations where the object is the source or the target, inherited ones included."""
        return [r for r in self.relations
                if (r.bron_uri == objectUri or r.doel_uri == objectUri)
                and r.bron_overerving == '' and r.doel_overerving == '']

    def _concrete_relations_of(self, objectUri: str) -> list[OSLORelatie]:
        """The direct relations of the object, where both sides are concrete classes."""
        return [r for r in self.relations
                if (r.bron_uri == objectUri or r.doel_uri == objectUri)
                and self.class_dict[r.bron_uri].abstract == 0
                and self.class_dict[r.doel_uri].abstract == 0]

    def _select_relations(self, relations: list[OSLORelatie], allow_duplicates: bool,
                          sort_by_uri: bool, is_source) -> list[OSLORelatie]:
        """Sort the relations, or filter out the ones where the object is not the source."""
        if not allow_duplicates:
            relations = [r for r in relations
                         if (r.richting == 'Unspecified' and is_source(r)) or r.richting != 'Unspecified']
        return self._sorted_or_as_is(relations, sort_by_uri)

    @staticmethod
    def _sorted_or_as_is(relations: list[OSLORelatie], sort_by_uri: bool) -> list[OSLORelatie]:
        return sorted(relations, key=lambda r: r.objectUri) if sort_by_uri else relations

    @classmethod
    def _c3_merge(cls, seqs: list[list[str]]) -> list[str]:
        """Perform C3 linearization merge on the given sequences."""
        result = []
        seqs = [list(s) for s in seqs if s]
        while seqs:
            candidate = cls._find_candidate(seqs)
            result.append(candidate)
            seqs = cls._remove_head(seqs, candidate)
        return result

    @classmethod
    def _find_candidate(cls, seqs: list[list[str]]) -> str:
        """The first head that does not appear in the tail of any sequence."""
        for seq in seqs:
            candidate = seq[0]
            if all(candidate not in s[1:] for s in seqs):
                return candidate
        raise TypeError(f"Inconsistent hierarchy: {seqs!r}")

    @classmethod
    def _remove_head(cls, seqs: list[list[str]], candidate: str) -> list[list[str]]:
        """Drop the candidate from the head of every sequence that starts with it."""
        trimmed = [s[1:] if s and s[0] == candidate else s for s in seqs]
        return [s for s in trimmed if s]

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
        """Topologically sort class_uris based on inheritances."""
        if not class_uris:
            return []
        indegree, children = cls._build_graph(class_uris, inheritances)
        order = cls._process_queue(deque(u for u, d in indegree.items() if d == 0), children, indegree)
        cls._raise_if_cyclic(order, class_uris)
        return order

    @classmethod
    def _build_graph(cls, class_uris: list[str], inheritances: list[Inheritance]
                     ) -> tuple[dict, defaultdict]:
        """Build the indegree map and the children adjacency list from the inheritances."""
        indegree = {u: 0 for u in class_uris}
        children = defaultdict(list)
        for inh in inheritances:
            if inh.base_uri in indegree and inh.class_uri in indegree:
                indegree[inh.class_uri] += 1
                children[inh.base_uri].append(inh.class_uri)
        return indegree, children

    @classmethod
    def _process_queue(cls, queue: deque, children: defaultdict, indegree: dict) -> list[str]:
        """Drain the queue, updating indegrees as children become reachable."""
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in children[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return order

    @classmethod
    def _raise_if_cyclic(cls, order: list[str], class_uris: list[str]) -> None:
        """Raise if the topological sort could not cover every class."""
        if len(order) != len(class_uris):
            cyclic_classes = list(set(order) ^ set(class_uris))
            raise RuntimeError(
                f"Cirkels in inheritance gedetecteerd. Betrokken klassen: {', '.join(cyclic_classes)}"
            )

    @classmethod
    def _compute_mros(cls, oslo_classes: list[OSLOClass], inheritances: list[Inheritance]
                      ) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
        """Compute MROs and direct base order for each class."""
        class_uris = [c.objectUri for c in oslo_classes]
        cls._raise_if_duplicate_uris(class_uris)

        direct_bases = cls._build_direct_bases(inheritances)
        order = cls._topo_sort(class_uris, inheritances)
        return cls._build_mro_maps(order, direct_bases)

    @classmethod
    def _raise_if_duplicate_uris(cls, class_uris: list[str]) -> None:
        """Raise if any class URI appears more than once."""
        if len(class_uris) != len(set(class_uris)):
            duplicates = {uri for uri in class_uris if class_uris.count(uri) > 1}
            raise ValueError("Duplicate class URIs found in oslo_classes: " + ", ".join(duplicates))

    @classmethod
    def _build_direct_bases(cls, inheritances: list[Inheritance]) -> defaultdict:
        """Map each class URI to the list of its direct base URIs."""
        direct_bases = defaultdict(list)
        for inh in inheritances:
            direct_bases[inh.class_uri].append(inh.base_uri)
        return direct_bases

    @classmethod
    def _build_mro_maps(cls, order: list[str], direct_bases: defaultdict
                        ) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
        """Build the MRO map and the direct-order map for every class in topological order."""
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

