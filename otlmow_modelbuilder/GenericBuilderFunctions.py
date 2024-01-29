import os
from typing import List, Dict

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_single_field_from_type_uri, get_type_link_from_attribuut, \
    get_type_name_of_complex_attribuut, get_type_name_of_union_attribuut, get_field_name_from_type_uri, \
    get_non_single_field_from_type_uri
from otlmow_modelbuilder.HelperFunctions import wrap_in_quotes, escape_backslash


def get_white_space_equivalent(string):
    return ''.join(' ' * len(string))


def import_datetime(datablock, var_datetime):
    for index, line in enumerate(datablock):
        if line == '':
            datablock.insert(1, f'from datetime import {var_datetime}')
            break
        if 'datetime' in line:
            datablock[index] = line + ', ' + var_datetime
            break


def cardinality_check(attribute, type_string, datablock):
    if attribute.kardinaliteit_max != '1':
        for index, line in enumerate(datablock):
            if line == '':
                datablock.insert(1, 'from typing import List')
                break
            if line == 'from typing import List':
                break
        return f'List[{type_string}]'
    else:
        return type_string


def get_type_hint_from_field(attribute, datablock, valid_uri_and_types):
    field_name = get_single_field_from_type_uri(attribute.type)
    if field_name == 'StringField' or field_name == 'URIField':
        return f' -> {cardinality_check(attribute, "str", datablock)}'
    elif field_name == 'FloatOrDecimalField':
        return f' -> {cardinality_check(attribute, "float", datablock)}'
    elif field_name == 'BooleanField':
        return f' -> {cardinality_check(attribute, "bool", datablock)}'
    elif field_name in ['IntegerField', 'NonNegIntegerField']:
        return f' -> {cardinality_check(attribute, "int", datablock)}'
    elif field_name == 'DateField':
        import_datetime(datablock, 'date')
        return f' -> {cardinality_check(attribute, "date", datablock)}'
    elif field_name == 'DateTimeField':
        import_datetime(datablock, 'datetime')
        return f' -> {cardinality_check(attribute, "datetime", datablock)}'
    elif field_name == 'TimeField':
        import_datetime(datablock, 'time')
        return f' -> {cardinality_check(attribute, "time", datablock)}'
    else:
        field_name = get_non_single_field_from_type_uri(attribute.type, valid_uri_and_types)
        if field_name[0] == 'KeuzelijstField':
            return f' -> {cardinality_check(attribute, "str", datablock)}'
        if field_name[0] == 'ComplexField' or field_name[0] == 'UnionTypeField':
            for index, line in enumerate(datablock):
                if line[0] not in ['#', 'f']:  # only loop over the import part
                    break
                if field_name[1] not in line:
                    continue
                if f'{field_name[1]}Waarden' in line:
                    break
                datablock[index] = line + f', {field_name[1]}Waarden'
                break
            return f' -> {cardinality_check(attribute, field_name[1] + "Waarden", datablock)}'
        else:
            print('not complexe waarde')
    return ''


def add_attributen_to_data_block(attributen, datablock: List[str], valid_uri_and_types: Dict, for_class_use=False,
                                 type_field=''):
    prop_datablock = []
    for attribuut in sorted(attributen, key=lambda a: a.name):
        if attribuut.overerving == 1:
            raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.objectUri}")

        whitespace = get_white_space_equivalent(f'        self._{attribuut.name} = OTLAttribuut(')
        field_name = get_single_field_from_type_uri(attribuut.type)

        if attribuut.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveil?igingssleutel':
            attribuut.objectUri = attribuut.objectUri.replace('?', '_')
            attribuut.name = attribuut.name.replace('?', '_')

        datablock.append(f'        self._{attribuut.name} = OTLAttribuut(field={field_name},')
        datablock.append(f'{whitespace}naam={wrap_in_quotes(attribuut.name)},')
        datablock.append(f'{whitespace}label={wrap_in_quotes(attribuut.label)},')
        datablock.append(f'{whitespace}objectUri={wrap_in_quotes(attribuut.objectUri)},')
        if attribuut.usagenote != '':
            datablock.append(f'{whitespace}usagenote={escape_backslash(wrap_in_quotes(attribuut.usagenote))},')
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

        type_hint = get_type_hint_from_field(attribuut, datablock, valid_uri_and_types)

        prop_datablock.append(f'    @property'),
        prop_datablock.append(f'    def {attribuut.name}(self){type_hint}:'),
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

    datablock.extend(prop_datablock)

    return datablock


def get_fields_to_import_from_list_of_attributes(oslo_collector, attributen, valid_uri_and_types,
                                                 list_to_start_from=None):
    if list_to_start_from is None:
        list_to_start_from = []
    if len(attributen) == 0:
        return list_to_start_from

    collected_list = []
    collected_list.extend(list_to_start_from)

    for attribuut in attributen:
        type_link = get_type_link_from_attribuut(oslo_collector, attribuut).item_tabel
        if type_link == "OSLOEnumeration":
            collected_list.append(attribuut.type.split('#')[1])
        elif type_link == "OSLODatatypePrimitive":
            collected_list.append(get_single_field_from_type_uri(attribuut.type))
        elif type_link == "OSLODatatypeComplex":
            collected_list.append(get_type_name_of_complex_attribuut(attribuut.type,
                                                                     valid_uri_and_types=valid_uri_and_types))
        elif type_link == "OSLODatatypeUnion":
            collected_list.append(get_type_name_of_union_attribuut(attribuut.type))
        else:
            raise not NotImplementedError(f"{type_link} not implemented")

    distinct_types_list = list(set(collected_list))
    sorted_list = sorted(distinct_types_list, key=lambda t: t)
    return sorted_list


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
