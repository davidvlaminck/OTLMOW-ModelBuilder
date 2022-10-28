import os
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import OSLODatatypePrimitive
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOTypeLink import OSLOTypeLink
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class PrimitiveDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.typeLinks = [
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#string", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#decimal", "OSLODatatypePrimitive", ""),
            OSLOTypeLink('http://www.w3.org/2000/01/rdf-schema#Literal', "OSLODatatypePrimitive", "")]


class OTLPrimitiveDatatypeCreatorTests(unittest.TestCase):
    def test_InvalidOSLODatatypePrimitiveEmptyUri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLPrimitiveDatatypeCreator(collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', objectUri='', definition='', label='', usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.create_block_to_write_from_primitive_types(osloDatatypePrimitive)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypePrimitive.objectUri is invalid. Value = ''")

    def test_InvalidOSLODatatypePrimitiveBadUri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLPrimitiveDatatypeCreator(collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', objectUri='Bad objectUri', definition='', label='',
                                                      usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.create_block_to_write_from_primitive_types(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypePrimitive.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLODatatypePrimitiveEmptyName(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLPrimitiveDatatypeCreator(collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                                      definition='', label='', usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_primitive_types(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypePrimitive.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_primitive = True
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLPrimitiveDatatypeCreator(collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_primitive_types(bad_primitive)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypePrimitive")

    def test_ValidOSLODatatypePrimitiveButNoResult(self):
        boolean_primitive = OSLODatatypePrimitive(name="Boolean", objectUri="http://www.w3.org/2001/XMLSchema#boolean",
                                                  definition="Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.",
                                                  label="Boolean", usagenote="https://www.w3.org/TR/xmlschema-2/#boolean",
                                                  deprecated_version="")
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        creator = OTLPrimitiveDatatypeCreator(collector)
        blockToWrite = creator.create_block_to_write_from_primitive_types(boolean_primitive)
        self.assertIsNone(blockToWrite)

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_create_block_dte(self):
        collector = self.setUp()
        creator = OTLPrimitiveDatatypeCreator(collector)
        datatype_DteTestEenvoudigType = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType')
        data_to_write = creator.create_block_to_write_from_primitive_types(datatype_DteTestEenvoudigType)
        self.assertEqual(expectedDte, data_to_write)

    def test_create_block_kwant_wrd(self):
        collector = self.setUp()
        creator = OTLPrimitiveDatatypeCreator(collector)
        datatype_KwantWrdTest = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest')
        data_to_write = creator.create_block_to_write_from_primitive_types(datatype_KwantWrdTest)
        self.assertEqual(expectedKwantWrd, data_to_write)


expectedKwantWrd = ['# coding=utf-8',
                    'from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut',
                    'from otlmow_model.BaseClasses.OTLField import OTLField',
                    'from otlmow_model.BaseClasses.WaardenObject import WaardenObject',
                    'from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField',
                    'from otlmow_model.BaseClasses.StringField import StringField',
                    '',
                    '',
                    '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
                    'class KwantWrdTestWaarden(WaardenObject):',
                    '    def __init__(self):',
                    '        WaardenObject.__init__(self)',
                    '        self._standaardEenheid = OTLAttribuut(field=StringField,',
                    "                                              naam='standaardEenheid',",
                    "                                              label='standaard eenheid',",
                    '                                              '
                    "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.standaardEenheid',",
                    '                                              usagenote=\'"%"^^cdt:ucumunit\',',
                    "                                              readonly=True,",
                    '                                              constraints=\'"%"^^cdt:ucumunit\',',
                    "                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in percent.',",
                    '                                              owner=self)',
                    '',
                    '        self._waarde = OTLAttribuut(field=FloatOrDecimalField,',
                    "                                    naam='waarde',",
                    "                                    label='waarde',",
                    '                                    '
                    "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde',",
                    "                                    definition='Bevat een getal die bij het datatype hoort.',",
                    '                                    owner=self)',
                    '',
                    '    @property',
                    '    def standaardEenheid(self):',
                    '        """De standaard eenheid bij dit datatype is uitgedrukt in percent."""',
                    '        return self._standaardEenheid.usagenote.split(\'"\')[1]',
                    '',
                    '    @property',
                    '    def waarde(self):',
                    '        """Bevat een getal die bij het datatype hoort."""',
                    '        return self._waarde.get_waarde()',
                    '',
                    '    @waarde.setter',
                    '    def waarde(self, value):',
                    '        self._waarde.set_waarde(value, owner=self._parent)',
                    '',
                    '',
                    '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
                    'class KwantWrdTest(OTLField):',
                    '    """Een kwantitatieve waarde voor test doeleinden."""',
                    "    naam = 'KwantWrdTest'",
                    "    label = 'Kwantitatieve test waarde'",
                    '    objectUri = '
                    "'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest'",
                    "    definition = 'Een kwantitatieve waarde voor test doeleinden.'",
                    '    waarde_shortcut_applicable = True',
                    '    waardeObject = KwantWrdTestWaarden',
                    '',
                    '    def __str__(self):',
                    '        return OTLField.__str__(self)',
                    '']

expectedDte = ['# coding=utf-8',
               'from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut',
               'from otlmow_model.BaseClasses.OTLField import OTLField',
               'from otlmow_model.BaseClasses.WaardenObject import WaardenObject',
               'from otlmow_model.BaseClasses.StringField import StringField',
               '',
               '',
               '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
               'class DteTestEenvoudigTypeWaarden(WaardenObject):',
               '    def __init__(self):',
               '        WaardenObject.__init__(self)',
               '        self._waarde = OTLAttribuut(field=StringField,',
               "                                    naam='waarde',",
               "                                    label='waarde',",
               '                                    '
               "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde',",
               "                                    definition='De string die het eenvoudige "
               "test datatype voorstelt.',",
               '                                    owner=self)',
               '',
               '    @property',
               '    def waarde(self):',
               '        """De string die het eenvoudige test datatype voorstelt."""',
               '        return self._waarde.get_waarde()',
               '',
               '    @waarde.setter',
               '    def waarde(self, value):',
               '        self._waarde.set_waarde(value, owner=self._parent)',
               '',
               '',
               '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
               'class DteTestEenvoudigType(OTLField):',
               '    """Beschrijft een tekst van een eenvoudig type."""',
               "    naam = 'DteTestEenvoudigType'",
               "    label = 'Test EenvoudigType'",
               '    objectUri = '
               "'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType'",
               "    definition = 'Beschrijft een tekst van een eenvoudig type.'",
               '    waarde_shortcut_applicable = True',
               '    waardeObject = DteTestEenvoudigTypeWaarden',
               '',
               '    def __str__(self):',
               '        return OTLField.__str__(self)',
               '']
