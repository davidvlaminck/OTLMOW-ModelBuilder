import logging

from otlmow_modelbuilder.GenericBuilderFunctions import add_attributen_to_data_block, \
    get_fields_to_import_from_list_of_attributes
from otlmow_modelbuilder.GeometrieArtefactCollector import GeometrieArtefactCollector
from otlmow_modelbuilder.GeometrieInheritanceProcessor import GeometrieInheritanceProcessor
from otlmow_modelbuilder.GeometrieType import GeometrieType
from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns
from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector


class OTLClassCreator(AbstractDatatypeCreator):
    def __init__(self, oslo_collector: OSLOCollector, geo_a_collector: GeometrieArtefactCollector = None):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLClassCreator")
        self.osloCollector = oslo_collector
        self.geoACollector = geo_a_collector
        self.geometry_types = []

        if geo_a_collector is not None:
            gip = GeometrieInheritanceProcessor(classes=oslo_collector.classes,
                                                geometrie_types=self.geoACollector.geometrie_types,
                                                inheritances=self.osloCollector.inheritances)
            self.geometry_types = gip.process_inheritances()

    def create_blocks_to_write_from_classes(self, oslo_class: OSLOClass, model_location='') -> [str]:
        if not isinstance(oslo_class, OSLOClass):
            raise ValueError(f"Input is not a OSLOClass")

        if oslo_class.objectUri == '' or not (
                oslo_class.objectUri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/') or oslo_class.objectUri.
                        startswith('http://purl.org/dc/terms')):
            raise ValueError(f"OSLOClass.objectUri is invalid. Value = '{oslo_class.objectUri}'")

        if oslo_class.name == '':
            raise ValueError(f"OSLOClass.name is invalid. Value = '{oslo_class.name}'")

        return self.create_block_from_class(oslo_class, model_location)

    def create_block_from_class(self, oslo_class: OSLOClass, model_location='') -> [str]:
        attributen = self.osloCollector.find_attributes_by_class(oslo_class)
        inheritances = self.osloCollector.find_inheritances_by_class(oslo_class)
        list_of_geometry_types = self.get_geometry_types_from_uri(oslo_class.objectUri)

        if oslo_class.objectUri in ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject',
                                    'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie']:
            inheritances.append(
                Inheritance(base_name='OTLAsset', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='RelationInteractor', base_uri='', class_name='', class_uri='',
                            deprecated_version=''))

        elif oslo_class.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject':
            inheritances.append(
                Inheritance(base_name='DavieRelatieAttributes', base_uri='', class_name='', class_uri='',
                            deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='OTLObject', base_uri='', class_name='', class_uri='', deprecated_version=''))

        elif oslo_class.objectUri == 'http://purl.org/dc/terms/Agent':
            inheritances.append(
                Inheritance(base_name='OTLObject', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='RelationInteractor', base_uri='', class_name='', class_uri='',
                            deprecated_version=''))

        datablock = ['# coding=utf-8']
        if len(attributen) > 0:
            datablock.append('from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut')

        if oslo_class.abstract == 1:
            if len(inheritances) + len(list_of_geometry_types) < 1:
                datablock.append('from abc import abstractmethod, ABC')
            else:
                datablock.append('from abc import abstractmethod')

        if len(inheritances) > 0:
            for inheritance in inheritances:
                if inheritance.base_name in ['OTLAsset', 'OTLObject', 'RelationInteractor', 'DavieRelatieAttributes']:
                    datablock.append(
                        f'from otlmow_model.BaseClasses.{inheritance.base_name} import {inheritance.base_name}')
                else:
                    class_directory = 'Classes'
                    ns = None
                    if inheritance.base_uri != 'http://purl.org/dc/terms/Agent':
                        ns, name = get_ns_and_name_from_uri(inheritance.base_uri)
                    if ns is not None:
                        class_directory = get_class_directory_from_ns(ns).replace('/', '.')

                    model_module = 'otlmow_model'
                    if model_location != '':
                        if 'UnitTests' in model_location:
                            model_module = 'UnitTests'
                        modules_index = model_location.rfind('/' + model_module)
                        modules = model_location[modules_index + 1:]
                        model_module = modules.replace('/', '.')
                    datablock.append(f'from {model_module}.{class_directory}.{inheritance.base_name} '
                                     f'import {inheritance.base_name}')

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        list_of_fields = get_fields_to_import_from_list_of_attributes(oslo_collector=self.oslo_collector,
                                                                      attributen=attributen)
        base_fields = ['BooleanField', 'ComplexField', 'DateField', 'DateTimeField', 'FloatOrDecimalField',
                       'IntegerField', 'KeuzelijstField', 'UnionTypeField', 'URIField', 'LiteralField',
                       'NonNegIntegerField', 'TimeField', 'StringField', 'UnionWaarden']
        for type_field in list_of_fields:
            model_module = 'otlmow_model'
            if model_location != '' and type_field not in base_fields:
                if 'UnitTests' in model_location:
                    model_module = 'UnitTests'
                modules_index = model_location.rfind('/' + model_module)
                modules = model_location[modules_index + 1:]
                model_module = modules.replace('/', '.')
            if type_field not in base_fields:
                datablock.append(f'from {model_module}.Datatypes.{type_field} import {type_field}')
            else:
                datablock.append(f'from {model_module}.BaseClasses.{type_field} import {type_field}')

        if 'Bevestiging' in oslo_class.objectUri:
            pass

        for geometry_type in list_of_geometry_types:
            datablock.append(f'from otlmow_model.GeometrieTypes.{geometry_type} import {geometry_type}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(self.get_class_line_from_class_and_inheritances(oslo_class=oslo_class,
                                                                         inheritances=inheritances,
                                                                         geometry_types=list_of_geometry_types))
        datablock.append(f'    """{oslo_class.definition}"""')
        datablock.append('')
        datablock.append(f"    typeURI = '{oslo_class.objectUri}'")
        datablock.append('    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""')

        if oslo_class.deprecated_version != '':
            datablock.append('')
            datablock.append(f"    deprecated_version = '{oslo_class.deprecated_version}'")

        datablock.append('')
        if oslo_class.abstract == 1:
            datablock.append('    @abstractmethod')
        datablock.append('    def __init__(self):')
        if len(inheritances) + len(list_of_geometry_types) == 1:
            datablock.append('        super().__init__()')
            datablock.append('')
        elif len(inheritances) + len(list_of_geometry_types) > 1:
            for inheritance in sorted(inheritances, key=lambda a: a.base_name):
                datablock.append(f'        {inheritance.base_name}.__init__(self)')
            for geo_type in sorted(list_of_geometry_types):
                datablock.append(f'        {geo_type}.__init__(self)')
            datablock.append('')

        self.add_relations_to_datablock(datablock, oslo_class.objectUri)

        add_attributen_to_data_block(attributen, datablock, for_class_use=True)
        if len(inheritances) == 0 and len(attributen) == 0:
            datablock.append('        pass')

        if datablock[-1] == '':
            datablock.pop()

        return datablock

    def get_class_line_from_class_and_inheritances(self, oslo_class: OSLOClass, inheritances: [Inheritance],
                                                   geometry_types: [GeometrieType]) -> str:
        if oslo_class.abstract + len(inheritances) + len(geometry_types) < 1:
            raise NotImplementedError(f"{oslo_class.objectUri} class structure not implemented")
        if oslo_class.abstract == 1 and len(inheritances) + len(geometry_types) < 1:
            return f'class {oslo_class.name}(ABC):'
        if len(inheritances) + len(geometry_types) > 0:
            line = f'class {oslo_class.name}('
            for inheritance in inheritances:
                line += inheritance.base_name + ', '
            for geometry_type in geometry_types:
                line += geometry_type + ', '
            line = line[:-2]
            line += '):'
            return line

        raise NotImplementedError(f"{oslo_class.objectUri} class structure not implemented")

    def get_geometry_types_from_uri(self, object_uri: str) -> [str]:
        if len(self.geometry_types) == 0:
            return []

        geom_type = next((g for g in self.geometry_types if g.objectUri == object_uri), None)
        if geom_type is None:
            return []

        geom_types = []
        if geom_type.geen_geometrie == 1:
            geom_types.append('GeenGeometrie')
        if geom_type.punt3D == 1:
            geom_types.append('PuntGeometrie')
        if geom_type.lijn3D == 1:
            geom_types.append('LijnGeometrie')
        if geom_type.polygoon3D == 1:
            geom_types.append('VlakGeometrie')

        return geom_types

    def add_relations_to_datablock(self, datablock: [str], object_uri: str) -> None:
        relations = self.osloCollector.find_outgoing_relations(object_uri)
        if len(relations) == 0:
            return

        for relation in relations:
            deprecated = ''
            if relation.deprecated_version != '':
                deprecated = f", deprecated='{relation.deprecated_version}'"
            datablock.append(
                f"        self.add_valid_relation(relation='{relation.objectUri}', target='{relation.doel_uri}'{deprecated})")
        datablock.append('')
