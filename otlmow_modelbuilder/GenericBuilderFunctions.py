import os
from typing import List

from otlmow_modelbuilder.DatatypeBuilderFunctions import get_single_field_from_type_uri, get_type_link_from_attribuut, \
    get_type_name_of_complex_attribuut, get_type_name_of_union_attribuut
from otlmow_modelbuilder.HelperFunctions import wrap_in_quotes


def get_white_space_equivalent(string):
    return ''.join(' ' * len(string))


def add_attributen_to_data_block(attributen, datablock: List[str], for_class_use=False, type_field=''):
    prop_datablock = []
    for attribuut in sorted(attributen, key=lambda a: a.name):
        if attribuut.overerving == 1:
            raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.objectUri}")

        whitespace = get_white_space_equivalent(f'        self._{attribuut.name} = OTLAttribuut(')
        field_name = get_single_field_from_type_uri(attribuut.type)

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

    datablock.extend(prop_datablock)

    return datablock


def get_fields_to_import_from_list_of_attributes(oslo_collector, attributen, list_to_start_from=None):
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
            collected_list.append(get_type_name_of_complex_attribuut(attribuut.type))
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
