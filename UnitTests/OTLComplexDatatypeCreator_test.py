import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplex import OSLODatatypeComplex
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedDtc = ["# coding=utf-8",
               "from otlmow_model.BaseClasses.OTLObject import OTLAttribuut",
               "from otlmow_model.BaseClasses.WaardenObject import WaardenObject",
               "from otlmow_model.BaseClasses.ComplexField import ComplexField",
               "from otlmow_model.BaseClasses.StringField import StringField",
               "",
               "",
               "# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit",
               "class DtcIdentificatorWaarden(WaardenObject):",
               "    def __init__(self):",
               "        WaardenObject.__init__(self)",
               "        self._identificator = OTLAttribuut(field=StringField,",
               "                                           naam='identificator',",
               "                                           label='identificator',",
               "                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',",
               "                                           definition='Een groep van tekens om een AIM object te identificeren of te benoemen.',",
               "                                           owner=self)",
               "",
               "        self._toegekendDoor = OTLAttribuut(field=StringField,",
               "                                           naam='toegekendDoor',",
               "                                           label='toegekend door',",
               "                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',",
               "                                           definition='Gegevens van de organisatie die de toekenning deed.',",
               "                                           owner=self)",
               "",
               "    @property",
               "    def identificator(self) -> str:",
               '        """Een groep van tekens om een AIM object te identificeren of te benoemen."""',
               "        return self._identificator.get_waarde()",
               "",
               "    @identificator.setter",
               "    def identificator(self, value):",
               "        self._identificator.set_waarde(value, owner=self._parent)",
               "",
               "    @property",
               "    def toegekendDoor(self) -> str:",
               '        """Gegevens van de organisatie die de toekenning deed."""',
               "        return self._toegekendDoor.get_waarde()",
               "",
               "    @toegekendDoor.setter",
               "    def toegekendDoor(self, value):",
               "        self._toegekendDoor.set_waarde(value, owner=self._parent)",
               "",
               "",
               "# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit",
               "class DtcIdentificator(ComplexField):",
               '    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""',
               "    naam = 'DtcIdentificator'",
               "    label = 'Identificator'",
               "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'",
               "    definition = 'Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.'",
               "    waardeObject = DtcIdentificatorWaarden",
               "",
               "    def __str__(self):",
               "        return ComplexField.__str__(self)",
               ""]

complex_datatype_validation_rules = {'valid_uri_and_types': {},
                                     'valid_regexes': ["^https://wegenenverkeer.data.vlaanderen.be/ns/.+#Dtc.+"]}


def test_InvalidOSLODatatypeComplexEmptyUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLComplexDatatypeCreator(collector)
    oslo_datatype_complex = OSLODatatypeComplex(name='name', objectUri='', definition='', label='', usagenote='',
                                                deprecated_version='')

    with pytest.raises(ValueError) as exception_empty_uri:
        creator.create_block_to_write_from_complex_types(
            oslo_datatype_complex, complex_datatype_validation_rules=complex_datatype_validation_rules)
    assert str(exception_empty_uri.value) == "OSLODatatypeComplex.objectUri is invalid. Value = ''"


def test_InvalidOSLODatatypeComplexBadUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLComplexDatatypeCreator(collector)
    oslo_datatype_complex = OSLODatatypeComplex(name='name', objectUri='Bad objectUri', definition='', label='',
                                                usagenote='', deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_uri:
        creator.create_block_to_write_from_complex_types(
            oslo_datatype_complex, complex_datatype_validation_rules=complex_datatype_validation_rules)
    assert str(exception_bad_uri.value) == "OSLODatatypeComplex.objectUri is invalid. Value = 'Bad objectUri'"


def test_InvalidOSLODatatypeComplexEmptyName():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLComplexDatatypeCreator(collector)
    oslo_datatype_complex = OSLODatatypeComplex(
        name='', definition='', label='', usagenote='', deprecated_version='',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')

    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_block_to_write_from_complex_types(
            oslo_datatype_complex, complex_datatype_validation_rules=complex_datatype_validation_rules)
    assert str(exception_bad_name.value) == "OSLODatatypeComplex.name is invalid. Value = ''"


def test_InValidType():
    bad_complex = True
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLComplexDatatypeCreator(collector)
    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_block_to_write_from_complex_types(
            bad_complex, complex_datatype_validation_rules=complex_datatype_validation_rules)
    assert str(exception_bad_name.value) == "Input is not a OSLODatatypeComplex"


def setUp() -> OSLOCollector:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')
    sql_reader = SQLDbReader(file_location)
    oslo_creator = OSLOInMemoryCreator(sql_reader)
    collector = OSLOCollector(oslo_creator)
    collector.collect()
    return collector


def test_create_block_dtc():
    collector = setUp()
    creator = OTLComplexDatatypeCreator(collector)
    datatype_complex = collector.find_complex_datatype_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
    data_to_write = creator.create_block_to_write_from_complex_primitive_or_union_types(
        datatype_complex, type_field='Complex')
    assert data_to_write == expectedDtc
