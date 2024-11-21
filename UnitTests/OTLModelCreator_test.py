from pathlib import Path

import pytest

from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut


def test_nested_lists(subtests):
    current_file_path = Path(__file__)
    base_dir = current_file_path.parents[0]
    subset_file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')

    collector = OSLOCollector(subset_file_location)
    collector.collect_all()

    with subtests.test(msg='valid testclass, no nested lists'):
        OTLModelCreator.check_for_nested_attributes_in_classes(collector=collector)

    with subtests.test(msg='invalid testclass, with nested lists'):
        c = OSLODatatypeComplexAttribuut(
            name='testKwantWrdMetKard', label='Test kwantitatieve waarde met kardinaliteit',
            definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1 in een complex filename.',
            class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
            kardinaliteit_min='1', kardinaliteit_max='*',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTestMetKard',
            type='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
            overerving=0, constraints='', readonly=0, usagenote='', deprecated_version='')
        collector.complex_datatype_attributen.append(c)

        with pytest.raises(NotImplementedError):
            OTLModelCreator.check_for_nested_attributes_in_classes(collector=collector)


def test_generate_relation_dict():
    current_file_path = Path(__file__)
    base_dir = current_file_path.parents[0]
    subset_file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')

    collector = OSLOCollector(subset_file_location)
    collector.collect_all()

    relation_dict = OTLModelCreator.generate_relation_dict(oslo_collector=collector)
    expected_relaltion_dict = {
        "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt": {
            "directional": True
        },
        "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging": {
            "directional": False
        }
    }

    assert relation_dict == expected_relaltion_dict


def test_generate_class_dict():
    current_file_path = Path(__file__)
    base_dir = current_file_path.parents[0]
    subset_file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')

    collector = OSLOCollector(subset_file_location)
    collector.collect_all()

    class_dict = OTLModelCreator.generate_class_dict(oslo_collector=collector)
    expected_class_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus':
            {'abstract': True, 'deprecated_version': '', 'label': 'AIM databank status', 'name': 'AIMDBStatus'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject':
            {'abstract': True, 'deprecated_version': '', 'label': 'AIM object', 'name': 'AIMObject'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand':
            {'abstract': True, 'deprecated_version': '', 'label': 'AIM Toestand', 'name': 'AIMToestand'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie':
            {'abstract': True, 'deprecated_version': '', 'label': 'Directionele relatie', 'name': 'DirectioneleRelatie'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie':
            {'abstract': True, 'deprecated_version': '', 'label': 'Niet-directionele relatie',
             'name': 'NietDirectioneleRelatie'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject':
            {'abstract': True, 'deprecated_version': '', 'label': 'Relatieobject', 'name': 'RelatieObject'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass':
            {'abstract': False, 'deprecated_version': '', 'label': 'All Cases TestClass', 'name': 'AllCasesTestClass'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass':
            {'abstract': False, 'deprecated_version': '', 'label': 'Another TestClass', 'name': 'AnotherTestClass'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging':
            {'abstract': False, 'deprecated_version': '', 'label': 'Bevestiging', 'name': 'Bevestiging'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass':
            {'abstract': False, 'deprecated_version': '2.0.0', 'label': 'Deprecated TestClass',
             'name': 'DeprecatedTestClass'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt':
            {'abstract': False, 'deprecated_version': '', 'label': 'Voedt', 'name': 'Voedt'}
    }

    assert class_dict == expected_class_dict
