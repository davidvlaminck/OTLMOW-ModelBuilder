def get_ns_and_name_from_uri(objectUri):
    if '/ns/' not in objectUri:
        raise ValueError(f"{objectUri} is not a valid uri because it does not define a namespace ('/ns' is missing)")

    if '#' not in objectUri:
        raise ValueError(f"{objectUri} is not a valid uri because can not be split into a ns and name ('#' is missing)")

    short_uri = objectUri.split('/ns/')[1]
    short_uri_array = short_uri.split('#')
    return short_uri_array[0], short_uri_array[1]


def get_class_directory_from_ns(ns):
    return 'Classes/' + get_titlecase_from_ns(ns)


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
    if text == '':
        return "''"
    singles = sum(1 for c in text if c == "'")
    doubles = sum(1 for c in text if c == '"')
    if singles > doubles:
        if doubles > 0:
            return '"' + text.replace('"', '\\"') + '"'
        return '"' + text + '"'
    else:
        if singles > 0:
            return "'" + text.replace("'", "\\'") + "'"
        return "'" + text + "'"
