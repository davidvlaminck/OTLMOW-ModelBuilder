import pytest

from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns, wrap_in_quotes, \
    escape_backslash


def test_escape_backslash_empty_string():
    result = escape_backslash('')
    assert result == ''


def test_escape_backslash():
    result = escape_backslash('\\d')
    assert result == '\\\\d'


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



# Parametrized test for happy path scenarios
@pytest.mark.parametrize("input_text, expected_output", [
    # ID: Test single word without quotes
    ("word", "'word'"),
    # ID: Test single word with single quotes
    ("'word'", '"\'word\'"'),
    # ID: Test single word with double quotes
    ('"word"', "'\"word\"'"),
    # ID: Test sentence with more double quotes than single quotes
    ('The "quick" brown fox', "'The \"quick\" brown fox'"),
    # ID: Test sentence with more single quotes than double quotes
    ("It's a beautiful day", '"It\'s a beautiful day"'),
    # ID: Test sentence with equal single and double quotes
    ('"Hello", she said, "It\'s a pleasure."', '\'"Hello", she said, "It\\\'s a pleasure."\''),
], ids=[
    "single_word_no_quotes",
    "single_word_single_quotes",
    "single_word_double_quotes",
    "sentence_more_double_quotes",
    "sentence_more_single_quotes",
    "sentence_equal_quotes"
])
def test_wrap_in_quotes_happy_path(input_text, expected_output):
    # Act
    result = wrap_in_quotes(input_text)

    # Assert
    assert result == expected_output

# Parametrized test for edge cases
@pytest.mark.parametrize("input_text, expected_output", [
    # ID: Test empty string
    ("", "''"),
    # ID: Test string with only single quotes
    ("''''''", "\"''''''\""),
    # ID: Test string with only double quotes
    ('""""""', "'\"\"\"\"\"\"'"),
    # ID: Test string with special characters
    ("!@#$%^&*()", "'!@#$%^&*()'"),
    # ID: Test string with newline characters
    ("line1\nline2", "'line1\nline2'"),
], ids=[
    "empty_string",
    "only_single_quotes",
    "only_double_quotes",
    "special_characters",
    "newline_characters"
])
def test_wrap_in_quotes_edge_cases(input_text, expected_output):
    # Act
    result = wrap_in_quotes(input_text)

    # Assert
    assert result == expected_output

# Parametrized test for error cases
@pytest.mark.parametrize("input_value, expected_exception", [
    # ID: Test None input
    (None, TypeError),
    # ID: Test integer input
    (123, TypeError),
    # ID: Test list input
    (['a', 'b', 'c'], TypeError),
    # ID: Test dict input
    ({"key": "value"}, TypeError),
], ids=[
    "none_input",
    "integer_input",
    "list_input",
    "dict_input"
])
def test_wrap_in_quotes_error_cases(input_value, expected_exception):
    # Act / Assert
    with pytest.raises(expected_exception):
        wrap_in_quotes(input_value)


def test_get_ns_and_name_from_uri_Agent():
    agent_uri = 'http://purl.org/dc/terms/Agent'
    assert get_ns_and_name_from_uri(agent_uri) == ('', 'Agent')


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
        'proefenmeting': 'Classes/ProefEnMeting',
        'besluit': 'Classes/Besluit'
    }

    for ns, class_dir in testset.items():
        with subtests.test(msg=f'get_class_directory_from {ns}'):
            result_class_dir = get_class_directory_from_ns(ns)
            assert result_class_dir == class_dir

    with subtests.test(msg='None'):
        with pytest.raises(ValueError):
            get_class_directory_from_ns(None)
