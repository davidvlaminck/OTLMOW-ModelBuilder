"""Characterisation tests for OTLModelCreator.

These tests pin the current behaviour of the model creator. They have to stay
green during a refactor: the generated model is compared with a golden snapshot
and every guard around the model creation is verified one by one.

Regenerate the golden snapshot after an intentional change with:

    UPDATE_GOLDEN=1 python -m pytest UnitTests/OTLModelCreator_characterisation_test.py
"""

import importlib
import json
import logging
import os
import warnings
from pathlib import Path
from typing import Any, Optional

import pytest

from otlmow_modelbuilder.Exceptions.NestedListAttributeError import NestedListAttributeError
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SettingsManager import load_settings
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLORelatie import OSLORelatie

CURRENT_DIR = Path(__file__).parent
SNAPSHOT_FILE = CURRENT_DIR / 'snapshots' / 'OTLModelCreator_model.json'
SUBSET_FILE = CURRENT_DIR / 'OTL_AllCasesTestClass.db'
KEUZELIJST_FILE = CURRENT_DIR / 'kl_testkeuzelijst' / 'KlTestKeuzelijst.ttl'
PACKAGE_DIR = CURRENT_DIR.parent / 'otlmow_modelbuilder'
LEGACY_TYPES_FILE = PACKAGE_DIR / 'legacy_types.csv'
SETTINGS_FILE = PACKAGE_DIR / 'settings_otlmow_modelbuilder.json'

CLASS_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
NESTED_LIST_ATTRIBUTE_URI = f'{CLASS_URI}.testComplexType'
NESTED_LIST_ATTRIBUTE_WITH_KARD_URI = f'{CLASS_URI}.testComplexTypeMetKard'


def stub_the_clone_of_the_fixed_classes(monkeypatch: pytest.MonkeyPatch) -> None:
    """Replace the git clone of the fixed classes: it needs the network."""
    monkeypatch.setattr(OTLModelCreator, 'copy_fixed_classes_from_otlmow_model',
                        staticmethod(lambda model_directory: None))


def settings_with_a_local_keuzelijst() -> dict:
    """Return the default settings, with the enumerations read from a local file."""
    settings = load_settings(SETTINGS_FILE)
    settings['enumeration_locations_by_environment'] = {
        'prd': [KEUZELIJST_FILE.resolve().as_uri()],
        'all': [],
    }
    return settings


def snapshot_of(directory: Path) -> dict[str, str]:
    """Return the content of every file in the directory, keyed by its relative path."""
    return {
        str(path.relative_to(directory)): path.read_text(encoding='utf-8')
        for path in sorted(directory.rglob('*')) if path.is_file()
    }


def collected_subset() -> OSLOCollector:
    """Return the collector of the test subset."""
    collector = OSLOCollector(SUBSET_FILE)
    collector.collect_all()
    return collector


def build_the_model(directory: Path, collector: Optional[OSLOCollector] = None,
                    include_legacy: bool = False) -> dict[str, str]:
    """Create the model of the test subset and return a snapshot of the result."""
    if collector is None:
        collector = collected_subset()

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        OTLModelCreator.create_full_model(
            directory=directory,
            oslo_collector=collector,
            geo_artefact_collector=None,
            settings=settings_with_a_local_keuzelijst(),
            include_legacy=include_legacy,
            environment='prd',
            include_kl_test_keuzelijst=False)

    return snapshot_of(directory / 'OtlmowModel')


def assert_snapshots_are_equal(actual: dict[str, str], expected: dict[str, str]) -> None:
    """Compare two snapshots and report the files that differ."""
    missing = sorted(set(expected) - set(actual))
    unexpected = sorted(set(actual) - set(expected))
    changed = sorted(name for name in set(actual) & set(expected) if actual[name] != expected[name])

    assert not missing and not unexpected and not changed, (
        f'the generated model changed: missing={missing}, unexpected={unexpected}, changed={changed}')


@pytest.mark.parametrize('use_rust', ['0', '1'])
def test_the_generated_model_is_unchanged(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, use_rust: str) -> None:
    """Golden test: the generated model has to stay exactly the same."""
    monkeypatch.setenv('OTLMOW_USE_RUST', use_rust)
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    monkeypatch.setitem(OTLEnumerationCreator.graph_dict, 'prd', {})

    snapshot = build_the_model(tmp_path)

    if os.environ.get('UPDATE_GOLDEN') == '1':
        SNAPSHOT_FILE.parent.mkdir(parents=True, exist_ok=True)
        SNAPSHOT_FILE.write_text(json.dumps(snapshot, indent=2, sort_keys=True), encoding='utf-8')

    assert_snapshots_are_equal(snapshot, json.loads(SNAPSHOT_FILE.read_text(encoding='utf-8')))


def test_the_generated_model_is_reproducible(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Two runs with the same input have to produce the same model."""
    monkeypatch.setenv('OTLMOW_USE_RUST', '0')
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    monkeypatch.setitem(OTLEnumerationCreator.graph_dict, 'prd', {})

    first = build_the_model(tmp_path / 'first')
    second = build_the_model(tmp_path / 'second')

    assert_snapshots_are_equal(second, first)


def test_the_rust_batch_generation_receives_the_expected_data(tmp_path: Path,
                                                               monkeypatch: pytest.MonkeyPatch) -> None:
    """The data handed over to the rust implementation is part of the contract."""
    rust_module = importlib.import_module('otlmow_modelbuilder._otlmow_modelbuilder_rs')

    captured: dict[str, Any] = {}

    def fake_generate_model_optimized(**kwargs: Any) -> tuple[int, int]:
        captured.update(kwargs)
        return 0, 0

    monkeypatch.setattr(rust_module, 'generate_model_optimized', fake_generate_model_optimized)
    monkeypatch.setenv('OTLMOW_USE_RUST', '1')
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    monkeypatch.setitem(OTLEnumerationCreator.graph_dict, 'prd', {})

    collector = collected_subset()
    build_the_model(tmp_path, collector=collector)

    assert sorted(captured) == [
        'attributes_by_class_uri',
        'class_validation_rules',
        'classes',
        'complex_datatype_validation_rules',
        'complex_datatypes',
        'complex_datatypes_lookup',
        'directory',
        'enumeration_adm_status',
        'enumeration_validation_rules',
        'enumeration_waardes',
        'enumerations',
        'enumerations_lookup',
        'geometry_type_map',
        'include_kl_test_keuzelijst',
        'inheritance_map',
        'inheritances_by_class_uri',
        'model_name',
        'primitive_datatype_validation_rules',
        'primitive_datatypes',
        'relations_by_object_uri',
        'settings',
        'type_links',
        'union_datatype_validation_rules',
        'union_datatypes',
        'union_datatypes_lookup',
    ]

    assert captured['directory'] == str(tmp_path / 'OtlmowModel')
    assert captured['model_name'] == 'OtlmowModel'
    assert captured['include_kl_test_keuzelijst'] is False
    assert captured['geometry_type_map'] == {}

    assert captured['enumerations_lookup'] == [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst', 'KlTestKeuzelijst'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand', 'KlAIMToestand'),
    ]
    assert captured['complex_datatypes_lookup'] == [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAssetVersie', 'DtcAssetVersie'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', 'DtcIdentificator'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType',
         'DtcTestComplexType'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
         'DtcTestComplexType2'),
    ]
    assert captured['union_datatypes_lookup'] == [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType', 'DtuTestUnionType'),
    ]
    assert captured['type_links'] == [
        ('http://www.w3.org/2000/01/rdf-schema#Literal', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#anyURI', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#boolean', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#date', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#dateTime', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#decimal', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#integer', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#string', 'OSLODatatypePrimitive'),
        ('http://www.w3.org/2001/XMLSchema#time', 'OSLODatatypePrimitive'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst', 'OSLOEnumeration'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAssetVersie', 'OSLODatatypeComplex'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', 'OSLODatatypeComplex'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType', 'OSLODatatypeComplex'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
         'OSLODatatypeComplex'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType',
         'OSLODatatypePrimitive'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType', 'OSLODatatypeUnion'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand', 'OSLOEnumeration'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMaand', 'OSLODatatypePrimitive'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt', 'OSLODatatypePrimitive'),
        ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest', 'OSLODatatypePrimitive'),
    ]

    # the attributes, the inheritances and the relations are looked up per class
    class_uris = {oslo_class.objectUri for oslo_class in collector.classes}
    datatype_uris = {attribute.class_uri for attribute in
                     (collector.primitive_datatype_attributen or []) +
                     (collector.complex_datatype_attributen or []) +
                     (collector.union_datatype_attributen or [])}

    assert set(captured['attributes_by_class_uri']) == class_uris | datatype_uris
    for uri, attributes in captured['attributes_by_class_uri'].items():
        assert [attribute.objectUri for attribute in attributes] == sorted(
            attribute.objectUri for attribute in attributes), f'the attributes of {uri} are not sorted'

    assert set(captured['inheritances_by_class_uri']) == class_uris
    assert set(captured['relations_by_object_uri']) == class_uris

    # the validation rules of the classes are merged with the ones of the complex datatypes
    assert captured['class_validation_rules'] == {
        **load_settings(SETTINGS_FILE)['class_validation_rules']['valid_uri_and_types'],
        **load_settings(SETTINGS_FILE)['complex_datatype_validation_rules']['valid_uri_and_types'],
    }
    assert captured['primitive_datatype_validation_rules'] == \
        load_settings(SETTINGS_FILE)['primitive_datatype_validation_rules']['valid_uri_and_types']
    assert captured['union_datatype_validation_rules'] == \
        load_settings(SETTINGS_FILE)['union_datatype_validation_rules']['valid_uri_and_types']
    assert captured['enumeration_validation_rules'] == \
        load_settings(SETTINGS_FILE)['enumeration_validation_rules']['valid_uri_and_types']

    # the values of the enumerations are read before the model is generated
    assert sorted(captured['enumeration_waardes']) == [
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand',
    ]
    assert len(captured['enumeration_waardes'][
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst']) == 6
    assert captured['enumeration_adm_status'][
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst'] == 'ingebruik'


def collector_with_attributes(*attributes: OSLOAttribuut) -> OSLOCollector:
    """Return a collector that only holds the given attributes."""
    collector = OSLOCollector(SUBSET_FILE)
    collector.attributes = list(attributes)
    return collector


def test_check_for_attributes_with_different_case_reports_the_conflict() -> None:
    """Two attributes that only differ in case are reported."""
    collector = collector_with_attributes(
        OSLOAttribuut(name='Naam', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.naam'),
        OSLOAttribuut(name='naam', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.NAAM'))

    with pytest.raises(NotImplementedError) as exception:
        OTLModelCreator.check_for_attributes_with_different_case(collector,
                                                                 attributes_with_different_cases_uris=[])

    problems = json.loads(str(exception.value).split('\n', 1)[1])
    assert list(problems) == ['naam']
    assert sorted(problems['naam']) == [
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.NAAM',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.naam']


def test_check_for_attributes_with_different_case_ignores_the_configured_uris() -> None:
    """A conflict between attributes that are on the ignore list is not an error."""
    collector = collector_with_attributes(
        OSLOAttribuut(name='Naam', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.naam'),
        OSLOAttribuut(name='naam', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.NAAM'))

    OTLModelCreator.check_for_attributes_with_different_case(
        collector,
        attributes_with_different_cases_uris=[
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.NAAM',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.naam'])


def test_check_for_attributes_with_different_case_ignores_deprecated_attributes() -> None:
    """A deprecated attribute does not conflict with its active counterpart."""
    collector = collector_with_attributes(
        OSLOAttribuut(name='Naam', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.naam'),
        OSLOAttribuut(name='naam', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Class.NAAM',
                      deprecated_version='1.0.0'))

    OTLModelCreator.check_for_attributes_with_different_case(collector, attributes_with_different_cases_uris=[])


def collector_with_a_nested_list_attribute() -> OSLOCollector:
    """Return the collector of the test subset, with a nested list attribute added."""
    collector = OSLOCollector(SUBSET_FILE)
    collector.collect_all()
    collector.complex_datatype_attributen.append(OSLODatatypeComplexAttribuut(
        name='testKwantWrdMetKard', label='Test kwantitatieve waarde met kardinaliteit',
        definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1 in een complex filename.',
        class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
        kardinaliteit_min='1', kardinaliteit_max='*',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTestMetKard',
        type='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
        overerving=0, constraints='', readonly=0, usagenote='', deprecated_version=''))
    return collector


def test_check_for_nested_attributes_in_classes_reports_the_nested_list() -> None:
    """A list inside a list is reported with the class and the attribute."""
    collector = collector_with_a_nested_list_attribute()

    with pytest.raises(NestedListAttributeError) as exception:
        OTLModelCreator.check_for_nested_attributes_in_classes(collector=collector)

    assert str(exception.value) == (
        'Nested list attributes are not supported for this attribute found in '
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass '
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType')


def test_check_for_nested_attributes_in_classes_ignores_the_known_attributes() -> None:
    """A nested list on the list of known attributes is not an error."""
    collector = collector_with_a_nested_list_attribute()

    OTLModelCreator.check_for_nested_attributes_in_classes(
        collector=collector,
        known_attribute_uris=[NESTED_LIST_ATTRIBUTE_URI])


def test_check_for_nested_attributes_in_classes_ignores_the_exception_attributes() -> None:
    """A nested list on the list of exceptions is not an error."""
    collector = collector_with_a_nested_list_attribute()

    OTLModelCreator.check_for_nested_attributes_in_classes(
        collector=collector,
        exceptions=[NESTED_LIST_ATTRIBUTE_URI, NESTED_LIST_ATTRIBUTE_WITH_KARD_URI])


def test_check_for_nested_attributes_in_classes_accepts_the_test_subset() -> None:
    """The test subset itself has no nested lists."""
    collector = OSLOCollector(SUBSET_FILE)
    collector.collect_all()

    OTLModelCreator.check_for_nested_attributes_in_classes(collector=collector)


def test_check_and_create_subdirectories_creates_the_expected_structure(tmp_path: Path,
                                                                      monkeypatch: pytest.MonkeyPatch) -> None:
    """The directories of the model are created, and the old content is removed."""
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    model_directory = tmp_path / 'OtlmowModel'
    (model_directory / 'Classes' / 'Onderdeel').mkdir(parents=True)
    (model_directory / 'Classes' / 'Onderdeel' / 'Stale.py').write_text('stale')

    OTLModelCreator.check_and_create_subdirectories(tmp_path)

    assert sorted(str(path.relative_to(tmp_path)) for path in tmp_path.rglob('*') if path.is_dir()) == [
        'OtlmowModel',
        'OtlmowModel/Classes',
        'OtlmowModel/Classes/Abstracten',
        'OtlmowModel/Classes/ImplementatieElement',
        'OtlmowModel/Classes/Installatie',
        'OtlmowModel/Classes/Legacy',
        'OtlmowModel/Classes/Levenscyclus',
        'OtlmowModel/Classes/Onderdeel',
        'OtlmowModel/Classes/ProefEnMeting',
        'OtlmowModel/Datatypes',
    ]
    assert not (model_directory / 'Classes' / 'Onderdeel' / 'Stale.py').exists()


def test_check_and_create_subdirectories_creates_the_directory(tmp_path: Path,
                                                               monkeypatch: pytest.MonkeyPatch) -> None:
    """The directory of the model is created when it does not exist yet."""
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    directory = tmp_path / 'a' / 'b'

    OTLModelCreator.check_and_create_subdirectories(directory)

    assert (directory / 'OtlmowModel').is_dir()


def test_clean_directory_removes_the_content(tmp_path: Path) -> None:
    """Everything in the directory is removed, the directory itself stays."""
    (tmp_path / 'Classes' / 'Onderdeel').mkdir(parents=True)
    (tmp_path / 'Classes' / 'Onderdeel' / 'Class.py').write_text('content')
    (tmp_path / 'file.py').write_text('content')

    OTLModelCreator.clean_directory(tmp_path)

    assert list(tmp_path.iterdir()) == []


def test_check_and_create_subdirectories_rejects_a_file(tmp_path: Path,
                                                        monkeypatch: pytest.MonkeyPatch) -> None:
    """The directory of the model has to be a directory."""
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    a_file = tmp_path / 'a_file'
    a_file.write_text('content')

    with pytest.raises(NotADirectoryError):
        OTLModelCreator.check_and_create_subdirectories(a_file)


def test_the_model_is_created_by_python_when_the_rust_extension_fails(tmp_path: Path,
                                                                     monkeypatch: pytest.MonkeyPatch) -> None:
    """Without the rust extension, the python path creates the same model."""
    rust_module = importlib.import_module('otlmow_modelbuilder._otlmow_modelbuilder_rs')

    def failing_generate_model_optimized(**kwargs: Any) -> tuple[int, int]:
        raise ModuleNotFoundError("No module named 'otlmow_modelbuilder._otlmow_modelbuilder_rs'")

    monkeypatch.setattr(rust_module, 'generate_model_optimized', failing_generate_model_optimized)
    monkeypatch.setenv('OTLMOW_USE_RUST', '1')
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    monkeypatch.setitem(OTLEnumerationCreator.graph_dict, 'prd', {})

    snapshot = build_the_model(tmp_path)

    assert_snapshots_are_equal(snapshot, json.loads(SNAPSHOT_FILE.read_text(encoding='utf-8')))


def test_the_legacy_classes_are_added_to_the_model(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The legacy classes are written and imported when they are asked for."""
    monkeypatch.setenv('OTLMOW_USE_RUST', '0')
    stub_the_clone_of_the_fixed_classes(monkeypatch)
    monkeypatch.setitem(OTLEnumerationCreator.graph_dict, 'prd', {})

    snapshot = build_the_model(tmp_path, include_legacy=True)

    assert 'Classes/Legacy/VKS.py' in snapshot
    assert 'from ..Classes.Legacy.VKS import VKS' in snapshot['Helpers/all_classes.py']
    assert 'from ..Classes.Legacy.LegacyObject import LegacyObject' not in snapshot['Helpers/all_classes.py']


def test_the_lookups_are_searched_in_the_collector_when_they_are_not_cached() -> None:
    """Without a cache, the attributes, the inheritances and the relations are searched per class."""
    collector = collected_subset()
    collector._attributes_by_class_uri = None
    collector._inheritances_by_class_uri = None
    collector._relations_by_uri = None

    lookups = OTLModelCreator._build_the_lookups(collector)

    assert lookups.attributes_by_class_uri[CLASS_URI] == collector.find_attributes_by_class(
        next(oslo_class for oslo_class in collector.classes if oslo_class.objectUri == CLASS_URI),
        sort_by_uri=True)
    assert lookups.inheritances_by_class_uri[CLASS_URI] == collector.find_inheritances_by_class(
        next(oslo_class for oslo_class in collector.classes if oslo_class.objectUri == CLASS_URI),
        sort_by_uri=True)
    assert lookups.relations_by_object_uri[CLASS_URI] == collector.find_all_relations(CLASS_URI,
                                                                                    allow_duplicates=False)


def test_only_the_relations_of_the_object_itself_are_kept() -> None:
    """An inherited relation and a relation of another object are not kept."""
    relations = [
        OSLORelatie(bron_overerving='', doel_overerving='', bron_uri=CLASS_URI,
                    doel_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Other',
                    objectUri='relation-1', richting='Unspecified', usagenote='', deprecated_version=''),
        OSLORelatie(bron_overerving='', doel_overerving='', bron_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Other',
                    doel_uri=CLASS_URI, objectUri='relation-2', richting='Unspecified',
                    usagenote='', deprecated_version=''),
        OSLORelatie(bron_overerving='1.0.0', doel_overerving='', bron_uri=CLASS_URI,
                    doel_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Other',
                    objectUri='relation-3', richting='Unspecified', usagenote='', deprecated_version=''),
        OSLORelatie(bron_overerving='', doel_overerving='', bron_uri=CLASS_URI,
                    doel_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Other',
                    objectUri='relation-4', richting='Naar', usagenote='', deprecated_version=''),
    ]

    filtered = OTLModelCreator._filter_the_relations(relations, CLASS_URI)

    assert [relation.objectUri for relation in filtered] == ['relation-1', 'relation-4']


def test_the_class_directory_follows_the_namespace_of_the_class() -> None:
    """A class is written in the directory of its namespace."""
    agent = OSLOClass(objectUri='http://purl.org/dc/terms/Agent', name='Agent', label='Agent',
                      deprecated_version='', definition='', abstract=0)
    onderdeel = OSLOClass(objectUri=f'{CLASS_URI}.Onderdeel', name='Onderdeel', label='Onderdeel',
                          deprecated_version='', definition='', abstract=0)

    assert OTLModelCreator._class_directory_of(agent) == 'Classes'
    assert OTLModelCreator._class_directory_of(onderdeel) == 'Classes/Onderdeel'


def test_the_import_statement_uses_the_validation_rules() -> None:
    """The name of a class in the validation rules is used in the helper."""
    oslo_class = OSLOClass(objectUri=f'{CLASS_URI}.Onderdeel', name='Onderdeel', label='Onderdeel',
                           deprecated_version='', definition='', abstract=0)
    class_validation_rules = {'valid_uri_and_types': {f'{CLASS_URI}.Onderdeel': 'Onderdeel'}}

    assert OTLModelCreator._import_statement_of(oslo_class, class_validation_rules) == \
        'from ..Classes.Onderdeel import Onderdeel'


def test_a_datatype_without_data_is_reported(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """A datatype without data is reported, and a datatype that failed is an error."""
    caplog.set_level(logging.INFO)
    OTLModelCreator._write_the_datatype('Empty', [], tmp_path)

    assert 'Could not create a class for Empty' in caplog.text
    assert (tmp_path / 'Datatypes' / 'Empty.py').read_text(encoding='utf-8') == ''

    with pytest.raises(TypeError):
        OTLModelCreator._write_the_datatype('Failed', None, tmp_path)


def test_a_class_without_data_is_reported(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """A class without data is reported."""
    caplog.set_level(logging.INFO)
    OTLModelCreator._write_the_class('Empty', [], 'Classes/Onderdeel', tmp_path)

    assert 'Could not create a class for Empty' in caplog.text
    assert (tmp_path / 'Classes' / 'Onderdeel' / 'Empty.py').read_text(encoding='utf-8') == ''


@pytest.mark.parametrize('name,expected', [
    ('Naam', 'Naam'),
    ('Naam.met.punt', 'Naam_met_punt'),
    ('Naam-met-streep', 'Naam_met_streep'),
    ('RIS', 'RISLegacy'),
    ('Fietstel', 'FietstelLegacy'),
    ('Brug', 'BeweegbareBrug'),
    ('Voedingskeuzeschakelaar', 'VKS'),
    ('Voedingskeuzeschakelaar.met.punt', 'Voedingskeuzeschakelaar_met_punt'),
])
def test_alter_legacy_class_name(name: str, expected: str) -> None:
    """The name of a legacy class is made a valid python name."""
    assert OTLModelCreator.alter_legacy_class_name(name) == expected


@pytest.mark.parametrize('directory,expected', [
    ('OtlmowModel', 'OtlmowModel'),
    ('TestModel/TestClasses', 'TestModel.TestClasses'),
])
def test_get_model_name_from_directory_path(directory: str, expected: str) -> None:
    """The name of the model is the name of the directory, with its parent for the test classes."""
    assert OTLModelCreator.get_model_name_from_directory_path(Path(directory)) == expected


def test_add_inheritances_adds_the_inheritance_and_the_placeholder_classes() -> None:
    """An additional inheritance adds a placeholder class for the base and the class."""
    collector = OSLOCollector(SUBSET_FILE)
    collector.collect_all()
    number_of_classes = len(collector.classes)

    OTLModelCreator.add_inheritances(oslo_collector=collector, additional_inheritances=[{
        'base_name': 'RelationInteractor',
        'base_uri': 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
        'class_name': 'LinkObjectSV',
        'class_uri': 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkObjectSV'}])

    assert len(collector.classes) == number_of_classes + 2
    assert Inheritance(
        base_name='RelationInteractor',
        base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
        class_name='LinkObjectSV',
        class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkObjectSV',
        deprecated_version='') in collector.inheritances

    for uri, name in [('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
                       'RelationInteractor'),
                      ('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkObjectSV', 'LinkObjectSV')]:
        placeholder = next(oslo_class for oslo_class in collector.classes if oslo_class.objectUri == uri)
        assert isinstance(placeholder, OSLOClass)
        assert placeholder.name == name
        assert placeholder.label == 'ignore this class when generating the model'
        assert placeholder.abstract == 1


def test_create_legacy_classes_writes_the_legacy_classes(tmp_path: Path) -> None:
    """Every legacy type becomes a class, and the classes are added to the helper."""
    collector = OSLOCollector(SUBSET_FILE)
    collector.collect_all()
    model_directory = tmp_path / 'OtlmowModel'

    OTLModelCreator.create_legacy_classes(oslo_collector=collector, directory=model_directory,
                                          legacy_types_path=LEGACY_TYPES_FILE)

    legacy_files = sorted(path.name for path in (model_directory / 'Classes' / 'Legacy').iterdir())

    assert len(legacy_files) == 259
    assert 'VKS.py' in legacy_files
    assert 'BeweegbareBrug.py' in legacy_files

    assert (model_directory / 'Classes' / 'Legacy' / 'VKS.py').read_text(encoding='utf-8') == '\n'.join([
        '# coding=utf-8',
        'from ...BaseClasses.LegacyObject import LegacyObject',
        '',
        '',
        '# Generated with LegacyClassCreator. To modify: extend, do not edit',
        'class VKS(LegacyObject):',
        '    """Voedingskeuzeschakelaar (Legacy)',
        '\tVoedingskeuzeschakelaar"""',
        '',
        "    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Voedingskeuzeschakelaar'",
        '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
        '',
        '    def __init__(self):',
        '        super().__init__()',
        ''])

    helper = (model_directory / 'Helpers' / 'all_classes.py').read_text(encoding='utf-8')
    assert 'from ..Classes.Legacy.VKS import VKS' in helper
