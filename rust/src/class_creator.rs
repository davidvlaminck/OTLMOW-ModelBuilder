use pyo3::prelude::*;
use std::collections::HashMap;

use crate::generic_builder_functions::{Attribute, TypeLookup, add_attributen_to_data_block};
use crate::helper_functions::{get_ns_and_name_from_uri, get_class_directory_from_ns, wrap_in_quotes};
use crate::datatype_builder_functions::get_fields_to_import_from_list_of_attributes;

#[derive(Clone)]
pub struct Inheritance {
    pub base_name: String,
    pub base_uri: String,
    pub class_uri: String,
    pub class_name: String,
    pub deprecated_version: String,
}

#[derive(Clone)]
pub struct OSLORelatie {
    pub bron_uri: String,
    pub doel_uri: String,
    pub object_uri: String,
    pub richting: String,
    pub deprecated_version: String,
}

pub fn create_block_from_class(
    attributen: Vec<Attribute>,
    inheritances: Vec<Inheritance>,
    relations: &[OSLORelatie],
    valid_uri_and_types: &HashMap<String, String>,
    lookups: &TypeLookup,
    inheritance_map: &[String],
    geometry_types: &[String],
    class_name: &str,
    class_definition: &str,
    class_object_uri: &str,
    class_abstract: i32,
    class_deprecated_version: &str,
    creator_name: &str,
) -> Vec<String> {
    let mut datablock: Vec<String> = vec!["# coding=utf-8".to_string()];

    if !attributen.is_empty() {
        if class_object_uri == "http://purl.org/dc/terms/Agent" {
            datablock.push("from ..BaseClasses.OTLObject import OTLAttribuut".to_string());
        } else {
            datablock.push("from ...BaseClasses.OTLObject import OTLAttribuut".to_string());
        }
    }

    if class_abstract == 1 {
        if inheritances.len() + geometry_types.len() < 1 {
            datablock.push("from abc import abstractmethod, ABC".to_string());
        } else {
            datablock.push("from abc import abstractmethod".to_string());
        }
    }

    if !inheritances.is_empty() {
        for inheritance in &inheritances {
            let base_names = ["OTLAsset", "OTLObject", "RelationInteractor", "DavieRelatieAttributes"];
            if base_names.contains(&inheritance.base_name.as_str()) {
                if class_object_uri == "http://purl.org/dc/terms/Agent" {
                    datablock.push(format!(
                        "from ..BaseClasses.{} import {}",
                        inheritance.base_name, inheritance.base_name
                    ));
                } else {
                    datablock.push(format!(
                        "from ...BaseClasses.{} import {}",
                        inheritance.base_name, inheritance.base_name
                    ));
                }
            } else {
                let mut class_directory = "Classes".to_string();
                if inheritance.base_uri != "http://purl.org/dc/terms/Agent" {
                    if let Ok((ns, _name)) = get_ns_and_name_from_uri(&inheritance.base_uri) {
                        if let Ok(cd) = get_class_directory_from_ns(&ns) {
                            class_directory = cd.replace('/', ".");
                        }
                    }
                }

                if inheritance.class_name == "Agent"
                    && (inheritance.base_name == "AIMDBStatus" || inheritance.base_name == "AIMVersie")
                {
                    datablock.push(format!(
                        "from ..{}.{} import {}",
                        class_directory, inheritance.base_name, inheritance.base_name
                    ));
                } else {
                    datablock.push(format!(
                        "from ...{}.{} import {}",
                        class_directory, inheritance.base_name, inheritance.base_name
                    ));
                }
            }
        }
    }

    let mut attr_list = attributen;
    let mut sorted_attrs: Vec<&mut Attribute> = attr_list.iter_mut().collect();
    sorted_attrs.sort_by(|a, b| a.name.cmp(&b.name));

    for attr in &sorted_attrs {
        if attr.overerving == 1 {
            panic!("overerving 1 is not implemented, found in attributen");
        }
    }

    let attribute_types: Vec<String> = attr_list.iter().map(|a| a.type_uri.clone()).collect();
    let list_of_fields = get_fields_to_import_from_list_of_attributes(
        &attribute_types,
        &lookups.type_links,
        valid_uri_and_types,
        vec![],
    ).unwrap_or_default();

    let base_fields = [
        "BooleanField", "ComplexField", "DateField", "DateTimeField",
        "FloatOrDecimalField", "IntegerField", "KeuzelijstField",
        "UnionTypeField", "URIField", "LiteralField",
        "NonNegIntegerField", "TimeField", "StringField", "UnionWaarden",
    ];

    for type_field in &list_of_fields {
        if !base_fields.contains(&type_field.as_str()) {
            if class_object_uri == "http://purl.org/dc/terms/Agent" {
                datablock.push(format!("from ..Datatypes.{} import {}", type_field, type_field));
            } else {
                datablock.push(format!("from ...Datatypes.{} import {}", type_field, type_field));
            }
        } else {
            if class_object_uri == "http://purl.org/dc/terms/Agent" {
                datablock.push(format!("from ..BaseClasses.{} import {}", type_field, type_field));
            } else {
                datablock.push(format!("from ...BaseClasses.{} import {}", type_field, type_field));
            }
        }
    }

    for geometry_type in geometry_types {
        datablock.push(format!("from ...GeometrieTypes.{} import {}", geometry_type, geometry_type));
    }

    datablock.push(String::new());
    datablock.push(String::new());
    datablock.push(format!("# Generated with {}. To modify: extend, do not edit", creator_name));

    let class_line = get_class_line_from_class_and_inheritances(
        class_name, class_abstract, &inheritances, geometry_types, inheritance_map,
    );
    datablock.push(class_line);
    datablock.push(format!("    \"\"\"{}\"\"\"", class_definition));
    datablock.push(String::new());
    datablock.push(format!("    typeURI = '{}'", class_object_uri));
    datablock.push("    \"\"\"De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI.\"\"\"".to_string());

    let mut deprecated_version = class_deprecated_version.to_string();
    if !deprecated_version.is_empty() {
        deprecated_version = deprecated_version.split('-').next().unwrap_or("").to_string();
        datablock.push(String::new());
        datablock.push(format!("    deprecated_version = '{}'", deprecated_version));
    }

    datablock.push(String::new());
    if class_abstract == 1 {
        datablock.push("    @abstractmethod".to_string());
    }
    datablock.push("    def __init__(self):".to_string());
    datablock.push("        super().__init__()".to_string());
    datablock.push(String::new());

    add_relations_to_datablock(&mut datablock, class_object_uri, &relations);

    let attributen_owned: Vec<Attribute> = attr_list.iter().cloned().collect();
    datablock = add_attributen_to_data_block(
        attributen_owned,
        datablock,
        valid_uri_and_types,
        lookups,
        true,
        "",
    );

    if inheritances.is_empty() && attr_list.is_empty() {
        datablock.push("        pass".to_string());
    }

    if datablock.last() == Some(&String::new()) {
        datablock.pop();
    }

    datablock
}

fn get_class_line_from_class_and_inheritances(
    class_name: &str,
    class_abstract: i32,
    inheritances: &[Inheritance],
    geometry_types: &[String],
    inheritance_map: &[String],
) -> String {
    let total = class_abstract + inheritances.len() as i32 + geometry_types.len() as i32;
    if total < 1 {
        panic!("class structure not implemented");
    }

    if class_abstract == 1 && inheritances.len() + geometry_types.len() < 1 {
        return format!("class {}(ABC):", class_name);
    }

    if !inheritances.is_empty() || !geometry_types.is_empty() {
        let mut line = format!("class {}(", class_name);

        if inheritance_map.len() != inheritances.len() {
            panic!(
                "Could not find all inheritances. Found {}, expected {}",
                inheritances.len(),
                inheritance_map.len()
            );
        }

        for inh_uri in inheritance_map {
            let inheritance = inheritances.iter().find(|i| &i.base_uri == inh_uri);
            if inheritance.is_none() {
                panic!("Could not find inheritance for {} in class", inh_uri);
            }
            line.push_str(&inheritance.unwrap().base_name);
            line.push_str(", ");
        }

        for geometry_type in geometry_types {
            line.push_str(geometry_type);
            line.push_str(", ");
        }

        line.pop();
        line.pop();
        line.push_str("):");
        return line;
    }

    panic!("class structure not implemented");
}

fn add_relations_to_datablock(
    datablock: &mut Vec<String>,
    object_uri: &str,
    relations: &[OSLORelatie],
) {
    if relations.is_empty() {
        return;
    }

    for relation in relations {
        let mut deprecated = String::new();
        if !relation.deprecated_version.is_empty() {
            let dv = relation.deprecated_version.split('-').next().unwrap_or("");
            deprecated = format!(", deprecated='{}'", dv);
        }

        let (direction, direction_comment, target_uri) = if relation.richting == "Unspecified" {
            if relation.bron_uri == object_uri {
                ("u", "# u = unidirectional", relation.doel_uri.clone())
            } else {
                ("u", "# u = unidirectional", relation.bron_uri.clone())
            }
        } else if relation.bron_uri == object_uri {
            ("o", "# o = direction: outgoing", relation.doel_uri.clone())
        } else {
            ("i", "# i = direction: incoming", relation.bron_uri.clone())
        };

        datablock.push(format!(
            "        self.add_valid_relation(relation='{}', target='{}', direction='{}'{})  {}",
            relation.object_uri, target_uri, direction, deprecated, direction_comment
        ));
    }
    datablock.push(String::new());
}

#[pyfunction]
#[pyo3(name = "create_block_from_class")]
#[pyo3(signature = (
    attributen,
    inheritances,
    relations,
    valid_uri_and_types,
    type_links,
    enumerations,
    complex_datatypes,
    union_datatypes,
    inheritance_map,
    geometry_types,
    class_name="",
    class_definition="",
    class_object_uri="",
    class_abstract=0,
    class_deprecated_version="",
    creator_name=""
))]
pub fn py_create_block_from_class(
    _py: Python<'_>,
    attributen: &Bound<'_, PyAny>,
    inheritances: Vec<(String, String, String, String, String)>,
    relations: Vec<(String, String, String, String, String)>,
    valid_uri_and_types: Vec<(String, String)>,
    type_links: Vec<(String, String)>,
    enumerations: Vec<(String, String)>,
    complex_datatypes: Vec<(String, String)>,
    union_datatypes: Vec<(String, String)>,
    inheritance_map: Vec<String>,
    geometry_types: Vec<String>,
    class_name: &str,
    class_definition: &str,
    class_object_uri: &str,
    class_abstract: i32,
    class_deprecated_version: &str,
    creator_name: &str,
) -> PyResult<Vec<String>> {
    let attrs_list: Vec<Bound<'_, PyAny>> = attributen.extract()?;
    let mut attrs: Vec<Attribute> = Vec::new();
    for obj in &attrs_list {
        attrs.push(crate::generic_builder_functions::extract_attribute(obj)?);
    }

    let inh: Vec<Inheritance> = inheritances
        .into_iter()
        .map(|(base_name, base_uri, class_uri, class_name, deprecated_version)| {
            Inheritance {
                base_name,
                base_uri,
                class_uri,
                class_name,
                deprecated_version,
            }
        })
        .collect();

    let rels: Vec<OSLORelatie> = relations
        .into_iter()
        .map(|(bron_uri, doel_uri, object_uri, richting, deprecated_version)| {
            OSLORelatie {
                bron_uri,
                doel_uri,
                object_uri,
                richting,
                deprecated_version,
            }
        })
        .collect();

    let valid_map: HashMap<String, String> = valid_uri_and_types
        .into_iter()
        .map(|(k, v)| (k.to_string(), v.to_string()))
        .collect();

    let lookups = TypeLookup::from_pairs(
        type_links.into_iter().map(|(k, v)| (k.to_string(), v.to_string())).collect(),
        enumerations.into_iter().map(|(k, v)| (k.to_string(), v.to_string())).collect(),
        complex_datatypes.into_iter().map(|(k, v)| (k.to_string(), v.to_string())).collect(),
        union_datatypes.into_iter().map(|(k, v)| (k.to_string(), v.to_string())).collect(),
    );

    let inh_map: Vec<String> = inheritance_map;
    let geo_types: Vec<String> = geometry_types;

    Ok(create_block_from_class(
        attrs,
        inh,
        &rels,
        &valid_map,
        &lookups,
        &inh_map,
        &geo_types,
        class_name,
        class_definition,
        class_object_uri,
        class_abstract,
        class_deprecated_version,
        creator_name,
    ))
}
