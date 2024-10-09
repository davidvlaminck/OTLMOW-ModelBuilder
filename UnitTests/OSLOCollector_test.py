from pathlib import Path

import pytest
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLORelatie import OSLORelatie

r1 = OSLORelatie(bron_uri='A', doel_uri='B', bron_overerving='', doel_overerving='', objectUri='R1',
                 richting='Source -> Destination', usagenote='', deprecated_version='')
r2 = OSLORelatie(bron_uri='Z', doel_uri='B', bron_overerving='A', doel_overerving='', objectUri='R1',
                 richting='Source -> Destination', usagenote='', deprecated_version='')
r3 = OSLORelatie(bron_uri='B', doel_uri='C', bron_overerving='', doel_overerving='', objectUri='R3',
                 richting='Unspecified', usagenote='', deprecated_version='')
r4 = OSLORelatie(bron_uri='C', doel_uri='B', bron_overerving='', doel_overerving='', objectUri='R3',
                 richting='Unspecified', usagenote='', deprecated_version='')
r5 = OSLORelatie(bron_uri='A', doel_uri='D', bron_overerving='', doel_overerving='', objectUri='R1',
                 richting='Source -> Destination', usagenote='', deprecated_version='')
r6 = OSLORelatie(bron_uri='A', doel_uri='E', bron_overerving='', doel_overerving='', objectUri='R2',
                 richting='Source -> Destination', usagenote='', deprecated_version='')


@pytest.fixture
def oslo_collector():
    # Arrange
    # Create a mock OSLOCollector with some predefined relations
    relations = [r1, r2, r3, r4, r5, r6]
    c = OSLOCollector(Path(''))
    c.relations = relations
    return c


@pytest.mark.parametrize('objectUri, allow_duplicates, expected, test_id', [
    ('A', True, [r1, r5, r6], 'directional_duplicates_allowed'),
    ('A', False, [r1, r5, r6], 'directional_no_duplicates_allowed'),
    ('Z', True, [], 'filter_inherited_duplicates_allowed'),
    ('Z', False, [], 'filter_inherited_no_duplicates_allowed'),
    ('D', True, [r5], 'filter_by_target_duplicates_allowed'),
    ('D', False, [r5], 'filter_by_target_no_duplicates_allowed'),
    ('C', True, [r3, r4], 'nondirectional_duplicates_allowed'),
    ('C', False, [r4], 'nondirectional_no_duplicates_allowed'),
    ('B', True, [r1, r3, r4], 'both_duplicates_allowed'),
    ('B', False, [r1, r3], 'both_no_duplicates_allowed')
])
def test_find_all_relations(oslo_collector, objectUri, allow_duplicates, expected, test_id):
    # Act
    result = oslo_collector.find_all_relations(objectUri, allow_duplicates)

    # Assert
    assert result == expected, f"Failed test case: {test_id}"