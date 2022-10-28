import os
from abc import ABC
from typing import List

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_attributen_by_type_field
from otlmow_modelbuilder.GenericBuilderFunctions import add_attributen_to_data_block, \
    get_fields_to_import_from_list_of_attributes
from otlmow_modelbuilder.HelperFunctions import wrap_in_quotes
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector


class AbstractDatatypeCreator(ABC):
    def __init__(self, oslo_collector: OSLOCollector):
        self.oslo_collector = oslo_collector

    def create_block_to_write_from_complex_primitive_or_union_types(self, oslo_datatype, type_field='',
                                                                    model_location=''):
        attributen = get_attributen_by_type_field(self.oslo_collector, type_field, oslo_datatype)

        datablock = ['# coding=utf-8',
                     'from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut']

        list_fields_to_start_with = [f'{type_field}Field']
        if type_field == 'UnionType':
            list_fields_to_start_with.append('UnionWaarden')
        elif type_field == 'Complex':
            datablock.append('from otlmow_model.BaseClasses.WaardenObject import WaardenObject')
        elif type_field == 'Primitive' or type_field == 'KwantWrd':
            datablock.append('from otlmow_model.BaseClasses.OTLField import OTLField')
            datablock.append('from otlmow_model.BaseClasses.WaardenObject import WaardenObject')
            list_fields_to_start_with = []
        list_of_fields = get_fields_to_import_from_list_of_attributes(self.oslo_collector, attributen, list_fields_to_start_with)
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
            datablock.append(f'class {oslo_datatype.name}Waarden(UnionWaarden):')
            datablock.append('    def __init__(self):')
#            datablock.append('        AttributeInfo.__init__(self, parent)')
            datablock.append('        UnionWaarden.__init__(self)')
        else:
            datablock.append(f'class {oslo_datatype.name}Waarden(WaardenObject):')
            datablock.append('    def __init__(self):')
            datablock.append('        WaardenObject.__init__(self)')

        add_attributen_to_data_block(attributen=attributen, datablock=datablock, type_field=type_field)

        if type_field == 'Primitive' or type_field == 'KwantWrd':
            type_field = 'OTL'

        datablock.append(''),
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(f'class {oslo_datatype.name}({type_field}Field):')
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

