from pathlib import Path

import pytest

from otlmow_modelbuilder.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from otlmow_modelbuilder.GeometrieType import GeometrieType

GEOMETRIE_DB = Path(__file__).parent / 'GeometrieArtefact_AllCasesTestClass.db'


def test_context_manager_connection_not_none():
    with GeometrieInMemoryCreator(GEOMETRIE_DB) as creator:
        assert creator.connection is not None


def test_get_all_geometrie_types_returns_list_of_geometrie_types():
    with GeometrieInMemoryCreator(GEOMETRIE_DB) as creator:
        types = creator.get_all_geometrie_types()

    assert isinstance(types, list)
    assert len(types) > 0
    for g in types:
        assert isinstance(g, GeometrieType)


def test_get_all_geometrie_types_known_values():
    with GeometrieInMemoryCreator(GEOMETRIE_DB) as creator:
        types = creator.get_all_geometrie_types()

    uris = [g.objectUri for g in types]
    assert 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass' in uris
    assert 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass' in uris
    assert 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass' in uris

    all_cases = next(g for g in types if g.objectUri.endswith('#AllCasesTestClass'))
    assert all_cases.label_nl == 'AllCasesTestClass'
    assert all_cases.punt3D == 1
    assert all_cases.lijn3D == 0
    assert all_cases.polygoon3D == 0


def test_file_not_found_raises():
    with pytest.raises(FileNotFoundError):
        GeometrieInMemoryCreator(Path('/nonexistent/path.db'))


def test_empty_string_path_sets_file_exists_false():
    creator = GeometrieInMemoryCreator('')
    assert creator.file_exists is False


def test_none_path_sets_file_exists_false():
    creator = GeometrieInMemoryCreator(None)
    assert creator.file_exists is False


def test_empty_path_object_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        GeometrieInMemoryCreator(Path(''))


def test_perform_read_query_returns_rows():
    with GeometrieInMemoryCreator(GEOMETRIE_DB) as creator:
        rows = creator.perform_read_query('SELECT * FROM GeometrieType')

    assert isinstance(rows, list)
    assert len(rows) > 0
    assert isinstance(rows[0], tuple)
