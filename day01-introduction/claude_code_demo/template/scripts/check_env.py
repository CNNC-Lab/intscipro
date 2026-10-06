"""Cheap environment check: imports, data presence, expected shape. Takes seconds."""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ["numpy", "pandas", "scipy", "statsmodels", "sklearn", "matplotlib", "seaborn", "markdown"]

missing = []
for name in PACKAGES:
    try:
        module = importlib.import_module(name)
        print(f"ok   {name} {getattr(module, '__version__', '')}")
    except ImportError:
        missing.append(name)
        print(f"MISSING {name}")

data = ROOT / "data" / "raw" / "Data_Cortex_Nuclear.csv"
if data.exists():
    import pandas as pd

    df = pd.read_csv(data)
    print(f"ok   data {data.relative_to(ROOT)} shape={df.shape}")
else:
    missing.append(str(data.relative_to(ROOT)))
    print(f"MISSING {data.relative_to(ROOT)}  (run scripts/fetch_data.py once, then commit it)")

sys.exit(1 if missing else 0)
