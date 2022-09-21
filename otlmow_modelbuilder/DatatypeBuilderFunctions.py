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


def get_field_name_from_type_uri(attribuut_type):
    if attribuut_type.startswith('http://www.w3.org/2001/XMLSchema#'):
        return get_single_field_from_type_uri(attribuut_type)
    if attribuut_type.startswith("https://schema.org/"):
        return get_non_single_field_from_type_uri(attribuut_type)[1]
    return get_non_single_field_from_type_uri(attribuut_type)[1]


def get_attributen_by_type_field(oslo_collector, type_field, oslo_datatype):
    if type_field == 'Complex':
        return oslo_collector.find_complex_datatype_attributes_by_class_uri(oslo_datatype.objectUri)
    elif type_field == 'UnionType':
        return oslo_collector.find_union_datatype_attributes_by_class_uri(oslo_datatype.objectUri)
    else:
        return oslo_collector.find_primitive_datatype_attributes_by_class_uri(oslo_datatype.objectUri)


def get_type_name_of_complex_attribuut(type_uri: str):
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


def get_type_link_from_attribuut(oslo_collector, attribuut):
    type_link = oslo_collector.find_type_link_by_uri(attribuut.type)
    if type_link is not None:
        return type_link


def get_fields_and_names_from_list_of_attributes(attributen):
    if len(attributen) == 0:
        return []

    primitive_types_list = list(
        filter(lambda t: t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))
    other_types_list = list(
        filter(lambda t: not t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))

    select_types_list = list(
        map(lambda a: (get_single_field_from_type_uri(a.type), a.name), primitive_types_list))

    for nonPrimitiveType in other_types_list:
        select_types_list.append((get_field_name_from_type_uri(nonPrimitiveType.type), nonPrimitiveType.name))

    distinct_types_list = list(set(select_types_list))
    sorted_list = sorted(distinct_types_list, key=lambda t: t)
    return sorted_list


def get_type_name_of_union_attribuut(type_uri: str):
    if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/"):
        return type_uri[type_uri.find("#") + 1::]

    raise NotImplementedError(f"get_type_name_of_complex_attribuut fails to get typename from {type_uri}")
