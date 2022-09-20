import os
from abc import ABC

from typing import List

from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.HelperFunctions import wrap_in_quotes


class AbstractDatatypeCreator(ABC):
    def __init__(self, oslo_collector: OSLOCollector):
        self.oslo_collector = oslo_collector

    def get_type_link_from_attribuut(self, attribuut):
        type_link = self.oslo_collector.find_type_link_by_uri(attribuut.type)
        if type_link is not None:
            return type_link

    @staticmethod
    def get_single_field_from_type_uri(field_type: str):
        if field_type.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/') and '#' in field_type:
            return field_type.split('#')[1]
        if field_type is None:
            return ''
        elif field_type == 'http://www.w3.org/2001/XMLSchema#decimal':
            return 'FloatOrDecimalField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#string':
            return 'StringField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#boolean':
            return 'BooleanField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#integer':
            return 'IntegerField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger':
            return 'NonNegIntegerField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#date':
            return 'DateField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#dateTime':
            return 'DateTimeField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#time':
            return 'TimeField'
        elif field_type == 'http://www.w3.org/2001/XMLSchema#anyURI':
            return 'URIField'
        elif field_type == 'https://schema.org/OpeningHoursSpecification':
            return 'DtcOpeningsurenSpecificatie'
        elif field_type == 'https://schema.org/ContactPoint':
            return 'DtcContactinfo'
        elif field_type == 'http://www.w3.org/2000/01/rdf-schema#Literal':
            return 'StringField'
        else:
            raise NotImplemented('not supported field_type in get_single_field_from_type_uri()')

    @staticmethod
    def get_non_single_field_from_type_uri(field_type: str):
        if '#Dtc' in field_type:
            type_name = field_type[field_type.find("#") + 1::]
            return ['ComplexField', type_name]
        if field_type.startswith("https://schema.org/"):
            if field_type == "https://schema.org/ContactPoint":
                return ['ComplexField', "DtcContactinfo"]
            if field_type == "https://schema.org/OpeningHoursSpecification":
                return ['ComplexField', "DtcOpeningsurenSpecificatie"]
            raise NotImplementedError(f"Field of type {field_type} is not implemented in DatatypeCreator")
        if '#Dte' in field_type or '#KwantWrd' in field_type:
            type_name = field_type[field_type.find("#") + 1::]
            return ['ComplexField', type_name]
        if '#Kl' in field_type:
            type_name = field_type[field_type.find("#") + 1::]
            return ['KeuzelijstField', type_name]
        if '#Dtu' in field_type:
            type_name = field_type[field_type.find("#") + 1::]
            return ['UnionTypeField', type_name]

        raise NotImplemented(f'not supported field_type {field_type} in get_non_single_field_from_type_uri()')

    @staticmethod
    def write_to_file(datatype, directory: str, data_to_write: List[str], relative_path=''):
        if relative_path == '':
            base_dir = os.path.dirname(os.path.realpath(__file__))
            base_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
        else:
            base_dir = relative_path
        path = f"{base_dir}/{directory}/{datatype.name}.py"

        with open(path, "w", encoding='utf-8') as file:
            for line in data_to_write:
                file.write(line + "\n")

    def get_fields_to_import_from_list_of_attributes(self, attributen, list_to_start_from=None):
        if list_to_start_from is None:
            list_to_start_from = []
        if len(attributen) == 0:
            return list_to_start_from

        collected_list = []
        collected_list.extend(list_to_start_from)

        for attribuut in attributen:
            type_link = self.get_type_link_from_attribuut(attribuut).item_tabel
            if type_link == "OSLOEnumeration":
                collected_list.append(self.get_type_name_of_enum_uri(attribuut.type))
            elif type_link == "OSLODatatypePrimitive":
                collected_list.append(self.get_single_field_from_type_uri(attribuut.type))
            elif type_link == "OSLODatatypeComplex":
                collected_list.append(self.get_type_name_of_complex_attribuut(attribuut.type))
            elif type_link == "OSLODatatypeUnion":
                collected_list.append(self.get_type_name_of_union_attribuut(attribuut.type))
            else:
                raise not NotImplementedError(f"{type_link} not implemented")

        distinct_types_list = list(set(collected_list))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list

    def get_fields_and_names_from_list_of_attributes(self, attributen):
        if len(attributen) == 0:
            return []

        primitive_types_list = list(
            filter(lambda t: t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))
        other_types_list = list(
            filter(lambda t: not t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))

        select_types_list = list(
            map(lambda a: (self.get_single_field_from_type_uri(a.type), a.name), primitive_types_list))

        for nonPrimitiveType in other_types_list:
            select_types_list.append((self.get_field_name_from_type_uri(nonPrimitiveType.type), nonPrimitiveType.name))

        distinct_types_list = list(set(select_types_list))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list

    @staticmethod
    def get_white_space_equivalent(string):
        return ''.join(' ' * len(string))

    def get_field_name_from_type_uri(self, attribuut_type):
        if attribuut_type.startswith('http://www.w3.org/2001/XMLSchema#'):
            return self.get_single_field_from_type_uri(attribuut_type)
        if attribuut_type.startswith("https://schema.org/"):
            return self.get_non_single_field_from_type_uri(attribuut_type)[1]
        return self.get_non_single_field_from_type_uri(attribuut_type)[1]

    @staticmethod
    def get_type_name_of_enum_uri(type_uri: str):
        return type_uri.split('#')[1]

    def get_type_name_of_union_attribuut(self, type_uri: str):
        if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/"):
            return type_uri[type_uri.find("#") + 1::]

        raise NotImplementedError(f"get_type_name_of_complex_attribuut fails to get typename from {type_uri}")

    def get_type_name_of_complex_attribuut(self, type_uri: str):
        if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/") or type_uri.startswith(
                "http://www.w3.org/2001/XMLSchema#"):
            return type_uri[type_uri.find("#") + 1::]
        elif type_uri.startswith("https://schema.org/"):
            if type_uri == "https://schema.org/ContactPoint":
                return "DtcContactinfo"
            if type_uri == "https://schema.org/OpeningHoursSpecification":
                return "DtcOpeningsurenSpecificatie"
            raise NotImplementedError(
                f"Field of type {type_uri} is not implemented in DatatypeCreator.get_type_name_of_complex_attribuut")

        raise NotImplementedError(f"get_type_name_of_complex_attribuut fails to get typename from {type_uri}")

    def create_block_to_write_from_complex_primitive_or_union_types(self, oslo_datatype, type_field='',
                                                                    model_location=''):
        attributen = AbstractDatatypeCreator.get_attributen_by_type_field(self.oslo_collector, type_field, oslo_datatype)

        datablock = ['# coding=utf-8',
                     'from otlmow_model.BaseClasses.AttributeInfo import AttributeInfo',
                     'from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut']

        list_fields_to_start_with = [f'{type_field}Field']
        if type_field == 'UnionType':
            list_fields_to_start_with.append('UnionWaarden')
        elif type_field == 'Primitive' or type_field == 'KwantWrd':
            datablock.append('from otlmow_model.BaseClasses.OTLField import OTLField')
            list_fields_to_start_with = []
        list_of_fields = self.get_fields_to_import_from_list_of_attributes(attributen, list_fields_to_start_with)
        base_fields = ['BooleanField', 'ComplexField', 'DateField', 'DateTimeField', 'FloatOrDecimalField',
                       'IntegerField',
                       'KeuzelijstField', 'UnionTypeField', 'URIField', 'LiteralField', 'NonNegIntegerField',
                       'TimeField',
                       'StringField', 'UnionWaarden']
        for module in list_of_fields:
            model_module = 'otlmow_model'
            if model_location != '' and module not in base_fields:
                if 'UnitTests' in model_location:
                    model_module = 'UnitTests'
                modules_index = model_location.rfind('/' + model_module)
                modules = model_location[modules_index + 1:]
                model_module = modules.replace('/', '.')
            if module not in base_fields:
                datablock.append(f'from {model_module}.Datatypes.{module} import {module}')
            else:
                datablock.append(f'from {model_module}.BaseClasses.{module} import {module}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        if type_field == 'UnionType':
            datablock.append(f'class {oslo_datatype.name}Waarden(AttributeInfo, UnionWaarden):')
            datablock.append('    def __init__(self, parent=None):')
            datablock.append('        AttributeInfo.__init__(self, parent)')
            datablock.append('        UnionWaarden.__init__(self)')
        else:
            datablock.append(f'class {oslo_datatype.name}Waarden(AttributeInfo):')
            datablock.append('    def __init__(self, parent=None):')
            datablock.append('        AttributeInfo.__init__(self, parent)')

        AbstractDatatypeCreator.add_attributen_to_data_block(attributen=attributen, datablock=datablock, type_field=type_field)

        if type_field == 'Primitive' or type_field == 'KwantWrd':
            type_field = 'OTL'

        datablock.append(''),
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(f'class {oslo_datatype.name}({type_field}Field, AttributeInfo):')
        datablock.append(f'    """{oslo_datatype.definition}"""')
        datablock.append(f'    naam = {wrap_in_quotes(oslo_datatype.name)}')
        datablock.append(f'    label = {wrap_in_quotes(oslo_datatype.label)}')
        datablock.append(f'    objectUri = {wrap_in_quotes(oslo_datatype.objectUri)}')
        datablock.append(f'    definition = {wrap_in_quotes(oslo_datatype.definition)}')
        if oslo_datatype.usagenote != '':
            datablock.append(f'    usagenote = {wrap_in_quotes(oslo_datatype.usagenote)}')
        if oslo_datatype.deprecated_version != '':
            datablock.append(f'    deprecated_version = {wrap_in_quotes(oslo_datatype.deprecated_version)}'),
        if type_field == 'OTL':
            datablock.append('    waarde_shortcut_applicable = True')
        datablock.append(f'    waardeObject = {oslo_datatype.name}Waarden')
        datablock.append(f'')
        datablock.append(f'    def __str__(self):')
        datablock.append(f'        return {type_field}Field.__str__(self)')
        datablock.append('')

        return datablock

    @staticmethod
    def get_attributen_by_type_field(oslo_collector, type_field, oslo_datatype):
        if type_field == 'Complex':
            return oslo_collector.find_complex_datatype_attributes_by_class_uri(oslo_datatype.objectUri)
        elif type_field == 'UnionType':
            return oslo_collector.find_union_datatype_attributes_by_class_uri(oslo_datatype.objectUri)
        else:
            return oslo_collector.find_primitive_datatype_attributes_by_class_uri(oslo_datatype.objectUri)

    @staticmethod
    def add_attributen_to_data_block(attributen, datablock, for_class_use=False, type_field=''):
        prop_datablock = []
        for attribuut in sorted(attributen, key=lambda a: a.name):
            if attribuut.overerving == 1:
                raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.objectUri}")

            whitespace = AbstractDatatypeCreator.get_white_space_equivalent(f'        self._{attribuut.name} = OTLAttribuut(')
            field_name = AbstractDatatypeCreator.get_single_field_from_type_uri(attribuut.type)

            datablock.append(f'        self._{attribuut.name} = OTLAttribuut(field={field_name},')
            datablock.append(f'{whitespace}naam={wrap_in_quotes(attribuut.name)},')
            datablock.append(f'{whitespace}label={wrap_in_quotes(attribuut.label)},')
            datablock.append(f'{whitespace}objectUri={wrap_in_quotes(attribuut.objectUri)},')
            if attribuut.usagenote != '':
                datablock.append(f'{whitespace}usagenote={wrap_in_quotes(attribuut.usagenote)},')
            if attribuut.readonly == 1:
                datablock.append(f'{whitespace}readonly=True,')
            if attribuut.deprecated_version != '':
                datablock.append(f'{whitespace}deprecated_version={wrap_in_quotes(attribuut.deprecated_version)},')
            if attribuut.constraints != '':
                datablock.append(f'{whitespace}constraints={wrap_in_quotes(attribuut.constraints)},')
            if attribuut.kardinaliteit_min != '1':
                datablock.append(f'{whitespace}kardinaliteit_min={wrap_in_quotes(attribuut.kardinaliteit_min)},')
            if attribuut.kardinaliteit_max != '1':
                datablock.append(f'{whitespace}kardinaliteit_max={wrap_in_quotes(attribuut.kardinaliteit_max)},')
            definitie = wrap_in_quotes(attribuut.definition.replace('\n', ''))
            datablock.append(f'{whitespace}definition={definitie},')
            datablock.append(f'{whitespace}owner=self)')
            datablock.append('')

            owner_self = ', owner=self'
            if not for_class_use:
                owner_self += '._parent'

            prop_datablock.append(f'    @property'),
            prop_datablock.append(f'    def {attribuut.name}(self):'),
            prop_datablock.append(f'        """{attribuut.definition}"""'),
            if type_field == 'KwantWrd' and attribuut.name == 'standaardEenheid':
                prop_datablock.append(f'        return self._{attribuut.name}.usagenote.split(\'"\')[1]'),
            else:
                prop_datablock.append(f'        return self._{attribuut.name}.get_waarde()'),
            prop_datablock.append(f''),
            if not attribuut.readonly:
                prop_datablock.append(f'    @{attribuut.name}.setter'),
                prop_datablock.append(f'    def {attribuut.name}(self, value):'),

                prop_datablock.append(f'        self._{attribuut.name}.set_waarde(value{owner_self})'),
                if type_field == 'UnionType':
                    prop_datablock.append(f'        if value is not None:')
                    prop_datablock.append(f"            self.clear_other_props('_{attribuut.name}')")
                prop_datablock.append(f'')

        for prop_line in prop_datablock:
            datablock.append(prop_line)

        return datablock
