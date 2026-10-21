from pathlib import Path

from otlmow_modelbuilder.OTLExtraChecker import OTLExtraChecker


def _naam_object_lines():
    return [
        '# coding=utf-8',
        'from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut',
        'from ..BaseClasses.StringField import StringField',
        '',
        '',
        'class AIMNaamObject(AIMObject):',
        '    """AIM Naam Object."""',
        '',
        "    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AIMNaamObject'",
        '',
        '    def __init__(self):',
        '        super().__init__()',
        '',
        "        self._naam = OTLAttribuut(field=StringField,",
        "                                  naam='naam',",
        "                                  label='Naam',",
        "                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AIMNaamObject.naam',",
        "                                  definition='De naam van het object.',",
        '                                  owner=self)',
        '',
    ]


def _naampad_object_lines():
    return [
        '# coding=utf-8',
        'from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject',
        'from ..BaseClasses.StringField import StringField',
        '',
        '',
        'class NaampadObject(AIMNaamObject):',
        '    """Naampad Object."""',
        '',
        "    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NaampadObject'",
        '',
        '    def __init__(self):',
        '        super().__init__()',
        '',
        "        self._naampad = OTLAttribuut(field=StringField,",
        "                                     naam='naampad',",
        "                                     label='Naampad',",
        "                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NaampadObject.naampad',",
        "                                     definition='De naampad van het object.',",
        '                                     owner=self)',
        '',
    ]


def _write_naam_object(tmp_path: Path):
    target = tmp_path / 'Classes' / 'ImplementatieElement' / 'AIMNaamObject.py'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(_naam_object_lines()))
    return target


def _write_naampad_object(tmp_path: Path):
    target = tmp_path / 'Classes' / 'ImplementatieElement' / 'NaampadObject.py'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(_naampad_object_lines()))
    return target


def test_modify_naamfield_adds_import_and_replaces_field(tmp_path):
    path = _write_naam_object(tmp_path)

    OTLExtraChecker.modify_naamfield(tmp_path)

    content = path.read_text()
    assert 'import re\n' in content
    assert 'class NaamField(StringField):\n' in content
    assert "self._naam = OTLAttribuut(field=NaamField,\n" in content
    assert 'field=StringField' not in content


def test_modify_naamfield_missing_file_is_noop(tmp_path):
    OTLExtraChecker.modify_naamfield(tmp_path)

    assert not (tmp_path / 'Classes' / 'ImplementatieElement' / 'AIMNaamObject.py').exists()


def test_modify_naampad_field_adds_import_and_replaces_field(tmp_path):
    path = _write_naampad_object(tmp_path)

    OTLExtraChecker.modify_naampad_field(tmp_path)

    content = path.read_text()
    assert 'import re\n' in content
    assert 'class NaampadField(NaamField):\n' in content
    assert "self._naampad = OTLAttribuut(field=NaampadField,\n" in content
    assert 'from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject, NaamField\n' in content
    assert 'field=StringField' not in content


def test_modify_naampad_field_missing_file_is_noop(tmp_path):
    OTLExtraChecker.modify_naampad_field(tmp_path)

    assert not (tmp_path / 'Classes' / 'ImplementatieElement' / 'NaampadObject.py').exists()


def test_modify_for_extra_checks_calls_both(tmp_path):
    _write_naam_object(tmp_path)
    _write_naampad_object(tmp_path)

    OTLExtraChecker.modify_for_extra_checks(tmp_path)

    naam_content = (tmp_path / 'Classes' / 'ImplementatieElement' / 'AIMNaamObject.py').read_text()
    naampad_content = (tmp_path / 'Classes' / 'ImplementatieElement' / 'NaampadObject.py').read_text()

    assert 'class NaamField(StringField):\n' in naam_content
    assert 'class NaampadField(NaamField):\n' in naampad_content
