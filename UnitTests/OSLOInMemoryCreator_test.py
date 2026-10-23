from pathlib import Path

import pytest

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

current_file_path = Path(__file__)
base_dir = current_file_path.parent
test_db_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')


@pytest.fixture
def db():
    with OSLOInMemoryCreator(test_db_location) as creator:
        yield creator


def test_get_general_info_returns_list_of_records(db):
    data = db.get_general_info()
    assert isinstance(data, list)
    assert len(data) > 0
    for row in data:
        assert isinstance(row, GeneralInfoRecord)


def test_get_general_info_has_expected_fields(db):
    data = db.get_general_info()
    for record in data:
        assert record.parameter is not None
        assert record.value is not None


def test_get_otl_version(db):
    version = db.get_otl_version()
    assert version is not None
    assert isinstance(version, str)


def test_get_otl_version_empty_db():
    empty_db = Path(f'{base_dir}/OTL_AllCasesTestClass_fewer_attributes.db')
    with OSLOInMemoryCreator(empty_db) as creator:
        version = creator.get_otl_version()
        assert version is not None


def test_get_all_classes_returns_list(db):
    classes = db.get_all_classes()
    assert isinstance(classes, list)
    assert len(classes) > 0
    for c in classes:
        assert isinstance(c, OSLOClass)


def test_get_all_classes_sorted_by_uri(db):
    classes = db.get_all_classes()
    uris = [c.objectUri for c in classes]
    assert uris == sorted(uris)


def test_get_all_classes_and_class_dict(db):
    classes, class_dict = db.get_all_classes_and_class_dict()
    assert isinstance(classes, list)
    assert isinstance(class_dict, dict)
    assert len(classes) == len(class_dict)
    for c in classes:
        assert class_dict[c.objectUri] == c


def test_get_class_by_uri(db):
    classes = db.get_all_classes()
    first_uri = classes[0].objectUri
    result = db.get_class_by_uri(first_uri)
    assert result is not None
    assert result.objectUri == first_uri


def test_get_class_by_uri_not_found(db):
    result = db.get_class_by_uri('nonexistent_uri')
    assert result is None


def test_get_class_by_uri_empty_returns_none(db):
    result = db.get_class_by_uri('')
    assert result is None


def test_get_all_attributes_returns_list(db):
    attrs = db.get_all_attributes()
    assert isinstance(attrs, list)
    assert len(attrs) > 0
    for a in attrs:
        assert isinstance(a, OSLOAttribuut)


def test_get_all_attributes_sorted_by_uri(db):
    attrs = db.get_all_attributes()
    uris = [a.objectUri for a in attrs]
    assert uris == sorted(uris)


def test_get_attributes_by_class_uri(db):
    classes = db.get_all_classes()
    first_class = classes[0]
    attrs = db.get_attributes_by_class_uri(first_class.objectUri)
    for a in attrs:
        assert a.class_uri == first_class.objectUri


def test_get_attributes_with_abstract(db):
    attrs = db.get_all_attributes(include_abstract=True)
    assert len(attrs) > 0


def test_get_attributes_excludes_typeURI(db):
    attrs = db.get_all_attributes()
    for a in attrs:
        assert a.name != 'typeURI'


def test_get_all_inheritances_returns_list(db):
    inheritances = db.get_all_inheritances()
    assert isinstance(inheritances, list)
    assert len(inheritances) > 0
    for i in inheritances:
        assert isinstance(i, Inheritance)


def test_get_all_inheritances_sorted_by_base_uri(db):
    inheritances = db.get_all_inheritances()
    pairs = [(i.base_uri, i.class_uri) for i in inheritances]
    assert pairs == sorted(pairs)


def test_get_all_inheritances_fields(db):
    inheritances = db.get_all_inheritances()
    for i in inheritances:
        assert i.base_name is not None
        assert i.base_uri is not None
        assert i.class_uri is not None
        assert i.class_name is not None
        assert i.deprecated_version is not None


def test_get_all_primitive_datatypes(db):
    prims = db.get_all_primitive_datatypes()
    assert isinstance(prims, list)
    for p in prims:
        assert isinstance(p, OSLODatatypePrimitive)


def test_get_all_primitive_datatypes_sorted_by_uri(db):
    prims = db.get_all_primitive_datatypes()
    uris = [p.objectUri for p in prims]
    assert uris == sorted(uris)


def test_get_all_primitive_datatype_attributes(db):
    attrs = db.get_all_primitive_datatype_attributes()
    assert isinstance(attrs, list)
    for a in attrs:
        assert isinstance(a, OSLODatatypePrimitiveAttribuut)


def test_get_all_complex_datatypes(db):
    complexes = db.get_all_complex_datatypes()
    assert isinstance(complexes, list)
    for c in complexes:
        assert isinstance(c, OSLODatatypeComplex)


def test_get_all_complex_datatype_attributes(db):
    attrs = db.get_all_complex_datatype_attributes()
    assert isinstance(attrs, list)
    for a in attrs:
        assert isinstance(a, OSLODatatypeComplexAttribuut)


def test_get_all_union_datatypes(db):
    unions = db.get_all_union_datatypes()
    assert isinstance(unions, list)
    for u in unions:
        assert isinstance(u, OSLODatatypeUnion)


def test_get_all_union_datatype_attributes(db):
    attrs = db.get_all_union_datatype_attributes()
    assert isinstance(attrs, list)
    for a in attrs:
        assert isinstance(a, OSLODatatypeUnionAttribuut)


def test_get_all_enumerations(db):
    enums = db.get_all_enumerations()
    assert isinstance(enums, list)
    for e in enums:
        assert isinstance(e, OSLOEnumeration)


def test_get_all_enumerations_sorted_by_uri(db):
    enums = db.get_all_enumerations()
    uris = [e.objectUri for e in enums]
    assert uris == sorted(uris)


def test_get_all_typelinks(db):
    links = db.get_all_typelinks()
    assert isinstance(links, list)
    for l in links:
        assert isinstance(l, OSLOTypeLink)


def test_get_all_typelinks_sorted_by_uri(db):
    links = db.get_all_typelinks()
    uris = [l.item_uri for l in links]
    assert uris == sorted(uris)


def test_get_all_relations(db):
    relations = db.get_all_relations()
    assert isinstance(relations, list)
    for r in relations:
        assert isinstance(r, OSLORelatie)


def test_get_all_relations_sorted(db):
    relations = db.get_all_relations()
    keys = [(r.objectUri, r.bron_uri, r.doel_uri) for r in relations]
    assert keys == sorted(keys)


def test_file_not_found_raises():
    with pytest.raises(FileNotFoundError):
        OSLOInMemoryCreator(Path('/nonexistent/path.db'))


def test_empty_path_raises_filenotfound():
    with pytest.raises(FileNotFoundError):
        OSLOInMemoryCreator(Path(''))


def test_none_path_sets_file_exists_false():
    creator = OSLOInMemoryCreator(None)
    assert creator.file_exists is False


def test_context_manager(db):
    assert db.connection is not None
