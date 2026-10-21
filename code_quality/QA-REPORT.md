# QA Report — otlmow_modelbuilder

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `e255395`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 537 | 🔴 |
| files needing `ruff format` | 0 | 49 | 🔴 |
| mypy errors | 0 | 274 | 🔴 |
| test coverage (lines) | ≥ 80.0 % | 87.6 % | 🟢 |
| test coverage (branches) | ≥ 75.0 % | 73.6 % | 🔴 |
| max CRAP score | ≤ 6.0 | 92.1 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 22 | 🔴 |
| bandit HIGH issues | 0 | 0 | 🟢 |
| dead code items | 0 | 10 | 🔴 |
| god classes | 0 | 1 | 🔴 |

## Lead refactor target (highest CRAP)

`otlmow_modelbuilder/OSLOCollector.py:51` → `_build_lookup_maps` — CRAP **92.1** — complexity **11** — coverage **12.5 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 3210 | 7 | 214 | 15 | `otlmow_modelbuilder/OTLClassCreator.py` |
| 1540 | 2 | 110 | 14 | `otlmow_modelbuilder/GeometrieInheritanceProcessor.py` |
| 1356 | 5 | 226 | 6 | `otlmow_modelbuilder/OTLModelCreator.py` |
| 924 | 3 | 42 | 22 | `otlmow_modelbuilder/AbstractDatatypeCreator.py` |
| 880 | 4 | 55 | 16 | `otlmow_modelbuilder/OSLOCollector.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `I001` | 80 |
| `N999` | 64 |
| `UP006` | 57 |
| `FA100` | 56 |
| `ISC004` | 47 |
| `LOG015` | 42 |
| `UP035` | 26 |
| `UP009` | 25 |
| `RUF013` | 24 |
| `F401` | 20 |
| `BLE001` | 14 |
| `F541` | 11 |
| `C417` | 9 |
| `SIM118` | 9 |
| `TRY004` | 7 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-20 | 95.9 | 86.4 | 181 | 18 | 35.1 | 35 | red |
| 2026-10-20 | 98.7 | 90.4 | 171 | 18 | 5.0 | 5 | red |
| 2026-10-21 | 99.0 | 0.0 | 0 | 0 | 5.0 | 5 | red |
| 2026-10-21 | 99.0 | 91.3 | 0 | 0 | 5.0 | 5 | green |
| 2026-10-21 | 99.0 | 91.3 | 0 | 0 | 5.0 | 5 | red |
| 2026-10-21 | 85.5 | 73.7 | 0 | 0 | 52.2 | 32 | red |
| 2026-10-21 | 86.5 | 71.9 | 536 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 87.6 | 73.6 | 536 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 87.6 | 73.6 | 537 | 274 | 92.1 | 22 | red |
| 2026-10-21 | 87.6 | 73.6 | 537 | 274 | 92.1 | 22 | red |
