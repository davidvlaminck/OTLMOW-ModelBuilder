from pathlib import Path

import pytest
from otlmow_modelbuilder.OSLOCollector import OSLOCollector

current_file_path = Path(__file__)
base_dir = current_file_path.parent
test_classes_subset_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')


def test_find_superclasses_uri_by_class_uri_using_testmodel():
    subset_collector = OSLOCollector(test_classes_subset_location)
    subset_collector.collect_all()

    aim_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject'
    subclasses = subset_collector.find_subclasses_uri_by_class_uri(aim_object_uri)
    assert subclasses == ['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass']

    relatie_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    subclasses = subset_collector.find_subclasses_uri_by_class_uri(relatie_object_uri)
    assert subclasses == ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie']

def test_find_indirect_superclasses_uri_by_class_uri_using_testmodel():
    subset_collector = OSLOCollector(test_classes_subset_location)
    subset_collector.collect_all()

    relatie_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    subclasses = subset_collector.find_indirect_subclasses_uri_by_class_uri(relatie_object_uri)
    assert subclasses == ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt']


@pytest.mark.parametrize("class_uri,sort_by_uri,expected", [
    ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', True,
     ['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass',
      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass']),
    ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject', True,
     ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie',
      'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie']),
    ('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', False,
     ['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass',
      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass']),
    ('nonexistent_uri', True, []),
    ('', True, []),
])
def test_rust_find_subclasses_matches_python(class_uri, sort_by_uri, expected):
    from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
    from otlmow_modelbuilder._otlmow_modelbuilder_rs import find_subclasses_uri_by_class_uri as rust_find

    rust_result = rust_find(str(test_classes_subset_location), class_uri, sort_by_uri)
    assert rust_result == expected

    collector = OSLOCollector(test_classes_subset_location)
    with OSLOInMemoryCreator(test_classes_subset_location) as creator:
        inheritances = creator.get_all_inheritances()
    collector.inheritances = inheritances
    python_result = collector.find_subclasses_uri_by_class_uri(class_uri, sort_by_uri)
    assert python_result == expected


def test_python_fallback_is_used_when_path_is_invalid():
    """When the path is not a valid file, the rust extension is skipped and the python implementation is used."""
    from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator

    collector = OSLOCollector(Path(''))
    with OSLOInMemoryCreator(test_classes_subset_location) as creator:
        collector.inheritances = creator.get_all_inheritances()

    aim_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject'
    result = collector.find_subclasses_uri_by_class_uri(aim_object_uri, sort_by_uri=True)
    assert result == ['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass']