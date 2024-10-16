from pathlib import Path

import pytest
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLORelatie import OSLORelatie


# see collector_relations_with_inheritances.png for a visual representation of the relations

i1 = Inheritance(base_name='A', base_uri='A', class_uri='B', class_name='B', deprecated_version='')
i2 = Inheritance(base_name='A', base_uri='A', class_uri='C', class_name='C', deprecated_version='')
i3 = Inheritance(base_name='A', base_uri='A', class_uri='F', class_name='F', deprecated_version='')
i4 = Inheritance(base_name='B', base_uri='B', class_uri='D', class_name='D', deprecated_version='')
i5 = Inheritance(base_name='B', base_uri='B', class_uri='E', class_name='E', deprecated_version='')
i6 = Inheritance(base_name='C', base_uri='C', class_uri='G', class_name='G', deprecated_version='')
i7 = Inheritance(base_name='C', base_uri='C', class_uri='H', class_name='H', deprecated_version='')

r1 = OSLORelatie(bron_uri='A', doel_uri='I', bron_overerving='', doel_overerving='', objectUri='R1',
                 richting='Source -> Destination', usagenote='', deprecated_version='')
r11 = OSLORelatie(bron_uri='D', doel_uri='I', bron_overerving='A', doel_overerving='', objectUri='R1',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r12 = OSLORelatie(bron_uri='E', doel_uri='I', bron_overerving='A', doel_overerving='', objectUri='R1',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r13 = OSLORelatie(bron_uri='F', doel_uri='I', bron_overerving='A', doel_overerving='', objectUri='R1',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r14 = OSLORelatie(bron_uri='G', doel_uri='I', bron_overerving='A', doel_overerving='', objectUri='R1',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r15 = OSLORelatie(bron_uri='H', doel_uri='I', bron_overerving='A', doel_overerving='', objectUri='R1',
                  richting='Source -> Destination', usagenote='', deprecated_version='')

r2 = OSLORelatie(bron_uri='B', doel_uri='B', bron_overerving='', doel_overerving='', objectUri='R2',
                 richting='Source -> Destination', usagenote='', deprecated_version='')
r21 = OSLORelatie(bron_uri='D', doel_uri='D', bron_overerving='B', doel_overerving='', objectUri='R2',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r22 = OSLORelatie(bron_uri='D', doel_uri='E', bron_overerving='B', doel_overerving='', objectUri='R2',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r23 = OSLORelatie(bron_uri='E', doel_uri='E', bron_overerving='B', doel_overerving='', objectUri='R2',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r24 = OSLORelatie(bron_uri='E', doel_uri='D', bron_overerving='B', doel_overerving='', objectUri='R2',
                  richting='Source -> Destination', usagenote='', deprecated_version='')

r3a = OSLORelatie(bron_uri='B', doel_uri='F', bron_overerving='', doel_overerving='', objectUri='R3',
                 richting='Source -> Destination', usagenote='', deprecated_version='')
r31 = OSLORelatie(bron_uri='D', doel_uri='F', bron_overerving='B', doel_overerving='', objectUri='R3',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r32 = OSLORelatie(bron_uri='E', doel_uri='F', bron_overerving='B', doel_overerving='', objectUri='R3',
                  richting='Source -> Destination', usagenote='', deprecated_version='')

r3b = OSLORelatie(bron_uri='F', doel_uri='C', bron_overerving='', doel_overerving='', objectUri='R3',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r33 = OSLORelatie(bron_uri='F', doel_uri='G', bron_overerving='', doel_overerving='C', objectUri='R3',
                  richting='Source -> Destination', usagenote='', deprecated_version='')
r34 = OSLORelatie(bron_uri='F', doel_uri='H', bron_overerving='', doel_overerving='C', objectUri='R3',
                  richting='Source -> Destination', usagenote='', deprecated_version='')

r4 = OSLORelatie(bron_uri='G', doel_uri='H', bron_overerving='', doel_overerving='', objectUri='R4',
                 richting='Source -> Destination', usagenote='', deprecated_version='')

r5a = OSLORelatie(bron_uri='B', doel_uri='G', bron_overerving='', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r5b = OSLORelatie(bron_uri='G', doel_uri='B', bron_overerving='', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r51 = OSLORelatie(bron_uri='D', doel_uri='G', bron_overerving='B', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r52 = OSLORelatie(bron_uri='E', doel_uri='G', bron_overerving='B', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r53 = OSLORelatie(bron_uri='G', doel_uri='D', bron_overerving='', doel_overerving='B', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r54 = OSLORelatie(bron_uri='G', doel_uri='E', bron_overerving='', doel_overerving='B', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')

r6 = OSLORelatie(bron_uri='C', doel_uri='C', bron_overerving='', doel_overerving='', objectUri='R5',
                 richting='Unspecified', usagenote='', deprecated_version='')
r61 = OSLORelatie(bron_uri='G', doel_uri='H', bron_overerving='C', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r62 = OSLORelatie(bron_uri='H', doel_uri='G', bron_overerving='C', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r63 = OSLORelatie(bron_uri='G', doel_uri='G', bron_overerving='C', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')
r64 = OSLORelatie(bron_uri='H', doel_uri='H', bron_overerving='C', doel_overerving='', objectUri='R5',
                  richting='Unspecified', usagenote='', deprecated_version='')

c1 = OSLOClass(label='A', name='A', objectUri='A', definition='', usagenote='', abstract=1, deprecated_version='')
c2 = OSLOClass(label='B', name='B', objectUri='B', definition='', usagenote='', abstract=1, deprecated_version='')
c3 = OSLOClass(label='C', name='C', objectUri='C', definition='', usagenote='', abstract=1, deprecated_version='')
c4 = OSLOClass(label='D', name='D', objectUri='D', definition='', usagenote='', abstract=0, deprecated_version='')
c5 = OSLOClass(label='E', name='E', objectUri='E', definition='', usagenote='', abstract=0, deprecated_version='')
c6 = OSLOClass(label='F', name='F', objectUri='F', definition='', usagenote='', abstract=0, deprecated_version='')
c7 = OSLOClass(label='G', name='G', objectUri='G', definition='', usagenote='', abstract=0, deprecated_version='')
c8 = OSLOClass(label='H', name='H', objectUri='H', definition='', usagenote='', abstract=0, deprecated_version='')
c9 = OSLOClass(label='I', name='I', objectUri='I', definition='', usagenote='', abstract=0, deprecated_version='')


@pytest.fixture
def oslo_collector():
    # Arrange
    # Create a mock OSLOCollector with some predefined relations
    c = OSLOCollector(Path(''))
    c.inheritances = [i1, i2, i3, i4, i5, i6, i7]
    c.relations = [r1, r11, r12, r13, r14, r15, r2, r21, r22, r23, r24, r3a, r31, r32, r3b, r33, r34, r4, r5a, r5b,
                   r51, r52, r53, r54, r6, r61, r62, r63, r64]
    c.classes = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
    c.class_dict = {c.objectUri: c for c in c.classes}
    return c


@pytest.mark.parametrize('objectUri, allow_duplicates, expected, test_id', [
    ('A', True, [r1], 'from_A_duplicates_allowed'),
    ('A', False, [r1], 'from_A_no_duplicates_allowed'),
    ('B', True, [r2, r3a, r5a, r5b], 'from_B_duplicates_allowed'),
    ('B', False, [r2, r3a, r5a], 'from_B_no_duplicates_allowed'),
    ('C', True, [r3b, r6], 'from_C_duplicates_allowed'),
    ('C', False, [r3b, r6], 'from_C_no_duplicates_allowed'),
    ('D', True, [], 'from_D_duplicates_allowed'),
    ('D', False, [], 'from_D_no_duplicates_allowed'),
    ('E', True, [], 'from_E_duplicates_allowed'),
    ('E', False, [], 'from_E_no_duplicates_allowed'),
    ('F', True, [r3a, r3b], 'from_F_duplicates_allowed'),
    ('F', False, [r3a, r3b], 'from_F_no_duplicates_allowed'),
    ('G', True, [r4, r5a, r5b], 'from_G_duplicates_allowed'),
    ('G', False, [r4, r5b], 'from_G_no_duplicates_allowed'),
    ('H', True, [r4], 'from_H_duplicates_allowed'),
    ('H', False, [r4], 'from_H_no_duplicates_allowed'),
    ('I', True, [r1], 'from_I_duplicates_allowed'),
    ('I', False, [r1], 'from_I_no_duplicates_allowed')
])
def test_find_all_relations(oslo_collector, objectUri, allow_duplicates, expected, test_id):
    # Act
    result = oslo_collector.find_all_relations(objectUri, allow_duplicates)

    # Assert
    assert result == expected, f"Failed test case: {test_id}"


@pytest.mark.parametrize('objectUri, allow_duplicates, expected, test_id', [
    ('D', True, [r11, r21, r22, r24, r31, r51, r53 ], 'from_D_duplicates_allowed'),
    ('D', False, [r11, r21, r22, r24, r31, r51], 'from_D_no_duplicates_allowed'),

    ('E', True, [r12, r22, r23, r24, r32, r52, r54], 'from_E_duplicates_allowed'),
    ('E', False, [r12, r22, r23, r24, r32, r52], 'from_E_no_duplicates_allowed'),

    ('F', True, [r13, r31, r32, r33, r34], 'from_F_duplicates_allowed'),
    ('F', False, [r13, r31, r32, r33, r34], 'from_F_no_duplicates_allowed'),

    ('G', True, [r14, r33, r4, r51, r52, r53, r54, r61, r62, r63], 'from_G_duplicates_allowed'),
    ('G', False, [r14, r33, r4, r53, r54, r61, r63], 'from_G_no_duplicates_allowed'),

    ('H', True, [r15, r34, r4, r61, r62, r64], 'from_H_duplicates_allowed'),
    ('H', False, [r15, r34, r4, r62, r64], 'from_H_no_duplicates_allowed'),

    ('I', True, [r11, r12, r13, r14, r15], 'from_I_duplicates_allowed'),
    ('I', False, [r11, r12, r13, r14, r15], 'from_I_no_duplicates_allowed'),
])
def test_find_all_concrete_relations(oslo_collector, objectUri, allow_duplicates, expected, test_id):
    # Act
    result = oslo_collector.find_all_concrete_relations(objectUri, allow_duplicates)

    # Assert
    assert result == expected, f"Failed test case: {test_id}"


def test_find_all_concrete_relations_input_not_concrete(oslo_collector):
    with pytest.raises(ValueError):
        oslo_collector.find_all_concrete_relations('A')
    with pytest.raises(ValueError):
        oslo_collector.find_all_concrete_relations('B')
    with pytest.raises(ValueError):
        oslo_collector.find_all_concrete_relations('C')
    with pytest.raises(ValueError):
        oslo_collector.find_all_concrete_relations('Z')
