# Day 1 AI-Assisted Coding Demonstration: Simple Example

## Scenario: First Look at Neuron Recording Data

**Context**: You've just received electrophysiological data from hippocampal neurons recorded under different pharmacological conditions. You want to quickly explore the data to understand what you're working with.

---

## Demonstration 1: ChatGPT/Generic AI Chat

### The Prompt:
```
I have a CSV file with neuron recording data. The file contains columns for:
- neuron_id: unique identifier for each neuron
- condition: experimental condition (control, drug_A, drug_B)
- spike_count: number of spikes recorded in 5-minute period
- isi_mean: mean inter-spike interval in milliseconds
- isi_std: standard deviation of inter-spike intervals
- burst_frequency: bursts per minute
- membrane_potential: resting membrane potential in mV
- treatment: specific treatment applied
- recording_duration: duration in seconds
- brain_region: hippocampal subregion (CA1, CA3, DG)

Can you help me:
1. Load and examine the basic structure of this data
2. Create some basic summary statistics
3. Make a few plots to visualize the key differences between conditions

The file is called 'sample_neuron_data.csv' and is stored in the folder 'datasets'
```

### Expected AI Response and Code:
The AI will typically provide something like:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
data = pd.read_csv('sample_neuron_data.csv')

# Basic data exploration
print("Dataset shape:", data.shape)
print("\nFirst few rows:")
print(data.head())

print("\nData types:")
print(data.dtypes)

print("\nBasic statistics:")
print(data.describe())

# Summary by condition
print("\nSummary by condition:")
summary = data.groupby('condition').agg({
    'spike_count': ['mean', 'std', 'count'],
    'isi_mean': ['mean', 'std'],
    'burst_frequency': ['mean', 'std'],
    'membrane_potential': ['mean', 'std']
}).round(2)
print(summary)

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Spike count comparison
sns.boxplot(data=data, x='condition', y='spike_count', ax=axes[0,0])
axes[0,0].set_title('Spike Count by Condition')

# ISI mean comparison
sns.boxplot(data=data, x='condition', y='isi_mean', ax=axes[0,1])
axes[0,1].set_title('Mean Inter-Spike Interval by Condition')

# Burst frequency comparison
sns.boxplot(data=data, x='condition', y='burst_frequency', ax=axes[1,0])
axes[1,0].set_title('Burst Frequency by Condition')

# Membrane potential comparison
sns.boxplot(data=data, x='condition', y='membrane_potential', ax=axes[1,1])
axes[1,1].set_title('Membrane Potential by Condition')

plt.tight_layout()
plt.show()

# Additional analysis: correlation matrix
plt.figure(figsize=(10, 8))
correlation_matrix = data.select_dtypes(include=[np.number]).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Neuronal Parameters')
plt.show()
```

---

## What you will learn:

### 1. **The Power of Clear Communication**
- Notice how specific the prompt was
- The AI understood the scientific context
- Clear column descriptions led to appropriate analysis choices

### 2. **AI's Scientific Intuition**
- AI automatically chose appropriate statistical summaries
- Selected relevant visualizations (boxplots for comparing groups)
- Included correlation analysis without being explicitly asked

### 3. **Code Structure**
- Logical flow: load → explore → summarize → visualize
- Proper imports at the top
- Clear comments explaining each step

### 4. **What to Watch For**
- AI might make assumptions about your data
- Always verify the code makes sense for your specific dataset
- Check that file paths and column names match exactly

---

## Next: from a chat assistant to an agent

In this demo you copied code from a chat window, ran it yourself and checked it. In the [Claude Code demo](claude_code_demo/README.md) an AI agent does the whole loop: it plans, writes and runs the code on a real dataset, and produces a report, while we direct it and verify the result.
