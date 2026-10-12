use pyo3::prelude::*;

pub fn escape_backslash(text: &str) -> String {
    text.replace('\\', "\\\\")
}

pub fn wrap_in_quotes(text: &str) -> String {
    if text.is_empty() {
        return "''".to_string();
    }
    let singles = text.matches('\'').count();
    let doubles = text.matches('"').count();
    if singles > doubles {
        if doubles > 0 {
            format!("\"{}\"", text.replace('"', "\\\""))
        } else {
            format!("\"{}\"", text)
        }
    } else if singles > 0 {
        format!("'{}'", text.replace('\'', "\\'"))
    } else {
        format!("'{}'", text)
    }
}

pub fn get_white_space_equivalent(string: &str) -> String {
    " ".repeat(string.len())
}

pub fn py_title(s: &str) -> String {
    let mut result = String::new();
    let mut capitalize_next = true;
    for c in s.chars() {
        if c.is_alphanumeric() {
            if capitalize_next {
                result.extend(c.to_uppercase());
                capitalize_next = false;
            } else {
                result.extend(c.to_lowercase());
            }
        } else {
            result.push(c);
            capitalize_next = true;
        }
    }
    result
}

pub fn get_titlecase_from_ns(ns: &str) -> Result<String, String> {
    match ns {
        "proefenmeting" => Ok("ProefEnMeting".to_string()),
        "implementatieelement" => Ok("ImplementatieElement".to_string()),
        "" => Err(format!("could not get titlecase for {ns}")),
        _ => Ok(py_title(ns)),
    }
}

pub fn get_class_directory_from_ns(ns: &str) -> Result<String, String> {
    let titlecase = get_titlecase_from_ns(ns)?;
    Ok(format!("Classes/{titlecase}"))
}

pub fn get_ns_and_name_from_uri(object_uri: &str) -> Result<(String, String), String> {
    if !object_uri.contains("/ns/") {
        let name_part = if object_uri.contains('#') {
            object_uri.split('#').last().unwrap_or("")
        } else {
            object_uri
        };
        let name = name_part.split('/').last().unwrap_or("");
        return Ok(("".to_string(), name.to_string()));
    }

    if !object_uri.contains('#') {
        return Err(format!(
            "{} is not a valid uri because can not be split into a ns and name ('#' is missing)",
            object_uri
        ));
    }

    let short_uri = object_uri.split("/ns/").nth(1).unwrap_or("");
    let parts: Vec<&str> = short_uri.splitn(2, '#').collect();
    let ns = parts.get(0).copied().unwrap_or("");
    let name = parts.get(1).copied().unwrap_or("");

    if object_uri.starts_with("https://lgc") {
        let name = if name.contains('.') {
            name.replace('.', "_")
        } else {
            name.to_string()
        };
        let name = if name.contains('-') {
            name.replace('-', "_")
        } else {
            name
        };
        let name = match name.as_str() {
            "RIS" => "RISLegacy".to_string(),
            "Fietstel" => "FietstelLegacy".to_string(),
            "Brug" => "BeweegbareBrug".to_string(),
            "Voedingskeuzeschakelaar" => "VKS".to_string(),
            other => other.to_string(),
        };
        return Ok(("legacy".to_string(), name));
    }

    Ok((ns.to_string(), name.to_string()))
}

#[pyfunction]
#[pyo3(name = "escape_backslash")]
pub fn py_escape_backslash(text: &str) -> String {
    escape_backslash(text)
}

#[pyfunction]
#[pyo3(name = "wrap_in_quotes")]
pub fn py_wrap_in_quotes(text: &str) -> String {
    wrap_in_quotes(text)
}

#[pyfunction]
#[pyo3(name = "get_white_space_equivalent")]
pub fn py_get_white_space_equivalent(string: &str) -> String {
    get_white_space_equivalent(string)
}

#[pyfunction]
#[pyo3(name = "get_ns_and_name_from_uri")]
pub fn py_get_ns_and_name_from_uri(object_uri: &str) -> PyResult<(String, String)> {
    get_ns_and_name_from_uri(object_uri)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_class_directory_from_ns")]
pub fn py_get_class_directory_from_ns(ns: &str) -> PyResult<String> {
    get_class_directory_from_ns(ns)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}

#[pyfunction]
#[pyo3(name = "get_titlecase_from_ns")]
pub fn py_get_titlecase_from_ns(ns: &str) -> PyResult<String> {
    get_titlecase_from_ns(ns)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e))
}
