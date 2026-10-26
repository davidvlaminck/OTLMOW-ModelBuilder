from pathlib import Path

from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector

GEOMETRIE_DB = Path(__file__).parent / 'GeometrieArtefact_AllCasesTestClass.db'


def test_collect_all_populates_geometrie_types():
    collector = GeometrieArtefactCollector(GEOMETRIE_DB)
    collector.collect_all()

    assert collector.geometrie_types is not None
    assert len(collector.geometrie_types) > 0


def test_find_by_objectUri_returns_matching_type():
    collector = GeometrieArtefactCollector(GEOMETRIE_DB)
    collector.collect_all()

    result = collector.find_by_objectUri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass')

    assert result is not None
    assert result.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
    assert result.label_nl == 'AllCasesTestClass'


def test_find_by_objectUri_returns_none_for_unknown_uri():
    collector = GeometrieArtefactCollector(GEOMETRIE_DB)
    collector.collect_all()

    result = collector.find_by_objectUri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NonExistent')

    assert result is None
