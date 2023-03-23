import pytest

from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns, wrap_in_quotes


def test_empty_string_returns_empty_string_in_single_quotes():
    result = wrap_in_quotes('')
    assert result == "''"


def test_none():
    with pytest.raises(TypeError):
        wrap_in_quotes(None)


def test_string_without_quotes_returns_string_with_single_quotes():
    result = wrap_in_quotes('a')
    assert result == "'a'"


def test_string_with_single_quotes_returns_string_with_double_quotes():
    result = wrap_in_quotes("kado's")
    assert result == '"kado\'s"'


def test_string_with_double_quotes_returns_string_with_single_quotes():
    result = wrap_in_quotes('ik "test" dit uit')
    assert result == '\'ik "test" dit uit\''


def test_string_with_more_doubles_than_singles_returns_string_with_single_quotes():
    result = wrap_in_quotes("ik \"test\" kado's uit")
    assert result == "\'ik \"test\" kado\\\'s uit\'"


def test_get_ns_and_name_from_uri_invalid_uris():
    agent_uri = 'http://purl.org/dc/terms/Agent'
    with pytest.raises(ValueError):
        get_ns_and_name_from_uri(agent_uri)


def test_get_ns_and_name_from_uri_valid_uris(subtests):
    testset = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType': ('abstracten', 'AOWSType'),
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex': (
            'implementatieelement', 'ActivityComplex'),
        'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie': (
            'installatie', 'Aardingsinstallatie'),
        'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie': (
            'levenscyclus', 'BeheerHoutigeVegetatie'),
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera': ('onderdeel', 'ANPRCamera'),
        'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring': ('proefenmeting', 'Keuring')
    }

    for uri, expected_tuple in testset.items():
        with subtests.test(msg=f'get_ns_and_name_from {uri}'):
            result_tuple = get_ns_and_name_from_uri(uri)
            assert result_tuple == expected_tuple


def test_get_class_directory_from_ns(subtests):
    testset = {
        'abstracten': 'Classes/Abstracten',
        'implementatieelement': 'Classes/ImplementatieElement',
        'installatie': 'Classes/Installatie',
        'levenscyclus': 'Classes/Levenscyclus',
        'onderdeel': 'Classes/Onderdeel',
        'proefenmeting': 'Classes/ProefEnMeting'
    }

    for ns, class_dir in testset.items():
        with subtests.test(msg=f'get_class_directory_from {ns}'):
            result_class_dir = get_class_directory_from_ns(ns)
            assert result_class_dir == class_dir

    with subtests.test(msg='bad value'):
        with pytest.raises(ValueError):
            get_class_directory_from_ns('bad_value')
