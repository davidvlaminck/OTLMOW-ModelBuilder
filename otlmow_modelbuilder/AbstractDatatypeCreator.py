from __future__ import annotations

from abc import ABC

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_attributen_by_type_field
from otlmow_modelbuilder.GenericBuilderFunctions import (
    add_attributen_to_data_block,
    get_fields_to_import_from_list_of_attributes,
)
from otlmow_modelbuilder.HelperFunctions import escape_backslash, wrap_in_quotes
from otlmow_modelbuilder.OSLOCollector import OSLOCollector


class AbstractDatatypeCreator(ABC):
    def __init__(self, oslo_collector: OSLOCollector):
        self.oslo_collector = oslo_collector

    def create_block_to_write_from_complex_primitive_or_union_types(self, oslo_datatype, type_field='',
                                                                    model_location='', valid_uri_and_types: dict | None = None):
        if valid_uri_and_types is None:
            valid_uri_and_types = {}

        try:
            from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
                create_block_to_write_from_complex_primitive_or_union_types as rust_create,
            )
            attributen = get_attributen_by_type_field(self.oslo_collector, type_field, oslo_datatype)
            type_links = [(t.item_uri, t.item_tabel) for t in self.oslo_collector.typeLinks]
            enumerations = [(e.objectUri, e.name) for e in self.oslo_collector.enumerations]
            complex_datatypes = [(c.objectUri, c.name) for c in self.oslo_collector.complex_datatypes]
            union_datatypes = [(u.objectUri, u.name) for u in self.oslo_collector.union_datatypes]
            valid_uri_and_types_list = list(valid_uri_and_types.items())
            return rust_create(
                [a for a in attributen],
                valid_uri_and_types_list,
                type_links,
                enumerations,
                complex_datatypes,
                union_datatypes,
                type_field,
                model_location,
                oslo_datatype.name,
                oslo_datatype.definition,
                oslo_datatype.label,
                oslo_datatype.objectUri,
                oslo_datatype.usagenote,
                oslo_datatype.deprecated_version,
                self.__class__.__name__)
        except ImportError:
            pass

        attributen = get_attributen_by_type_field(self.oslo_collector, type_field, oslo_datatype)

        datablock = ['# coding=utf-8',
                     'from ..BaseClasses.OTLObject import OTLAttribuut']

        list_fields_to_start_with = [f'{type_field}Field']
        if type_field == 'UnionType':
            list_fields_to_start_with.append('UnionWaarden')
        elif type_field == 'Complex':
            datablock.append('from ..BaseClasses.WaardenObject import WaardenObject')
        elif type_field in {'Primitive', 'KwantWrd'}:
            datablock.extend(
                (
                    'from ..BaseClasses.OTLField import OTLField',
                    'from ..BaseClasses.WaardenObject import WaardenObject',
                )
            )
            list_fields_to_start_with = []
        list_of_fields = get_fields_to_import_from_list_of_attributes(self.oslo_collector, attributen,
                                                                      valid_uri_and_types=valid_uri_and_types,
                                                                      list_to_start_from=list_fields_to_start_with)
        base_fields = {'BooleanField', 'ComplexField', 'DateField', 'DateTimeField', 'FloatOrDecimalField',
                       'IntegerField', 'KeuzelijstField', 'UnionTypeField', 'URIField', 'LiteralField',
                       'NonNegIntegerField', 'TimeField', 'StringField', 'UnionWaarden'}
        for module in list_of_fields:
            if module not in base_fields:
                datablock.append(f'from ..Datatypes.{module} import {module}')
            else:
                datablock.append(f'from ..BaseClasses.{module} import {module}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        if type_field == 'UnionType':
            datablock.append(f'class {oslo_datatype.name}Waarden(UnionWaarden):')
            datablock.append('    def __init__(self):')
            datablock.append('        UnionWaarden.__init__(self)')
        else:
            datablock.append(f'class {oslo_datatype.name}Waarden(WaardenObject):')
            datablock.append('    def __init__(self):')
            datablock.append('        WaardenObject.__init__(self)')

        add_attributen_to_data_block(oslo_collector=self.oslo_collector, attributen=attributen, datablock=datablock,
                                     type_field=type_field, valid_uri_and_types=valid_uri_and_types)

        if type_field in ['Primitive', 'KwantWrd']:
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
            if oslo_datatype.deprecated_version != '' and 'uit gebruik sinds versie' in oslo_datatype.usagenote:
                no_tag = oslo_datatype.deprecated_version.split('-')[0]
                oslo_datatype.usagenote = oslo_datatype.usagenote.replace(oslo_datatype.deprecated_version, no_tag)
            datablock.append(f'    usagenote = {escape_backslash(wrap_in_quotes(oslo_datatype.usagenote))}')
        if oslo_datatype.deprecated_version != '':
            oslo_datatype.deprecated_version = oslo_datatype.deprecated_version.split('-')[0]
            datablock.append(f'    deprecated_version = {wrap_in_quotes(oslo_datatype.deprecated_version)}'),
        if type_field == 'OTL':
            datablock.append('    waarde_shortcut_applicable = True')
        datablock.append(f'    waardeObject = {oslo_datatype.name}Waarden')
        datablock.append('')
        datablock.append('    def __str__(self):')
        datablock.append(f'        return {type_field}Field.__str__(self)')
        datablock.append('')

        return datablock

