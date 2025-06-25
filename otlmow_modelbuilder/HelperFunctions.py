def get_ns_and_name_from_uri(object_uri) -> tuple[str, str]:
    if '/ns/' not in object_uri:
        if '#' in object_uri:
            object_uri = object_uri.split('#')[-1]
        name = object_uri.split('/')[-1]
        return '', name

    if '#' not in object_uri:
        raise ValueError(f"{object_uri} is not a valid uri because can not be split into a ns and name ('#' is missing)")

    short_uri = object_uri.split('/ns/')[1]
    short_uri_array = short_uri.split('#')
    ns, name = short_uri_array[0], short_uri_array[1]
    if object_uri.startswith('https://lgc'):
        if '.' in name:
            name = name.replace('.', '_')
        if '-' in name:
            name = name.replace('-', '_')
        if name == "RIS":
            name = "RISLegacy"
        elif name == 'Fietstel':
            name = 'FietstelLegacy'
        elif name == 'Brug':
            name = 'BeweegbareBrug'
        elif name == 'Voedingskeuzeschakelaar':
            name = 'VKS'
        return 'legacy', name
    return ns, name



def get_class_directory_from_ns(ns) -> str:
    return f'Classes/{get_titlecase_from_ns(ns)}'


def get_titlecase_from_ns(ns: str) -> str:
    if ns == 'proefenmeting':
        return 'ProefEnMeting'
    elif ns == 'implementatieelement':
        return 'ImplementatieElement'
    elif ns is None:
        raise ValueError(f'could not get titlecase for {ns}')
    else:
        return ns.title()


def escape_backslash(text: str) -> str:
    return text.replace('\\', '\\\\')


def wrap_in_quotes(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError
    if not text:
        return "''"
    singles = text.count("'")
    doubles = text.count('"')
    if singles > doubles:
        return '"' + text.replace('"', '\\"') + '"' if doubles > 0 else f'"{text}"'
    return "'" + text.replace("'", "\\'") + "'" if singles > 0 else f"'{text}'"
