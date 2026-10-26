# Code Quality — measure → characterise → refactor → verify → ratchet

The operating manual for AI agents (and humans) that improve a Python repository
without breaking it.

Everything in this folder is self-contained:

| Path | What it is |
|---|---|
| `README.md` | This document — the process |
| `PY-ANTI-PATTERNS.md` | Banned constructs, each mapped to the ruff rule that detects it |
| `QA-REPORT.md` | **Generated** dashboard — never edit by hand |
| `scripts/qa_report.py` | Runs every gate and writes `QA-REPORT.md` + `reports/qa.json` |
| `scripts/crap_scores.py` | CRAP ranking and change hot spots |
| `coverage.cfg` | Coverage configuration for the quality gate only |
| `ci/quality.yml` | GitHub Actions workflow to copy into `.github/workflows/` |
| `reports/` | Machine-readable artefacts (generated) |

---

## 1. Philosophy

1. **Measure** objectively: lint, types, tests, coverage, complexity, security, dead code.
2. **Characterise** the behaviour before touching it — a refactor without a pinned
   behaviour is a rewrite with extra steps.
3. **Publish** a dashboard of current numbers against thresholds.
4. **Refactor** the worst offender first: highest CRAP, broken by change hot spot.
5. **Verify**: same behaviour, green tests, ratchet not regressed.
6. **Ratchet**: the gate may only get tighter. Never trade a metric for another.

The one-line summary: **metrics tell you where to look, characterisation tells you
whether you broke something.** Neither alone is a quality process.

---

## 2. The loop

```
┌────────────────┐
│ 1. Measure     │────┐
│ lint/types/    │    │
│ tests/complex  │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 2. Report      │    │
│ QA-REPORT.md   │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 3. Characterise│    │  ← pin behaviour BEFORE editing
│ golden tests   │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 4. Refactor    │    │
│ highest CRAP   │    │
│ hot spot first │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 5. Verify      │────┘  ← behaviour identical, tests green,
│ behaviour+tests│         ratchet not regressed
└───────┬────────┘
        ▼
    ratchet down
```

**Loop rule.** One target per cycle, one commit per behaviour change. Stop when the
cycle takes longer than the target is worth — write down why in the report and pick
the next one.

---

## 3. Tool mapping

| Stage | Tool | Catches | Does **not** catch |
|---|---|---|---|
| Lint / anti-patterns | `ruff` | style, bugs, imports, banned constructs, dead branches | design problems |
| Format | `ruff format` | formatting drift | — |
| Static types | `mypy` (staged, see §6) | wrong types, broken contracts | runtime behaviour |
| Tests | `pytest` + `pytest-cov` | regressions | whether the assertions mean anything |
| Test strength | `mutmut` | tests that assert nothing | — |
| Complexity | `radon` | unreadable functions | whether the function is needed |
| CRAP score | `radon` + `coverage` | risky code | — |
| Hot spots | `radon` + `git log` | code that keeps breaking | — |
| Security | `bandit` | injection, unsafe deserialisation | dependency CVEs → `pip-audit` |
| Dead code | `vulture` | unreachable code | public API that is used externally |
| Dependencies | `pip-audit` | known CVEs | — |
| Duplication | `jscpd` | copy-paste | — |
| Import cycles | `lint-imports` | architectural drift | — |
| Docstrings | `pydoclint` | docstring/signature mismatch | — |

Install the quality tools **into the project virtualenv** so they see the project
dependencies:

```bash
uv pip install ruff==0.17.0 "mypy<2" radon bandit vulture
uv pip install mutmut pip-audit jscpd        # optional, see sections 8 and 3
```

`radon` is optional — `scripts/crap_scores.py` falls back to `uvx radon` when it is
not installed.

---

## 4. Configuration

The blocks below are already applied in `pyproject.toml` for this repository. For a
new repository, copy them and adjust the paths.

### 4.1 ruff

```toml
[tool.ruff]
line-length = 100
target-version = "py39"
src = ["otlmow_modelbuilder", "UnitTests"]
# Vendored third-party code is not ours to lint.
extend-exclude = ["UnitTests/TestModel"]

[tool.ruff.lint]
select = [
    "E", "F", "I", "B", "C4", "UP", "PYI", "PT", "RUF", "S", "BLE", "TRY", "FLY",
    "A", "C", "PL", "Q", "RET", "N", "W", "T20", "G", "LOG", "PIE", "SIM", "PERF",
    "ARG", "TID", "PTH",
]
ignore = ["E501"]

[tool.ruff.lint.flake8-tidy-imports]
ban-relative-imports = "all"

[tool.ruff.lint.flake8-quotes]
inline-quotes = "single"
docstring-quotes = "double"

[tool.ruff.lint.per-file-ignores]
"UnitTests/**" = ["S101", "N802", "N803", "N815", "PLR2004", "PT006"]
"otlmow_modelbuilder/**/*.py" = ["N802", "N803", "N815", "N806"]
# CLI tooling: printing to stdout is the interface, and subprocess calls always
# use an argument list (never shell=True).
"code_quality/scripts/*.py" = ["T201", "S603"]

[tool.ruff.format]
docstring-code-format = true
quote-style = "single"
```

Three traps, all hit and verified in this repository:

- **`"P"` is not a ruff selector.** `select = [... "P" ...]` makes ruff abort with
  `Unknown rule selector 'P'`. The pylint rules are selected with `"PL"`. (`"PG"` is
  also invalid — those pygrep rules were removed from ruff.)
- **`T20` and `G` must be selected explicitly.** `PY-ANTI-PATTERNS.md` bans `print()`
  and f-strings in logging calls; without `"T20"` / `"G"` in `select` those bans never
  fire.
- **Quote style is two settings.** `[tool.ruff.format] quote-style` drives the
  formatter; `[tool.ruff.lint.flake8-quotes] inline-quotes` drives the `Q000` linter.
  Set both to the style the code already uses, otherwise every string in the
  repository becomes a diff.

### 4.2 pytest

Do **not** put `--cov` into `addopts` in a repository whose CI already computes
coverage in a separate workflow: it changes the published coverage badge and can
break the existing test matrix. Invoke coverage explicitly in the quality job:

```bash
python -m pytest --cov=otlmow_modelbuilder --cov-report=json:code_quality/reports/coverage.json -q
```

`testpaths` may still be set to the real test directory (`UnitTests` here) so that a
bare `pytest` does not collect the whole repository.

### 4.3 coverage

The quality gate uses its own configuration file so it cannot interfere with the
badge produced by `.github/workflows/coverage.yml`:

```ini
# code_quality/coverage.cfg
[run]
source = otlmow_modelbuilder
omit =
    UnitTests/TestModel/*
    */__pycache__/*

[report]
exclude_also =
    if TYPE_CHECKING:
    raise NotImplementedError
    @abstractmethod
    if __name__ == .__main__.:
```

Use it with `COVERAGE_RCFILE=code_quality/coverage.cfg` (the QA script does this
automatically) or `--cov-config=code_quality/coverage.cfg`.

---

## 5. Gates that actually gate

The single most common failure in a quality document is a gate that cannot fail.
Every command below was executed against this repository; the exit codes are real.

| Command | What it enforces | Exit code on violation |
|---|---|---|
| `ruff check <src> <tests> <scripts>` | every selected rule | 1 |
| `ruff format --check <src> <tests> <scripts>` | formatting is applied | 1 |
| `mypy <src> <tests> <scripts>` | type errors | 1 |
| `pytest --cov-fail-under=80` | coverage floor | 1 |
| `radon cc -j <src>` + the `max complexity` row of the QA report | complexity ceiling | 1 |
| `bandit -q -r <src>` | security findings | 1 |
| `vulture <src> --min-confidence 80` | dead code | 1 |
| `qa_report.py --fail-on <gates>` | the named gates **and the ratchet** | 1 |

The quality tooling in `code_quality/scripts/` is linted and type-checked by the
same gate: a gate that does not check itself is not a gate.

> **`radon cc -n C` is not a gate.** `-n` only filters what is printed; radon exits 0
> even for a grade-`F` function.

> **radon 6 removed `--fail-under`.** `radon cc --fail-under 15 <src>` exits 2 with
> `unrecognized arguments: --fail-under`, whatever the code looks like — a gate that
> fails for the wrong reason. The complexity ceiling is the `max complexity` row of
> `QA-REPORT.md`: `qa_report.py` exits 1 when it is breached, and `ci/quality.yml`
> checks the same ceiling on the json output of radon.

> **the `ruff format` counter has to follow the ruff version.** ruff 0.17 prints
> `unformatted: File would be reformatted` per file, older versions printed
> `Would reformat: <path>`. A counter that only knows the old output reports 0
> files and the gate can never fail.

> **`ruff format --check` crashed** on the vendored `UnitTests/TestModel` tree
> (`panicked at crates/ruff_annotate_snippets/.../source_map.rs`). Excluding vendored
> code with `extend-exclude` fixes it. Pin the ruff version in CI so a new release
> cannot break the build.

---

## 6. Type checking — staged adoption, ending at `strict`

`strict = true` on a codebase without annotations produces thousands of errors and
is never adopted. Adopt it in three stages; each stage is a mergeable, green commit.

| Stage | Configuration | Errors in this repo | Exit criteria |
|---|---|---|---|
| 1 | bodies checked, signatures optional | **18** | zero errors |
| 2 | `disallow_untyped_defs` per module | **77** | package fully annotated |
| 3 | `strict = true` | **81** | strict enabled permanently |

Stage 1 (current state):

```toml
[tool.mypy]
python_version = "3.9"
warn_unused_ignores = true
check_untyped_defs = true
disallow_any_generics = true
no_implicit_optional = true
strict_equality = true
warn_return_any = true

[[tool.mypy.overrides]]
module = ["otlmow_modelbuilder.*"]
disallow_untyped_defs = false
```

Stage 2 — flip one module at a time, never the whole package at once:

```toml
[[tool.mypy.overrides]]
module = ["otlmow_modelbuilder.SubsetTemplateCreator"]
disallow_untyped_defs = true
```

Stage 3 — the endgame. Once stage 2 is green, replace the whole block with:

```toml
[tool.mypy]
python_version = "3.9"
strict = true
```

Stage 3 is only four errors beyond stage 2, so the path is short. **Do not skip
straight to stage 3**: the intermediate stages keep every commit mergeable.

> **mypy must stay below version 2.** mypy 2.x refuses to target Python 3.9
> (`Python 3.9 is not supported (must be 3.10 or higher)`) and exits with an error,
> so a package that supports 3.9 has to pin `mypy<2`. On Python 3.9 uv resolves
> `mypy<2` to 1.19.1 automatically.

---

## 7. Behaviour preservation — the gate metrics cannot replace

A refactor can halve complexity, keep coverage at 91 %, and change every cell of a
generated Excel file. Metrics do not notice. The only defence is to pin the current
behaviour **before** editing.

### 7.1 Characterisation test

Write a test that captures the *current* output of the target function and fails if
that output changes unintentionally:

```python
def test_alter_excel_sheet_is_unchanged(tmp_path):
    """Golden file: the generated template must stay byte-identical."""
    result = SubsetTemplateCreator.generate_template_from_subset(
        subset_path=SUBSET_XML, template_file_path=tmp_path / "out.xlsx")
    assert workbook_snapshot(tmp_path / "out.xlsx") == GOLDEN_SNAPSHOT
```

Build the snapshot from *content*, not from bytes: Excel files embed timestamps,
so compare cell values, sheet names, order and formatting attributes.

For CSV output compare the text; for XML compare the parsed tree.

**A template with random content cannot be compared byte by byte.** In this
repository the dummy values are random, the sheet and column order depends on the
order in which the parallel generation finishes, and the model picks a random
branch of a union type — three runs of the same input produce three different
workbooks. The snapshot must therefore normalise:

- random values become a marker that keeps their type (`<text>`, `<number>`,
  `<date>`, `<bool>`), so a value that changes type is still detected;
- the columns of the choice-list sheet are sorted by their header;
- the columns of a union type are collapsed into one key.

`UnitTests/Subset/template_snapshot.py` implements exactly that, and
`UnitTests/Subset/SubsetTemplateCreator_structure_test.py` uses it to pin the
generated template in `UnitTests/Subset/snapshots/`. Regenerate the golden file
after an intentional change with:

```bash
UPDATE_GOLDEN=1 python -m pytest UnitTests/Subset/SubsetTemplateCreator_structure_test.py
```

### 7.2 The rule

> No refactor of a function starts before a characterisation test exists for it.

If the function cannot be characterised (side effects, network, database), write the
characterisation test for the seam above it instead.

### 7.3 Verification step

Before/after comparison is the actual gate:

```bash
git stash                  # or: work on a branch and keep the old revision
python -m pytest UnitTests -k "golden"
git stash pop
python -m pytest UnitTests -k "golden"
```

Both runs must pass. If the golden test fails after the refactor, either the
refactor changed behaviour (bug) or the golden file was updated to match the new
behaviour (review that diff with the same care as the code change).

---

## 8. Test strength — coverage is not proof

Coverage says a line ran. It does not say an assertion checked it. A test suite can
sit at 91 % coverage and assert nothing meaningful. Mutation testing measures the
thing that actually matters: **would the test fail if the code were wrong?**

```toml
# pyproject.toml
[tool.mutmut]
source_paths = ["otlmow_modelbuilder"]
tests_dir = ["UnitTests"]        # a list in pyproject.toml, a string in setup.cfg
```

```bash
uv run mutmut run
uv run mutmut results
```

- `source_paths` is mandatory; without it mutmut cannot find the code to mutate.
- The package must be importable under its real name (mutmut's trampoline rejects
  `src.module` style package names).
- Interpret the score as *surviving mutants*, not as a percentage to optimise. A
  surviving mutant is either a missing test or a genuinely equivalent mutation —
  review them, then write the test or add `# noqa` with a reason.

Adopt mutation testing per module, starting with the module you are about to
refactor. A module with no surviving mutants can be refactored with far less fear.

---

## 9. CRAP score and change hot spots

### 9.1 Formula

```
CRAP = complexity² × (1 − coverage/100)³ + complexity
```

- `complexity` = cyclomatic complexity of the function (`radon cc -j -s`)
- `coverage` = percentage of executable lines of that function covered by tests

### 9.2 Interpretation — and its limit

| Coverage | Effect |
|---|---|
| 100 % | CRAP = complexity |
| 0 % | CRAP = complexity² + complexity |

**At high coverage CRAP degenerates into raw complexity.** In this repository
coverage is 99 %, so CRAP is a rescaled complexity score. Three consequences:

- Adding tests will not move the metric for well-covered code. Target complexity.
- The absolute threshold (≤ 6 here) is only meaningful for weakly covered code. Read the
  CRAP column *together with* the complexity and coverage columns, never alone.
- A function can be "improved" by splitting it into ten small ones. That is metric
  gaming, not a refactor: require the behaviour to stay identical and the tests to
  stay green, and review the resulting structure on its merits.

### 9.3 Bands

| CRAP | Meaning | Action |
|---|---|---|
| ≤ 5 | clean | leave alone |
| 5–10 | acceptable | monitor |
| 10–30 | risky | refactor soon |
| 30–60 | dangerous | refactor now |
| > 60 | critical | block merge |

### 9.4 Computing it

`scripts/crap_scores.py` does it and is the reference implementation:

```bash
python -m pytest --cov=otlmow_modelbuilder --cov-report=json:code_quality/reports/coverage.json -q
python code_quality/scripts/crap_scores.py --source otlmow_modelbuilder --top 25
```

It maps radon's blocks to covered line ranges (radon's JSON has a different shape
for one file than for many), skips class-level blocks, and reports the ranking:

```
| CRAP | Complexity | Coverage | Function | Location |
|---:|---:|---:|---|---|
| 5.0 | 5 | 100.0 % | `add_choice_list_validation` | `otlmow_template/SubsetTemplateCreator.py:818` |
```

### 9.5 Change hot spots — complexity alone picks the wrong target

The real risk of a function is complexity **times how often it changes**. A
complex function nobody touches is less urgent than a medium one that breaks every
month. The script combines git churn with complexity:

```
| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 540 | 7 | 108 | 5 | `otlmow_template/SubsetTemplateCreator.py` |
```

Selection rule for the lead target:

1. Rank by CRAP.
2. Rank by hot-spot score.
3. Take the function that appears high in **both**. A file that is hot but simple
   usually needs a different fix (a design change), not a local refactor.

---

## 10. AI-specific code smells

These are the failure modes that code written by a language model produces
repeatedly. Each has a detection rule, so they can be found mechanically rather
than by reading everything.

| Smell | Why it is a problem | Detection |
|---|---|---|
| **Speculative parameters** — `**kwargs` forwarded to a call that ignores them | hides typos, widens the API surface | `grep -n "\*\*kwargs" <src>`; ruff `ARG001`/`ARG002` |
| **Defensive swallowing** — `except AttributeError: pass` | hides real errors | ruff `S110`, `BLE001`, `TRY300` |
| **Duplicated sync/async twins** | two implementations, one behaviour | `jscpd --min-tokens 50 <src>` |
| **Docstring that restates the code** | noise that hides useful docs | `pydoclint`; `interrogate --fail-under 100` |
| **Silent fallback / default** — returns `[]` instead of raising | callers cannot distinguish "empty" from "broken" | review every `return None` / `return []` in a diff |
| **Renaming without behaviour change** | diff noise, hides the real change | require the diff to contain a behavioural assertion |
| **Speculative generality** — abstraction for one caller | indirection without reuse | `vulture` + "is there a second caller?" |
| **Accurate-looking but unverified API use** | hallucinated library call | see §12 |
| **Copy-pasted test fixtures** | tests assert the fixture, not the code | `jscpd` over the test tree |
| **Tautological assertions** — `assert result is not None` | proves nothing | mutation testing (§8) |

Extra rules to keep in mind when *writing* AI-assisted code:

- Prefer the smallest change that solves the problem. Do not "improve" surrounding
  code in the same edit.
- Do not add a layer of abstraction with exactly one implementation.
- Never invent a parameter, a return value or an exception that no caller uses.
- When unsure about a library API, look it up (§12) — do not guess and do not
  silence the type checker to make the guess compile.

---

## 11. Agent guardrails and commit discipline

An agent without guardrails will rewrite the repository. These limits keep the work
reviewable:

1. **One target per cycle.** The lead target from the report, nothing else.
2. **One behaviour change per commit.** Commits must be bisectable: each one is
   green on its own.
3. **Never reformat unrelated files.** If `ruff format` must run, it is its own
   commit, first, before any refactor.
4. **Never change a public API** of a published package without explicit approval.
   The camelCase names flagged by `N802`/`N803` are this package's published API —
   they are excluded in the ruff config on purpose.
5. **Never weaken a gate** to make something pass: no `# noqa` without a reason
   comment, no deleted test, no lowered threshold, no `except: pass`.
6. **Never touch vendored code** (`UnitTests/TestModel`).
7. **Do not commit generated noise** — coverage HTML, `.db` files, `.xlsx` outputs.
8. **Stop when the diff grows.** If a "small" refactor touches more than ~3 files or
   ~200 lines, it is not a refactor; split it or ask.
9. **Report honestly.** If a metric cannot be improved without changing behaviour,
   say so in the report instead of gaming the number.

### 11.1 Definition of done for a cycle

- [ ] Characterisation/golden test exists for the target and passes.
- [ ] The refactor is committed on its own, tests green.
- [ ] The golden test still passes unchanged.
- [ ] `ruff`, `mypy`, `pytest`, `bandit` are green (or the ratchet did not regress).
- [ ] `QA-REPORT.md` regenerated; the lead target moved to the next offender.
- [ ] The report states what changed and what was deliberately left alone.

---

## 12. Anti-hallucination: verify every third-party API

This repository depends on `otlmow-converter` and `otlmow-modelbuilder`, which are
not part of the standard library and are not in the training data of most models.
An agent that guesses an API produces code that looks right and fails at runtime.

**Rule: never write a call to a third-party API that has not been verified in the
installed package.**

```bash
uv run python -c "import inspect; from otlmow_converter.OtlmowConverter import OtlmowConverter; print(inspect.signature(OtlmowConverter.from_objects_to_file))"
uv run python -c "import otlmow_converter; print(otlmow_converter.__version__)"
```

Also allowed: reading the installed source
(`python -c "import x; print(x.__file__)"`) or the package's own docs/tests in
`.venv/`. Pin behaviour to the versions in `uv.lock`.

If an API cannot be verified, the correct output is a question, not an assumption.

---

## 13. Concurrency, determinism and performance checklist

Code that uses threads, async or retries breaks in ways no metric catches. Before
refactoring such code, verify:

- **Determinism** — does the output order depend on dict/set iteration or on thread
  completion order? Pin it with a sorted comparison or an explicit sort.
- **Shared state** — is a mutable default, a class attribute or a module-level
  cache mutated from a worker? (ruff `RUF012`, `B006`.)
- **Exception policy** — is an exception swallowed in a worker so the main path
  believes it succeeded?
- **Retry loops** — is there a `while True` without a bound? A retry without a
  maximum is an infinite loop waiting for a bad day.
- **Resource cleanup** — are executors, sessions and file handles closed on the
  error path?
- **Complexity** — did the refactor turn an O(n) loop into an O(n²) one? Check the
  number of database or file reads inside a loop.

---

## 14. Ratchet and diff-scoped gates

A repository with a history of violations cannot reach "zero issues" in one pass,
and an agent asked to do so will either churn the whole codebase or give up. Use a
**ratchet** instead: the budget may only shrink.

`scripts/qa_report.py` implements this. It stores the per-rule lint counts of the
previous cycle in `reports/qa-history.json` and fails when any rule count went up:

```
ratchet regressions:
  I001: 29 -> 34
```

Rules for the agent:

- Fixing a rule that is not part of the current target is allowed only if it does
  not touch unrelated code — otherwise it belongs to a separate commit.
- A rule count may never increase, including "fixes" that introduce a new rule.
- Thresholds may only be tightened, never loosened.
- The history table in `QA-REPORT.md` is the audit trail of the ratchet.

Diff-scoped checks (for a pull request, not for the whole repository):

```bash
CHANGED=$(git diff --name-only origin/master...HEAD -- '*.py')
ruff check $CHANGED
mypy $CHANGED
```

---

## 15. The QA report is generated

```bash
python code_quality/scripts/qa_report.py
```

writes `code_quality/QA-REPORT.md` and `code_quality/reports/qa.json`, and appends a
row to `reports/qa-history.json`.

- The report is **never edited by hand**. Change a threshold in the script instead.
- Regenerating it produces a small diff (only the rows that moved), so it stays
  reviewable.
- `reports/` holds generated artefacts: keep `qa.json` if you want the history in
  git, and ignore the rest.
- `--skip-tests` reuses the existing coverage report, `--no-history` keeps the
  ratchet history untouched (for a run on the CI) and `--fail-on <gates>` limits
  the gates that block the run — see §16.

The report contains: the threshold table, the enforced gates, the lead refactor
target, the hot spots, the per-rule lint breakdown and the cycle history.

---

## 16. CI enforcement

Copy `ci/quality.yml` to `.github/workflows/quality.yml`. In this repository the
gate is installed: `.github/workflows/quality.yml` runs on every push and pull
request, and `ci/quality.yml` is the template of that file — keep the two in sync.

**Roll it out in two stages**, otherwise the first run is red and the workflow gets
disabled on day two:

1. **Advisory** — the gates with a known budget report but do not block
   (`continue-on-error: true`): lint, format check, type check. They become
   blocking when their budget is zero, one rule at a time: add the gate to the
   `--fail-on` list below.
2. **Enforcing** — the gates that are green today block the merge, and so does the
   ratchet (lint counts may not increase). The absolute zero-issue gate comes
   last, once the budget is actually zero.

The individual `ruff`/`mypy`/`bandit`/`vulture` steps only make the findings
visible in the log; the thresholds that decide whether a merge is blocked live in
`DEFAULT_THRESHOLDS` of `qa_report.py`, so the workflow and the report can never
disagree.

Which gates block is decided in one place, in the script:

```yaml
- name: Quality gates
  run: |
    uv run python code_quality/scripts/qa_report.py \
      --skip-tests \
      --no-history \
      --fail-on coverage,coverage-branch,crap,complexity,bandit,dead-code
```

- `--fail-on <gates>` — the comma separated gates that must pass; without it,
  *every* gate must pass. The thresholds stay in `DEFAULT_THRESHOLDS` of the
  script, so the workflow and the report can never disagree.
- `--skip-tests` — reuse the coverage report of the test step instead of running
  the suite twice.
- `--no-history` — a run on the CI must not append a row to the ratchet history;
  the history is the audit trail of the real cycles.

The ratchet is enforced by every run, with or without `--fail-on`.

Notes:

- Use `uv pip install -r pyproject.toml --extra test` for the project dependencies,
  then add the quality tools explicitly: `uv pip install ruff==0.17.0 "mypy<2"
  radon bandit vulture`.
- `uv sync` **removes** tools that are not in the lock file (including a locally
  installed ruff), so do not use `uv sync` and then `uv run ruff`.
- `uv run --python 3.9` **recreates** the project virtualenv with that interpreter.
  Use a separate virtualenv when you need a second interpreter.
- Pin the ruff version (`ruff==0.17.0`) so a new release cannot break the gate, and
  keep `mypy<2` while the package supports Python 3.9.
- Run the gate on the lowest supported Python version as well; type and lint
  results differ per version.

---

## 17. Anti-patterns

See `PY-ANTI-PATTERNS.md` for the banned constructs and the exact ruff rule that
detects each one. Every rule listed there is enabled in `pyproject.toml`.

---

## 18. Appendix — measured baseline (OTLMOW-Template, 2026-10-20)

Generated by `code_quality/scripts/qa_report.py`.

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 171 | 🔴 |
| files needing `ruff format` | 0 | 31 | 🔴 |
| mypy errors (stage 1) | 0 | 18 | 🔴 |
| test coverage (lines) | ≥ 80 % | **98.7 %** | 🟢 |
| test coverage (branches) | ≥ 75 % | **90.4 %** | 🟢 |
| max CRAP | ≤ 6 | 5.0 | 🟢 |
| max complexity | ≤ 6 | 5 | 🟢 |
| bandit HIGH | 0 | 0 | 🟢 |
| dead code | 0 | 0 | 🟢 |

The coverage numbers are the ones *after* the test suite was strengthened — see
§20 for what the suite could not detect before.

> The `ruff format` counter used to report 0 files: it looked for output that
> ruff 0.17 no longer prints, so the gate could not fail. The counter is fixed;
> the 31 files it exposes are the pre-existing formatting debt of plan item 4,
> not a regression of the last cycle.

### CRAP ranking

| CRAP | Complexity | Coverage | Function | Location |
|---:|---:|---:|---|---|
| 5.0 | 5 | 100.0 % | `add_choice_list_validation` | `otlmow_template/SubsetTemplateCreator.py:818` |
| 5.0 | 5 | 100.0 % | `delete_dummy_rows` | `otlmow_template/SubsetTemplateCreator.py:862` |
| 4.0 | 4 | 100.0 % | `add_attribute` | `otlmow_template/SubsetTemplateCreator.py:70` |
| 4.0 | 4 | 100.0 % | `generate_template_from_subset_async` | `otlmow_template/SubsetTemplateCreator.py:135` |
| 4.0 | 4 | 100.0 % | `generate_template_from_subset` | `otlmow_template/SubsetTemplateCreator.py:197` |
| 4.0 | 4 | 100.0 % | `create_x_objects` | `otlmow_template/SubsetTemplateCreator.py:259` |

No function of the package is above a CRAP of 5 any more; the ceiling of the
gate was tightened from 10 to 6 so it cannot drift back.

### Hot spot

`otlmow_template/SubsetTemplateCreator.py` — **116 of the 133 commits** in the
repository that touch the package touch this one file. It was both the CRAP
leader and the hot spot; after the refactor its worst-case complexity is 5.

### Findings that are noise, and findings that are not

Noise (excluded or ignored on purpose):

- `UnitTests/TestModel/**` — vendored copy of `otlmow_model` (1753 findings, and the
  formatter crashes on it).
- `N802`/`N803` in the package — the published camelCase API.
- `S101` in tests — assertions are the point of a test.

Real findings worth fixing, in order of value:

| Rule | Count | Meaning |
|---|---:|---|
| `PLR0913` + `PLR0917` | 16 + 16 | functions with 12+ arguments — the API shape is the problem |
| `RUF013` | 5 | implicit `Optional` (`x: Path = None`) |
| `TRY003` | 5 | exceptions raised with a bare string instead of a dedicated type |
| `PTH123` | 7 | `open()` instead of `Path.open()` |
| `UP006` | 13 | `typing.List` instead of `list` |
| `T201` | 2 | `print()` inside the library |
| `G004` | 1 | f-string in a logging call (eagerly formatted) |
| `LOG015` | 1 | root logger call instead of a module logger |
| `E712` / `E721` | 2 + 2 | `== True` comparisons and type comparisons by equality |

`C901` (5) and `PLR0912` (3) are gone: no function of the package is above a
complexity of 5 any more. `Q000` (27) and `I001` (29) are formatting/import
order: mechanical, safe, and they belong in one dedicated commit. `UP009` (21) is
the `coding: utf-8` header, which Python 3 defaults away — one commit removes
all of them.

### Ordered plan

The tests come first: a refactor is only safe when the suite can detect that the
behaviour changed.

0. ~~Strengthen the test suite~~ — done, see §20. The behaviour of the generated
   template is pinned by a golden structure snapshot, the synchronous and the
   asynchronous implementation are compared for nine option combinations, and the
   error paths are covered.
1. ~~`alter_excel_sheet` (complexity 35)~~ — done. The sheet writer, the csv
   writer, the object generation and the relation builder were split into
   helpers; the package has no function above a complexity of 5 any more, and
   the CRAP gate was tightened from 10 to 6.
2. ~~The CI gate~~ — done. `.github/workflows/quality.yml` runs on every push and
   pull request: the coverage, CRAP, complexity, security and dead-code gates
   and the ratchet block a merge, the lint, format and type budgets are
   reported (§16).
3. The 12-argument public methods — introduce a small configuration object
   (`TemplateOptions`) instead of growing the parameter list; keep the old signature
   working as a thin wrapper so the published API does not break.
4. mypy stage 1 (18 errors) → stage 2 (77) → stage 3 `strict` (81).
5. `ruff format` over the package and the real tests — **as its own commit**.
   31 files are waiting for it.
6. The remaining ruff findings, per rule, as separate commits.

### What the last cycle deliberately left alone

- The 12-argument public methods (`PLR0913`/`PLR0917`): changing the published
  signature needs explicit approval (§11.4), so the argument lists stay.
- The two `print()` calls of the progress report (`T201`): they are the only
  feedback the long parallel generation gives, and replacing them is a separate
  decision about the interface of the library.
- The `logging.warning` on the root logger (`LOG015`): a module logger is a
  one-line change, but it changes what a caller sees in its logs.
- The formatting debt of the 31 files (plan item 4) and the mypy stages
  (plan item 3): separate commits, by design (§11.2, §11.3).
- The lint, format and type budgets of 171, 31 and 18 findings: the CI reports
  them but does not block on them yet (§16). Each of them becomes blocking when
  its budget reaches zero.

---


## 19. Using this bundle in another repository

The bundle is designed to be copied. This section is the checklist for doing that.

### Copy as-is, no edits

| File | Why it is portable |
|---|---|
| `code_quality/scripts/crap_scores.py` | every path is derived from `__file__`; the package, the coverage report and the churn window are CLI arguments. Falls back to `uvx radon` when radon is not installed. |
| `code_quality/scripts/qa_report.py` | same; the project name in the report title is read from `pyproject.toml`. The thresholds in `DEFAULT_THRESHOLDS` are the ones of the repository it was written for — every one of them has a CLI flag (`--max-crap`, `--max-complexity`, `--coverage-min`, `--coverage-branch-min`), or you edit the constant. |
| `code_quality/PY-ANTI-PATTERNS.md` | documentation only, no repository specifics. |

### Copy and edit these values

| File | What to change |
|---|---|
| `code_quality/coverage.cfg` | `source = <package>` and the `omit` list (drop the vendored-model entry if there is none). |
| `code_quality/ci/quality.yml` | the four path arguments (`otlmow_modelbuilder`, `UnitTests`), the Python version, the tool pins (`ruff==…`, `mypy<2`) and the list of gates that block the merge in the `--fail-on` step. |
| `code_quality/README.md` | §4.1/§6 config blocks; delete §18 (the measured baseline) and §20 (the test analysis of this repository) and write your own. |
| `pyproject.toml` | `[tool.ruff*]`, `[tool.mypy]`: the `src`, `extend-exclude` and `per-file-ignores` paths. |

### Do not copy

`code_quality/QA-REPORT.md` and `code_quality/reports/` — they are generated.
Running the script recreates them.

### Verify after copying

```bash
python -m pytest --cov=<package> --cov-report=json:code_quality/reports/coverage.json -q
python code_quality/scripts/crap_scores.py --source <package>
python code_quality/scripts/qa_report.py --source <package> --tests <tests>
```

The first two commands must print a CRAP table; the third must print the eight
metrics and write `QA-REPORT.md`. If `radon` is missing, the CRAP table comes back
empty — install it (`uv pip install radon`) or let the script use `uvx radon`.

---

## 20. Test sufficiency analysis (this repository, 2026-10-20)

A gate can only be switched on when the tests can actually *detect* a defect.
This section records what the test suite could not detect, and what was added to
close the gaps. It is the evidence behind the order of work in §18.3.

### 20.1 What the suite could not detect

| Gap | Evidence | Consequence |
|---|---|---|
| **The generated template is not reproducible.** The dummy values come from `random` inside `otlmow_model`, the sheet and column order depend on the order in which the parallel generation finishes, and the model picks a random branch of a union type. | Two runs of the same input produce different workbooks — different values, different column order, different union columns. | No golden-file test was possible, so a refactor could change the whole template without a single test failing. |
| **The asynchronous implementation was barely tested.** It is a copy of the synchronous one. | `ignore_relations`, `abbreviate_excel_sheettitles`, `add_deprecated`, `add_attribute_info`, `filter_attributes_by_subset` and `generate_choice_list` were never exercised asynchronously; the relation branch of the async path was unreachable in the suite. | The two copies could drift apart silently. The async one would have produced a template without relations. |
| **The error and guard paths were untested.** | 41 statements and 48 branches were never executed, including every `raise` that guards a bad input and every path that swallows a problem. | A changed guard, a changed message or a swallowed defect was invisible. The swallowing paths are the dangerous ones: they turn a defect into a template that looks fine. |
| **Coverage was measured on lines only.** | 91.1 % line coverage but only **78.2 %** branch coverage. | The gate would have passed on the comfortable number. |
| **The assertions were shallow.** | Most assertions check a header list or that a file exists (`assert excel_path.exists()`); nothing verified which cells are filled, which data validations are attached or what the choice lists contain. | The most user-visible parts of the template — the choice lists and the dropdown validations — were not verified at all. |

### 20.2 What was added

| File | What it does |
|---|---|
| `UnitTests/Subset/template_snapshot.py` | Normalises a generated workbook into a comparable snapshot: the random values become type markers, the choice-list columns are sorted, the union columns are collapsed. The result is stable across runs. |
| `UnitTests/Subset/snapshots/OTL_AllCasesTestClass.structure.json` | The golden structure of the generated template. Regenerate with `UPDATE_GOLDEN=1 python -m pytest UnitTests/Subset/SubsetTemplateCreator_structure_test.py`. |
| `UnitTests/Subset/SubsetTemplateCreator_structure_test.py` | Behaviour preservation: the generated template must keep its structure, the generation must be reproducible, every asset sheet must have its `typeURI` column, the choice lists and the data validations must be present. |
| `UnitTests/Subset/SubsetTemplateCreator_parity_test.py` | The synchronous and the asynchronous implementation must produce the same template, for nine option combinations. |
| `UnitTests/Subset/SubsetTemplateCreator_guard_test.py` | The error paths: an empty class filter, a sheet title without a namespace, a duplicate choice-list column, an unknown attribute in a csv, a sheet without a matching instance. |
| `UnitTests/Subset/SubsetTemplateCreator_helpers_test.py` | The paths that *skip* something: a column without a header, the asset id of the agent sheet, a sheet title that is only the beginning of the type uri, and the lookup of the standard unit of a datatype. |

### 20.3 The numbers now

| Metric | Before | After |
|---|---:|---:|
| tests | 216 | 249 |
| line coverage | 91.1 % | **98.7 %** |
| branch coverage | 78.2 % | **90.4 %** |
| uncovered statements | 41 | 8 |
| uncovered branches | 48 | 21 |

The remaining uncovered code is the parallel retry loop (the duplicate-asset-id
detection) and a few edge cases of the relation builder — all of them need a
fixture that reproduces the failure, which is the next cycle's work.

Branch coverage is now measured (`branch = true` in `code_quality/coverage.cfg`)
and gated separately from the line coverage.
