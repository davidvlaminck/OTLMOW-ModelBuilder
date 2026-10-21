use pyo3::prelude::*;

mod class_creator;
mod datatype_builder_functions;
mod datatype_creator;
mod enumeration_creator;
mod generic_builder_functions;
mod helper_functions;
mod model_creator;
mod sqlite_reader;
mod ttl_reader;

use datatype_builder_functions::{
    py_get_field_name_by_type_uri, py_get_field_name_from_type_uri,
    py_get_fields_to_import_from_list_of_attributes, py_get_non_single_field_from_type_uri,
    py_get_single_field_from_type_uri, py_get_type_name_of_complex_attribuut,
    py_get_type_name_of_union_attribuut,
};
use class_creator::py_create_block_from_class;
use datatype_creator::py_create_block_to_write_from_complex_primitive_or_union_types;
use enumeration_creator::py_create_block_to_write_from_enumeration;
use generic_builder_functions::py_add_attributen_to_data_block;
use helper_functions::{
    py_escape_backslash, py_get_class_directory_from_ns, py_get_ns_and_name_from_uri,
    py_get_titlecase_from_ns, py_get_white_space_equivalent, py_wrap_in_quotes,
};
use sqlite_reader::{py_find_subclasses_uri_by_class_uri, py_get_all_inheritances, PyInheritance};
use ttl_reader::{
    py_get_adm_status_from_ttl, py_get_enumerations_from_dir, py_get_keuzelijstwaardes_from_ttl,
    py_parse_file_or_dir_to_dict, py_parse_graph_to_dict, PyKeuzelijstWaarde,
};
use model_creator::py_generate_model_optimized;

#[pyfunction]
fn rust_hello() -> String {
    "Hello from Rust!".to_string()
}

#[pymodule]
fn _otlmow_modelbuilder_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rust_hello, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_all_inheritances, m)?)?;
    m.add_function(wrap_pyfunction!(py_find_subclasses_uri_by_class_uri, m)?)?;
    m.add_class::<PyInheritance>()?;
    m.add_class::<PyKeuzelijstWaarde>()?;
    m.add_function(wrap_pyfunction!(py_get_keuzelijstwaardes_from_ttl, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_adm_status_from_ttl, m)?)?;
    m.add_function(wrap_pyfunction!(py_parse_graph_to_dict, m)?)?;
    m.add_function(wrap_pyfunction!(py_parse_file_or_dir_to_dict, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_enumerations_from_dir, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_keuzelijstwaardes_from_ttl, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_adm_status_from_ttl, m)?)?;
    m.add_function(wrap_pyfunction!(py_escape_backslash, m)?)?;
    m.add_function(wrap_pyfunction!(py_wrap_in_quotes, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_white_space_equivalent, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_ns_and_name_from_uri, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_class_directory_from_ns, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_titlecase_from_ns, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_single_field_from_type_uri, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_non_single_field_from_type_uri, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_type_name_of_complex_attribuut, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_type_name_of_union_attribuut, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_field_name_from_type_uri, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_field_name_by_type_uri, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_fields_to_import_from_list_of_attributes, m)?)?;
    m.add_function(wrap_pyfunction!(py_add_attributen_to_data_block, m)?)?;
    m.add_function(wrap_pyfunction!(py_create_block_to_write_from_complex_primitive_or_union_types, m)?)?;
    m.add_function(wrap_pyfunction!(py_create_block_to_write_from_enumeration, m)?)?;
    m.add_function(wrap_pyfunction!(py_create_block_from_class, m)?)?;
    m.add_function(wrap_pyfunction!(py_generate_model_optimized, m)?)?;
    Ok(())
}
