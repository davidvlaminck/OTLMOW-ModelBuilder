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
