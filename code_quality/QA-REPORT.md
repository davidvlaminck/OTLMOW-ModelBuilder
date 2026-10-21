# QA Report — otlmow_modelbuilder

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `f4484b4`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 0 | 🟢 |
| files needing `ruff format` | 0 | 0 | 🟢 |
| mypy errors | 0 | 0 | 🟢 |
| test coverage (lines) | ≥ 80.0 % | 85.5 % | 🟢 |
| test coverage (branches) | ≥ 75.0 % | 73.7 % | 🔴 |
| max CRAP score | ≤ 6.0 | 52.2 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 32 | 🔴 |
| bandit HIGH issues | 0 | 0 | 🟢 |
| dead code items | 0 | 0 | 🟢 |
| god classes | 0 | 0 | 🟢 |

## Lead refactor target (highest CRAP)

`otlmow_modelbuilder/OSLOCollector.py:169` → `find_outgoing_relations` — CRAP **52.2** — complexity **10** — coverage **25.0 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 1269 | 4 | 47 | 27 | `otlmow_modelbuilder/OTLClassCreator.py` |
| 512 | 1 | 16 | 32 | `otlmow_modelbuilder/GeometrieInheritanceProcessor.py` |
| 432 | 2 | 27 | 16 | `otlmow_modelbuilder/DatatypeBuilderFunctions.py` |
| 352 | 2 | 22 | 16 | `otlmow_modelbuilder/OTLModelCreator.py` |
| 306 | 2 | 18 | 17 | `otlmow_modelbuilder/GenericBuilderFunctions.py` |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-21 | 85.5 | 73.7 | 0 | 0 | 52.2 | 32 | red |
