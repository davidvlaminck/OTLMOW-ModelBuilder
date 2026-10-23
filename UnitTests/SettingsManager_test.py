from pathlib import Path

import pytest

from otlmow_modelbuilder.SettingsManager import (
    _check_settings_with_default,
    load_settings,
)

DEFAULT_SETTINGS_PATH = Path(__file__).parent.parent / 'otlmow_modelbuilder' / 'settings_otlmow_modelbuilder.json'


def test_load_settings_returns_dict_with_expected_keys():
    settings = load_settings(None)

    assert isinstance(settings, dict)
    assert 'nested_list_attribute_uris' in settings
    assert 'class_validation_rules' in settings
    assert 'complex_datatype_validation_rules' in settings
    assert 'primitive_datatype_validation_rules' in settings
    assert 'union_datatype_validation_rules' in settings
    assert 'enumeration_validation_rules' in settings


def test_load_settings_with_explicit_path():
    settings = load_settings(DEFAULT_SETTINGS_PATH)

    assert isinstance(settings, dict)
    assert 'nested_list_attribute_uris' in settings


def test_load_settings_nonexistent_file_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_settings(Path('/nonexistent/path/settings.json'))


def test_check_settings_with_default_returns_default_path_when_none():
    result = _check_settings_with_default(None)

    assert result == DEFAULT_SETTINGS_PATH


def test_check_settings_with_default_nonexistent_path_raises():
    with pytest.raises(FileNotFoundError):
        _check_settings_with_default(Path('/nonexistent/path/settings.json'))
