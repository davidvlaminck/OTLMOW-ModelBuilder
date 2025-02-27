def get_ns_and_name_from_uri(objectUri):
    if '/ns/' not in objectUri:
        if '#' in objectUri:
            objectUri = objectUri.split('#')[-1]
        name = objectUri.split('/')[-1]
        return None, name

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
    elif ns == 'besluit':
        return 'Besluit'
    elif ns == 'mobiliteit':
        return 'Mobiliteit'
    elif ns == 'proefenmeting':
        return 'ProefEnMeting'
    elif ns == 'core':
        return 'Core'
    else:
        raise ValueError(f'could not get titlecase for {ns}')


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
