import builtins
import os

from otlmow_modelbuilder.DatatypeBuilderFunctions import (
    get_field_name_by_type_uri,
    get_non_single_field_from_type_uri,
    get_single_field_from_type_uri,
    get_type_link_from_attribuut,
    get_type_name_of_complex_attribuut,
    get_type_name_of_union_attribuut,
)
from otlmow_modelbuilder.HelperFunctions import escape_backslash, wrap_in_quotes
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLOAttribuut import OSLOAttribuut


def get_white_space_equivalent(string):
    return ''.join(' ' * len(string))


def add_noqa_ruf001_if_needed(line: str) -> str:
    if '×' in line:
        return f'{line}  # noqa: RUF001'
    return line


def shadows_builtin(name: str) -> bool:
    """True when the name shadows a Python builtin, which ruff reports as A003 on a setter decorator."""
    return name in builtins.__dict__


def import_datetime(datablock, var_datetime):
    for index, line in enumerate(datablock):
        if line == '':
            datablock.insert(1, f'from datetime import {var_datetime}')
            break
        if 'datetime' in line:
            if var_datetime not in line:
                datablock[index] = line + ', ' + var_datetime
            break


def cardinality_check(attribute, type_string):
    if attribute.kardinaliteit_max != '1':
        return f'list[{type_string}]'
    else:
        return type_string


def get_type_hint_from_field(oslo_collector, attribute, datablock, valid_uri_and_types):
    field_name = get_field_name_by_type_uri(oslo_collector, attribute.type)
    if field_name == 'StringField' or field_name == 'URIField':
        return f' -> {cardinality_check(attribute, "str")}'
    elif field_name == 'FloatOrDecimalField':
        return f' -> {cardinality_check(attribute, "float")}'
    elif field_name == 'BooleanField':
        return f' -> {cardinality_check(attribute, "bool")}'
    elif field_name in ['IntegerField', 'NonNegIntegerField']:
        return f' -> {cardinality_check(attribute, "int")}'
    elif field_name == 'DateField':
        import_datetime(datablock, 'date')
        return f' -> {cardinality_check(attribute, "date")}'
    elif field_name == 'DateTimeField':
        import_datetime(datablock, 'datetime')
        return f' -> {cardinality_check(attribute, "datetime")}'
    elif field_name == 'TimeField':
        import_datetime(datablock, 'time')
        return f' -> {cardinality_check(attribute, "time")}'
    else:
        field_name = get_non_single_field_from_type_uri(attribute.type, valid_uri_and_types)
        if field_name[0] == 'KeuzelijstField':
            return f' -> {cardinality_check(attribute, "str")}'
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
            return f' -> {cardinality_check(attribute, field_name[1] + "Waarden")}'
        else:
            print('not complexe waarde')
    return ''


def add_attributen_to_data_block(oslo_collector: OSLOCollector, attributen: list[OSLOAttribuut], datablock: list[str],
                                 valid_uri_and_types: dict, for_class_use=False, type_field=''):
    prop_datablock = []
    for attribuut in sorted(attributen, key=lambda a: a.name):
        if attribuut.overerving == 1:
            raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.objectUri}")

        whitespace = get_white_space_equivalent(f'        self._{attribuut.name} = OTLAttribuut(')
        field_name = get_field_name_by_type_uri(oslo_collector, attribuut.type)

        if attribuut.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveil?igingssleutel':
            attribuut.objectUri = attribuut.objectUri.replace('?', '_')
            attribuut.name = attribuut.name.replace('?', '_')

        datablock.append(add_noqa_ruf001_if_needed(f'        self._{attribuut.name} = OTLAttribuut(field={field_name},'))
        datablock.append(f'{whitespace}naam={wrap_in_quotes(attribuut.name)},')
        datablock.append(f'{whitespace}label={wrap_in_quotes(attribuut.label)},')
        datablock.append(f'{whitespace}objectUri={wrap_in_quotes(attribuut.objectUri)},')

        if attribuut.usagenote != '':
            if attribuut.deprecated_version != '' and 'uit gebruik sinds versie' in attribuut.usagenote:
                no_tag = attribuut.deprecated_version.split('-')[0]
                attribuut.usagenote = attribuut.usagenote.replace(attribuut.deprecated_version, no_tag)
            datablock.append(f'{whitespace}usagenote={escape_backslash(wrap_in_quotes(attribuut.usagenote))},')
        if attribuut.readonly == 1:
            datablock.append(f'{whitespace}readonly=True,')
        if attribuut.deprecated_version != '':
            attribuut.deprecated_version = attribuut.deprecated_version.split('-')[0]
            datablock.append(f'{whitespace}deprecated_version={wrap_in_quotes(attribuut.deprecated_version)},')
        if attribuut.constraints != '':
            datablock.append(f'{whitespace}constraints={wrap_in_quotes(attribuut.constraints)},')
        if attribuut.kardinaliteit_min != '1':
            datablock.append(f'{whitespace}kardinaliteit_min={wrap_in_quotes(attribuut.kardinaliteit_min)},')
        if attribuut.kardinaliteit_max != '1':
            datablock.append(f'{whitespace}kardinaliteit_max={wrap_in_quotes(attribuut.kardinaliteit_max)},')
        definitie = wrap_in_quotes(attribuut.definition.replace('\n', ''))
        datablock.append(add_noqa_ruf001_if_needed(f'{whitespace}definition={definitie},'))
        datablock.append(f'{whitespace}owner=self)')
        datablock.append('')

        owner_self = ', owner=self'
        if not for_class_use:
            owner_self += '._parent'

        type_hint = get_type_hint_from_field(oslo_collector, attribuut, datablock, valid_uri_and_types)

        getter_body = f'        return self._{attribuut.name}.get_waarde()'
        if type_field == 'KwantWrd' and attribuut.name == 'standaardEenheid':
            getter_body = f'        return self._{attribuut.name}.usagenote.split(\'"\')[1]'

        setter_body = [f'        self._{attribuut.name}.set_waarde(value{owner_self})']
        if type_field == 'UnionType':
            setter_body.append('        if value is not None:')
            setter_body.append(f"            self.clear_other_props('_{attribuut.name}')")

        if shadows_builtin(attribuut.name):
            prop_datablock.append(f'    def _get_{attribuut.name}(self){type_hint}:')
            prop_datablock.append(add_noqa_ruf001_if_needed(f'        """{attribuut.definition}"""'))
            prop_datablock.append(getter_body)
            prop_datablock.append('')
            if attribuut.readonly:
                prop_datablock.append(f'    {attribuut.name} = property(_get_{attribuut.name})')
            else:
                prop_datablock.append(f'    def _set_{attribuut.name}(self, value):')
                prop_datablock.extend(setter_body)
                prop_datablock.append(f'    {attribuut.name} = property(_get_{attribuut.name}, '
                                      f'_set_{attribuut.name})')
            prop_datablock.append('')
        else:
            prop_datablock.append('    @property')
            prop_datablock.append(f'    def {attribuut.name}(self){type_hint}:')
            prop_datablock.append(add_noqa_ruf001_if_needed(f'        """{attribuut.definition}"""'))
            prop_datablock.append(getter_body)
            prop_datablock.append('')
            if not attribuut.readonly:
                prop_datablock.append(f'    @{attribuut.name}.setter')
                prop_datablock.append(f'    def {attribuut.name}(self, value):')
                prop_datablock.extend(setter_body)
                prop_datablock.append('')

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


_MAX_IMPORT_LINE_LENGTH = 88


def _import_name_sort_key(name: str) -> tuple[int, str]:
    """Sort imported names the way ruff's isort does with order-by-type: constants, classes, then the rest."""
    if name.isupper():
        group = 0
    elif name[:1].isupper():
        group = 1
    else:
        group = 2
    return group, name.lower()


def _parse_import_line(line: str) -> tuple[str, list[str]]:
    """Split a generated import line into its module path and the imported names."""
    if line.startswith('from '):
        module, _, names = line[len('from '):].partition(' import ')
        return module, [name.strip() for name in names.split(',') if name.strip()]
    if line.startswith('import '):
        return line[len('import '):], []
    return line, []


def _render_import(module: str, names: list[str], is_from: bool) -> list[str]:
    """Render a single import as one line, or as a parenthesised block when it exceeds the line length."""
    sorted_names = sorted(set(names), key=_import_name_sort_key)
    if not is_from:
        return [f'import {module}']
    single_line = f'from {module} import {", ".join(sorted_names)}'
    if len(single_line) <= _MAX_IMPORT_LINE_LENGTH:
        return [single_line]
    rendered = [f'from {module} import (']
    rendered.extend(f'    {name},' for name in sorted_names)
    rendered.append(')')
    return rendered


def organize_import_block(lines: list[str]) -> list[str]:
    """Group, merge and sort the leading import block so it matches ruff's isort rules (I001).

    Standard library imports are placed first, followed by a blank line and the relative
    (local folder) imports. Imports of the same module are merged, the names inside each
    import are sorted, and lines that get too long are wrapped in parentheses.
    """
    end = len(lines)
    for index, line in enumerate(lines):
        if line == '':
            end = index
            break

    comments: list[str] = []
    stdlib_modules: dict[str, list[str]] = {}
    local_modules: dict[str, list[str]] = {}
    plain_imports: list[str] = []
    for line in lines[:end]:
        if line.startswith('#'):
            comments.append(line)
            continue
        module, names = _parse_import_line(line)
        is_from = line.startswith('from ')
        if not is_from:
            plain_imports.append(_render_import(module, names, is_from=False)[0])
            continue
        target = local_modules if module.startswith('.') else stdlib_modules
        target.setdefault(module, []).extend(names)

    def render_group(modules: dict[str, list[str]]) -> list[str]:
        rendered: list[str] = []
        for module in sorted(modules, key=str.lower):
            rendered.extend(_render_import(module, modules[module], is_from=True))
        return rendered

    stdlib_lines = plain_imports + render_group(stdlib_modules)
    stdlib_lines.sort(key=lambda line: _parse_import_line(line)[0].lower())
    local_lines = render_group(local_modules)

    organized = list(comments)
    organized.extend(stdlib_lines)
    if stdlib_lines and local_lines:
        organized.append('')
    organized.extend(local_lines)
    return organized + lines[end:]


def write_to_file(filename, directory: str, data_to_write: list[str], relative_path='', write_mode='w'):
    if relative_path == '':
        base_dir = os.path.dirname(os.path.realpath(__file__))
        base_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
    else:
        base_dir = relative_path
    path = f"{base_dir}/{directory}/{filename}.py"
    dir_path = f"{base_dir}/{directory}"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(path, write_mode, encoding='utf-8') as file:
        file.writelines(line + "\n" for line in organize_import_block(data_to_write))
