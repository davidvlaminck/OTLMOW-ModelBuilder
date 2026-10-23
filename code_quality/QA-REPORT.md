# QA Report — otlmow_modelbuilder

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-23 · commit `863d820`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 140 | 🔴 |
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
| 6894 | 4 | 1149 | 6 | `otlmow_modelbuilder/OTLModelCreator.py` |
| 2565 | 6 | 513 | 5 | `otlmow_modelbuilder/OTLClassCreator.py` |
| 2244 | 3 | 374 | 6 | `otlmow_modelbuilder/OSLOCollector.py` |
| 1540 | 2 | 110 | 14 | `otlmow_modelbuilder/GeometrieInheritanceProcessor.py` |
| 780 | 2 | 39 | 20 | `otlmow_modelbuilder/AbstractDatatypeCreator.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `N999` | 64 |
| `LOG015` | 42 |
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
| 2026-10-23 | 92.6 | 0.0 | 528 | 270 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 522 | 270 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 522 | 270 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 160 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 159 | 252 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 160 | 251 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 157 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 157 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 161 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 140 | 250 | 6.0 | 6 | red |
