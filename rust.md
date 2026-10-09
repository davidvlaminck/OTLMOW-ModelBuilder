# otlmow-modelbuilder → Rust migratieplan

Doel: de Python-API van `otlmow-modelbuilder` behouden (bestaande gebruikers zoals
`otlmow_model`, `otlmow_gui`, … blijven ongewijzigd werken), terwijl zware
verwerkingsstappen in Rust worden geschreven.

## 1. Uitgangssituatie (analyse van de repo)

- Pakket is fundamenteel een **codegenerator**: leest OTL-data → genereert
  Python-broncode voor `otlmow_model`.
- ~30 modules; afhankelijkheden: `rdflib`, `tqdm`. Python ≥ 3.9.
- **Belangrijk inzicht:** rdflib wordt maar in één module gebruikt:
  `OTLEnumerationCreator.py`. De rest van de modelbuilder is puur
  **SQLite-inlezen** (`OSLOInMemoryCreator`, `GeometrieInMemoryCreator` via
  `sqlite3`) + **codegeneratie** (`OTL*Creator`, `DatatypeBuilderFunctions`).
- rdflib wordt gebruikt zonder SPARQL, enkel voor:
  1. TTL parsen: `g.parse(file, format='turtle')` (keuzelijsten, skos)
  2. Groeperen per ConceptScheme (`parse_graph_to_dict`)
  3. Waarden uitlezen: `skos:notation`, `skos:definition`, `skos:prefLabel`,
     `adms:status` via `g.value(subject, predicate)`
  4. Klein beetje triples toevoegen bij ontbrekende graphs (`create_empty_graph`)
- Bestaande pytest-suite in `UnitTests/` met fixtures in `InputFiles/` en
  `UnitTests/kl_testkeuzelijst/KlTestKeuzelijst.ttl` — dit is de
  **golden test suite** voor de migratie.

## 2. Repo-strategie: zelfde repo (monorepo)

Niet aparte repo. Redenen:

1. De Python-API is het contract met de andere otlmow-pakketten; de bestaande
   tests draaien direct tegen de Rust-versie als guardrails.
2. **maturin ondersteunt "mixed layout"**: `rust/` naast de bestaande
   Python-package, één versienummer, één release-cadans.
3. Aparte repo = losse release-cyclus en sync-problemen.

Doelstructuur:

```
OTLMOW-ModelBuilder/
├── otlmow_modelbuilder/        ← bestaande Python-api (blijft, wordt dun)
│   ├── OTLEnumerationCreator.py  ← wrapper: delegatie naar _rust
│   └── ...
├── rust/                       ← nieuwe crate
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs              ← PyO3-exposes
│       ├── sqlite_reader.rs    ← rusqlite
│       └── ttl_reader.rs       ← oxigraph/oxttl
├── pyproject.toml              ← build-system → maturin
└── UnitTests/                  ← ongewijzigd, draait op de Rust-backend
```

pyproject.toml wijziging:

```toml
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"
```

## 3. Rust-crates

| Onderdeel | Crate | Opmerking |
|---|---|---|
| SQLite | `rusqlite` (bundled) | 1-op-1 port van `OSLOInMemoryCreator` |
| Turtle parsen + store | `oxigraph` | Parse + in-memory store; SPARQL 1.1 beschikbaar voor de toekomst |
| Alternatief lichtgewicht | `oxttl` / `rio_turtle` + eigen HashMap-index | Alleen parsen, zelf navigeren |
| RDF-abstraktie | `sophia` | Optie als navigatie over triples centraal wordt |
| Bindings | `pyo3` | `#[pyclass]`, `#[pymethods]`, `#[pyfunction]` |
| Build/distributie | `maturin` | `maturin develop` lokaal, `maturin build --release` voor wheels |
| Download/unzip (optioneel) | `reqwest` + `zip` | Mag ook in Python blijven (`urlretrieve`) |

Geen SPARQL-compatibiliteitsrisico: de huidige code gebruikt geen SPARQL.

## 4. Migratiestrategie (incrementeel, verticale slices)

1. **Setup-slice**: `rust/`-crate met maturin-config, eerste `#[pyfunction]`
   die iets triviaals teruggeeft; `maturin develop`; bestaande test groen.
2. **SQLite-slice**: porteer één methode van `OSLOInMemoryCreator`
   (bijv. `get_all_classes`) met `rusqlite`; Python-wrapper eromheen;
   `UnitTests/OSLOCollector_test.py` groen.
3. **TTL-slice**: porteer `parse_graph_to_dict` + `get_keuzelijstwaardes_from_graph`
   + `get_adm_status_from_graph` met oxigraph; expose als
   `collect_keuzelijsten(paths) -> list[KeuzelijstWaarde]`;
   `UnitTests/OTLEnumerationCreator_test.py` groen (inclusief
   `KlTestKeuzelijst.ttl`-fixture).
4. **Generatie-slice**: `OTL*Creator`-classes die strings uitschrijven —
   lineair werk, doel is **byte-identieke output** (anders gigantische diffs
   in gegenereerde `otlmow_model`).
5. Per slice: implementeer → tests groen → merge. Nooit alles tegelijk.

## 5. Aandachtspunten & valkuilen

- **rdflib `g.value()`-semantiek**: bij meerdere triples met dezelfde
  subject+predicate keert rdflib er "toevallig" één terug (eerste gevonden).
  In Rust expliciet maken (eerste of laatste triple) en met tests vastleggen.
- **Blank nodes / literals**: let op datatype- en language-tag-verschillen
  (`lang='nl'`) bij het vergelijken van uitvoer.
- **tqdm**: niet in Rust; optionele callback of progress via PyO3.
- **GIL**: bundel werk in één Python-call, niet per-triple over de grens.
- **output-stabiliteit**: bij codegeneratie byte-identiek blijven; test door
  volledige gegenereerde models te diffen tegen de huidige output.
- **CI**: maturin wheel-build per platform + bestaande pytest-suite erop.
- **Beslismoment**: als oxigraph/oxttl de TTL's niet 1-op-1 leest, laat de
  enumeration-module in Rust links liggen — collector (SQLite) en
  generatie-kant zijn al netjes gescheiden en zijn de hoofdprijs.

## 6. Realistische inschatting

- **Snel win**: SQLite-inlezen (`rusqlite`), dataverwerking, stringgeneratie.
- **Kostbaar**: TTL/rdflib-equivalentie (edge cases), inheritance/MRO-logica
  (`_c3_merge`, `_topo_sort` — best wel algoritmes, goed in Rust te porten).
- **Bewaar in Python**: glue-code die andere otlmow-pakketten hergebruiken,
  instellingen/settings, eventuele download-stappen.

Begin op een tak (`rust-prototype`) en beslis na slice 1–3 op basis van
groene tests of je doorbijt.

## 7. Handige commando's

```bash
# lokale ontwikkeling
cd rust && maturin develop          # bouwt + installeert in huidige venv
maturin develop --release
python -m pytest UnitTests/

# distributie
maturin build --release             # wheels in target/wheels/
```
