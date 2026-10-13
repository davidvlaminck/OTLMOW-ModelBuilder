use pyo3::prelude::*;
use std::collections::HashMap;

use crate::helper_functions::{get_white_space_equivalent, wrap_in_quotes};
use crate::ttl_reader::PyKeuzelijstWaarde;

pub struct KeuzelijstWaarde {
    pub invulwaarde: String,
    pub label: String,
    pub definitie: String,
    pub object_uri: String,
    pub status: String,
}

pub fn create_block_to_write_from_enumeration(
    valid_uri_and_types: &HashMap<String, String>,
    keuzelijst_waardes: &[PyKeuzelijstWaarde],
    adm_status: &str,
    datatype_name: &str,
    datatype_definition: &str,
    datatype_label: &str,
    datatype_object_uri: &str,
    datatype_codelist: &str,
    datatype_deprecated_version: &str,
    creator_name: &str,
) -> Vec<String> {
    let mut datablock = vec![
        "# coding=utf-8".to_string(),
        "from ..BaseClasses.KeuzelijstField import KeuzelijstField".to_string(),
    ];

    if !keuzelijst_waardes.is_empty() {
        datablock.push("from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde".to_string());
    }

    datablock.extend([
        String::new(),
        String::new(),
        format!("# Generated with {}. To modify: extend, do not edit", creator_name),
        format!("class {}(KeuzelijstField):", datatype_name),
        format!("    \"\"\"{}\"\"\"", datatype_definition),
        format!("    naam = {}", wrap_in_quotes(datatype_name)),
        format!("    label = {}", wrap_in_quotes(datatype_label)),
        format!("    objectUri = {}", wrap_in_quotes(datatype_object_uri)),
        format!("    definition = {}", wrap_in_quotes(datatype_definition)),
    ]);

    if !adm_status.is_empty() {
        datablock.push(format!("    status = {}", wrap_in_quotes(adm_status)));
    }

    if !datatype_deprecated_version.is_empty() {
        let dv = datatype_deprecated_version.split('-').next().unwrap_or("").to_string();
        datablock.push(format!("    deprecated_version = {}", wrap_in_quotes(&dv)));
    }

    datablock.push(format!("    codelist = {}", wrap_in_quotes(datatype_codelist)));
    datablock.push("    options = {".to_string());

    let mut sorted_waardes: Vec<&PyKeuzelijstWaarde> = keuzelijst_waardes.iter().collect();
    sorted_waardes.sort_by(|a, b| a.invulwaarde.cmp(&b.invulwaarde));

    for waarde in sorted_waardes {
        let invulwaarde = &waarde.invulwaarde;
        let label = &waarde.label;
        let definitie = &waarde.definitie;
        let object_uri = &waarde.objectUri;
        let status = &waarde.status;

        let whitespace = get_white_space_equivalent(&format!("        '{}': KeuzelijstWaarde(", invulwaarde));

        datablock.push(format!("        '{}': KeuzelijstWaarde(invulwaarde='{}',", invulwaarde, invulwaarde));
        datablock.push(format!("{}label={},", whitespace, wrap_in_quotes(label)));

        if !status.is_empty() {
            datablock.push(format!("{}status='{}',", whitespace, status));
        }

        if !definitie.is_empty() {
            datablock.push(format!("{}definitie={},", whitespace, wrap_in_quotes(definitie)));
        }

        datablock.push(format!("{}objectUri='{}'),", whitespace, object_uri));
    }

    if !keuzelijst_waardes.is_empty() {
        let last = datablock.pop().unwrap();
        datablock.push(last[..last.len().saturating_sub(1)].to_string());
    }

    datablock.push("    }".to_string());
    datablock.push(String::new());
    datablock.push("    @classmethod".to_string());
    datablock.push("    def create_dummy_data(cls):".to_string());
    datablock.push("        return cls.create_dummy_data_keuzelijst(cls.options)".to_string());
    datablock.push(String::new());

    datablock
}

#[pyfunction]
#[pyo3(name = "create_block_to_write_from_enumeration")]
#[pyo3(signature = (
    keuzelijst_waardes,
    adm_status,
    datatype_name,
    datatype_definition,
    datatype_label,
    datatype_object_uri,
    datatype_codelist,
    datatype_deprecated_version,
    creator_name="OTLEnumerationCreator"
))]
pub fn py_create_block_to_write_from_enumeration(
    _py: Python<'_>,
    keuzelijst_waardes: Vec<PyKeuzelijstWaarde>,
    adm_status: &str,
    datatype_name: &str,
    datatype_definition: &str,
    datatype_label: &str,
    datatype_object_uri: &str,
    datatype_codelist: &str,
    datatype_deprecated_version: &str,
    creator_name: &str,
) -> PyResult<Vec<String>> {
    let valid_uri_and_types: HashMap<String, String> = HashMap::new();
    Ok(create_block_to_write_from_enumeration(
        &valid_uri_and_types,
        &keuzelijst_waardes,
        adm_status,
        datatype_name,
        datatype_definition,
        datatype_label,
        datatype_object_uri,
        datatype_codelist,
        datatype_deprecated_version,
        creator_name,
    ))
}
