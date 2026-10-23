import pytest
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    escape_backslash as rust_escape_backslash,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    get_class_directory_from_ns as rust_get_class_directory_from_ns,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    get_ns_and_name_from_uri as rust_get_ns_and_name_from_uri,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    get_titlecase_from_ns as rust_get_titlecase_from_ns,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    get_white_space_equivalent as rust_get_white_space_equivalent,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    wrap_in_quotes as rust_wrap_in_quotes,
)

from otlmow_modelbuilder.GenericBuilderFunctions import get_white_space_equivalent
from otlmow_modelbuilder.HelperFunctions import (
    escape_backslash,
    get_class_directory_from_ns,
    get_ns_and_name_from_uri,
    get_titlecase_from_ns,
    wrap_in_quotes,
)


class TestEscapeBackslash:
    @pytest.mark.parametrize("text", [
        "",
        "hello",
        "\\d",
        "\\\\d",
        "path\\to\\file",
        "no backslashes here",
        "mixed \\ and / paths",
        "\\",
        "\\n",
    ])
    def test_matches_python(self, text):
        assert rust_escape_backslash(text) == escape_backslash(text)


class TestWrapInQuotes:
    @pytest.mark.parametrize("text", [
        "",
        "a",
        "hello world",
        "word",
        "kado's",
        'ik "test" dit uit',
        "It's a beautiful day",
        '"Hello", she said, "It\'s a pleasure."',
        "''''''",
        '""""""',
        "!@#$%^&*()",
        "line1\nline2",
        "The \"quick\" brown fox",
        "single ' quote",
        'double " quote',
        "'both' \"kinds\"",
    ])
    def test_matches_python(self, text):
        assert rust_wrap_in_quotes(text) == wrap_in_quotes(text)

    def test_type_error_on_none(self):
        with pytest.raises(TypeError):
            rust_wrap_in_quotes(None)


class TestGetWhiteSpaceEquivalent:
    @pytest.mark.parametrize("string", [
        "",
        "a",
        "aa",
        "hello",
        "1234567890",
    ])
    def test_matches_python(self, string):
        assert rust_get_white_space_equivalent(string) == get_white_space_equivalent(string)


class TestGetNsAndNameFromUri:
    @pytest.mark.parametrize("uri, expected_ns, expected_name", [
        ("http://purl.org/dc/terms/Agent", "", "Agent"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType", "abstracten", "AOWSType"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex", "implementatieelement", "ActivityComplex"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie", "installatie", "Aardingsinstallatie"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie", "levenscyclus", "BeheerHoutigeVegetatie"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera", "onderdeel", "ANPRCamera"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring", "proefenmeting", "Keuring"),
        ("https://wegenenverkeer.data.vlaanderen.be/ns/besluit#SomeName", "besluit", "SomeName"),
    ])
    def test_matches_python(self, uri, expected_ns, expected_name):
        assert rust_get_ns_and_name_from_uri(uri) == get_ns_and_name_from_uri(uri)
        assert rust_get_ns_and_name_from_uri(uri) == (expected_ns, expected_name)

    def test_missing_hash_raises_value_error(self):
        uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten"
        with pytest.raises(ValueError):
            get_ns_and_name_from_uri(uri)
        with pytest.raises(ValueError):
            rust_get_ns_and_name_from_uri(uri)


class TestGetTitlecaseFromNs:
    @pytest.mark.parametrize("ns, expected", [
        ("proefenmeting", "ProefEnMeting"),
        ("implementatieelement", "ImplementatieElement"),
        ("abstracten", "Abstracten"),
        ("installatie", "Installatie"),
        ("levenscyclus", "Levenscyclus"),
        ("onderdeel", "Onderdeel"),
        ("besluit", "Besluit"),
        ("some_other_namespace", "Some_Other_Namespace"),
    ])
    def test_matches_python(self, ns, expected):
        assert rust_get_titlecase_from_ns(ns) == get_titlecase_from_ns(ns)
        assert rust_get_titlecase_from_ns(ns) == expected


class TestGetClassDirectoryFromNs:
    @pytest.mark.parametrize("ns, expected", [
        ("abstracten", "Classes/Abstracten"),
        ("implementatieelement", "Classes/ImplementatieElement"),
        ("installatie", "Classes/Installatie"),
        ("levenscyclus", "Classes/Levenscyclus"),
        ("onderdeel", "Classes/Onderdeel"),
        ("proefenmeting", "Classes/ProefEnMeting"),
        ("besluit", "Classes/Besluit"),
    ])
    def test_matches_python(self, ns, expected):
        assert rust_get_class_directory_from_ns(ns) == get_class_directory_from_ns(ns)
        assert rust_get_class_directory_from_ns(ns) == expected
