from pathlib import Path
from unittest import mock

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.OSLOCollector import OSLOCollector

OTL_DB = Path(__file__).parent / 'OTL_AllCasesTestClass.db'
DTC_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'


def _creator():
    collector = OSLOCollector(OTL_DB)
    collector.collect_all()
    return collector, AbstractDatatypeCreator(collector)


def test_create_block_returns_list_starting_with_header():
    collector, creator = _creator()
    dtc = collector.find_complex_datatype_by_uri(DTC_URI)

    result = creator.create_block_to_write_from_complex_primitive_or_union_types(
        dtc, type_field='Complex')

    assert isinstance(result, list)
    assert result[0] == '# coding=utf-8'
    assert 'class DtcIdentificatorWaarden' in '\n'.join(result)
    assert 'class DtcIdentificator(ComplexField)' in '\n'.join(result)


def test_create_block_primitive_type():
    collector, creator = _creator()
    dtc = collector.find_complex_datatype_by_uri(DTC_URI)

    result = creator.create_block_to_write_from_complex_primitive_or_union_types(
        dtc, type_field='Primitive')

    assert isinstance(result, list)
    assert result[0] == '# coding=utf-8'


def test_create_block_union_type():
    collector, creator = _creator()
    dtc = collector.find_complex_datatype_by_uri(DTC_URI)

    result = creator.create_block_to_write_from_complex_primitive_or_union_types(
        dtc, type_field='UnionType')

    assert isinstance(result, list)
    assert result[0] == '# coding=utf-8'


def test_create_block_falls_back_to_python_when_rust_fails(monkeypatch):
    collector, creator = _creator()
    dtc = collector.find_complex_datatype_by_uri(DTC_URI)

    # Force the rust call to raise so the Python fallback path is exercised.
    def rust_raises(*args, **kwargs):
        raise RuntimeError('rust unavailable')

    with mock.patch(
        'otlmow_modelbuilder._otlmow_modelbuilder_rs.'
        'create_block_to_write_from_complex_primitive_or_union_types',
        rust_raises,
    ):
        result = creator.create_block_to_write_from_complex_primitive_or_union_types(
            dtc, type_field='Complex')

    assert isinstance(result, list)
    assert result[0] == '# coding=utf-8'
    assert 'class DtcIdentificatorWaarden(WaardenObject):' in '\n'.join(result)
    assert 'class DtcIdentificator(ComplexField)' in '\n'.join(result)
