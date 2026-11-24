use pyo3::prelude::*;

const MAX_IMPORT_LINE_LENGTH: usize = 88;

fn import_name_sort_key(name: &str) -> (u8, String) {
    let has_cased = name.chars().any(|c| c.is_alphabetic());
    let all_upper = has_cased && name.chars().filter(|c| c.is_alphabetic()).all(|c| c.is_uppercase());
    let first_upper = name.chars().next().map(|c| c.is_uppercase()).unwrap_or(false);
    let group = if all_upper {
        0
    } else if first_upper {
        1
    } else {
        2
    };
    (group, name.to_lowercase())
}

fn parse_import_line(line: &str) -> (String, Vec<String>, bool) {
    if let Some(rest) = line.strip_prefix("from ") {
        if let Some((module, names)) = rest.split_once(" import ") {
            let names = names
                .split(',')
                .map(|s| s.trim().to_string())
                .filter(|s| !s.is_empty())
                .collect();
            (module.to_string(), names, true)
        } else {
            (rest.to_string(), Vec::new(), true)
        }
    } else if let Some(rest) = line.strip_prefix("import ") {
        (rest.to_string(), Vec::new(), false)
    } else {
        (line.to_string(), Vec::new(), true)
    }
}

fn render_import(module: &str, names: &[String], is_from: bool) -> Vec<String> {
    if !is_from {
        return vec![format!("import {module}")];
    }
    let mut sorted: Vec<String> = names.to_vec();
    sorted.sort_by(|a, b| import_name_sort_key(a).cmp(&import_name_sort_key(b)).then(a.cmp(b)));
    sorted.dedup();
    let single_line = format!("from {module} import {}", sorted.join(", "));
    if single_line.len() <= MAX_IMPORT_LINE_LENGTH {
        return vec![single_line];
    }
    let mut rendered = vec![format!("from {module} import (")];
    rendered.extend(sorted.iter().map(|name| format!("    {name},")));
    rendered.push(")".to_string());
    rendered
}

fn merge_import(modules: &mut Vec<(String, Vec<String>)>, module: String, names: Vec<String>) {
    if let Some(entry) = modules.iter_mut().find(|(existing, _)| *existing == module) {
        entry.1.extend(names);
    } else {
        modules.push((module, names));
    }
}

fn render_import_group(mut modules: Vec<(String, Vec<String>)>) -> Vec<String> {
    modules.sort_by(|a, b| a.0.to_lowercase().cmp(&b.0.to_lowercase()));
    let mut rendered = Vec::new();
    for (module, names) in &modules {
        rendered.extend(render_import(module, names, true));
    }
    rendered
}

/// Group, merge and sort the leading import block so it matches ruff's isort rules (I001).
pub fn organize_import_block(lines: Vec<String>) -> Vec<String> {
    let end = lines.iter().position(|line| line.is_empty()).unwrap_or(lines.len());

    let mut comments: Vec<String> = Vec::new();
    let mut stdlib_modules: Vec<(String, Vec<String>)> = Vec::new();
    let mut local_modules: Vec<(String, Vec<String>)> = Vec::new();
    let mut plain_imports: Vec<String> = Vec::new();

    for line in &lines[..end] {
        if line.starts_with('#') {
            comments.push(line.clone());
            continue;
        }
        let (module, names, is_from) = parse_import_line(line);
        if !is_from {
            plain_imports.push(format!("import {module}"));
            continue;
        }
        if module.starts_with('.') {
            merge_import(&mut local_modules, module, names);
        } else {
            merge_import(&mut stdlib_modules, module, names);
        }
    }

    let mut stdlib_lines = plain_imports;
    stdlib_lines.extend(render_import_group(stdlib_modules));
    stdlib_lines.sort_by_key(|line| parse_import_line(line).0.to_lowercase());
    let local_lines = render_import_group(local_modules);

    let mut organized = comments;
    let has_stdlib = !stdlib_lines.is_empty();
    organized.append(&mut stdlib_lines);
    if has_stdlib && !local_lines.is_empty() {
        // a blank line separates the standard library imports from the relative imports
        organized.push(String::new());
    }
    organized.extend(local_lines);
    organized.extend(lines[end..].iter().cloned());
    organized
}

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

pub fn add_noqa_ruf001_if_needed(line: &str) -> String {
    if line.contains('×') {
        format!("{line}  # noqa: RUF001")
    } else {
        line.to_string()
    }
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
#[pyo3(name = "add_noqa_ruf001_if_needed")]
pub fn py_add_noqa_ruf001_if_needed(line: &str) -> String {
    add_noqa_ruf001_if_needed(line)
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
