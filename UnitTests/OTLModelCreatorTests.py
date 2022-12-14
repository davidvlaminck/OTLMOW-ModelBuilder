import logging
from pathlib import Path
from unittest import TestCase

from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLModelCreator import OTLModelCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from otlmow_modelbuilder.SQLDbReader import SQLDbReader


class OTLModelCreatorTests(TestCase):
    def test_nested_lists(self):
        current_file_path = Path(__file__)
        base_dir = current_file_path.parents[0]
        subset_file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')

        sql_reader = SQLDbReader(subset_file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        with self.subTest('valid testclass, no nested lists'):
            OTLModelCreator.check_for_nested_attributes_in_classes(collector=collector)
            self.assertTrue(True)

        with self.subTest('invalid testclass, with nested lists'):
            c = OSLODatatypeComplexAttribuut(
                name='testKwantWrdMetKard', label='Test kwantitatieve waarde met kardinaliteit',
                definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1 in een complex datatype.',
                class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
                kardinaliteit_min='1', kardinaliteit_max='*',
                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTestMetKard',
                type='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2',
                overerving=0, constraints='', readonly=0, usagenote='', deprecated_version='')
            collector.complex_datatype_attributen.append(c)

            with self.assertRaises(NotImplementedError) as exc:
                OTLModelCreator.check_for_nested_attributes_in_classes(collector=collector)
