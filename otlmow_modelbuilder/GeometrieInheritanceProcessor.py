import copy

from otlmow_modelbuilder.GeometrieType import GeometrieType
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass


class GeometrieInheritanceProcessor:
    """This class uses the geometry type definitions and OTL classes and inheritances to determine what classes can inherit their geometry type definition instead of directly. The result is a changed set of geometry type definitions that contains both concrete and base classes. Inheritance works from at least one geometry type definition."""
    def __init__(self, geometrie_types: list[GeometrieType], inheritances: list[Inheritance], classes: list[OSLOClass]):
        self.geometrie_types = geometrie_types
        self.inheritances = copy.copy(inheritances)
        self.classes = copy.copy(classes)

    def process_inheritances(self) -> list[GeometrieType]:
        while len(self.inheritances) > 0:
            # zoek een inheritance en gebruik die voor een goede base class af te leiden

            inheritance = next(c for c in self.inheritances)
            base = self.search_for_valid_base_using_inheritance(inheritance.base_uri)
            self.process_inheritance_for_base(base)
        return self.geometrie_types

    def search_for_valid_base_using_inheritance(self, base):
        inheritances = list(filter(lambda i: i.base_uri == base, self.inheritances))
        if len(inheritances) == 0:
            return base
        for inheritance in inheritances:
            sub_inheritances = list(filter(lambda i: i.base_uri == inheritance.class_uri, self.inheritances))
            if len(sub_inheritances) > 0:
                return self.search_for_valid_base_using_inheritance(inheritance.class_uri)
        return base

    def process_inheritance_for_base(self, base):
        inheritances = list(filter(lambda i: i.base_uri == base, self.inheritances))
        if len(inheritances) == 0:
            return

        common = self._compute_common_geometry(inheritances)
        no_None_types = common is not None

        if no_None_types:
            geen, point, line, polygon = common
            if (geen + point + line + polygon) > 0:
                self._create_base_geometry_type(base, geen, point, line, polygon)
                self._strip_common_geometry(inheritances, geen, point, line, polygon)

        for inheritance in inheritances:
            self.inheritances.remove(inheritance)

    def _compute_common_geometry(self, inheritances):
        geo_types = [next((g for g in self.geometrie_types if g.objectUri == i.class_uri), None) for i in inheritances]
        if any(g is None for g in geo_types):
            return None
        geen = 1 if all(t.geen_geometrie == 1 for t in geo_types) else 0
        point = 1 if all(t.punt3D == 1 for t in geo_types) else 0
        line = 1 if all(t.lijn3D == 1 for t in geo_types) else 0
        polygon = 1 if all(t.polygoon3D == 1 for t in geo_types) else 0
        return (geen, point, line, polygon)

    def _create_base_geometry_type(self, base, geen, point, line, polygon):
        new_geo_type = GeometrieType()
        new_geo_type.objectUri = base
        cls = next((g for g in self.classes if g.objectUri == base), None)
        if cls is not None:
            new_geo_type.label_nl = cls.label
        new_geo_type.geen_geometrie = geen
        new_geo_type.punt3D = point
        new_geo_type.lijn3D = line
        new_geo_type.polygoon3D = polygon
        self.geometrie_types.append(new_geo_type)

    def _strip_common_geometry(self, inheritances, geen, point, line, polygon):
        for inheritance in inheritances:
            current_geo_type = next((g for g in self.geometrie_types if g.objectUri == inheritance.class_uri), None)
            if current_geo_type is None:
                continue
            if geen == 1:
                current_geo_type.geen_geometrie = 0
            if point == 1:
                current_geo_type.punt3D = 0
            if line == 1:
                current_geo_type.lijn3D = 0
            if polygon == 1:
                current_geo_type.polygoon3D = 0
            if all(getattr(current_geo_type, a) != 1 for a in ('geen_geometrie', 'punt3D', 'lijn3D', 'polygoon3D')):
                self.geometrie_types.remove(current_geo_type)

