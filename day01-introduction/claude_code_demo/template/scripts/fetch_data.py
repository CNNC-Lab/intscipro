"""Download the Mice Protein Expression dataset and validate it.

Source: UCI Machine Learning Repository, dataset 342 (CC BY 4.0).
Higuera C, Gardiner KJ, Cios KJ. Self-organizing feature maps identify proteins
critical to learning in a mouse model of Down syndrome. PLoS ONE 10(6): e0129126.

Run this ONCE on a machine with open internet access, then commit the files in
data/raw/. The analysis session itself never needs the network.

    python scripts/fetch_data.py
"""
import hashlib
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
XLS_NAME = "Data_Cortex_Nuclear.xls"
CSV_NAME = "Data_Cortex_Nuclear.csv"
URLS = [
    "https://archive.ics.uci.edu/static/public/342/mice+protein+expression.zip",
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00342/Data_Cortex_Nuclear.xls",
]
EXPECTED_ROWS = 1080
EXPECTED_COLUMNS = 82
EXPECTED_MICE = 72
EXPECTED_CLASSES = {"c-CS-s", "c-CS-m", "c-SC-s", "c-SC-m", "t-CS-s", "t-CS-m", "t-SC-s", "t-SC-m"}


def download() -> bytes:
    """Return the raw bytes of the .xls file, trying each known URL in turn."""
    for url in URLS:
        try:
            print(f"Trying {url}")
            with urllib.request.urlopen(url, timeout=60) as response:
                payload = response.read()
        except OSError as err:
            print(f"  failed: {err}")
            continue
        if url.endswith(".zip"):
            with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                member = next(n for n in archive.namelist() if n.lower().endswith(".xls"))
                return archive.read(member)
        return payload
    sys.exit("Could not download the dataset from any known URL.")


def validate(df: pd.DataFrame) -> None:
    """Fail loudly if the file is not the dataset the analysis expects."""
    assert df.shape == (EXPECTED_ROWS, EXPECTED_COLUMNS), f"unexpected shape {df.shape}"
    for column in ("MouseID", "Genotype", "Treatment", "Behavior", "class"):
        assert column in df.columns, f"missing column {column}"
    assert set(df["class"].unique()) == EXPECTED_CLASSES, "unexpected class labels"
    n_mice = df["MouseID"].str.split("_").str[0].nunique()
    print(f"Distinct mice (MouseID prefix): {n_mice} (expected {EXPECTED_MICE})")
    print(f"Missing values: {int(df.isna().sum().sum())} cells in {int(df.isna().any().sum())} columns")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    xls_bytes = download()
    xls_path = RAW_DIR / XLS_NAME
    xls_path.write_bytes(xls_bytes)
    print(f"Saved {xls_path}  sha256={hashlib.sha256(xls_bytes).hexdigest()}")

    df = pd.read_excel(xls_path)  # needs xlrd for .xls files
    validate(df)
    csv_path = RAW_DIR / CSV_NAME
    df.to_csv(csv_path, index=False)
    print(f"Saved {csv_path} ({len(df)} rows, {df.shape[1]} columns)")


if __name__ == "__main__":
    main()
