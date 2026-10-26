"""The data that is needed to create the model of an OTL subset."""

from typing import NamedTuple


class EnumerationData(NamedTuple):
    """The values of the enumerations, read before the model is generated."""

    waardes: dict[str, list]
    adm_status: dict[str, str]


class Lookups(NamedTuple):
    """The attributes, the inheritances and the relations of every class."""

    attributes_by_class_uri: dict[str, list]
    inheritances_by_class_uri: dict[str, list]
    relations_by_object_uri: dict[str, list]


class ModelData(NamedTuple):
    """The data that is needed to generate the model."""

    type_links: list[tuple[str, str]]
    enumerations: list[tuple[str, str]]
    complex_datatypes: list[tuple[str, str]]
    union_datatypes: list[tuple[str, str]]
    enumeration_waardes: dict[str, list]
    enumeration_adm_status: dict[str, str]
    inheritance_map: dict[str, list]
    lookups: Lookups
    class_validation_rules: dict
