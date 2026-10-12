use pyo3::prelude::*;
use rusqlite::{params, Connection};
use std::path::Path;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Inheritance {
    pub base_name: String,
    pub base_uri: String,
    pub class_uri: String,
    pub class_name: String,
    pub deprecated_version: String,
}

pub fn get_all_inheritances(path: &Path) -> rusqlite::Result<Vec<Inheritance>> {
    let conn = Connection::open(path)?;
    let mut stmt = conn.prepare(
        "SELECT base_name, base_uri, class_uri, class_name, deprecated_version
         FROM InternalBaseClass
         ORDER BY base_uri, class_uri",
    )?;
    let inheritances: Vec<Inheritance> = stmt
        .query_map([], |row| {
            Ok(Inheritance {
                base_name: row.get(0)?,
                base_uri: row.get(1)?,
                class_uri: row.get(2)?,
                class_name: row.get(3)?,
                deprecated_version: row.get(4)?,
            })
        })?
        .filter_map(|r| r.ok())
        .collect();
    Ok(inheritances)
}

pub fn find_subclasses_uri_by_class_uri(
    path: &Path,
    class_uri: &str,
    sort_by_uri: bool,
) -> rusqlite::Result<Vec<String>> {
    if class_uri.is_empty() {
        return Ok(vec![]);
    }
    let conn = Connection::open(path)?;
    if sort_by_uri {
        let mut stmt = conn.prepare(
            "SELECT class_uri FROM InternalBaseClass
             WHERE base_uri = ?
             ORDER BY class_uri",
        )?;
        let result: Vec<String> = stmt
            .query_map(params![class_uri], |row| row.get(0))?
            .filter_map(|r| r.ok())
            .collect();
        Ok(result)
    } else {
        let mut stmt = conn.prepare(
            "SELECT class_uri FROM InternalBaseClass
             WHERE base_uri = ?
             ORDER BY base_uri, class_uri",
        )?;
        let result: Vec<String> = stmt
            .query_map(params![class_uri], |row| row.get(0))?
            .filter_map(|r| r.ok())
            .collect();
        Ok(result)
    }
}

#[pyclass(name = "Inheritance")]
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct PyInheritance {
    #[pyo3(get)]
    pub base_name: String,
    #[pyo3(get)]
    pub base_uri: String,
    #[pyo3(get)]
    pub class_uri: String,
    #[pyo3(get)]
    pub class_name: String,
    #[pyo3(get)]
    pub deprecated_version: String,
}

#[pyfunction]
#[pyo3(name = "get_all_inheritances")]
pub fn py_get_all_inheritances(_py: Python<'_>, path: &str) -> PyResult<Vec<PyInheritance>> {
    let p = Path::new(path);
    if !p.exists() {
        return Err(pyo3::exceptions::PyFileNotFoundError::new_err(format!(
            "{} is not a valid path. File does not exist.",
            p.display()
        )));
    }
    let inheritances =
        get_all_inheritances(p).map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))?;
    Ok(inheritances
        .into_iter()
        .map(|i| PyInheritance {
            base_name: i.base_name,
            base_uri: i.base_uri,
            class_uri: i.class_uri,
            class_name: i.class_name,
            deprecated_version: i.deprecated_version,
        })
        .collect())
}

#[pyfunction]
#[pyo3(name = "find_subclasses_uri_by_class_uri")]
pub fn py_find_subclasses_uri_by_class_uri(
    _py: Python<'_>,
    path: &str,
    class_uri: &str,
    sort_by_uri: bool,
) -> PyResult<Vec<String>> {
    let p = Path::new(path);
    if !p.exists() {
        return Ok(vec![]);
    }
    let result = find_subclasses_uri_by_class_uri(p, class_uri, sort_by_uri)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))?;
    Ok(result)
}
