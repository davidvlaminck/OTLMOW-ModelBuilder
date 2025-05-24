def get_shortened_uri(object_uri: str) -> str:
    if object_uri == 'http://purl.org/dc/terms/Agent':
        return 'purl:Agent'
    if '/ns/' not in object_uri:
        raise ValueError(f'{object_uri} is not a valid uri to extract a namespace from')
    shorter_uri = object_uri.split('/ns/')[1]
    if object_uri.startswith('https://lgc.'):
        return f'lgc:{shorter_uri}'
    return shorter_uri


def get_ns_and_name_from_uri(object_uri) -> tuple[str, str]:
    if object_uri == 'http://purl.org/dc/terms/Agent':
        return '', 'Agent'
    short_uri = get_shortened_uri(object_uri)
    short_uri_array = short_uri.split('#')
    ns, name = short_uri_array[0], short_uri_array[1]
    if ns.startswith('lgc:'):
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
    if ns == 'abstracten':
        return 'Abstracten'
    elif ns == 'implementatieelement':
        return 'ImplementatieElement'
    elif ns == 'installatie':
        return 'Installatie'
    elif ns == 'levenscyclus':
        return 'Levenscyclus'
    elif ns == 'onderdeel':
        return 'Onderdeel'
    elif ns == 'proefenmeting':
        return 'ProefEnMeting'
    else:
        raise ValueError()


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
