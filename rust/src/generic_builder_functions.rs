use pyo3::prelude::*;
use pyo3::types::PyAnyMethods;
use std::collections::HashMap;

use crate::helper_functions::{escape_backslash, wrap_in_quotes, get_white_space_equivalent};
use crate::datatype_builder_functions::{
    get_single_field_from_type_uri, get_non_single_field_from_type_uri,
    get_type_name_of_complex_attribuut, get_type_name_of_union_attribuut,
    get_field_name_by_type_uri,
};

#[derive(Clone)]
pub struct Attribute {
    pub name: String,
    pub label: String,
    pub definition: String,
    pub kardinaliteit_min: String,
    pub kardinaliteit_max: String,
    pub objectUri: String,
    pub type_uri: String,
    pub constraints: String,
    pub readonly: i32,
    pub usagenote: String,
    pub deprecated_version: String,
    pub overerving: i32,
}

pub struct TypeLookup {
    pub type_links: HashMap<String, String>,
    pub enumerations: HashMap<String, String>,
    pub complex_datatypes: HashMap<String, String>,
    pub union_datatypes: HashMap<String, String>,
}

impl TypeLookup {
    pub fn from_pairs(
        type_links: Vec<(String, String)>,
        enumerations: Vec<(String, String)>,
        complex_datatypes: Vec<(String, String)>,
        union_datatypes: Vec<(String, String)>,
    ) -> Self {
        TypeLookup {
            type_links: type_links.into_iter().collect(),
            enumerations: enumerations.into_iter().collect(),
            complex_datatypes: complex_datatypes.into_iter().collect(),
            union_datatypes: union_datatypes.into_iter().collect(),
        }
    }
}

fn import_datetime(datablock: &mut Vec<String>, var_datetime: &str) {
    for (index, line) in datablock.iter().enumerate() {
        if line.is_empty() {
            datablock.insert(1, format!("from datetime import {var_datetime}"));
            return;
        }
        if line.contains("datetime") {
            datablock[index] = format!("{line}, {var_datetime}");
            return;
        }
    }
}

fn cardinality_check(attr: &Attribute, type_string: &str, datablock: &mut Vec<String>) -> String {
    if attr.kardinaliteit_max != "1" {
        for (index, line) in datablock.iter().enumerate() {
            if line.is_empty() {
                datablock.insert(1, "from typing import List".to_string());
                break;
            }
            if line == "from typing import List" {
                break;
            }
        }
        format!("List[{type_string}]")
    } else {
        type_string.to_string()
    }
}

fn get_type_hint_from_field(
    attr: &mut Attribute,
    datablock: &mut Vec<String>,
    valid_uri_and_types: &HashMap<String, String>,
    lookups: &TypeLookup,
) -> Result<String, String> {
    let field_name = get_field_name_by_type_uri(
        &attr.type_uri,
        &lookups.type_links,
        &lookups.enumerations,
        &lookups.complex_datatypes,
        &lookups.union_datatypes,
    )?;

    match field_name.as_str() {
        "StringField" | "URIField" => {
            Ok(format!(" -> {}", cardinality_check(attr, "str", datablock)))
        }
        "FloatOrDecimalField" => {
            Ok(format!(" -> {}", cardinality_check(attr, "float", datablock)))
        }
        "BooleanField" => {
            Ok(format!(" -> {}", cardinality_check(attr, "bool", datablock)))
        }
        "IntegerField" | "NonNegIntegerField" => {
            Ok(format!(" -> {}", cardinality_check(attr, "int", datablock)))
        }
        "DateField" => {
            import_datetime(datablock, "date");
            Ok(format!(" -> {}", cardinality_check(attr, "date", datablock)))
        }
        "DateTimeField" => {
            import_datetime(datablock, "datetime");
            Ok(format!(" -> {}", cardinality_check(attr, "datetime", datablock)))
        }
        "TimeField" => {
            import_datetime(datablock, "time");
            Ok(format!(" -> {}", cardinality_check(attr, "time", datablock)))
        }
        _ => {
            let field_parts = get_non_single_field_from_type_uri(&attr.type_uri, valid_uri_and_types)?;
            match field_parts[0].as_str() {
                "KeuzelijstField" => {
                    Ok(format!(" -> {}", cardinality_check(attr, "str", datablock)))
                }
                "ComplexField" | "UnionTypeField" => {
                    let type_name = &field_parts[1];
                    let type_name_waarden = format!("{type_name}Waarden");

                    for (index, line) in datablock.iter().enumerate() {
                        if !line.starts_with('#') && !line.starts_with('f') {
                            break;
                        }
                        if !line.contains(type_name) {
                            continue;
                        }
                        if line.contains(&type_name_waarden) {
                            break;
                        }
                        datablock[index] = format!("{line}, {type_name_waarden}");
                        break;
                    }

                    let hint_type = if type_name_waarden == "str" {
                        "str".to_string()
                    } else {
                        type_name_waarden.clone()
                    };
                    Ok(format!(" -> {}", cardinality_check(attr, &type_name_waarden, datablock)))
                }
                _ => {
                    eprintln!("not complexe waarde");
                    Ok(String::new())
                }
            }
        }
    }
}

pub fn add_attributen_to_data_block(
    attributen: Vec<Attribute>,
    mut datablock: Vec<String>,
    valid_uri_and_types: &HashMap<String, String>,
    lookups: &TypeLookup,
    for_class_use: bool,
    type_field: &str,
) -> Vec<String> {
    let mut prop_datablock: Vec<String> = Vec::new();

    let mut sorted = attributen;
    sorted.sort_by(|a, b| a.name.cmp(&b.name));

    for mut attribuut in sorted {
        if attribuut.overerving == 1 {
            panic!("overerving 1 is not implemented, found in attributen");
        }

        let whitespace = get_white_space_equivalent(&format!("        self._{} = OTLAttribuut(", attribuut.name));
        let field_name = get_field_name_by_type_uri(
            &attribuut.type_uri,
            &lookups.type_links,
            &lookups.enumerations,
            &lookups.complex_datatypes,
            &lookups.union_datatypes,
        ).expect("Failed to get field name");

        if attribuut.objectUri == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveil?igingssleutel" {
            attribuut.objectUri = attribuut.objectUri.replace('?', "_");
            attribuut.name = attribuut.name.replace('?', "_");
        }

        datablock.push(format!("        self._{} = OTLAttribuut(field={},", attribuut.name, field_name));
        datablock.push(format!("{whitespace}naam={},", wrap_in_quotes(&attribuut.name)));
        datablock.push(format!("{whitespace}label={},", wrap_in_quotes(&attribuut.label)));
        datablock.push(format!("{whitespace}objectUri={},", wrap_in_quotes(&attribuut.objectUri)));

        if attribuut.usagenote != "" {
            if attribuut.deprecated_version != "" && attribuut.usagenote.contains("uit gebruik sinds versie") {
                let no_tag = attribuut.deprecated_version.split('-').next().unwrap_or("");
                attribuut.usagenote = attribuut.usagenote.replace(&attribuut.deprecated_version, no_tag);
            }
            datablock.push(format!("{whitespace}usagenote={},", escape_backslash(&wrap_in_quotes(&attribuut.usagenote))));
        }
        if attribuut.readonly == 1 {
            datablock.push(format!("{whitespace}readonly=True,"));
        }
        if attribuut.deprecated_version != "" {
            attribuut.deprecated_version = attribuut.deprecated_version.split('-').next().unwrap_or("").to_string();
            datablock.push(format!("{whitespace}deprecated_version={},", wrap_in_quotes(&attribuut.deprecated_version)));
        }
        if attribuut.constraints != "" {
            datablock.push(format!("{whitespace}constraints={},", wrap_in_quotes(&attribuut.constraints)));
        }
        if attribuut.kardinaliteit_min != "1" {
            datablock.push(format!("{whitespace}kardinaliteit_min={},", wrap_in_quotes(&attribuut.kardinaliteit_min)));
        }
        if attribuut.kardinaliteit_max != "1" {
            datablock.push(format!("{whitespace}kardinaliteit_max={},", wrap_in_quotes(&attribuut.kardinaliteit_max)));
        }
        let definitie = wrap_in_quotes(&attribuut.definition.replace('\n', ""));
        datablock.push(format!("{whitespace}definition={},", definitie));
        datablock.push(format!("{whitespace}owner=self)"));
        datablock.push(String::new());

        let owner_self = if for_class_use {
            ", owner=self"
        } else {
            ", owner=self._parent"
        };

        let type_hint = match get_type_hint_from_field(&mut attribuut, &mut datablock, valid_uri_and_types, lookups) {
            Ok(hint) => hint,
            Err(e) => panic!("Failed to get type hint: {e}"),
        };

        prop_datablock.push("    @property".to_string());
        prop_datablock.push(format!("    def {}(self){}:", attribuut.name, type_hint));
        prop_datablock.push(format!("        \"\"\"{}\"\"\"", attribuut.definition));
        if type_field == "KwantWrd" && attribuut.name == "standaardEenheid" {
            prop_datablock.push(format!("        return self._{}.usagenote.split('\"')[1]", attribuut.name));
        } else {
            prop_datablock.push(format!("        return self._{}.get_waarde()", attribuut.name));
        }
        prop_datablock.push(String::new());

        if attribuut.readonly == 0 {
            prop_datablock.push(format!("    @{}.setter", attribuut.name));
            prop_datablock.push(format!("    def {}(self, value):", attribuut.name));
            prop_datablock.push(format!("        self._{}.set_waarde(value{})", attribuut.name, owner_self));

            if type_field == "UnionType" {
                prop_datablock.push("        if value is not None:".to_string());
                prop_datablock.push(format!("            self.clear_other_props('_{}')", attribuut.name));
            }
            prop_datablock.push(String::new());
        }
    }

    datablock.extend(prop_datablock);
    datablock
}

pub fn extract_attribute(obj: &Bound<'_, PyAny>) -> PyResult<Attribute> {
    Ok(Attribute {
        name: obj.getattr("name")?.extract::<String>()?,
        label: obj.getattr("label")?.extract::<String>()?,
        definition: obj.getattr("definition")?.extract::<String>()?,
        kardinaliteit_min: obj.getattr("kardinaliteit_min")?.extract::<String>()?,
        kardinaliteit_max: obj.getattr("kardinaliteit_max")?.extract::<String>()?,
        objectUri: obj.getattr("objectUri")?.extract::<String>()?,
        type_uri: obj.getattr("type")?.extract::<String>()?,
        constraints: obj.getattr("constraints")?.extract::<String>()?,
        readonly: obj.getattr("readonly")?.extract::<i32>()?,
        usagenote: obj.getattr("usagenote")?.extract::<String>()?,
        deprecated_version: obj.getattr("deprecated_version")?.extract::<String>()?,
        overerving: obj.getattr("overerving")?.extract::<i32>()?,
    })
}

#[pyfunction]
#[pyo3(name = "add_attributen_to_data_block")]
#[pyo3(signature = (attributen, datablock, valid_uri_and_types, type_links, enumerations, complex_datatypes, union_datatypes, for_class_use=false, type_field=""))]
pub fn py_add_attributen_to_data_block(
    py: Python<'_>,
    attributen: &Bound<'_, PyAny>,
    datablock: Vec<String>,
    valid_uri_and_types: Vec<(String, String)>,
    type_links: Vec<(String, String)>,
    enumerations: Vec<(String, String)>,
    complex_datatypes: Vec<(String, String)>,
    union_datatypes: Vec<(String, String)>,
    for_class_use: bool,
    type_field: &str,
) -> PyResult<Vec<String>> {
    let attrs_list: Vec<Bound<'_, PyAny>> = attributen.extract()?;
    let mut attrs: Vec<Attribute> = Vec::new();
    for obj in &attrs_list {
        attrs.push(extract_attribute(obj)?);
    }

    let lookups = TypeLookup::from_pairs(
        type_links, enumerations, complex_datatypes, union_datatypes,
    );

    let valid_map: HashMap<String, String> = valid_uri_and_types.into_iter().collect();

    Ok(add_attributen_to_data_block(
        attrs,
        datablock,
        &valid_map,
        &lookups,
        for_class_use,
        type_field,
    ))
}
