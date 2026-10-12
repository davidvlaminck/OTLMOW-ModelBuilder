use pyo3::prelude::*;
use std::collections::BTreeMap;
use std::io::BufRead;
use std::path::Path;

use oxrdf::{NamedOrBlankNode, NamedNode, Term, Triple};
use oxttl::TurtleParser;

const SKOS: &str = "http://www.w3.org/2004/02/skos/core#";
const ADMS_STATUS: &str = "https://www.w3.org/ns/adms#status";
const CONCEPT_SCHEME_PREFIX: &str = "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/";
const CONCEPT_SCHEME_TEST_PREFIX: &str = "https://wegenenverkeer-test.data.vlaanderen.be/id/conceptscheme/";
const KL_ADMS_PREFIX: &str =
    "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/";
const RDF_TYPE: &str = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

fn term_to_str(term: &Term) -> String {
    match term {
        Term::NamedNode(nn) => nn.as_str().to_string(),
        Term::Literal(lit) => lit.value().to_string(),
        _ => String::new(),
    }
}

struct TripleStore {
    triples: Vec<Triple>,
}

impl TripleStore {
    fn load(path: &Path) -> Result<Self, String> {
        let parser = TurtleParser::new();
        let reader =
            std::io::BufReader::new(std::fs::File::open(path).map_err(|e| e.to_string())?);
        let triples: Vec<Triple> = parser
            .for_reader(reader)
            .map(|r| r.map_err(|e| e.to_string()))
            .collect::<Result<Vec<_>, _>>()
            .map_err(|e| format!("Failed to parse TTL: {}", e))?;
        Ok(TripleStore { triples })
    }

    fn subjects(&self) -> Vec<String> {
        let mut set: std::collections::HashSet<String> = std::collections::HashSet::new();
        for t in &self.triples {
            if let NamedOrBlankNode::NamedNode(nn) = &t.subject {
                set.insert(nn.as_str().to_string());
            }
        }
        let mut result: Vec<String> = set.into_iter().collect();
        result.sort();
        result
    }

    fn object_for(&self, subject: &str, predicate: &str) -> Option<String> {
        let subj = NamedNode::new(subject).ok()?;
        let pred = NamedNode::new(predicate).ok()?;
        for t in &self.triples {
            if t.subject == NamedOrBlankNode::NamedNode(subj.clone()) && t.predicate == pred {
                return Some(term_to_str(&t.object));
            }
        }
        None
    }

    fn concept_scheme_subjects(&self) -> Vec<String> {
        let type_pred = NamedNode::new(RDF_TYPE).ok();
        let cs_type = NamedNode::new(SKOS.to_string() + "ConceptScheme").ok();
        let mut result: Vec<String> = self
            .triples
            .iter()
            .filter_map(|t| {
                if t.predicate == type_pred.clone()? && t.object == Term::NamedNode(cs_type.clone()?) {
                    if let NamedOrBlankNode::NamedNode(nn) = &t.subject {
                        Some(nn.as_str().to_string())
                    } else {
                        None
                    }
                } else {
                    None
                }
            })
            .collect();
        result.sort();
        result
    }

    fn in_scheme_subjects(&self, concept_scheme_uri: &str) -> Vec<String> {
        let cs = NamedNode::new(concept_scheme_uri).ok();
        let in_scheme = NamedNode::new(SKOS.to_string() + "inScheme").ok();
        let mut result: Vec<String> = self
            .triples
            .iter()
            .filter_map(|t| {
                if t.predicate == in_scheme.clone()? && t.object == Term::NamedNode(cs.clone()?) {
                    if let NamedOrBlankNode::NamedNode(nn) = &t.subject {
                        Some(nn.as_str().to_string())
                    } else {
                        None
                    }
                } else {
                    None
                }
            })
            .collect();
        result.sort();
        result
    }

    fn triples_for_subject(&self, subject: &str) -> Vec<(String, String, String)> {
        let subj = NamedNode::new(subject).ok();
        self.triples
            .iter()
            .filter_map(|t| {
                if t.subject == NamedOrBlankNode::NamedNode(subj.clone()?) {
                    Some((
                        subject.to_string(),
                        t.predicate.as_str().to_string(),
                        term_to_str(&t.object),
                    ))
                } else {
                    None
                }
            })
            .collect()
    }
}

pub fn parse_graph_to_dict(
    path: &Path,
) -> Result<BTreeMap<String, Vec<(String, String, String)>>, String> {
    let store = TripleStore::load(path)?;
    let mut result: BTreeMap<String, Vec<(String, String, String)>> = BTreeMap::new();

    let concept_schemes = store.concept_scheme_subjects();

    for cs_uri in concept_schemes {
        let mut triples: Vec<(String, String, String)> = Vec::new();

        triples.extend(store.triples_for_subject(&cs_uri));

        let in_scheme_subjects = store.in_scheme_subjects(&cs_uri);
        for subj_uri in in_scheme_subjects {
            triples.extend(store.triples_for_subject(&subj_uri));
        }

        result.insert(cs_uri, triples);
    }

    Ok(result)
}

#[pyclass(name = "KeuzelijstWaarde")]
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct PyKeuzelijstWaarde {
    #[pyo3(get, set)]
    pub invulwaarde: String,
    #[pyo3(get, set)]
    pub label: String,
    #[pyo3(get, set)]
    pub definitie: String,
    #[pyo3(get, set)]
    pub objectUri: String,
    #[pyo3(get, set)]
    pub status: String,
}

#[pymethods]
impl PyKeuzelijstWaarde {
    #[new]
    fn new(
        invulwaarde: Option<String>,
        label: Option<String>,
        definitie: Option<String>,
        object_uri: Option<String>,
        status: Option<String>,
    ) -> Self {
        let object_uri = object_uri.unwrap_or_default();
        PyKeuzelijstWaarde {
            invulwaarde: invulwaarde.unwrap_or_default(),
            label: label.unwrap_or_default(),
            definitie: definitie.unwrap_or_default(),
            objectUri: object_uri,
            status: status.unwrap_or_default(),
        }
    }

    fn __repr__(&self) -> String {
        format!(
            "KeuzelijstWaarde(invulwaarde='{}', label='{}', ...)",
            self.invulwaarde, self.label
        )
    }
}

fn get_keuzelijstwaardes_from_store(store: &TripleStore, env: &str) -> Vec<PyKeuzelijstWaarde> {
    let subjects = store.subjects();
    let mut result: Vec<PyKeuzelijstWaarde> = Vec::new();

    for subject_str in subjects {
        if subject_str.starts_with(CONCEPT_SCHEME_PREFIX) {
            continue;
        }
        if env != "prd" && subject_str.starts_with(CONCEPT_SCHEME_TEST_PREFIX) {
            continue;
        }

        let mut waarde = PyKeuzelijstWaarde {
            invulwaarde: String::new(),
            label: String::new(),
            definitie: String::new(),
            objectUri: String::new(),
            status: String::new(),
        };

        waarde.objectUri = subject_str.replace("-test.data", ".data");
        if let Some(v) = store.object_for(&subject_str, &(SKOS.to_string() + "notation")) {
            waarde.invulwaarde = v;
        }
        if let Some(v) = store.object_for(&subject_str, &(SKOS.to_string() + "definition")) {
            waarde.definitie = v;
        }
        if let Some(v) = store.object_for(&subject_str, &(SKOS.to_string() + "prefLabel")) {
            waarde.label = v;
        }
        if let Some(status) = store.object_for(&subject_str, ADMS_STATUS) {
            waarde.status = status
                .replace("-test.data", ".data")
                .replace(KL_ADMS_PREFIX, "");
        }

        result.push(waarde);
    }

    result
}

#[pyfunction]
#[pyo3(name = "get_keuzelijstwaardes_from_ttl")]
pub fn py_get_keuzelijstwaardes_from_ttl(path: &str, env: &str) -> PyResult<Vec<PyKeuzelijstWaarde>> {
    let p = Path::new(path);
    if !p.exists() {
        return Err(pyo3::exceptions::PyFileNotFoundError::new_err(format!(
            "File not found: {}", p.display()
        )));
    }
    let store = TripleStore::load(p).map_err(|e| {
        pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to load TTL: {}", e))
    })?;
    Ok(get_keuzelijstwaardes_from_store(&store, env))
}

#[pyfunction]
#[pyo3(name = "get_adm_status_from_ttl")]
pub fn py_get_adm_status_from_ttl(path: &str, uri: &str, env: &str) -> PyResult<String> {
    let p = Path::new(path);
    if !p.exists() {
        return Err(pyo3::exceptions::PyFileNotFoundError::new_err(format!(
            "File not found: {}", p.display()
        )));
    }
    let store = TripleStore::load(p).map_err(|e| {
        pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to load TTL: {}", e))
    })?;

    let lookup_uri = if env == "tei" {
        uri.replace("wegenenverkeer", "wegenenverkeer-test")
    } else {
        uri.to_string()
    };

    if let Some(status) = store.object_for(&lookup_uri, ADMS_STATUS) {
        Ok(status.replace(KL_ADMS_PREFIX, ""))
    } else {
        Ok(String::new())
    }
}

#[pyfunction]
#[pyo3(name = "parse_graph_to_dict")]
pub fn py_parse_graph_to_dict(
    path: &str,
) -> PyResult<Vec<(String, Vec<(String, String, String)>)>> {
    let p = Path::new(path);
    if !p.exists() {
        return Err(pyo3::exceptions::PyFileNotFoundError::new_err(format!(
            "File not found: {}", p.display()
        )));
    }
    let dict = parse_graph_to_dict(p).map_err(|e| {
        pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to parse graph: {}", e))
    })?;
    Ok(dict.into_iter().collect())
}
