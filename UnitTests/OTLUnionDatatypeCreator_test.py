import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnion import OSLODatatypeUnion

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedDtu = ['# coding=utf-8',
               'from ..BaseClasses.OTLObject import OTLAttribuut',
               'from ..Datatypes.KwantWrdTest import KwantWrdTest, KwantWrdTestWaarden',
               'from ..BaseClasses.StringField import StringField',
               'from ..BaseClasses.UnionTypeField import UnionTypeField',
               'from ..BaseClasses.UnionWaarden import UnionWaarden',
               '',
               '',
               '# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit',
               'class DtuTestUnionTypeWaarden(UnionWaarden):',
               '    def __init__(self):',
               '        UnionWaarden.__init__(self)',
               '        self._unionKwantWrd = OTLAttribuut(field=KwantWrdTest,',
               "                                           naam='unionKwantWrd',",
               "                                           label='Union kwantitatieve "
               "waarde',",
               '                                           '
               "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionKwantWrd',",
               "                                           kardinaliteit_min='0',",
               "                                           definition='Kwantitatieve waarde "
               "van het test Union datatype',",
               '                                           owner=self)',
               '',
               '        self._unionString = OTLAttribuut(field=StringField,',
               "                                         naam='unionString',",
               "                                         label='Union tekstveld',",
               '                                         '
               "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString',",
               "                                         kardinaliteit_min='0',",
               "                                         definition='Vrij tekstveld van het "
               "test Union datatype',",
               '                                         owner=self)',
               '',
               '    @property',
               '    def unionKwantWrd(self) -> KwantWrdTestWaarden:',
               '        """Kwantitatieve waarde van het test Union datatype"""',
               '        return self._unionKwantWrd.get_waarde()',
               '',
               '    @unionKwantWrd.setter',
               '    def unionKwantWrd(self, value):',
               '        self._unionKwantWrd.set_waarde(value, owner=self._parent)',
               '        if value is not None:',
               "            self.clear_other_props('_unionKwantWrd')",
               '',
               '    @property',
               '    def unionString(self) -> str:',
               '        """Vrij tekstveld van het test Union datatype"""',
               '        return self._unionString.get_waarde()',
               '',
               '    @unionString.setter',
               '    def unionString(self, value):',
               '        self._unionString.set_waarde(value, owner=self._parent)',
               '        if value is not None:',
               "            self.clear_other_props('_unionString')",
               '',
               '',
               '# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit',
               'class DtuTestUnionType(UnionTypeField):',
               '    """Union datatype voor test doeleinden."""',
               "    naam = 'DtuTestUnionType'",
               "    label = 'Test UnionType'",
               '    objectUri = '
               "'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType'",
               "    definition = 'Union datatype voor test doeleinden.'",
               '    waardeObject = DtuTestUnionTypeWaarden',
               '',
               '    def __str__(self):',
               '        return UnionTypeField.__str__(self)',
               '']

union_datatype_validation_rules = {
    "valid_uri_and_types": {},
    "valid_regexes": ["^https://wegenenverkeer.data.vlaanderen.be/ns/.+#Dtu.+"]
}


def test_invalid_oslo_datatype_union(subtests):
    creator = OTLUnionDatatypeCreator(MagicMock(spec=OSLOCollector))

    with subtests.test(msg='empty name'):
        oslo_datatype_union = OSLODatatypeUnion(name='',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel'
                                                          '#DtuLichtmastMasthoogte',
                                                definition='', label='', usagenote='',
                                                deprecated_version='')

        with pytest.raises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_union_types(
                oslo_datatype_union, union_datatype_validation_rules=union_datatype_validation_rules)
        assert str(exception_bad_name.value) == "OSLODatatypeUnion.name is invalid. Value = ''"

    with subtests.test(msg='empty uri'):
        oslo_datatype_union = OSLODatatypeUnion(name='name', objectUri='', definition='', label='',
                                                usagenote='',
                                                deprecated_version='')

        with pytest.raises(ValueError) as exception_bad_uri:
            creator.create_block_to_write_from_union_types(
                oslo_datatype_union, union_datatype_validation_rules=union_datatype_validation_rules)
        assert str(exception_bad_uri.value) == "OSLODatatypeUnion.objectUri is invalid. Value = ''"

    with subtests.test(msg='bad uri'):
        oslo_datatype_union = OSLODatatypeUnion(name='name', objectUri='bad objectUri', definition='', label='',
                                                usagenote='',
                                                deprecated_version='')

        with pytest.raises(ValueError) as exception_bad_uri:
            creator.create_block_to_write_from_union_types(
                oslo_datatype_union, union_datatype_validation_rules=union_datatype_validation_rules)
        assert str(exception_bad_uri.value) == "OSLODatatypeUnion.objectUri is invalid. Value = 'bad objectUri'"

    with subtests.test(msg='invalid type'):
        with pytest.raises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_union_types(union_datatype=None,
                                                           union_datatype_validation_rules=union_datatype_validation_rules)
        assert str(exception_bad_name.value) == 'Input is not a OSLODatatypeUnion'


def set_up() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


def test_create_block():
    collector = set_up()
    creator = OTLUnionDatatypeCreator(collector)
    datatype_dtu_test_union_type = collector.find_union_datatype_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType')
    data_to_write = creator.create_block_to_write_from_union_types(
        datatype_dtu_test_union_type, union_datatype_validation_rules=union_datatype_validation_rules)
    assert data_to_write == expectedDtu
