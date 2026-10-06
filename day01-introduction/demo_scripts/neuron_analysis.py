from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(REPO_ROOT / "datasets" / "sample_neuron_data.csv")

# Basic structure
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

# Summary statistics by condition
print("\n=== SUMMARY BY CONDITION ===")
summary = df.groupby('condition')[['spike_count', 'isi_mean', 'burst_frequency', 'membrane_potential']].agg(['mean', 'std', 'count'])
print(summary)

# Visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Spike count by condition
sns.boxplot(data=df, x='condition', y='spike_count', ax=axes[0,0])
axes[0,0].set_title('Spike Count by Condition')
axes[0,0].set_ylabel('Spike Count (5 min)')

# 2. ISI mean by condition
sns.violinplot(data=df, x='condition', y='isi_mean', ax=axes[0,1])
axes[0,1].set_title('Inter-Spike Interval by Condition')
axes[0,1].set_ylabel('ISI Mean (ms)')

# 3. Burst frequency by condition and brain region
sns.barplot(data=df, x='condition', y='burst_frequency', hue='brain_region', ax=axes[1,0])
axes[1,0].set_title('Burst Frequency by Condition & Region')
axes[1,0].set_ylabel('Bursts/min')

# 4. Membrane potential distribution
for condition in df['condition'].unique():
    subset = df[df['condition'] == condition]
    axes[1,1].hist(subset['membrane_potential'], alpha=0.5, label=condition, bins=15)
axes[1,1].set_title('Membrane Potential Distribution')
axes[1,1].set_xlabel('Membrane Potential (mV)')
axes[1,1].set_ylabel('Count')
axes[1,1].legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'neuron_analysis.png', dpi=300)
plt.show()

# Additional: correlation matrix for numeric variables
numeric_cols = ['spike_count', 'isi_mean', 'isi_std', 'burst_frequency', 'membrane_potential']
corr = df[numeric_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'correlation_matrix.png', dpi=300)
plt.show()
