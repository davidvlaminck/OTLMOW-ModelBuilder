# QA Report — otlmow_modelbuilder

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-23 · commit `09eb118`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 13 | 🔴 |
| files needing `ruff format` | 0 | 49 | 🔴 |
| mypy errors | 0 | 223 | 🔴 |
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
| 7506 | 9 | 1251 | 6 | `otlmow_modelbuilder/OTLModelCreator.py` |
| 2700 | 10 | 540 | 5 | `otlmow_modelbuilder/OTLClassCreator.py` |
| 2490 | 6 | 415 | 6 | `otlmow_modelbuilder/OSLOCollector.py` |
| 1620 | 4 | 81 | 20 | `otlmow_modelbuilder/AbstractDatatypeCreator.py` |
| 1596 | 3 | 114 | 14 | `otlmow_modelbuilder/GeometrieInheritanceProcessor.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `RUF012` | 6 |
| `PLW0602` | 3 |
| `SIM117` | 3 |
| `E722` | 1 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-23 | 92.6 | 0.0 | 75 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 68 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 34 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 33 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 28 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 27 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 26 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 20 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 13 | 250 | 6.0 | 6 | red |
| 2026-10-23 | 92.6 | 0.0 | 14 | 224 | 6.0 | 6 | red |
