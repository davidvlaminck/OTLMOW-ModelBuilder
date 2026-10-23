# QA Report — otlmow_modelbuilder

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-23 · commit `8720b6b`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 34 | 🔴 |
| files needing `ruff format` | 0 | 49 | 🔴 |
| mypy errors | 0 | 250 | 🔴 |
| test coverage (lines) | ≥ 80.0 % | 92.6 % | 🟢 |
| test coverage (branches) | ≥ 75.0 % | 0.0 % | 🔴 |
| max CRAP score | ≤ 6.0 | 6.0 | 🟢 |
| max cyclomatic complexity | ≤ 6 | 6 | 🟢 |
| bandit HIGH issues | 0 | 0 | 🟢 |
| dead code items | 0 | 9 | 🔴 |
| god classes | 0 | 3 | 🔴 |
| membership-list violations | 0 | 0 | 🟢 |

## Lead refactor target (highest CRAP)

`otlmow_modelbuilder/OSLOCollector.py:267` → `_direct_relations_of` — CRAP **6.0** — complexity **6** — coverage **100.0 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 7062 | 5 | 1177 | 6 | `otlmow_modelbuilder/OTLModelCreator.py` |
| 2660 | 7 | 532 | 5 | `otlmow_modelbuilder/OTLClassCreator.py` |
| 2454 | 4 | 409 | 6 | `otlmow_modelbuilder/OSLOCollector.py` |
| 1580 | 3 | 79 | 20 | `otlmow_modelbuilder/AbstractDatatypeCreator.py` |
| 1540 | 2 | 110 | 14 | `otlmow_modelbuilder/GeometrieInheritanceProcessor.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `BLE001` | 12 |
| `TRY004` | 7 |
| `RUF012` | 6 |
| `PLW0602` | 3 |
| `SIM117` | 3 |
| `S110` | 2 |
| `E722` | 1 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-23 | 92.6 | 0.0 | 159 | 252 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 160 | 251 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 157 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 157 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 161 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 140 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 76 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 75 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 68 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 34 | 250 | 6.0 | 6 | red |
