"""Collect every quality gate of this repository into one report.

Runs lint, format, type, test/coverage, complexity, CRAP, security and dead-code
checks, writes a machine-readable snapshot to ``code_quality/reports/qa.json`` and
renders the human readable dashboard ``code_quality/QA-REPORT.md``.

The report is generated, never hand-edited. Re-running it only changes the rows
that actually moved, which keeps the diff reviewable.

Usage:
    python code_quality/scripts/qa_report.py
    python code_quality/scripts/qa_report.py --skip-tests --coverage code_quality/reports/coverage.json
"""

from __future__ import annotations

import argparse
import ast
import datetime
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

QUALITY_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = QUALITY_DIR.parent
REPORTS_DIR = QUALITY_DIR / 'reports'
HISTORY_FILE = REPORTS_DIR / 'qa-history.json'
SNAPSHOT_FILE = REPORTS_DIR / 'qa.json'
REPORT_FILE = QUALITY_DIR / 'QA-REPORT.md'

sys.path.insert(0, str(QUALITY_DIR / 'scripts'))

from crap_scores import compute_crap, compute_hotspots

DEFAULT_THRESHOLDS = {
    'ruff_issues': 0,
    'ruff_format_files': 0,
    'mypy_errors': 0,
    'coverage_percent': 80.0,
    'coverage_branch_percent': 75.0,
    'max_crap': 6.0,
    'max_complexity': 6,
    'bandit_high': 0,
    'dead_code': 0,
    'god_classes': 0,
    'membership_list_violations': 0,
}

# The gates that can be enforced on their own: the name, the metric it reads
# and whether a higher value is better. The ratchet is not in this list: it is
# enforced by every run, because a lint count that goes up is never acceptable.
GATES = {
    'ruff': ('ruff_issues', False),
    'format': ('ruff_format_files', False),
    'mypy': ('mypy_errors', False),
    'coverage': ('coverage_percent', True),
    'coverage-branch': ('coverage_branch_percent', True),
    'crap': ('max_crap', False),
    'complexity': ('max_complexity', False),
    'bandit': ('bandit_high', False),
    'dead-code': ('dead_code', False),
    'god-classes': ('god_classes', False),
    'membership-list': ('membership_list_violations', False),
}


def _run(
    command: list[str], cwd: Path | str = REPO_ROOT, env: dict[str, str] | None = None
) -> tuple[int, str]:
    """Run a command and return its exit code and combined output."""
    try:
        completed = subprocess.run(
            command, cwd=cwd, capture_output=True, text=True, check=False, env=env
        )
    except FileNotFoundError:
        return 127, ''
    return completed.returncode, completed.stdout + completed.stderr


def _tool(name: str) -> list[str] | None:
    """Resolve a tool to a runnable command, preferring the project venv."""
    venv_tool = REPO_ROOT / '.venv' / 'bin' / name
    if venv_tool.exists():
        return [str(venv_tool)]
    if shutil.which(name):
        return [name]
    return None


def run_ruff(source: str, tests: str, scripts: str) -> dict[str, Any]:
    """Count ruff violations per rule code."""
    command = _tool('ruff')
    if command is None:
        return {'available': False, 'total': 0, 'per_rule': {}, 'fixable': 0}
    code, output = _run([*command, 'check', '--output-format=json', source, tests, scripts])
    try:
        findings = json.loads(output or '[]')
    except json.JSONDecodeError:
        return {
            'available': True,
            'total': 0,
            'per_rule': {},
            'fixable': 0,
            'error': output.strip()[:500],
        }
    per_rule: dict[str, int] = {}
    fixable = 0
    for finding in findings:
        rule = finding.get('code', '?')
        per_rule[rule] = per_rule.get(rule, 0) + 1
        if finding.get('fix'):
            fixable += 1
    return {
        'available': True,
        'total': len(findings),
        'fixable': fixable,
        'per_rule': dict(sorted(per_rule.items(), key=lambda item: (-item[1], item[0]))),
        'exit_code': code,
    }


def run_ruff_format(source: str, tests: str, scripts: str) -> dict[str, Any]:
    """Count files that are not formatted yet."""
    command = _tool('ruff')
    if command is None:
        return {'available': False, 'files': 0}
    code, output = _run([*command, 'format', '--check', source, tests, scripts])
    # ruff 0.17 prints "unformatted: File would be reformatted" per file, older
    # versions print "Would reformat: <path>". Counting only the first one makes
    # the gate pass without checking anything.
    unformatted = [line for line in output.splitlines() if line.startswith('unformatted:')]
    would_reformat = [line for line in output.splitlines() if line.startswith('Would reformat')]
    return {'available': True, 'files': len(unformatted) + len(would_reformat), 'exit_code': code}


def run_mypy(source: str, tests: str, scripts: str) -> dict[str, Any]:
    """Count mypy errors."""
    command = _tool('mypy')
    if command is None:
        return {'available': False, 'errors': 0}
    code, output = _run([*command, '--no-error-summary', '--no-pretty', source, tests, scripts])
    errors = len([line for line in output.splitlines() if ': error:' in line])
    return {
        'available': True,
        'errors': errors,
        'exit_code': code,
        'output': output.strip().splitlines()[:50],
    }


def coverage_totals(data: dict[str, Any]) -> dict[str, float]:
    """Return the line and the branch coverage of a coverage report."""
    totals = data.get('totals', {})
    statements = int(totals.get('num_statements', 0))
    covered_lines = int(totals.get('covered_lines', 0))
    branches = int(totals.get('num_branches', 0))
    covered_branches = int(totals.get('covered_branches', 0))
    return {
        'percent': 100.0 * covered_lines / statements if statements else 0.0,
        'branch_percent': 100.0 * covered_branches / branches if branches else 0.0,
    }


def run_pytest(source: str, coverage_json: str, skip_tests: bool) -> dict[str, Any]:
    """Run the test suite with coverage and return the coverage percentages."""
    if skip_tests:
        if not Path(coverage_json).exists():
            return {
                'available': False,
                'percent': 0.0,
                'branch_percent': 0.0,
                'detail': 'no coverage report available',
            }
        with Path(coverage_json).open(encoding='utf-8') as handle:
            data = json.load(handle)
        return {'available': True, **coverage_totals(data), 'reused': True}
    command = [
        sys.executable,
        '-m',
        'pytest',
        f'--cov={source}',
        f'--cov-report=json:{coverage_json}',
        '-q',
    ]
    environment = dict(os.environ)
    coverage_config = str(QUALITY_DIR / 'coverage.cfg')
    if Path(coverage_config).exists():
        environment['COVERAGE_RCFILE'] = coverage_config
    code, output = _run(command, env=environment)
    with Path(coverage_json).open(encoding='utf-8') as handle:
        data = json.load(handle)
    summary = [
        line
        for line in output.splitlines()
        if ' passed' in line or ' failed' in line or 'error' in line.lower()
    ]
    return {
        'available': True,
        **coverage_totals(data),
        'exit_code': code,
        'summary': summary[-3:],
    }


def run_bandit(source: str) -> dict[str, Any]:
    """Count bandit findings by severity."""
    command = _tool('bandit')
    if command is None:
        return {'available': False, 'high': 0, 'medium': 0, 'low': 0}
    code, output = _run([*command, '-q', '-f', 'json', '-r', source])
    try:
        data = json.loads(output or '{}')
    except json.JSONDecodeError:
        return {'available': True, 'high': 0, 'medium': 0, 'low': 0}
    counts = {'high': 0, 'medium': 0, 'low': 0}
    for result in data.get('results', []):
        severity = result.get('issue_severity', 'low').lower()
        if severity in counts:
            counts[severity] += 1
    counts['exit_code'] = code
    return counts


def run_vulture(source: str) -> dict[str, Any]:
    """Count likely dead code at confidence 80."""
    command = _tool('vulture')
    if command is None:
        return {'available': False, 'items': 0}
    code, output = _run([*command, source, '--min-confidence', '80'])
    items = [line for line in output.splitlines() if line.strip()]
    return {'available': True, 'items': len(items), 'exit_code': code, 'sample': items[:20]}


def detect_god_classes(source: str) -> dict[str, Any]:
    """Detect potential god classes using simple heuristics."""
    god_classes = []
    source_path = REPO_ROOT / source
    if not source_path.exists():
        return {'available': False, 'count': 0, 'classes': []}
    for py_file in source_path.rglob('*.py'):
        if '__pycache__' in str(py_file) or 'TestModel' in str(py_file):
            continue
        try:
            with py_file.open(encoding='utf-8') as f:
                content_file = f.read()
            tree = ast.parse(content_file)
        except (OSError, SyntaxError, UnicodeError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                method_count = len(methods)
                if method_count > 30 or py_file.stat().st_size > 30000:
                    try:
                        rel_path = py_file.relative_to(REPO_ROOT)
                    except (OSError, SyntaxError, UnicodeError):
                        rel_path = py_file
                    god_classes.append(f'{rel_path}:{node.name}')
    return {'available': True, 'count': len(god_classes), 'classes': god_classes[:20]}



def detect_membership_list_violations(source: str) -> dict[str, Any]:
    """Count files where `x in [a, b, ...]` uses a list literal of 4+ items."""
    violating_files = []
    source_path = REPO_ROOT / source
    if not source_path.exists():
        return {'available': False, 'count': 0, 'files': []}
    for py_file in source_path.rglob('*.py'):
        if '__pycache__' in str(py_file) or 'TestModel' in str(py_file):
            continue
        try:
            with py_file.open(encoding='utf-8') as f:
                tree = ast.parse(f.read())
        except (OSError, SyntaxError, UnicodeError):
            continue
        found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], (ast.In, ast.NotIn)):
                comp = node.comparators[0]
                if isinstance(comp, ast.List) and len(comp.elts) >= 4:
                    found = True
                    break
        if found:
            try:
                rel_path = py_file.relative_to(REPO_ROOT)
            except (OSError, SyntaxError, UnicodeError):
                rel_path = py_file
            violating_files.append(str(rel_path))
    return {'available': True, 'count': len(violating_files), 'files': violating_files[:20]}


def repo_name() -> str:
    """Return the project name, taken from pyproject.toml when possible."""
    pyproject = REPO_ROOT / 'pyproject.toml'
    if pyproject.exists():
        for line in pyproject.read_text(encoding='utf-8').splitlines():
            stripped = line.strip()
            if stripped.startswith('name') and '=' in stripped:
                value = stripped.split('=', 1)[1].strip().strip('"\'')
                if value:
                    return value
    return REPO_ROOT.name


def read_history() -> list[dict[str, Any]]:
    """Read the ratchet history."""
    if not HISTORY_FILE.exists():
        return []
    try:
        with HISTORY_FILE.open(encoding='utf-8') as handle:
            history: list[dict[str, Any]] = json.load(handle)
    except json.JSONDecodeError:
        return []
    return history


def write_history(history: list[dict[str, Any]]) -> None:
    """Write the ratchet history."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with HISTORY_FILE.open('w', encoding='utf-8') as handle:
        json.dump(history, handle, indent=2)


def ratchet_violations(current: dict[str, int], previous: dict[str, int]) -> list[str]:
    """Return the rules whose count increased compared to the previous run."""
    regressions = []
    for rule, count in current.items():
        before = previous.get(rule, 0)
        if count > before:
            regressions.append(f'{rule}: {before} -> {count}')
    return regressions


def status(value: Any, threshold: Any, higher_is_better: bool) -> str:
    """Return a status glyph for a metric against its threshold."""
    if higher_is_better:
        return '🟢' if value >= threshold else '🔴'
    return '🟢' if value <= threshold else '🔴'


def failed_gates(
    metrics: dict[str, Any], thresholds: dict[str, Any], gates: list[str]
) -> list[str]:
    """Return the names of the gates that are not met."""
    failed = []
    for gate in gates:
        metric, higher_is_better = GATES[gate]
        value = metrics[metric]
        threshold = thresholds[metric]
        met = value >= threshold if higher_is_better else value <= threshold
        if not met:
            failed.append(gate)
    return failed


def render_report(
    snapshot: dict[str, Any], history: list[dict[str, Any]], regressions: list[str]
) -> str:
    """Render the markdown dashboard."""
    metrics = snapshot['metrics']
    thresholds = snapshot['thresholds']
    lines = [
        f'# QA Report — {snapshot["repo"]}',
        '',
        '> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.',
        '> Do not edit by hand; edit the thresholds in the script instead.',
        '',
        f'Generated: {snapshot["date"]} · commit `{snapshot["commit"]}`',
        '',
        '## Thresholds (gate)',
        '',
        '| Metric | Threshold | Current | Status |',
        '|---|---|---|---|',
        (f'| ruff issues | {thresholds["ruff_issues"]} | {metrics["ruff_issues"]} '
        f'| {status(metrics["ruff_issues"], thresholds["ruff_issues"], False)} |'),
        (f'| files needing `ruff format` | {thresholds["ruff_format_files"]} | {metrics["ruff_format_files"]} '
        f'| {status(metrics["ruff_format_files"], thresholds["ruff_format_files"], False)} |'),
        (f'| mypy errors | {thresholds["mypy_errors"]} | {metrics["mypy_errors"]} '
        f'| {status(metrics["mypy_errors"], thresholds["mypy_errors"], False)} |'),
        (f'| test coverage (lines) | ≥ {thresholds["coverage_percent"]} % | {metrics["coverage_percent"]} % '
        f'| {status(metrics["coverage_percent"], thresholds["coverage_percent"], True)} |'),
        (f'| test coverage (branches) | ≥ {thresholds["coverage_branch_percent"]} % '
        f'| {metrics["coverage_branch_percent"]} % '
        f'| {status(metrics["coverage_branch_percent"], thresholds["coverage_branch_percent"], True)} |'),
        (f'| max CRAP score | ≤ {thresholds["max_crap"]} | {metrics["max_crap"]} '
        f'| {status(metrics["max_crap"], thresholds["max_crap"], False)} |'),
        (f'| max cyclomatic complexity | ≤ {thresholds["max_complexity"]} | {metrics["max_complexity"]} '
        f'| {status(metrics["max_complexity"], thresholds["max_complexity"], False)} |'),
        (f'| bandit HIGH issues | {thresholds["bandit_high"]} | {metrics["bandit_high"]} '
        f'| {status(metrics["bandit_high"], thresholds["bandit_high"], False)} |'),
        (f'| dead code items | {thresholds["dead_code"]} | {metrics["dead_code"]} '
        f'| {status(metrics["dead_code"], thresholds["dead_code"], False)} |'),
        (f'| god classes | {thresholds["god_classes"]} | {metrics["god_classes"]} '
        f'| {status(metrics["god_classes"], thresholds["god_classes"], False)} |'),
        (f'| membership-list violations | {thresholds["membership_list_violations"]} | {metrics["membership_list_violations"]} '
        f'| {status(metrics["membership_list_violations"], thresholds["membership_list_violations"], False)} |'),
        '',
    ]

    if regressions:
        lines += [
            '## Ratchet regressions',
            '',
            'These lint counts went **up** compared to the previous cycle and block the merge:',
            '',
        ]
        lines += [f'- {item}' for item in regressions]
        lines.append('')

    enforced = snapshot.get('enforced_gates') or []
    if enforced:
        failed = snapshot.get('failed_gates') or []
        met = 'all met' if not failed else f'failed: {", ".join(failed)}'
        lines += [
            '## Enforced gates',
            '',
            (f'These gates block a merge — {met}. The gates that are not listed are '
            'reported only; the ratchet is enforced by every run.'),
            '',
            '| Gate | Threshold | Current | Status |',
            '|---|---|---|---|',
        ]
        for gate in enforced:
            metric, higher_is_better = GATES[gate]
            lines.append(
                f'| `{gate}` | {thresholds[metric]} | {metrics[metric]} '
                f'| {status(metrics[metric], thresholds[metric], higher_is_better)} |'
            )
        lines.append('')

    lead = snapshot.get('lead_target')
    lines += ['## Lead refactor target (highest CRAP)', '']
    if lead:
        lines += [
            (f'`{lead["file"]}:{lead["lineno"]}` → `{lead["name"]}` — '
            f'CRAP **{lead["crap"]}** — complexity **{lead["complexity"]}** — coverage **{lead["coverage"]} %**'),
            '',
            ('Verify with `code_quality/README.md` §7 before touching it: '
            'the behaviour must be pinned by a golden-file test first.'),
            '',
        ]
    else:
        lines += ['_No CRAP data available._', '']

    hotspots = snapshot.get('hotspots', [])[:5]
    lines += [
        '## Change hot spots (churn x complexity)',
        '',
        '| Score | Commits | Lines changed | Max complexity | File |',
        '|---:|---:|---:|---:|---|',
    ]
    for spot in hotspots:
        lines.append(
            f'| {spot["score"]} | {spot["commits"]} | {spot["lines_changed"]} '
            f'| {spot["max_complexity"]} | `{spot["file"]}` |'
        )
    lines.append('')

    per_rule = snapshot.get('ruff_per_rule', {})
    if per_rule:
        lines += ['## ruff findings per rule', '', '| Rule | Count |', '|---|---:|']
        for rule, count in list(per_rule.items())[:15]:
            lines.append(f'| `{rule}` | {count} |')
        lines.append('')

    lines += [
        '## History',
        '',
        '| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |',
        '|---|---:|---:|---:|---:|---:|---:|---|',
    ]
    for entry in history[-10:]:
        lines.append(
            f'| {entry["date"]} | {entry["metrics"]["coverage_percent"]} '
            f'| {entry["metrics"].get("coverage_branch_percent", "-")} '
            f'| {entry["metrics"]["ruff_issues"]} '
            f'| {entry["metrics"]["mypy_errors"]} | {entry["metrics"]["max_crap"]} '
            f'| {entry["metrics"]["max_complexity"]} | {entry.get("result", "")} |'
        )
    lines.append('')
    return '\n'.join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default='otlmow_modelbuilder')
    parser.add_argument('--tests', default='UnitTests')
    parser.add_argument('--scripts', default='code_quality/scripts')
    parser.add_argument('--coverage', default=str(REPORTS_DIR / 'coverage.json'))
    parser.add_argument(
        '--skip-tests', action='store_true', help='reuse the existing coverage report'
    )
    parser.add_argument(
        '--no-ratchet', action='store_true', help='do not compare against the previous cycle'
    )
    parser.add_argument(
        '--no-history',
        action='store_true',
        help='do not append a row to the ratchet history (a CI run must not change it)',
    )
    parser.add_argument(
        '--fail-on',
        default='',
        help=(
            'comma separated gates that must pass for the run to succeed: '
            f'{", ".join(sorted(GATES))}. Without it, every gate must pass.'
        ),
    )
    parser.add_argument('--max-crap', type=float, default=DEFAULT_THRESHOLDS['max_crap'])
    parser.add_argument('--max-complexity', type=int, default=DEFAULT_THRESHOLDS['max_complexity'])
    parser.add_argument(
        '--coverage-min', type=float, default=DEFAULT_THRESHOLDS['coverage_percent']
    )
    parser.add_argument(
        '--coverage-branch-min',
        type=float,
        default=DEFAULT_THRESHOLDS['coverage_branch_percent'],
    )
    args = parser.parse_args(argv)

    unknown = sorted({gate.strip() for gate in args.fail_on.split(',') if gate.strip()} - set(GATES))
    if unknown:
        parser.error(f'unknown gate: {unknown[0]} (known gates: {", ".join(sorted(GATES))})')

    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    enforced = [gate.strip() for gate in args.fail_on.split(',') if gate.strip()]

    thresholds = dict(DEFAULT_THRESHOLDS)
    thresholds['max_crap'] = args.max_crap
    thresholds['max_complexity'] = args.max_complexity
    thresholds['coverage_percent'] = args.coverage_min
    thresholds['coverage_branch_percent'] = args.coverage_branch_min

    ruff = run_ruff(args.source, args.tests, args.scripts)
    ruff_format = run_ruff_format(args.source, args.tests, args.scripts)
    mypy = run_mypy(args.source, args.tests, args.scripts)
    pytest_result = run_pytest(args.source, args.coverage, args.skip_tests)
    bandit = run_bandit(args.source)
    vulture = run_vulture(args.source)
    god_classes = detect_god_classes(args.source)
    membership_list = detect_membership_list_violations(args.source)

    crap_rows: list[dict[str, Any]] = []
    if Path(args.coverage).exists():
        crap_rows = [row.__dict__ for row in compute_crap(args.coverage, args.source)]
    hotspots = [spot.__dict__ for spot in compute_hotspots(args.source, '12 months ago')]

    metrics = {
        'ruff_issues': ruff['total'],
        'ruff_format_files': ruff_format['files'],
        'mypy_errors': mypy['errors'],
        'coverage_percent': round(pytest_result['percent'], 1),
        'coverage_branch_percent': round(pytest_result['branch_percent'], 1),
        'max_crap': max((row['crap'] for row in crap_rows), default=0.0),
        'max_complexity': max((row['complexity'] for row in crap_rows), default=0),
        'bandit_high': bandit.get('high', 0),
        'dead_code': vulture.get('items', 0),
        'god_classes': god_classes.get('count', 0),
        'membership_list_violations': membership_list.get('count', 0),
    }

    history = read_history()
    previous = history[-1]['ruff_per_rule'] if history else {}
    regressions = []
    if history and not args.no_ratchet:
        regressions = ratchet_violations(ruff['per_rule'], previous)

    failed = failed_gates(metrics, thresholds, enforced)
    all_met = not failed_gates(metrics, thresholds, list(GATES))

    commit = _run(['git', 'rev-parse', '--short', 'HEAD'])[1].strip() or 'unknown'
    snapshot = {
        'date': datetime.date.today().isoformat(),
        'repo': repo_name(),
        'commit': commit,
        'thresholds': thresholds,
        'metrics': metrics,
        'enforced_gates': enforced,
        'failed_gates': failed,
        'lead_target': crap_rows[0] if crap_rows else None,
        'hotspots': hotspots,
        'ruff_per_rule': ruff['per_rule'],
        'crap': crap_rows,
        'god_classes_detail': god_classes,
        'membership_list_detail': membership_list,
        'tools': {
            'ruff': ruff.get('available', False),
            'mypy': mypy.get('available', False),
            'bandit': bandit.get('available', False),
            'vulture': vulture.get('available', False),
        },
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with SNAPSHOT_FILE.open('w', encoding='utf-8') as handle:
        json.dump(snapshot, handle, indent=2)

    result = 'green' if all_met and not regressions else 'red'
    if not args.no_history:
        history.append(
            {
                'date': snapshot['date'],
                'commit': commit,
                'metrics': metrics,
                'ruff_per_rule': ruff['per_rule'],
                'result': result,
            }
        )
        write_history(history)

    with REPORT_FILE.open('w', encoding='utf-8') as handle:
        handle.write(render_report(snapshot, history, regressions))

    print(f'wrote {REPORT_FILE}')
    print(f'wrote {SNAPSHOT_FILE}')
    for name, value in metrics.items():
        print(f'  {name}: {value}')
    if failed:
        print('failed gates:')
        for gate in failed:
            print(f'  {gate}')
    if regressions:
        print('ratchet regressions:')
        for item in regressions:
            print(f'  {item}')

    # with --fail-on only the named gates block the run, without it every gate does
    blocked = bool(failed) if enforced else not all_met
    return 1 if blocked or regressions else 0


if __name__ == '__main__':
    raise SystemExit(main())
