#![allow(dead_code, non_snake_case)]

use pyo3::prelude::*;
use pyo3::types::PyAnyMethods;
use std::collections::HashMap;
use std::fs;
use std::path::Path;

use crate::datatype_creator::create_block_to_write_from_complex_primitive_or_union_types;
use crate::enumeration_creator::create_block_to_write_from_enumeration;
use crate::class_creator::{create_block_from_class, Inheritance, OSLORelatie};
use crate::generic_builder_functions::{Attribute, TypeLookup};
use crate::ttl_reader::PyKeuzelijstWaarde;

fn write_file_content(directory: &str, subdirectory: &str, filename: &str, datablock: &[String]) -> Result<(), String> {
    let path = Path::new(directory).join(subdirectory).join(format!("{}.py", filename));
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent).map_err(|e| e.to_string())?;
    }
    let content = datablock.join("\n");
    let content = format!("{}\n", content);
    fs::write(&path, content).map_err(|e| e.to_string())?;
    Ok(())
}

fn is_valid_uri(uri: &str, valid_map: &HashMap<String, String>, regexes: &[String]) -> bool {
    if valid_map.contains_key(uri) {
        return true;
    }
    for regex_str in regexes {
        if let Ok(re) = regex::Regex::new(regex_str) {
            if re.is_match(uri) {
                return true;
            }
        }
    }
    false
}

#[derive(Debug, Clone)]
pub struct PyClassData {
    pub object_uri: String,
    pub name: String,
    pub definition: String,
    pub label: String,
    pub usagenote: String,
    pub abstract_val: i32,
    pub deprecated_version: String,
}

#[derive(Debug, Clone)]
pub struct PyDatatypeData {
    pub object_uri: String,
    pub name: String,
    pub definition: String,
    pub label: String,
    pub usagenote: String,
    pub deprecated_version: String,
}

#[pyfunction]
#[pyo3(name = "generate_model_optimized")]
#[pyo3(signature = (
    directory,
    model_name,
    settings,
    type_links,
    enumerations_lookup,
    complex_datatypes_lookup,
    union_datatypes_lookup,
    primitive_datatypes,
    complex_datatypes,
    union_datatypes,
    enumerations,
    enumeration_waardes,
    enumeration_adm_status,
    classes,
    geometry_type_map,
    inheritance_map,
    attributes_by_class_uri,
    inheritances_by_class_uri,
    relations_by_object_uri,
    complex_datatype_validation_rules,
    primitive_datatype_validation_rules,
    union_datatype_validation_rules,
    enumeration_validation_rules,
    class_validation_rules,
    include_kl_test_keuzelijst
))]
pub fn py_generate_model_optimized(
    _py: Python<'_>,
    directory: &str,
    model_name: &str,
    settings: &Bound<'_, PyAny>,
    type_links: Vec<(String, String)>,
    enumerations_lookup: Vec<(String, String)>,
    complex_datatypes_lookup: Vec<(String, String)>,
    union_datatypes_lookup: Vec<(String, String)>,
    primitive_datatypes: Vec<Bound<'_, PyAny>>,
    complex_datatypes: Vec<Bound<'_, PyAny>>,
    union_datatypes: Vec<Bound<'_, PyAny>>,
    enumerations: Vec<Bound<'_, PyAny>>,
    enumeration_waardes: &Bound<'_, PyAny>,
    enumeration_adm_status: &Bound<'_, PyAny>,
    classes: Vec<Bound<'_, PyAny>>,
    geometry_type_map: HashMap<String, Vec<String>>,
    inheritance_map: HashMap<String, Vec<String>>,
    attributes_by_class_uri: &Bound<'_, PyAny>,
    inheritances_by_class_uri: &Bound<'_, PyAny>,
    relations_by_object_uri: &Bound<'_, PyAny>,
    complex_datatype_validation_rules: HashMap<String, String>,
    primitive_datatype_validation_rules: HashMap<String, String>,
    union_datatype_validation_rules: HashMap<String, String>,
    enumeration_validation_rules: HashMap<String, String>,
    class_validation_rules: HashMap<String, String>,
    include_kl_test_keuzelijst: bool,
) -> PyResult<(usize, usize)> {
    let _ = include_kl_test_keuzelijst;
    let lookups = TypeLookup::from_pairs(
        type_links, enumerations_lookup, complex_datatypes_lookup, union_datatypes_lookup,
    );

    let skip_primitive_uris = [
        "http://www.w3.org/2000/01/rdf-schema#Literal",
        "http://www.w3.org/2001/XMLSchema#dateTime",
        "http://www.w3.org/2001/XMLSchema#integer",
        "http://www.w3.org/2001/XMLSchema#decimal",
        "http://www.w3.org/2001/XMLSchema#time",
        "http://www.w3.org/2001/XMLSchema#date",
        "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
        "http://www.w3.org/2001/XMLSchema#string",
        "http://www.w3.org/1999/02/22-rdf-syntax-ns#langString",
        "http://www.w3.org/2001/XMLSchema#boolean",
        "http://www.w3.org/2001/XMLSchema#anyURI",
    ];

    let mut files_written = 0usize;
    let mut errors = 0usize;

    // Pre-extract all attributes, inheritances, relations into Rust
    let attr_map: HashMap<String, Vec<Attribute>> = {
        let dict: HashMap<String, Vec<Bound<'_, PyAny>>> = attributes_by_class_uri.extract()?;
        let mut map = HashMap::new();
        for (key, items) in dict {
            let mut attrs = Vec::new();
            for obj in &items {
                attrs.push(crate::generic_builder_functions::extract_attribute(obj)?);
            }
            map.insert(key, attrs);
        }
        map
    };

    let inh_map: HashMap<String, Vec<Inheritance>> = {
        let dict: HashMap<String, Vec<Bound<'_, PyAny>>> = inheritances_by_class_uri.extract()?;
        let mut map = HashMap::new();
        for (key, items) in dict {
            let mut inh = Vec::new();
            for obj in &items {
                inh.push(Inheritance {
                    base_name: obj.getattr("base_name")?.extract()?,
                    base_uri: obj.getattr("base_uri")?.extract()?,
                    class_uri: obj.getattr("class_uri")?.extract()?,
                    class_name: obj.getattr("class_name")?.extract()?,
                    deprecated_version: obj.getattr("deprecated_version")?.extract()?,
                });
            }
            map.insert(key, inh);
        }
        map
    };

    let rel_map: HashMap<String, Vec<OSLORelatie>> = {
        let dict: HashMap<String, Vec<Bound<'_, PyAny>>> = relations_by_object_uri.extract()?;
        let mut map = HashMap::new();
        for (key, items) in dict {
            let mut rels = Vec::new();
            for obj in &items {
                rels.push(OSLORelatie {
                    bron_uri: obj.getattr("bron_uri")?.extract()?,
                    doel_uri: obj.getattr("doel_uri")?.extract()?,
                    object_uri: obj.getattr("objectUri")?.extract()?,
                    richting: obj.getattr("richting")?.extract()?,
                    deprecated_version: obj.getattr("deprecated_version")?.extract()?,
                });
            }
            map.insert(key, rels);
        }
        map
    };

    // Get validation regexes from settings
    let class_valid_regexes: Vec<String> = {
        let rules = settings.getattr("get")?.call1(("class_validation_rules",))?;
        rules.getattr("get")?.call1(("valid_regexes",))?.extract().unwrap_or_default()
    };
    // Merge class + complex datatype valid_uri_and_types
    let class_valid_map = {
        let mut map = class_validation_rules.clone();
        map.extend(complex_datatype_validation_rules.clone());
        map
    };

    // Primitive datatypes
    for dt in &primitive_datatypes {
        let uri: String = dt.getattr("objectUri")?.extract()?;
        let name: String = dt.getattr("name")?.extract()?;
        if skip_primitive_uris.contains(&uri.as_str()) {
            continue;
        }
        if !is_valid_uri(&uri, &primitive_datatype_validation_rules, &class_valid_regexes) {
            continue;
        }
        let attrs = attr_map.get(&uri).cloned().unwrap_or_default();
        let type_field = if uri.contains("#KwantWrd") { "KwantWrd" } else { "Primitive" };
        let data = create_block_to_write_from_complex_primitive_or_union_types(
            attrs,
            &HashMap::new(),
            &lookups,
            &type_field,
            model_name,
            &name,
            &dt.getattr("definition").unwrap().extract::<String>().unwrap_or_default(),
            &dt.getattr("label").unwrap().extract::<String>().unwrap_or_default(),
            &uri,
            &dt.getattr("usagenote").unwrap().extract::<String>().unwrap_or_default(),
            &dt.getattr("deprecated_version").unwrap().extract::<String>().unwrap_or_default(),
            "OTLPrimitiveDatatypeCreator",
        );
        if write_file_content(directory, "Datatypes", &name, &data).is_ok() {
            files_written += 1;
        } else {
            errors += 1;
        }
    }

    // Complex datatypes
    let complex_valid_regexes: Vec<String> = {
        let rules = settings.getattr("get")?.call1(("complex_datatype_validation_rules",))?;
        rules.getattr("get")?.call1(("valid_regexes",))?.extract().unwrap_or_default()
    };
    for dt in &complex_datatypes {
        let uri: String = dt.getattr("objectUri")?.extract()?;
        let name: String = dt.getattr("name")?.extract()?;
        if !is_valid_uri(&uri, &complex_datatype_validation_rules, &complex_valid_regexes) {
            continue;
        }
        let attrs = attr_map.get(&uri).cloned().unwrap_or_default();
        let data = create_block_to_write_from_complex_primitive_or_union_types(
            attrs,
            &complex_datatype_validation_rules,
            &lookups,
            "Complex",
            model_name,
            &name,
            &dt.getattr("definition").unwrap().extract::<String>().unwrap_or_default(),
            &dt.getattr("label").unwrap().extract::<String>().unwrap_or_default(),
            &uri,
            &dt.getattr("usagenote").unwrap().extract::<String>().unwrap_or_default(),
            &dt.getattr("deprecated_version").unwrap().extract::<String>().unwrap_or_default(),
            "OTLComplexDatatypeCreator",
        );
        if write_file_content(directory, "Datatypes", &name, &data).is_ok() {
            files_written += 1;
        } else {
            errors += 1;
        }
    }

    // Union datatypes
    let union_valid_regexes: Vec<String> = {
        let rules = settings.getattr("get")?.call1(("union_datatype_validation_rules",))?;
        rules.getattr("get")?.call1(("valid_regexes",))?.extract().unwrap_or_default()
    };
    for dt in &union_datatypes {
        let uri: String = dt.getattr("objectUri")?.extract()?;
        let name: String = dt.getattr("name")?.extract()?;
        if !is_valid_uri(&uri, &union_datatype_validation_rules, &union_valid_regexes) {
            continue;
        }
        let attrs = attr_map.get(&uri).cloned().unwrap_or_default();
        let data = create_block_to_write_from_complex_primitive_or_union_types(
            attrs,
            &union_datatype_validation_rules,
            &lookups,
            "UnionType",
            model_name,
            &name,
            &dt.getattr("definition").unwrap().extract::<String>().unwrap_or_default(),
            &dt.getattr("label").unwrap().extract::<String>().unwrap_or_default(),
            &uri,
            &dt.getattr("usagenote").unwrap().extract::<String>().unwrap_or_default(),
            &dt.getattr("deprecated_version").unwrap().extract::<String>().unwrap_or_default(),
            "OTLUnionDatatypeCreator",
        );
        if write_file_content(directory, "Datatypes", &name, &data).is_ok() {
            files_written += 1;
        } else {
            errors += 1;
        }
    }

    // Enumerations
    let enum_valid_regexes: Vec<String> = {
        let rules = settings.getattr("get")?.call1(("enumeration_validation_rules",))?;
        rules.getattr("get")?.call1(("valid_regexes",))?.extract().unwrap_or_default()
    };
    for en in &enumerations {
        let uri: String = en.getattr("objectUri")?.extract()?;
        let name: String = en.getattr("name")?.extract()?;
        if !is_valid_uri(&uri, &enumeration_validation_rules, &enum_valid_regexes) {
            continue;
        }

        let waardes: Vec<PyKeuzelijstWaarde> = match enumeration_waardes.call_method1("__getitem__", (&uri,)) {
            Ok(v) => {
                let list = v.downcast::<pyo3::types::PyList>().unwrap();
                list.iter().map(|item| {
                    PyKeuzelijstWaarde {
                        invulwaarde: item.getattr("invulwaarde").unwrap().extract::<String>().unwrap_or_default(),
                        label: item.getattr("label").unwrap().extract::<String>().unwrap_or_default(),
                        definitie: item.getattr("definitie").unwrap().extract::<String>().unwrap_or_default(),
                        object_uri: item.getattr("objectUri").unwrap().extract::<String>().unwrap_or_default(),
                        status: item.getattr("status").unwrap().extract::<String>().unwrap_or_default(),
                    }
                }).collect()
            },
            Err(_) => Vec::new(),
        };

        let adm_status: String = match enumeration_adm_status.call_method1("__getitem__", (&uri,)) {
            Ok(v) => v.extract().unwrap_or_default(),
            Err(_) => String::new(),
        };

        let valid_uri_and_types: HashMap<String, String> = HashMap::new();

        let data = create_block_to_write_from_enumeration(
            &valid_uri_and_types,
            &waardes,
            &adm_status,
            &name,
            &en.getattr("definition").unwrap().extract::<String>().unwrap_or_default(),
            &en.getattr("label").unwrap().extract::<String>().unwrap_or_default(),
            &uri,
            &en.getattr("codelist").unwrap().extract::<String>().unwrap_or_default(),
            &en.getattr("deprecated_version").unwrap().extract::<String>().unwrap_or_default(),
            "OTLEnumerationCreator",
        );
        if write_file_content(directory, "Datatypes", &name, &data).is_ok() {
            files_written += 1;
        } else {
            errors += 1;
        }
    }

    // Classes
    for cls in &classes {
        let label: String = cls.getattr("label")?.extract().unwrap_or_default();
        if label == "ignore this class when generating the model" {
            continue;
        }

        let uri: String = cls.getattr("objectUri")?.extract()?;
        let name: String = cls.getattr("name")?.extract()?;

        if !is_valid_uri(&uri, &class_valid_map, &class_valid_regexes) {
            continue;
        }

        let attrs = attr_map.get(&uri).cloned().unwrap_or_default();
        let inh = inh_map.get(&uri).cloned().unwrap_or_default();
        let relations = rel_map.get(&uri).cloned().unwrap_or_default();
        let geom_types = geometry_type_map.get(&uri).cloned().unwrap_or_default();
        let inh_uri_map = inheritance_map.get(&uri).cloned().unwrap_or_default();

        let data = create_block_from_class(
            attrs,
            inh,
            &relations,
            &class_valid_map,
            &lookups,
            &inh_uri_map,
            &geom_types,
            &name,
            &cls.getattr("definition").unwrap().extract::<String>().unwrap_or_default(),
            &uri,
            cls.getattr("abstract").unwrap().extract::<i32>().unwrap_or(0),
            &cls.getattr("deprecated_version").unwrap().extract::<String>().unwrap_or_default(),
            "OTLClassCreator",
        );
        let class_dir = {
            let mut dir = "Classes".to_string();
            if uri != "http://purl.org/dc/terms/Agent" {
                if let Ok((ns, _)) = crate::helper_functions::get_ns_and_name_from_uri(&uri) {
                    if !ns.is_empty() {
                        if let Ok(cd) = crate::helper_functions::get_class_directory_from_ns(&ns) {
                            dir = cd;
                        }
                    }
                }
            }
            dir
        };
                if write_file_content(directory, &class_dir, &name, &data).is_ok() {
            files_written += 1;
        } else {
            errors += 1;
        }
    }

    // all_classes helper file
    {
        let mut data_to_write: Vec<String> = Vec::new();
        for cls in &classes {
            let abstract_val: i32 = cls.getattr("abstract")?.extract().unwrap_or(0);
            if abstract_val != 0 {
                continue;
            }
            let object_uri: String = cls.getattr("objectUri")?.extract()?;

            let name = if class_valid_map.contains_key(&object_uri) {
                class_valid_map.get(&object_uri).cloned().unwrap_or_default()
            } else {
                if let Ok((ns, n)) = crate::helper_functions::get_ns_and_name_from_uri(&object_uri) {
                    n
                } else {
                    continue;
                }
            };

            if let Ok((ns, _)) = crate::helper_functions::get_ns_and_name_from_uri(&object_uri) {
                if !ns.is_empty() {
                    let titlecase = crate::helper_functions::get_titlecase_from_ns(&ns).unwrap_or_else(|_| ns.to_string());
                    data_to_write.push(format!("from ..Classes.{}.{} import {}", titlecase, name, name));
                } else {
                    data_to_write.push(format!("from ..Classes.{} import {}", name, name));
                }
            } else {
                data_to_write.push(format!("from ..Classes.{} import {}", name, name));
            }
        }

        if !data_to_write.is_empty() {
            if let Err(_) = write_file_content(directory, "Helpers", "all_classes", &data_to_write) {
                errors += 1;
            } else {
                files_written += 1;
            }
        }
    }

    Ok((files_written, errors))
}
