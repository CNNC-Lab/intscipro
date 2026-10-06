"""Fail if any notebook is committed with outputs or execution counts."""
import json
import sys
from pathlib import Path

bad = []
for path in sorted(Path(".").rglob("*.ipynb")):
    if ".ipynb_checkpoints" in path.parts:
        continue
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code" and (cell.get("outputs") or cell.get("execution_count")):
            bad.append(str(path))
            break

if bad:
    print("Notebooks with outputs (run `pre-commit run nbstripout --all-files`):")
    print("\n".join(f"  {name}" for name in bad))
    sys.exit(1)
print("All notebooks are clean.")
