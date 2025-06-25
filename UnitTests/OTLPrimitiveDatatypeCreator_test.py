import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import OSLODatatypePrimitive
from otlmow_modelbuilder.SQLDataClasses.OSLOTypeLink import OSLOTypeLink

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class PrimitiveDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.typeLinks = [
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#string", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#decimal", "OSLODatatypePrimitive", ""),
            OSLOTypeLink('http://www.w3.org/2000/01/rdf-schema#Literal', "OSLODatatypePrimitive", "")]


primitive_datatype_validation_rules = {
    "valid_uri_and_types": {},
    "valid_regexes": [
        "^http://www.w3.org/200.+",
        "^https://wegenenverkeer.data.vlaanderen.be/ns/.+#Dte.+",
        "^https://wegenenverkeer.data.vlaanderen.be/ns/.+#KwantWrd.+"]
}


def test_InvalidOSLODatatypePrimitiveEmptyUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLPrimitiveDatatypeCreator(collector)
    oslo_datatype_primitive = OSLODatatypePrimitive(name='name', objectUri='', definition='', label='',
                                                    usagenote='', deprecated_version='')

    with pytest.raises(ValueError) as exception_empty_uri:
        creator.create_block_to_write_from_primitive_types(
            oslo_datatype_primitive, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert str(exception_empty_uri.value) == "OSLODatatypePrimitive.objectUri is invalid. Value = ''"


def test_InvalidOSLODatatypePrimitiveBadUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLPrimitiveDatatypeCreator(collector)
    oslo_datatype_primitive = OSLODatatypePrimitive(name='name', objectUri='Bad objectUri', definition='', label='',
                                                    usagenote='', deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_uri:
        creator.create_block_to_write_from_primitive_types(
            oslo_datatype_primitive, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert str(exception_bad_uri.value) == "OSLODatatypePrimitive.objectUri is invalid. Value = 'Bad objectUri'"


def test_InvalidOSLODatatypePrimitiveEmptyName():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLPrimitiveDatatypeCreator(collector)
    oslo_datatype_primitive = OSLODatatypePrimitive(
        name='', objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd1',
        definition='', label='', usagenote='', deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_block_to_write_from_primitive_types(
            oslo_datatype_primitive, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert str(exception_bad_name.value) == "OSLODatatypePrimitive.name is invalid. Value = ''"


def test_InValidType():
    bad_primitive = True
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLPrimitiveDatatypeCreator(collector)
    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_block_to_write_from_primitive_types(
            bad_primitive, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert str(exception_bad_name.value) == "Input is not a OSLODatatypePrimitive"


def test_ValidOSLODatatypePrimitive():
    boolean_primitive = OSLODatatypePrimitive(name="Boolean", objectUri="http://www.w3.org/2001/XMLSchema#boolean",
                                              definition="Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.",
                                              label="Boolean", usagenote="https://www.w3.org/TR/xmlschema-2/#boolean",
                                              deprecated_version="")
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    collector.primitive_datatype_attributen = []
    creator = OTLPrimitiveDatatypeCreator(collector)
    block_to_write = creator.create_block_to_write_from_primitive_types(
        boolean_primitive, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert (block_to_write ==
            ['# coding=utf-8', 'from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut',
             'from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField',
             'from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject',
             '',
             '',
             '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
             'class BooleanWaarden(WaardenObject):',
             '    def __init__(self):',
             '        WaardenObject.__init__(self)',
             '',
             '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
             'class Boolean(OTLField):',
             '    """Beschrijft een boolean volgens '
             'http://www.w3.org/2001/XMLSchema#boolean."""',
             "    naam = 'Boolean'",
             "    label = 'Boolean'",
             "    objectUri = 'http://www.w3.org/2001/XMLSchema#boolean'",
             "    definition = 'Beschrijft een boolean volgens "
             "http://www.w3.org/2001/XMLSchema#boolean.'",
             "    usagenote = 'https://www.w3.org/TR/xmlschema-2/#boolean'",
             '    waarde_shortcut_applicable = True',
             '    waardeObject = BooleanWaarden',
             '',
             '    def __str__(self):',
             '        return OTLField.__str__(self)',
             ''])


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def test_create_block_dte():
    collector = set_up()
    creator = OTLPrimitiveDatatypeCreator(collector)
    datatype_DteTestEenvoudigType = collector.find_primitive_datatype_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType')
    data_to_write = creator.create_block_to_write_from_primitive_types(
        datatype_DteTestEenvoudigType, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert data_to_write == expectedDte


def test_create_block_kwant_wrd():
    collector = set_up()
    creator = OTLPrimitiveDatatypeCreator(collector)
    datatype_KwantWrdTest = collector.find_primitive_datatype_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest')
    data_to_write = creator.create_block_to_write_from_primitive_types(
        datatype_KwantWrdTest, primitive_datatype_validation_rules=primitive_datatype_validation_rules)
    assert data_to_write == expectedKwantWrd


expectedKwantWrd = ['# coding=utf-8',
                    'from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut',
                    'from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField',
                    'from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject',
                    'from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField',
                    'from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField',
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
                    '    def standaardEenheid(self) -> str:',
                    '        """De standaard eenheid bij dit datatype is uitgedrukt in percent."""',
                    '        return self._standaardEenheid.usagenote.split(\'"\')[1]',
                    '',
                    '    @property',
                    '    def waarde(self) -> float:',
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
               'from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut',
               'from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField',
               'from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject',
               'from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField',
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
               '    def waarde(self) -> str:',
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
