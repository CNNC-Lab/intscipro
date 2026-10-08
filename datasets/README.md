# Datasets

Small datasets shared across sessions. Anything a script or notebook generates is written to a git-ignored `outputs/` folder, never here.

## `sample_neuron_data.csv`

A small **synthetic** table of single-neuron recordings, used in the Day 1 AI-assisted coding demo and the README quick start. 27 neurons (9 per hippocampal subregion, 3 per condition within each).

| Column | Description | Unit |
|--------|-------------|------|
| `neuron_id` | Unique neuron identifier | – |
| `condition` | Experimental condition: `control`, `drug_A`, `drug_B` | – |
| `spike_count` | Spikes recorded in the recording window | count |
| `isi_mean` | Mean inter-spike interval | ms |
| `isi_std` | Standard deviation of the inter-spike interval | ms |
| `burst_frequency` | Bursts per minute | 1/min |
| `membrane_potential` | Resting membrane potential | mV |
| `treatment` | Applied treatment (`saline` for control) | – |
| `recording_duration` | Length of the recording window | s |
| `brain_region` | Hippocampal subregion: `CA1`, `CA3`, `DG` | – |

## Other datasets

Later days generate synthetic data inside the notebooks or use small files stored next to them (for example `day05-data/notebooks/example_data.csv` and `gene_expression.xlsx`). The Day 1 Claude Code demo uses a real dataset that ships inside the `scanpy` package, so nothing needs to be downloaded; see [`day01-introduction/claude_code_demo/`](../day01-introduction/claude_code_demo/).
