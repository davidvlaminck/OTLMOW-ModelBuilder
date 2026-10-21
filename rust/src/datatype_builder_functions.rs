use pyo3::prelude::*;
use std::collections::HashMap;

pub fn get_single_field_from_type_uri(field_type: &str) -> Result<String, String> {
    if field_type.starts_with("https://wegenenverkeer.data.vlaanderen.be/ns/") && field_type.contains('#') {
        if let Some(idx) = field_type.find('#') {
            return Ok(field_type[idx + 1..].to_string());
        }
    }

    match field_type {
        "" => Err("field_type is None".to_string()),
        "http://www.w3.org/2001/XMLSchema#decimal" => Ok("FloatOrDecimalField".to_string()),
        "http://www.w3.org/2001/XMLSchema#string" => Ok("StringField".to_string()),
        "http://www.w3.org/1999/02/22-rdf-syntax-ns#langString" => Ok("StringField".to_string()),
        "http://www.w3.org/2001/XMLSchema#boolean" => Ok("BooleanField".to_string()),
        "http://www.w3.org/2001/XMLSchema#integer" => Ok("IntegerField".to_string()),
        "http://www.w3.org/2001/XMLSchema#nonNegativeInteger" => Ok("NonNegIntegerField".to_string()),
        "http://www.w3.org/2001/XMLSchema#date" => Ok("DateField".to_string()),
        "http://www.w3.org/2001/XMLSchema#dateTime" => Ok("DateTimeField".to_string()),
        "http://www.w3.org/2001/XMLSchema#time" => Ok("TimeField".to_string()),
        "http://www.w3.org/2001/XMLSchema#anyURI" => Ok("URIField".to_string()),
        "https://schema.org/OpeningHoursSpecification" => Ok("DtcOpeningsurenSpecificatie".to_string()),
        "https://schema.org/ContactPoint" => Ok("DtcContactinfo".to_string()),
        "http://www.w3.org/2000/01/rdf-schema#Literal" => Ok("StringField".to_string()),
        _ => Err(format!(
            "not supported field_type in get_single_field_from_type_uri() for {}",
            field_type
        )),
    }
}

pub fn get_non_single_field_from_type_uri(
    field_type: &str,
    valid_uri_and_types: &HashMap<String, String>,
) -> Result<Vec<String>, String> {
    if field_type.contains("#Dtc") {
        if let Some(idx) = field_type.find('#') {
            let type_name = &field_type[idx + 1..];
            return Ok(vec!["ComplexField".to_string(), type_name.to_string()]);
        }
    }

    if let Some(type_name) = valid_uri_and_types.get(field_type) {
        return Ok(vec!["ComplexField".to_string(), type_name.clone()]);
    }

    if field_type.contains("#Dte") || field_type.contains("#KwantWrd") {
        if let Some(idx) = field_type.find('#') {
            let type_name = &field_type[idx + 1..];
            return Ok(vec!["ComplexField".to_string(), type_name.to_string()]);
        }
    }

    let special_types = [
        "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaalType",
        "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KLLuidsprekerVormgeving",
    ];
    if field_type.contains("#Kl") || special_types.contains(&field_type) {
        if let Some(idx) = field_type.find('#') {
            let type_name = &field_type[idx + 1..];
            return Ok(vec!["KeuzelijstField".to_string(), type_name.to_string()]);
        }
    }

    if field_type.contains("#Dtu") {
        if let Some(idx) = field_type.find('#') {
            let type_name = &field_type[idx + 1..];
            return Ok(vec!["UnionTypeField".to_string(), type_name.to_string()]);
        }
    }

    Err(format!(
        "not supported field_type {} in get_non_single_field_from_type_uri()",
        field_type
    ))
}

pub fn get_type_name_of_complex_attribuut(
    type_uri: &str,
    valid_uri_and_types: &HashMap<String, String>,
) -> Result<String, String> {
    if let Some(type_name) = valid_uri_and_types.get(type_uri) {
        return Ok(type_name.clone());
    }
    if type_uri.contains("/ns/") || type_uri.starts_with("http://www.w3.org/2001/XMLSchema#") {
        if let Some(idx) = type_uri.find('#') {
            return Ok(type_uri[idx + 1..].to_string());
        }
    }

    Err(format!(
        "get_type_name_of_complex_attribuut fails to get typename from {}",
        type_uri
    ))
}

pub fn get_type_name_of_union_attribuut(type_uri: &str) -> Result<String, String> {
    if type_uri.contains("/ns/") && type_uri.contains('#') {
        if let Some(idx) = type_uri.find('#') {
            return Ok(type_uri[idx + 1..].to_string());
        }
    }

    Err(format!(
        "get_type_name_of_complex_attribuut fails to get typename from {}",
        type_uri
    ))
}

pub fn get_field_name_from_type_uri(
    attribuut_type: &str,
    valid_uri_and_types: &HashMap<String, String>,
) -> Result<String, String> {
    if attribuut_type.starts_with("http://www.w3.org/2001/XMLSchema#") {
        return get_single_field_from_type_uri(attribuut_type);
    }
    if attribuut_type.starts_with("https://schema.org/") {
        let result = get_non_single_field_from_type_uri(attribuut_type, valid_uri_and_types)?;
        return Ok(result[1].clone());
    }
    let result = get_non_single_field_from_type_uri(attribuut_type, valid_uri_and_types)?;
    Ok(result[1].clone())
}

pub fn get_type_link_from_type_uri(
    type_uri: &str,
    type_links: &HashMap<String, String>,
) -> Result<String, String> {
    type_links
        .get(type_uri)
        .cloned()
        .ok_or_else(|| format!("type_link not found for {type_uri}"))
}

pub fn get_field_name_by_type_uri(
    type_uri: &str,
    type_links: &HashMap<String, String>,
    enumerations: &HashMap<String, String>,
    complex_datatypes: &HashMap<String, String>,
    union_datatypes: &HashMap<String, String>,
) -> Result<String, String> {
    let item_tabel = get_type_link_from_type_uri(type_uri, type_links)?;

    match item_tabel.as_str() {
        "OSLOEnumeration" => enumerations
            .get(type_uri)
            .cloned()
            .ok_or_else(|| format!("enumeration not found for {type_uri}")),
        "OSLODatatypePrimitive" => get_single_field_from_type_uri(type_uri),
        "OSLODatatypeComplex" => complex_datatypes
            .get(type_uri)
            .cloned()
            .ok_or_else(|| format!("complex datatype not found for {type_uri}")),
        "OSLODatatypeUnion" => union_datatypes
            .get(type_uri)
            .cloned()
            .ok_or_else(|| format!("union datatype not found for {type_uri}")),
        _ => Err(format!("not supported item_tabel {item_tabel} in get_field_name_by_type_uri()")),
    }
}

pub fn get_fields_to_import_from_list_of_attributes(
    attribute_types: &[String],
    type_links: &HashMap<String, String>,
    valid_uri_and_types: &HashMap<String, String>,
    list_to_start_from: Vec<String>,
) -> Result<Vec<String>, String> {
    let mut collected_list = list_to_start_from;

    for attribuut_type in attribute_types {
        let item_tabel = get_type_link_from_type_uri(attribuut_type, type_links)?;

        match item_tabel.as_str() {
            "OSLOEnumeration" => {
                if let Some(idx) = attribuut_type.find('#') {
                    collected_list.push(attribuut_type[idx + 1..].to_string());
                } else {
                    return Err(format!("no '#' found in type_uri {attribuut_type}"));
                }
            }
            "OSLODatatypePrimitive" => {
                collected_list.push(get_single_field_from_type_uri(attribuut_type)?);
            }
            "OSLODatatypeComplex" => {
                collected_list.push(get_type_name_of_complex_attribuut(attribuut_type, valid_uri_and_types)?);
            }
            "OSLODatatypeUnion" => {
                collected_list.push(get_type_name_of_union_attribuut(attribuut_type)?);
            }
            other => {
                return Err(format!("{other} not implemented"));
            }
        }
    }

    let mut distinct: std::collections::BTreeSet<String> = std::collections::BTreeSet::new();
    for item in &collected_list {
        distinct.insert(item.clone());
    }
    Ok(distinct.into_iter().collect())
}

fn vec_to_hashmap(pairs: Vec<(String, String)>) -> HashMap<String, String> {
    pairs.into_iter().collect()
}

#[pyfunction]
#[pyo3(name = "get_single_field_from_type_uri")]
pub fn py_get_single_field_from_type_uri(field_type: Option<&str>) -> PyResult<String> {
    match field_type {
        None => Err(pyo3::exceptions::PyValueError::new_err(
            "not supported field_type in get_single_field_from_type_uri() for None",
        )),
        Some(ft) => get_single_field_from_type_uri(ft)
            .map_err(|e| pyo3::exceptions::PyValueError::new_err(e)),
    }
}

#[pyfunction]
#[pyo3(name = "get_non_single_field_from_type_uri")]
pub fn py_get_non_single_field_from_type_uri(
    field_type: &str,
    valid_uri_and_types: Vec<(String, String)>,
) -> PyResult<Vec<String>> {
    let map = vec_to_hashmap(valid_uri_and_types);
    get_non_single_field_from_type_uri(field_type, &map)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_type_name_of_complex_attribuut")]
pub fn py_get_type_name_of_complex_attribuut(
    type_uri: &str,
    valid_uri_and_types: Vec<(String, String)>,
) -> PyResult<String> {
    let map = vec_to_hashmap(valid_uri_and_types);
    get_type_name_of_complex_attribuut(type_uri, &map)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_type_name_of_union_attribuut")]
pub fn py_get_type_name_of_union_attribuut(type_uri: &str) -> PyResult<String> {
    get_type_name_of_union_attribuut(type_uri)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_field_name_from_type_uri")]
pub fn py_get_field_name_from_type_uri(
    attribuut_type: &str,
    valid_uri_and_types: Vec<(String, String)>,
) -> PyResult<String> {
    let map = vec_to_hashmap(valid_uri_and_types);
    get_field_name_from_type_uri(attribuut_type, &map)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_field_name_by_type_uri")]
pub fn py_get_field_name_by_type_uri(
    type_uri: &str,
    type_links: Vec<(String, String)>,
    enumerations: Vec<(String, String)>,
    complex_datatypes: Vec<(String, String)>,
    union_datatypes: Vec<(String, String)>,
) -> PyResult<String> {
    let type_links_map = vec_to_hashmap(type_links);
    let enumerations_map = vec_to_hashmap(enumerations);
    let complex_map = vec_to_hashmap(complex_datatypes);
    let union_map = vec_to_hashmap(union_datatypes);
    get_field_name_by_type_uri(type_uri, &type_links_map, &enumerations_map, &complex_map, &union_map)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_fields_to_import_from_list_of_attributes")]
pub fn py_get_fields_to_import_from_list_of_attributes(
    attribute_types: Vec<String>,
    type_links: Vec<(String, String)>,
    valid_uri_and_types: Vec<(String, String)>,
    list_to_start_from: Vec<String>,
) -> PyResult<Vec<String>> {
    let type_links_map = vec_to_hashmap(type_links);
    let valid_uri_and_types_map = vec_to_hashmap(valid_uri_and_types);
    get_fields_to_import_from_list_of_attributes(
        &attribute_types,
        &type_links_map,
        &valid_uri_and_types_map,
        list_to_start_from,
    )    .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}
