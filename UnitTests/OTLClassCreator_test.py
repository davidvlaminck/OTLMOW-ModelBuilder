import os
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

import pytest

from otlmow_modelbuilder.GeometrieType import GeometrieType
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator
from otlmow_modelbuilder.OTLClassCreator import OTLClassCreator
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLORelatie import OSLORelatie
from otlmow_modelbuilder.SQLDataClasses.OSLOTypeLink import OSLOTypeLink

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

        self.class_dict = {c.objectUri: c for c in self.classes}

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

class_validation_rules = {
        "valid_uri_and_types" : {
            "http://purl.org/dc/terms/Agent": "Agent",
            "http://www.w3.org/2004/02/skos/core#Concept": "Concept",
            "https://www.w3.org/2004/02/skos/core#ConceptScheme": "Codelijst",
        },
        "valid_regexes" : ["^https://wegenenverkeer.data.vlaanderen.be/ns/.+#.+"]
    }

def set_up_real_collector_and_creator():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_location = Path(f'{base_dir}/OTL 2.3.db')
    collector = OSLOCollector(file_location)
    collector.collect_all()
    creator = OTLClassCreator(collector)

    # Add missing base classes for inheritance resolution
    collector.classes.append(OSLOClass(
        name='RelationInteractor',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
        definition='',
        label='RelationInteractor',
        usagenote='',
        abstract=0,
        deprecated_version=''
    ))
    collector.classes.append(OSLOClass(
        name='OTLObject',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLObject',
        definition='',
        label='OTLObject',
        usagenote='',
        abstract=0,
        deprecated_version=''
    ))
    collector.classes.append(OSLOClass(
        name='OTLAsset',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLAsset',
        definition='',
        label='OTLAsset',
        usagenote='',
        abstract=0,
        deprecated_version=''
    ))
    collector.classes.append(OSLOClass(
        name='AIMVersie',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMVersie',
        definition='',
        label='AIMVersie',
        usagenote='',
        abstract=0,
        deprecated_version=''
    ))
    collector.classes.append(OSLOClass(
        name='DavieRelatieAttributes',
        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DavieRelatieAttributes',
        definition='',
        label='DavieRelatieAttributes',
        usagenote='',
        abstract=0,
        deprecated_version=''
    ))

    collector.inheritances.append(
        Inheritance(base_name='OTLAsset',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLAsset',
                    class_name='AIMObject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                    deprecated_version=''))
    collector.inheritances.append(
        Inheritance(base_name='RelationInteractor',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
                    class_name='AIMObject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                    deprecated_version=''))
    collector.inheritances.append(
        Inheritance(base_name='AIMVersie',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMVersie',
                    class_name='AIMObject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                    deprecated_version=''))
    collector.inheritances.append(
        Inheritance(base_name='OTLObject',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLObject',
                    class_name='OTLAsset',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLAsset',
                    deprecated_version=''))

    collector.inheritances.append(
        Inheritance(base_name='OTLAsset',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLAsset',
                    class_name='Derdenobject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject',
                    deprecated_version=''))
    collector.inheritances.append(
        Inheritance(base_name='RelationInteractor',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
                    class_name='Derdenobject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject',
                    deprecated_version=''))

    collector.inheritances.append(
        Inheritance(base_name='DavieRelatieAttributes',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DavieRelatieAttributes',
                    class_name='RelatieObject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject',
                    deprecated_version=''))

    collector.inheritances.append(
        Inheritance(base_name='OTLObject',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLObject',
                    class_name='RelatieObject',
                    class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject',
                    deprecated_version=''))

    collector.inheritances.append(
        Inheritance(base_name='RelationInteractor',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelationInteractor',
                    class_name='Agent', class_uri='http://purl.org/dc/terms/Agent',
                    deprecated_version=''))
    collector.inheritances.append(
        Inheritance(base_name='OTLObject',
                    base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#OTLObject',
                    class_name='Agent', class_uri='http://purl.org/dc/terms/Agent', deprecated_version=''))

    collector.class_dict = {c.objectUri: c for c in collector.classes}

    return collector, creator


def test_InvalidOSLOClassEmptyUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    osloClass = OSLOClass(name='name', objectUri='', definition='', label='', usagenote='', abstract=1,
                          deprecated_version='')

    with pytest.raises(ValueError) as exception_empty_uri:
        creator.create_blocks_to_write_from_classes(osloClass, class_validation_rules=class_validation_rules)
    assert str(exception_empty_uri.value) == "OSLOClass.objectUri is invalid (empty). Value = ''"


def test_InvalidOSLODatatypeComplexBadUri():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    osloClass = OSLOClass(name='name', objectUri='Bad objectUri', definition='', label='', usagenote='', abstract=1,
                          deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_uri:
        creator.create_blocks_to_write_from_classes(osloClass, class_validation_rules=class_validation_rules)
    assert str(exception_bad_uri.value) == "OSLOClass.objectUri is invalid. It's not included in valid_uri_and_types of class_validation_rules or doesn't match one of valid regex in class_validation_rules. Value = 'Bad objectUri'"


def test_InvalidOSLODatatypeComplexEmptyName():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    osloClass = OSLOClass(name='',
                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                          definition='', label='', usagenote='', abstract=1,
                          deprecated_version='')

    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_blocks_to_write_from_classes(osloClass, class_validation_rules=class_validation_rules)
    assert str(exception_bad_name.value) == "OSLOClass.name is invalid (empty). Value = ''"


def test_InValidType():
    collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
    creator = OTLClassCreator(collector)
    with pytest.raises(ValueError) as exception_bad_name:
        creator.create_blocks_to_write_from_classes('bad input')
    assert str(exception_bad_name.value) == 'Input is not a OSLOClass'


expectedDataContainerBuis = ['# coding=utf-8',
                             'from typing import List',
                             'from ...BaseClasses.OTLObject import OTLAttribuut',
                             'from abc import abstractmethod, ABC',
                             'from ...BaseClasses.StringField import StringField',
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
                             '','        '
                             "self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', "
                             "target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis', "
                             "direction='o', deprecated='2.3.0')  # o = direction: outgoing",
                             '        '
                             "self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', "
                             "target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis', "
                             "direction='o', deprecated='2.3.0')  # o = direction: outgoing",
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
    data_to_write = creator.create_blocks_to_write_from_classes(container_buis, class_validation_rules=class_validation_rules)
    assert data_to_write == expectedDataContainerBuis


expectedDataGebouw = ['# coding=utf-8',
                      'from ...BaseClasses.OTLObject import OTLAttribuut',
                      'from ...Classes.Abstracten.Behuizing import Behuizing',
                      'from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden',
                      'from ...GeometrieTypes.VlakGeometrie import VlakGeometrie',
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
                      '        '
                      "self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', "
                      "target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord', "
                      "direction='u')  # u = unidirectional",
                      '        '
                      "self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', "
                      "target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', "
                      "direction='u')  # u = unidirectional",
                      '        '
                      "self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', "
                      "target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', "
                      "direction='u')  # u = unidirectional",
                      '',
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

def test_Gebouw_DtcKardMax1():
    # Arrange
    collector, creator = set_up_real_collector_and_creator()
    geo_collector = GeometrieArtefactCollectorDouble()
    creator = OTLClassCreator(collector)
    creator.geometry_types = geo_collector.geometrie_types

    # Act
    gebouw = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
    data_to_write = creator.create_blocks_to_write_from_classes(gebouw, class_validation_rules=class_validation_rules)

    # Assert
    assert data_to_write == expectedDataGebouw


# TODO change these tests to implementation assumptions
def test_CheckInheritances_Agent():
    collector, creator = set_up_real_collector_and_creator()

    agent = collector.find_class_by_uri('http://purl.org/dc/terms/Agent')
    class_validation_rules['valid_uri_and_types'].update({"https://schema.org/ContactPoint": "DtcContactinfo"})
    data_to_write = creator.create_blocks_to_write_from_classes(agent, class_validation_rules=class_validation_rules)
    inheritance_line = 'class Agent(RelationInteractor, OTLObject):'

    assert data_to_write[11] == inheritance_line


def test_CheckInheritances_AIMObject():
    collector, creator = set_up_real_collector_and_creator()

    aim_object = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject')
    data_to_write = creator.create_blocks_to_write_from_classes(aim_object, class_validation_rules=class_validation_rules)
    inheritance_line = 'class AIMObject(AIMDBStatus, AIMToestand, OTLAsset, RelationInteractor, AIMVersie):'

    assert data_to_write[17] == inheritance_line


def test_CheckInheritances_RelatieObject():
    collector, creator = set_up_real_collector_and_creator()

    relatie_object = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject')
    data_to_write = creator.create_blocks_to_write_from_classes(relatie_object, class_validation_rules=class_validation_rules)
    inheritance_line = 'class RelatieObject(AIMDBStatus, DavieRelatieAttributes, OTLObject):'

    assert data_to_write[10] == inheritance_line


def test_CheckInheritances_DerdenObject():
    collector, creator = set_up_real_collector_and_creator()

    derdenobject = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject')
    data_to_write = creator.create_blocks_to_write_from_classes(derdenobject,
                                                                class_validation_rules=class_validation_rules)
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
    inheritance_line = creator.create_blocks_to_write_from_classes(c_class,
                                                                   class_validation_rules=class_validation_rules)[6]
    assert inheritance_line == 'class C(B, A):'


# --- the behaviour of the class creator, pinned one case at a time ------------

OBJECT_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Object'
OTHER_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Other'
AGENT_URI = 'http://purl.org/dc/terms/Agent'
AIM_OBJECT_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject'


class CollectorStub:
    """A collector with only the data the class creator asks for."""

    def __init__(self, relations=None, inheritances_by_class_uri=None, inheritance_map=None, attributes=None,
                 type_links=None, enumerations=None, complex_datatypes=None, union_datatypes=None):
        self.relations = relations if relations is not None else []
        self.inheritances_by_class_uri = inheritances_by_class_uri if inheritances_by_class_uri is not None else {}
        self.inheritance_map = inheritance_map if inheritance_map is not None else {}
        self.attributes = attributes if attributes is not None else []
        self.typeLinks = type_links if type_links is not None else []
        self.enumerations = enumerations if enumerations is not None else []
        self.complex_datatypes = complex_datatypes if complex_datatypes is not None else []
        self.union_datatypes = union_datatypes if union_datatypes is not None else []

    def find_all_relations(self, object_uri, allow_duplicates=False, sort_by_uri=True):
        return [r for r in self.relations if r.bron_uri == object_uri or r.doel_uri == object_uri]

    def find_inheritances_by_class_uri(self, oslo_class_uri, sort_by_uri=True):
        return self.inheritances_by_class_uri.get(oslo_class_uri, [])

    def find_inheritances_by_class(self, oslo_class, sort_by_uri=True):
        return self.find_inheritances_by_class_uri(oslo_class.objectUri, sort_by_uri)

    def find_attributes_by_class(self, oslo_class, sort_by_uri=True):
        return [a for a in self.attributes if a.class_uri == oslo_class.objectUri]

    def get_inheritance_map(self):
        return self.inheritance_map


def a_relation(bron_uri, doel_uri, richting, object_uri=OBJECT_URI, deprecated_version=''):
    return OSLORelatie(bron_overerving='', doel_overerving='', bron_uri=bron_uri, doel_uri=doel_uri,
                       objectUri=object_uri, richting=richting, usagenote='', deprecated_version=deprecated_version)


def an_inheritance(base_name, base_uri, class_uri=OBJECT_URI, class_name='Object'):
    return Inheritance(base_name=base_name, base_uri=base_uri, class_uri=class_uri, class_name=class_name)


def an_oslo_class(name='Object', object_uri=OBJECT_URI, abstract=0):
    return OSLOClass(name=name, objectUri=object_uri, definition='The definition.', label=name, usagenote='',
                     abstract=abstract, deprecated_version='')


def a_creator(collector):
    return OTLClassCreator(collector)


def test_the_direction_of_an_unspecified_relation_is_unidirectional():
    creator = a_creator(CollectorStub())
    relation = a_relation(OBJECT_URI, OTHER_URI, 'Unspecified')

    assert creator._get_direction_and_target(relation, OBJECT_URI) == \
           ('u', OTHER_URI, '# u = unidirectional')


def test_an_unspecified_relation_that_comes_from_the_other_side_keeps_the_source_as_target():
    creator = a_creator(CollectorStub())
    relation = a_relation(OTHER_URI, OBJECT_URI, 'Unspecified')

    assert creator._get_direction_and_target(relation, OBJECT_URI) == \
           ('u', OTHER_URI, '# u = unidirectional')


def test_the_direction_of_a_relation_that_starts_at_the_object_is_outgoing():
    creator = a_creator(CollectorStub())
    relation = a_relation(OBJECT_URI, OTHER_URI, 'Outgoing')

    assert creator._get_direction_and_target(relation, OBJECT_URI) == \
           ('o', OTHER_URI, '# o = direction: outgoing')


def test_the_direction_of_a_relation_that_ends_at_the_object_is_incoming():
    creator = a_creator(CollectorStub())
    relation = a_relation(OTHER_URI, OBJECT_URI, 'Incoming')

    assert creator._get_direction_and_target(relation, OBJECT_URI) == \
           ('i', OTHER_URI, '# i = direction: incoming')


def test_a_relation_without_a_deprecated_version_has_no_deprecated_argument():
    creator = a_creator(CollectorStub())
    relation = a_relation(OBJECT_URI, OTHER_URI, 'Outgoing')

    assert creator._get_deprecated_argument(relation) == ''


def test_a_deprecated_relation_keeps_the_version_without_the_suffix():
    creator = a_creator(CollectorStub())
    relation = a_relation(OBJECT_URI, OTHER_URI, 'Outgoing', deprecated_version='2.3.0-onthef')

    assert creator._get_deprecated_argument(relation) == ", deprecated='2.3.0'"
    assert relation.deprecated_version == '2.3.0'


def test_the_relations_are_added_to_the_datablock_with_their_direction():
    collector = CollectorStub(relations=[
        a_relation(OBJECT_URI, OTHER_URI, 'Outgoing'),
        a_relation(OTHER_URI, OBJECT_URI, 'Incoming'),
        a_relation(OBJECT_URI, OTHER_URI, 'Unspecified'),
    ])
    creator = a_creator(collector)
    datablock = []

    creator.add_relations_to_datablock(datablock, OBJECT_URI)

    assert datablock == [
        (
            f"        self.add_valid_relation(relation='{OBJECT_URI}', target='{OTHER_URI}', direction='o')"
            '  # o = direction: outgoing'
        ),
        (
            f"        self.add_valid_relation(relation='{OBJECT_URI}', target='{OTHER_URI}', direction='i')"
            '  # i = direction: incoming'
        ),
        (
            f"        self.add_valid_relation(relation='{OBJECT_URI}', target='{OTHER_URI}', direction='u')"
            '  # u = unidirectional'
        ),
        '',
    ]


def test_a_class_without_relations_gets_no_relations_in_the_datablock():
    creator = a_creator(CollectorStub())
    datablock = []

    creator.add_relations_to_datablock(datablock, OBJECT_URI)

    assert datablock == []


def test_a_class_that_inherits_from_a_relation_interactor_is_found():
    collector = CollectorStub(inheritances_by_class_uri={
        OBJECT_URI: [an_inheritance('AIMObject', AIM_OBJECT_URI)],
    })
    creator = a_creator(collector)

    assert creator.search_recursive_inheritance_for_relation_interactor(OBJECT_URI) is True


def test_a_class_that_inherits_indirectly_from_a_relation_interactor_is_found():
    collector = CollectorStub(inheritances_by_class_uri={
        OBJECT_URI: [an_inheritance('Middle', OTHER_URI)],
        OTHER_URI: [an_inheritance('AIMObject', AIM_OBJECT_URI)],
    })
    creator = a_creator(collector)

    assert creator.search_recursive_inheritance_for_relation_interactor(OBJECT_URI) is True


def test_a_class_that_does_not_inherit_from_a_relation_interactor_is_not_found():
    collector = CollectorStub(inheritances_by_class_uri={
        OBJECT_URI: [an_inheritance('Other', OTHER_URI)],
    })
    creator = a_creator(collector)

    assert creator.search_recursive_inheritance_for_relation_interactor(OBJECT_URI) is False


def test_a_class_without_inheritances_is_not_a_relation_interactor():
    creator = a_creator(CollectorStub())

    assert creator.search_recursive_inheritance_for_relation_interactor(OBJECT_URI) is False


def test_an_abstract_class_without_bases_imports_abc():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_abstract_import(datablock, an_oslo_class(abstract=1), [], [])

    assert datablock == ['from abc import abstractmethod, ABC']


def test_an_abstract_class_with_bases_imports_only_the_decorator():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_abstract_import(datablock, an_oslo_class(abstract=1), [an_inheritance('Other', OTHER_URI)], [])

    assert datablock == ['from abc import abstractmethod']


def test_a_class_that_is_not_abstract_does_not_import_the_decorator():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_abstract_import(datablock, an_oslo_class(abstract=0), [], [])

    assert datablock == []


def test_the_base_classes_are_imported_from_the_base_classes_module():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_inheritance_imports(datablock, an_oslo_class(),
                                    [an_inheritance('OTLObject', 'https://example.org#OTLObject')])

    assert datablock == ['from ...BaseClasses.OTLObject import OTLObject']


def test_the_agent_class_imports_the_base_classes_one_level_higher():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_inheritance_imports(datablock, an_oslo_class(name='Agent', object_uri=AGENT_URI),
                                    [an_inheritance('OTLObject', 'https://example.org#OTLObject')])

    assert datablock == ['from ..BaseClasses.OTLObject import OTLObject']


def test_an_inheritance_of_the_agent_class_is_imported_one_level_higher():
    creator = a_creator(CollectorStub())
    datablock = []
    inheritance = an_inheritance('AIMDBStatus',
                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus',
                                 class_uri=AGENT_URI, class_name='Agent')

    creator._add_inheritance_imports(datablock, an_oslo_class(name='Agent', object_uri=AGENT_URI), [inheritance])

    assert datablock == ['from ..Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus']


def test_an_inheritance_is_imported_from_the_class_directory_of_its_namespace():
    creator = a_creator(CollectorStub())
    datablock = []
    inheritance = an_inheritance('Behuizing',
                                 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')

    creator._add_inheritance_imports(datablock, an_oslo_class(), [inheritance])

    assert datablock == ['from ...Classes.Abstracten.Behuizing import Behuizing']


def test_a_class_without_inheritances_has_no_inheritance_imports():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_inheritance_imports(datablock, an_oslo_class(), [])

    assert datablock == []


def test_the_geometry_types_are_imported_from_the_geometry_types_module():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_geometry_imports(datablock, ['VlakGeometrie'])

    assert datablock == ['from ...GeometrieTypes.VlakGeometrie import VlakGeometrie']


def test_a_class_without_attributes_has_no_attribute_import():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_attribute_import(datablock, an_oslo_class(), [])

    assert datablock == []


def test_a_class_with_attributes_imports_the_attribute_class():
    creator = a_creator(CollectorStub())
    datablock = []

    creator._add_attribute_import(datablock, an_oslo_class(), ['an attribute'])

    assert datablock == ['from ...BaseClasses.OTLObject import OTLAttribuut']


def test_a_class_without_bases_and_without_attributes_gets_a_pass():
    creator = a_creator(CollectorStub())
    datablock = ['        pass']

    creator._finalize_datablock(datablock, [], [])

    assert datablock == ['        pass', '        pass']


def test_a_class_with_bases_does_not_get_a_pass():
    creator = a_creator(CollectorStub())
    datablock = ['    def __init__(self):']

    creator._finalize_datablock(datablock, [an_inheritance('Other', OTHER_URI)], [])

    assert datablock == ['    def __init__(self):']


def test_a_class_without_bases_and_without_abstract_is_not_implemented():
    creator = a_creator(CollectorStub())

    with pytest.raises(NotImplementedError) as exception:
        creator.get_class_line_from_class_and_inheritances(an_oslo_class(abstract=0), [], [])

    assert str(exception.value) == f'{OBJECT_URI} class structure not implemented'


def test_an_abstract_class_without_bases_inherits_from_abc():
    creator = a_creator(CollectorStub())

    assert creator.get_class_line_from_class_and_inheritances(an_oslo_class(abstract=1), [], []) == \
           'class Object(ABC):'


def test_a_class_with_more_bases_than_the_inheritance_map_is_not_implemented():
    creator = a_creator(CollectorStub(inheritance_map={OBJECT_URI: []}))

    with pytest.raises(ValueError) as exception:
        creator.get_class_line_from_class_and_inheritances(
            an_oslo_class(), [an_inheritance('Other', OTHER_URI)], [])

    assert str(exception.value) == f'Could not find all inheritances for {OBJECT_URI}. Found 1, expected 0'


def test_a_class_with_a_base_that_is_not_in_the_inheritances_is_not_implemented():
    creator = a_creator(CollectorStub(inheritance_map={OBJECT_URI: ['https://example.org#Missing']}))

    with pytest.raises(ValueError) as exception:
        creator.get_class_line_from_class_and_inheritances(
            an_oslo_class(), [an_inheritance('Other', OTHER_URI)], [])

    assert str(exception.value) == f'Could not find inheritance for https://example.org#Missing in {OBJECT_URI}'


def test_a_class_without_class_validation_rules_is_not_valid():
    creator = a_creator(CollectorStub())

    with pytest.raises(ValueError) as exception:
        creator.create_blocks_to_write_from_classes(an_oslo_class())

    assert str(exception.value) == (
        "OSLOClass.objectUri is invalid. It's not included in valid_uri_and_types of class_validation_rules"
        f" or doesn't match one of valid regex in class_validation_rules. Value = '{OBJECT_URI}'")


def test_the_python_fallback_generates_the_same_class_as_the_rust_implementation():
    collector, creator = set_up_real_collector_and_creator()
    container_buis = collector.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')

    with_rust = creator.create_blocks_to_write_from_classes(container_buis,
                                                            class_validation_rules=class_validation_rules)

    collector_without_rust, creator_without_rust = set_up_real_collector_and_creator()
    creator_without_rust._create_block_with_rust = lambda *args, **kwargs: None
    container_buis = collector_without_rust.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')

    without_rust = creator_without_rust.create_blocks_to_write_from_classes(
        container_buis, class_validation_rules=class_validation_rules)

    assert without_rust == with_rust


def test_the_python_fallback_generates_the_same_relations_as_the_rust_implementation():
    collector, creator = set_up_real_collector_and_creator()
    gebouw = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')

    with_rust = creator.create_blocks_to_write_from_classes(gebouw, class_validation_rules=class_validation_rules)

    collector_without_rust, creator_without_rust = set_up_real_collector_and_creator()
    creator_without_rust._create_block_with_rust = lambda *args, **kwargs: None
    gebouw = collector_without_rust.find_class_by_uri(
        'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')

    without_rust = creator_without_rust.create_blocks_to_write_from_classes(
        gebouw, class_validation_rules=class_validation_rules)

    assert without_rust == with_rust
