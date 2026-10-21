# QA Report — otlmow_modelbuilder

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `ae07920`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 529 | 🔴 |
| files needing `ruff format` | 0 | 49 | 🔴 |
| mypy errors | 0 | 268 | 🔴 |
| test coverage (lines) | ≥ 80.0 % | 88.4 % | 🟢 |
| test coverage (branches) | ≥ 75.0 % | 74.7 % | 🔴 |
| max CRAP score | ≤ 6.0 | 92.1 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 22 | 🔴 |
| bandit HIGH issues | 0 | 0 | 🟢 |
| dead code items | 0 | 10 | 🔴 |
| god classes | 0 | 2 | 🔴 |

## Lead refactor target (highest CRAP)

`otlmow_modelbuilder/OSLOCollector.py:51` → `_build_lookup_maps` — CRAP **92.1** — complexity **11** — coverage **12.5 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 7026 | 6 | 1171 | 6 | `otlmow_modelbuilder/OTLModelCreator.py` |
| 1540 | 2 | 110 | 14 | `otlmow_modelbuilder/GeometrieInheritanceProcessor.py` |
| 1070 | 7 | 214 | 5 | `otlmow_modelbuilder/OTLClassCreator.py` |
| 924 | 3 | 42 | 22 | `otlmow_modelbuilder/AbstractDatatypeCreator.py` |
| 880 | 4 | 55 | 16 | `otlmow_modelbuilder/OSLOCollector.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `I001` | 80 |
| `N999` | 64 |
| `FA100` | 56 |
| `UP006` | 55 |
| `ISC004` | 47 |
| `LOG015` | 42 |
| `UP009` | 25 |
| `UP035` | 25 |
| `RUF013` | 23 |
| `F401` | 20 |
| `BLE001` | 14 |
| `F541` | 11 |
| `C417` | 9 |
| `SIM118` | 8 |
| `TRY004` | 7 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-21 | 99.0 | 0.0 | 0 | 0 | 5.0 | 5 | red |
| 2026-10-21 | 99.0 | 91.3 | 0 | 0 | 5.0 | 5 | green |
| 2026-10-21 | 99.0 | 91.3 | 0 | 0 | 5.0 | 5 | red |
| 2026-10-21 | 85.5 | 73.7 | 0 | 0 | 52.2 | 32 | red |
| 2026-10-21 | 86.5 | 71.9 | 536 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 87.6 | 73.6 | 536 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 87.6 | 73.6 | 537 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 87.6 | 73.6 | 537 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 88.4 | 74.7 | 545 | 268 | 92.1 | 22 | red |
| 2026-10-21 | 88.4 | 74.7 | 529 | 268 | 92.1 | 22 | red |
