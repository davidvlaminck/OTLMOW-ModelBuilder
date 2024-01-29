import os
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

import pytest

from otlmow_modelbuilder.GeometrieType import GeometrieType
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLOTypeLink import OSLOTypeLink
from otlmow_modelbuilder.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ClassOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.classes = [
            OSLOClass('Gebouw', 'Gebouw', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw',
                      'Elk bouwwerk, dat een voor mensen toegankelijke overdekte, geheel of gedeeltelijk met wanden omsloten ruimte vormt.',
                      '', 0, '')]
        self.attributes = [
            OSLOAttribuut('grondplan', 'grondplan',
                          'Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer.',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', '1', '1',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument', 0, '', 0, '',
                          '')]
        self.inheritances = [
            Inheritance('Behuizing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing',
                        'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'Gebouw', '')
        ]

        self.typeLinks = [
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument",
                         "OSLODatatypeComplex",
                         "")
        ]

        self.expectedDataGebouw = ['# coding=utf-8',
                                   'from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut',
                                   'from ...Classes.Abstracten.Behuizing import Behuizing',
                                   'from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden',
                                   'from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie',
                                   '',
                                   '',
                                   '# Generated with OTLClassCreator. To modify: extend, do not edit',
                                   "class Gebouw(Behuizing, VlakGeometrie):",
                                   '    """Elk bouwwerk, dat een voor mensen toegankelijke overdekte, geheel of gedeeltelijk met wanden omsloten ruimte vormt."""',
                                   "",
                                   "    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw'",
                                   '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
                                   "",
                                   "    def __init__(self):",
                                   '        super().__init__()',
                                   "",
                                   "        self._grondplan = OTLAttribuut(field=DtcDocument,",
                                   "                                       naam='grondplan',",
                                   "                                       label='grondplan',",
                                   "                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan',",
                                   "                                       definition='Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer.',",
                                   "                                       owner=self)",
                                   "",
                                   "    @property",
                                   "    def grondplan(self) -> DtcDocumentWaarden:",
                                   '        """Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""',
                                   "        return self._grondplan.get_waarde()",
                                   "",
                                   "    @grondplan.setter",
                                   "    def grondplan(self, value):",
                                   "        self._grondplan.set_waarde(value, owner=self)"]


class GeometrieArtefactCollectorDouble:
    def __init__(self):
        self.geometrie_types = [
            GeometrieType(objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw',
                          label_nl='Gebouw',
                          geen_geometrie=0, punt3D=0, lijn3D=0,
                          polygoon3D=1)]


def set_up_real_collector_and_creator():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL 2.3.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    creator = OTLClassCreator(collector)
    return collector, creator


def test_InvalidOSLOClassEmptyUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    osloClass = OSLOClass(name='name', objectUri='', definition='', label='', usagenote='', abstract=1,
                          deprecated_version='')

    with pytest.raises(ValueError) as exception_empty_uri:
        creator.create_blocks_to_write_from_classes(osloClass)
    assert str(exception_empty_uri.value) == "OSLOClass.objectUri is invalid. Value = ''"


def test_InvalidOSLODatatypeComplexBadUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    osloClass = OSLOClass(name='name', objectUri='Bad objectUri', definition='', label='', usagenote='', abstract=1,
                          deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_uri:
        creator.create_blocks_to_write_from_classes(osloClass)
    assert str(exception_bad_uri.value) == "OSLOClass.objectUri is invalid. Value = 'Bad objectUri'"


def test_InvalidOSLODatatypeComplexEmptyName():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    osloClass = OSLOClass(name='',
                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                          definition='', label='', usagenote='', abstract=1,
                          deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_blocks_to_write_from_classes(osloClass)
    assert str(exception_bad_name.value) == "OSLOClass.name is invalid. Value = ''"


def test_InValidType():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_blocks_to_write_from_classes('bad input')
    assert str(exception_bad_name.value) == 'Input is not a OSLOClass'


expectedDataContainerBuis = ['# coding=utf-8',
                             'from typing import List',
                             'from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut',
                             'from abc import abstractmethod, ABC',
                             'from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField',
                             '',
                             '',
                             '# Generated with OTLClassCreator. To modify: extend, do not edit',
                             'class ContainerBuis(ABC):',
                             '    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""',
                             '',
                             "    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis'",
                             '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
                             '',
                             '    @abstractmethod',
                             '    def __init__(self):',
                             '        super().__init__()',
                             '',
                             "        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', "
                             "target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis', "
                             "deprecated='2.3.0')",
                             "        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', "
                             "target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis', "
                             "deprecated='2.3.0')",
                             '',
                             '        self._kleur = OTLAttribuut(field=StringField,',
                             "                                   naam='kleur',",
                             "                                   label='kleur',",
                             "                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur',",
                             "                                   kardinaliteit_max='*',",
                             "                                   definition='De kleur van de coating.',",
                             "                                   owner=self)",
                             '',
                             '    @property',
                             '    def kleur(self) -> List[str]:',
                             '        """De kleur van de coating."""',
                             '        return self._kleur.get_waarde()',
                             '',
                             '    @kleur.setter',
                             '    def kleur(self, value):',
                             '        self._kleur.set_waarde(value, owner=self)']


def test_ContainerBuis():
    collector, creator = set_up_real_collector_and_creator()
    container_buis = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
    data_to_write = creator.create_blocks_to_write_from_classes(container_buis)
    assert data_to_write == expectedDataContainerBuis


def test_Gebouw_DtcKardMax1():
    collector = ClassOSLOCollector(mock)
    collector.relations = []
    geo_collector = GeometrieArtefactCollectorDouble()
    creator = OTLClassCreator(collector)
    creator.geometry_types = geo_collector.geometrie_types
    gebouw = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
    data_to_write = creator.create_blocks_to_write_from_classes(gebouw)
    assert data_to_write == collector.expectedDataGebouw


# TODO change these tests to implementation assumptions
def test_CheckInheritances_Agent():
    collector, creator = set_up_real_collector_and_creator()

    agent = collector.find_class_by_uri('http://purl.org/dc/terms/Agent')
    data_to_write = creator.create_blocks_to_write_from_classes(agent, valid_uri_and_types={
        "https://schema.org/ContactPoint": "DtcContactinfo",
        "https://schema.org/OpeningHoursSpecification": "DtcOpeningsurenSpecificatie"
    })
    inheritance_line = 'class Agent(OTLObject, RelationInteractor):'

    assert data_to_write[11] == inheritance_line


def test_CheckInheritances_AIMObject():
    collector, creator = set_up_real_collector_and_creator()

    aim_object = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject')
    data_to_write = creator.create_blocks_to_write_from_classes(aim_object)
    inheritance_line = 'class AIMObject(AIMDBStatus, AIMToestand, OTLAsset, RelationInteractor):'

    assert data_to_write[16] == inheritance_line


def test_CheckInheritances_RelatieObject():
    collector, creator = set_up_real_collector_and_creator()

    relatie_object = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject')
    data_to_write = creator.create_blocks_to_write_from_classes(relatie_object)
    inheritance_line = 'class RelatieObject(AIMDBStatus, DavieRelatieAttributes, OTLObject):'

    assert data_to_write[10] == inheritance_line


def test_CheckInheritances_DerdenObject():
    collector, creator = set_up_real_collector_and_creator()

    derdenobject = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject')
    data_to_write = creator.create_blocks_to_write_from_classes(derdenobject)
    inheritance_line = 'class Derdenobject(AIMDBStatus, AIMToestand, OTLAsset, RelationInteractor):'

    assert data_to_write[14] == inheritance_line


def test_check_inheritances_RelationInteractor():
    collector = OSLOCollector(mock.Mock(spec=OSLOInMemoryCreator))
    collector.classes = [
        OSLOClass('A', 'A', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#A',
                  'A (does not inherit from RelationInteractor', '', 0, ''),
        OSLOClass('B', 'B', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#B',
                  'B (inherits from RelationInteractor indirectly through D', '', 0, ''),
        OSLOClass('D', 'D', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#D',
                  'D (inherits from RelationInteractor through AIMObject', '', 0, ''),
        OSLOClass('C', 'C', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#C',
                  'C (inherits from A and B', '', 0, ''),
        OSLOClass('AIMObject', 'AIMObject',
                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                  'AIMObject', '', 0, '')
    ]
    collector.inheritances = [
        Inheritance('AIMObject', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                    'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#D', 'D', ''),
        Inheritance('D', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#D',
                    'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#B', 'B', ''),
        Inheritance('B', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#B',
                    'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#C', 'C', ''),
        Inheritance('A', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#A',
                    'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#C', 'C', '')
    ]
    collector.attributes = []
    collector.relations = []
    creator = OTLClassCreator(collector)
    c_class = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#C')
    inheritance_line = creator.create_blocks_to_write_from_classes(c_class)[6]
    assert inheritance_line == 'class C(A, B):'
