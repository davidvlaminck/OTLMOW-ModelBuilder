use pyo3::prelude::*;

mod sqlite_reader;
mod ttl_reader;

use sqlite_reader::{py_find_subclasses_uri_by_class_uri, py_get_all_inheritances, PyInheritance};
use ttl_reader::{py_get_keuzelijstwaardes_from_ttl, py_get_adm_status_from_ttl, py_parse_graph_to_dict, PyKeuzelijstWaarde};

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
    Ok(())
}
