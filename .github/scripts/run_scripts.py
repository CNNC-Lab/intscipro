"""Run every example and solution script headless and report failures.

Scripts that read from the keyboard (``input(``) are skipped. Each script runs from
its own folder, so relative paths behave as they do for students.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TIMEOUT_S = 300
PATTERNS = ["day*/solutions/*.py", "day*/examples/*.py", "day01-introduction/demo_scripts/neuron_analysis.py"]
SKIP_NAMES = {"_setup.py", "__init__.py"}

env = {**os.environ, "MPLBACKEND": "Agg"}
failures = []
ran = 0
for pattern in PATTERNS:
    for script in sorted(ROOT.glob(pattern)):
        text = script.read_text(encoding="utf-8")
        if script.name in SKIP_NAMES or "input(" in text or script.name.startswith("test_"):
            continue
        ran += 1
        try:
            result = subprocess.run(
                [sys.executable, script.name], cwd=script.parent, env=env,
                stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=TIMEOUT_S,
            )
            if result.returncode != 0:
                failures.append((script, result.stderr.strip().splitlines()[-1:] or ["non-zero exit"]))
        except subprocess.TimeoutExpired:
            failures.append((script, [f"timed out after {TIMEOUT_S}s"]))

print(f"Ran {ran} scripts, {len(failures)} failed")
for script, message in failures:
    print(f"FAIL {script.relative_to(ROOT)}: {message[0]}")
sys.exit(1 if failures else 0)
