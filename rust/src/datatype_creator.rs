use pyo3::prelude::*;
use std::collections::HashMap;

use crate::datatype_builder_functions::{
    get_single_field_from_type_uri, get_type_name_of_complex_attribuut,
};
use crate::generic_builder_functions::{add_attributen_to_data_block, Attribute, TypeLookup};
use crate::helper_functions::{wrap_in_quotes, escape_backslash};

pub fn create_block_to_write_from_complex_primitive_or_union_types(
    attributen: Vec<Attribute>,
    valid_uri_and_types: &HashMap<String, String>,
    lookups: &TypeLookup,
    type_field: &str,
    model_location: &str,
    datatype_name: &str,
    datatype_definition: &str,
    datatype_label: &str,
    datatype_object_uri: &str,
    datatype_usagenote: &str,
    datatype_deprecated_version: &str,
    creator_name: &str,
) -> Vec<String> {
    let mut datablock = vec![
        "# coding=utf-8".to_string(),
        "from ..BaseClasses.OTLObject import OTLAttribuut".to_string(),
    ];

    let mut list_fields_to_start_with = vec![format!("{}Field", type_field)];
    if type_field == "UnionType" {
        list_fields_to_start_with.push("UnionWaarden".to_string());
    } else if type_field == "Complex" {
        datablock.push("from ..BaseClasses.WaardenObject import WaardenObject".to_string());
    } else if type_field == "Primitive" || type_field == "KwantWrd" {
        datablock.push("from ..BaseClasses.OTLField import OTLField".to_string());
        datablock.push("from ..BaseClasses.WaardenObject import WaardenObject".to_string());
        list_fields_to_start_with.clear();
    }

    let list_of_fields = collect_fields_to_import(&attributen, valid_uri_and_types, &list_fields_to_start_with, lookups);

    let base_fields = [
        "BooleanField", "ComplexField", "DateField", "DateTimeField",
        "FloatOrDecimalField", "IntegerField", "KeuzelijstField",
        "UnionTypeField", "URIField", "LiteralField",
        "NonNegIntegerField", "TimeField", "StringField", "UnionWaarden",
    ];

    for module in list_of_fields {
        if base_fields.contains(&module.as_str()) {
            datablock.push(format!("from ..BaseClasses.{} import {}", module, module));
        } else {
            datablock.push(format!("from ..Datatypes.{} import {}", module, module));
        }
    }

    datablock.push(String::new());
    datablock.push(String::new());
    datablock.push(format!("# Generated with {}. To modify: extend, do not edit", creator_name));

    if type_field == "UnionType" {
        datablock.push(format!("class {}Waarden(UnionWaarden):", datatype_name));
        datablock.push("    def __init__(self):".to_string());
        datablock.push("        UnionWaarden.__init__(self)".to_string());
    } else {
        datablock.push(format!("class {}Waarden(WaardenObject):", datatype_name));
        datablock.push("    def __init__(self):".to_string());
        datablock.push("        WaardenObject.__init__(self)".to_string());
    }

    datablock = add_attributen_to_data_block(attributen, datablock, valid_uri_and_types, lookups, false, type_field);

    let effective_type_field = if type_field == "Primitive" || type_field == "KwantWrd" {
        "OTL"
    } else {
        type_field
    };

    datablock.push(String::new());
    datablock.push(format!("# Generated with {}. To modify: extend, do not edit", creator_name));
    datablock.push(format!("class {}({}Field):", datatype_name, effective_type_field));
    datablock.push(format!("    \"\"\"{}\"\"\"", datatype_definition));
    datablock.push(format!("    naam = {}", wrap_in_quotes(datatype_name)));
    datablock.push(format!("    label = {}", wrap_in_quotes(datatype_label)));
    datablock.push(format!("    objectUri = {}", wrap_in_quotes(datatype_object_uri)));
    datablock.push(format!("    definition = {}", wrap_in_quotes(datatype_definition)));

    if datatype_usagenote != "" {
        let usagenote = if !datatype_deprecated_version.is_empty() && datatype_usagenote.contains("uit gebruik sinds versie") {
            let no_tag = datatype_deprecated_version.split('-').next().unwrap_or("");
            datatype_usagenote.replace(datatype_deprecated_version, no_tag)
        } else {
            datatype_usagenote.to_string()
        };
        datablock.push(format!("    usagenote = {}", escape_backslash(&wrap_in_quotes(&usagenote))));
    }

    if !datatype_deprecated_version.is_empty() {
        let dv = datatype_deprecated_version.split('-').next().unwrap_or("").to_string();
        datablock.push(format!("    deprecated_version = {}", wrap_in_quotes(&dv)));
    }

    if effective_type_field == "OTL" {
        datablock.push("    waarde_shortcut_applicable = True".to_string());
    }

    datablock.push(format!("    waardeObject = {}Waarden", datatype_name));
    datablock.push(String::new());
    datablock.push("    def __str__(self):".to_string());
    datablock.push(format!("        return {}Field.__str__(self)", effective_type_field));
    datablock.push(String::new());

    datablock
}

fn collect_fields_to_import(
    attributen: &[Attribute],
    valid_uri_and_types: &HashMap<String, String>,
    list_to_start_from: &[String],
    lookups: &TypeLookup,
) -> Vec<String> {
    if attributen.is_empty() {
        return list_to_start_from.to_vec();
    }

    let mut collected_list = list_to_start_from.to_vec();

    for attr in attributen {
        let type_link = lookups.type_links.get(&attr.type_uri);
        if let Some(tabel) = type_link {
            match tabel.as_str() {
                "OSLOEnumeration" => {
                    if let Some(name) = attr.type_uri.split('#').nth(1) {
                        collected_list.push(name.to_string());
                    }
                }
                "OSLODatatypePrimitive" => {
                    collected_list.push(get_single_field_from_type_uri(&attr.type_uri).unwrap_or_default());
                }
                "OSLODatatypeComplex" => {
                    let type_name = get_type_name_of_complex_attribuut(&attr.type_uri, valid_uri_and_types).unwrap_or_default();
                    collected_list.push(type_name);
                }
                "OSLODatatypeUnion" => {
                    let type_name = attr.type_uri.split('#').nth(1).unwrap_or("").to_string();
                    collected_list.push(type_name);
                }
                _ => {}
            }
        }
    }

    let mut set: Vec<String> = collected_list.into_iter().collect::<std::collections::HashSet<_>>().into_iter().collect();
    set.sort();
    set
}

#[pyfunction]
#[pyo3(name = "create_block_to_write_from_complex_primitive_or_union_types")]
#[pyo3(signature = (
    attributen,
    valid_uri_and_types,
    type_links,
    enumerations,
    complex_datatypes,
    union_datatypes,
    type_field="",
    model_location="",
    datatype_name="",
    datatype_definition="",
    datatype_label="",
    datatype_object_uri="",
    datatype_usagenote="",
    datatype_deprecated_version="",
    creator_name=""
))]
pub fn py_create_block_to_write_from_complex_primitive_or_union_types(
    py: Python<'_>,
    attributen: &Bound<'_, PyAny>,
    valid_uri_and_types: Vec<(String, String)>,
    type_links: Vec<(String, String)>,
    enumerations: Vec<(String, String)>,
    complex_datatypes: Vec<(String, String)>,
    union_datatypes: Vec<(String, String)>,
    type_field: &str,
    model_location: &str,
    datatype_name: &str,
    datatype_definition: &str,
    datatype_label: &str,
    datatype_object_uri: &str,
    datatype_usagenote: &str,
    datatype_deprecated_version: &str,
    creator_name: &str,
) -> PyResult<Vec<String>> {
    let attrs_list: Vec<Bound<'_, PyAny>> = attributen.extract()?;
    let mut attrs: Vec<Attribute> = Vec::new();
    for obj in &attrs_list {
        attrs.push(crate::generic_builder_functions::extract_attribute(obj)?);
    }

    let lookups = TypeLookup::from_pairs(
        type_links, enumerations, complex_datatypes, union_datatypes,
    );

    let valid_map: HashMap<String, String> = valid_uri_and_types.into_iter().collect();

    Ok(create_block_to_write_from_complex_primitive_or_union_types(
        attrs,
        &valid_map,
        &lookups,
        type_field,
        model_location,
        datatype_name,
        datatype_definition,
        datatype_label,
        datatype_object_uri,
        datatype_usagenote,
        datatype_deprecated_version,
        creator_name,
    ))
}
