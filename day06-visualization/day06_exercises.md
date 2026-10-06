# Day 6 Exercises: Visualization & Communication
_PhD Course in Integrative Neurosciences - Introduction to Scientific Programming_

---

## Exercise 1: Multi-Panel Publication Figure (Matplotlib)

### Task
Create a publication-ready multi-panel figure showing neural activity data across different conditions.

### Requirements
1. Create a 2x2 subplot layout (7" x 6")
2. Panel A: Line plot showing neural activity over time for 3 conditions
3. Panel B: Bar plot comparing mean activity across conditions (with error bars)
4. Panel C: Scatter plot showing correlation between two variables
5. Panel D: Histogram showing distribution of firing rates
6. Add panel labels (A, B, C, D)
7. Remove top and right spines
8. Use colorblind-safe colors
9. Export as PDF at 300 DPI

### Data Generation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Generate sample data
time = np.linspace(0, 10, 100)
control = 10 + 3 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, 0.8, 100)
treatment1 = 12 + 4 * np.sin(2 * np.pi * 0.5 * time + 0.3) + np.random.normal(0, 0.8, 100)
treatment2 = 15 + 5 * np.sin(2 * np.pi * 0.5 * time + 0.6) + np.random.normal(0, 0.9, 100)

# Mean activity for bar plot
conditions = ['Control', 'Treatment 1', 'Treatment 2']
means = [np.mean(control), np.mean(treatment1), np.mean(treatment2)]
sems = [stats.sem(control), stats.sem(treatment1), stats.sem(treatment2)]

# Correlation data
var1 = np.random.randn(50) * 2 + 10
var2 = var1 * 0.8 + np.random.randn(50) * 1.5

# Firing rate distribution
firing_rates = np.concatenate([control, treatment1, treatment2])
```

### Hints
- Use `plt.subplots(2, 2, figsize=(7, 6))`
- Use `ax.text(-0.15, 1.1, label, transform=ax.transAxes, ...)` for panel labels
- Use `ax.spines['top'].set_visible(False)` to remove spines
- Use tab10 or colorblind palette
- Use `fig.savefig('figure1.pdf', dpi=300, bbox_inches='tight')`

---

## Exercise 2: Statistical Comparison with Seaborn

### Task
Create a comprehensive statistical visualization comparing reaction times across experimental conditions using Seaborn.

### Requirements
1. Create three separate plots:
   - Violin plot with individual points showing RT by condition and age group
   - Point plot showing means with confidence intervals
   - Pair plot showing relationships between RT, accuracy, age, and condition
2. Use colorblind-safe palette
3. Add appropriate titles and labels
4. Remove legend frames
5. Export as PNG at 600 DPI

### Data Generation

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Generate experimental data
n_subjects = 60

data = pd.DataFrame({
    'subject_id': range(n_subjects),
    'control_rt': np.random.normal(450, 50, n_subjects),
    'drug_rt': np.random.normal(400, 45, n_subjects),
    'age': np.random.randint(20, 65, n_subjects),
    'age_group': np.random.choice(['Young', 'Old'], n_subjects),
    'sex': np.random.choice(['Male', 'Female'], n_subjects),
    'accuracy': np.clip(0.7 + 0.2 * np.random.random(n_subjects), 0, 1)
})

# Convert to long format
data_long = pd.melt(data,
                     id_vars=['subject_id', 'age_group', 'sex', 'age', 'accuracy'],
                     value_vars=['control_rt', 'drug_rt'],
                     var_name='condition',
                     value_name='reaction_time')
data_long['condition'] = data_long['condition'].str.replace('_rt', '').str.capitalize()
```

### Hints
- Use `sns.set_theme(style='whitegrid', palette='colorblind')`
- For violin + points: `sns.violinplot()` then `sns.stripplot()` on same axes
- Use `errorbar='ci'` for confidence intervals
- Use `sns.pairplot(hue='age_group')`

---

## Exercise 3: Interactive Dashboard with Plotly

### Task
Create an interactive dashboard for exploring neural recording data using Plotly.

### Requirements
1. Create a 2x2 subplot layout using `make_subplots()`
2. Panel 1: Interactive scatter plot (trial vs firing rate, colored by condition)
3. Panel 2: Line plot showing average firing rate over time
4. Panel 3: Box plot comparing firing rates across conditions
5. Panel 4: 3D scatter plot (PC1, PC2, PC3 from PCA)
6. Add hover information showing trial number, condition, and neuron ID
7. Export as HTML

### Data Generation

```python
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(42)

# Generate neural data
n_trials = 200

data = pd.DataFrame({
    'trial': range(n_trials),
    'firing_rate': 10 + 5 * np.sin(2 * np.pi * np.arange(n_trials) / 50) + np.random.randn(n_trials) * 2,
    'condition': np.random.choice(['Control', 'Treatment'], n_trials),
    'neuron_id': np.random.choice([f'N{i+1}' for i in range(10)], n_trials),
    'session': np.tile(range(1, 21), n_trials // 20)
})

# PCA coordinates (simulated)
data['PC1'] = np.random.randn(n_trials) * 2
data['PC2'] = np.random.randn(n_trials) * 1.5
data['PC3'] = np.random.randn(n_trials) * 1.2
```

### Hints
- Use `make_subplots(rows=2, cols=2, specs=...)`
- Specify subplot types in specs (e.g., `{'type': 'scatter3d'}`)
- Use `fig.add_trace(go.Scatter(...), row=1, col=1)`
- Use `fig.write_html('dashboard.html')`

---

## Exercise 4: Fixing Bad Visualizations

### Task
The following figure has multiple problems. Identify and fix all issues.

### Problematic Code

```python
import matplotlib.pyplot as plt
import numpy as np

data1 = [98, 99, 100, 101, 99.5]
data2 = [97, 98, 99, 100, 98.5]
categories = ['A', 'B', 'C', 'D', 'E']

fig, ax = plt.subplots(figsize=(6, 4))

# Plot with problems
ax.bar(categories, data1, color='red', label='Group 1')
ax.bar(categories, data2, color='green', alpha=0.5, label='Group 2')
ax.set_ylim(95, 102)  # Truncated axis
ax.set_title('My Data')  # Uninformative title
ax.legend()
plt.show()
```

### Problems to Fix
1. Truncated y-axis (exaggerates differences)
2. Red-green color scheme (not colorblind-safe)
3. Uninformative title
4. Missing axis labels and units
5. Overlapping bars (hard to compare)
6. Legend has frame
7. Top and right spines present

### Task
Rewrite the code to fix all problems and create a publication-quality figure.

---

## Exercise 5: Multi-Dimensional Data Exploration

### Task
You have a dataset with measurements from multiple neurons across different brain regions, conditions, and time points. Create visualizations to explore relationships in the data.

### Requirements
1. Create a FacetGrid showing firing rates by region and condition
2. Create a pairplot showing relationships between firing_rate, synchrony, and variability
3. Create a correlation heatmap
4. Create an interactive 3D plot showing clustering in neural space

### Data Generation

```python
import numpy as np
import pandas as pd

np.random.seed(42)

n_neurons = 150

data = pd.DataFrame({
    'neuron_id': range(n_neurons),
    'region': np.random.choice(['V1', 'V2', 'MT'], n_neurons),
    'condition': np.random.choice(['Rest', 'Task'], n_neurons),
    'firing_rate': np.random.gamma(5, 2, n_neurons),
    'synchrony': np.random.beta(2, 5, n_neurons),
    'variability': np.random.exponential(0.3, n_neurons),
    'response_latency': np.random.normal(150, 30, n_neurons)
})

# Add some correlations
data['firing_rate'] += data['synchrony'] * 3
data['variability'] -= data['synchrony'] * 0.2
```

### Hints
- Use `sns.FacetGrid(data, col='region', row='condition')`
- Use `sns.pairplot(data, hue='region')`
- Use `px.scatter_3d()` for interactive 3D

---

## Exercise 6: Time Series Visualization

### Task
Visualize neural oscillations and phase relationships across multiple channels.

### Requirements
1. Create a multi-panel figure showing:
   - Raw signals from 3 channels
   - Power spectral density for each channel
   - Spectrogram (time-frequency representation)
   - Phase coherence between channels
2. Use appropriate colormaps (perceptually uniform)
3. Add colorbar for spectrogram
4. Synchronize x-axes across time-based plots

### Data Generation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate oscillatory signals
fs = 1000  # Sampling frequency
t = np.linspace(0, 10, fs * 10)

# Three channels with different frequency content
ch1 = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 30 * t) + np.random.randn(len(t)) * 0.1
ch2 = np.sin(2 * np.pi * 15 * t) + 0.3 * np.sin(2 * np.pi * 45 * t) + np.random.randn(len(t)) * 0.1
ch3 = np.sin(2 * np.pi * 20 * t) + 0.4 * np.sin(2 * np.pi * 60 * t) + np.random.randn(len(t)) * 0.1

# Compute spectrogram for ch1
f, t_spec, Sxx = signal.spectrogram(ch1, fs, nperseg=256)

# Compute PSD
f_psd, psd1 = signal.welch(ch1, fs, nperseg=1024)
_, psd2 = signal.welch(ch2, fs, nperseg=1024)
_, psd3 = signal.welch(ch3, fs, nperseg=1024)
```

### Hints
- Use GridSpec for complex layout
- Use `ax.sharex(ax_other)` to synchronize axes
- Use `viridis` or `plasma` for spectrogram
- Log scale for frequency axis: `ax.set_yscale('log')`

---

## Exercise 7: Creating a Figure Style Template

### Task
Create a reusable style configuration that can be applied to all figures in your project.

### Requirements
1. Create a custom rcParams dictionary
2. Define settings for:
   - Figure size and DPI
   - Font family and sizes
   - Line widths
   - Colors (colorblind-safe)
   - Spine visibility
   - Legend style
3. Create a function that applies the style
4. Create example figures demonstrating the style

### Template Structure

```python
def set_publication_style():
    """
    Apply publication-ready style to all matplotlib figures.
    Based on Nature journal guidelines.
    """
    # TODO: Define custom_params dictionary
    # TODO: Apply with plt.rcParams.update(custom_params)
    pass

def reset_style():
    """Reset to matplotlib defaults."""
    plt.rcdefaults()

# Color palette (colorblind-safe)
COLORS = {
    'blue': '#0173B2',
    'orange': '#DE8F05',
    'green': '#029E73',
    'red': '#CC78BC',
    'purple': '#CA9161',
    'brown': '#ECE133',
}
```

### Task
Complete the functions and create three example plots demonstrating the style.

---

## Solutions

Solutions are provided in a separate notebook: `notebooks/solutions.ipynb`

---

## Bonus Challenges

### Challenge 1: Animated Learning Curve
Create an animated Plotly figure showing how model performance improves over training epochs.

### Challenge 2: Custom Colormap
Design and implement a perceptually uniform colormap for your specific data type.

### Challenge 3: Interactive Report
Create a multi-page HTML report with interactive Plotly figures and navigation between sections.

### Challenge 4: Publication Pipeline
Write a script that automatically generates all figures for a paper in consistent style and exports them in multiple formats.


Remember: The goal is to learn, not just to complete exercises. Take time to understand the principles behind good visualization!

---

*Exercises prepared for CNC-UC Introduction to Scientific Programming*  
*University of Coimbra*
