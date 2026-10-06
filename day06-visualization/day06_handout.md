# Day 6 Handout: Visualization & Communication
*PhD Course in Integrative Neurosciences - Introduction to Scientific Programming*

---

## Table of Contents

1. [Introduction to Scientific Visualization](#introduction)
2. [Matplotlib Fundamentals](#matplotlib)
3. [Seaborn for Statistical Visualization](#seaborn)
4. [Interactive Visualization with Plotly](#plotly)
5. [Best Practices for Scientific Figures](#best-practices)
6. [Color Accessibility](#color-accessibility)
7. [Export Formats and Resolution](#export-formats)
8. [Common Mistakes to Avoid](#common-mistakes)
9. [Quick Reference](#quick-reference)
10. [Further Resources](#resources)

---

## <a name="introduction"></a>1. Introduction to Scientific Visualization

### Why Visualization Matters

Figures are the **primary communication medium** in scientific research:
- Experimental results are often judged by figure quality
- A well-designed figure tells a story without requiring text
- Poor visualization can obscure important findings
- Publication acceptance often depends on figure clarity

### The Python Visualization Ecosystem

```
Matplotlib (Foundation)
    ↓
Seaborn (High-level statistical)
    ↓
Plotly (Interactive)
```

**Decision Framework:**
- **Publication figures?** → Matplotlib + SciencePlots
- **Statistical comparisons?** → Seaborn
- **Data exploration?** → Plotly
- **Multiple panels?** → Matplotlib with GridSpec

### Static vs Interactive Visualizations

| Feature | Static (Matplotlib/Seaborn) | Interactive (Plotly) |
|---------|---------------------------|----------------------|
| **Use case** | Publications, reports | Exploration, dashboards |
| **Advantages** | Precise control, publication-ready | Zoom, pan, hover details |
| **Format** | PDF, PNG, SVG | HTML, web-based |
| **Best for** | Journal submissions | Large datasets, web sharing |

---

## <a name="matplotlib"></a>2. Matplotlib Fundamentals

### Architecture Overview

Matplotlib has a hierarchical structure:

```
Figure (entire canvas)
  └── Axes (individual plot)
        └── Axis (x and y axes with ticks, labels)
```

**Important terminology:**
- **Figure**: The entire window/canvas
- **Axes**: Individual plots (NOT the same as "axis"!)
- **Axis**: The x-axis or y-axis objects

### Pyplot vs Object-Oriented Interface

**❌ Pyplot Interface (AVOID for complex plots):**
```python
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
```

**✅ Object-Oriented Interface (RECOMMENDED):**
```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
```

**Why OO is better:**
- Explicit control over which axes you're modifying
- Essential for multi-panel figures
- Clearer code organization
- Easier to customize individual panels

### Creating Multi-Panel Figures

#### Simple Subplots

```python
# 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Access individual axes
axes[0, 0].plot(x1, y1)  # Top-left
axes[0, 1].plot(x2, y2)  # Top-right
axes[1, 0].plot(x3, y3)  # Bottom-left
axes[1, 1].plot(x4, y4)  # Bottom-right

# Shared axes
fig, axes = plt.subplots(2, 1, sharex=True, sharey=False)
```

#### Advanced Layouts with GridSpec

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

# Spanning multiple cells
ax1 = fig.add_subplot(gs[0, :])      # Top row, all columns
ax2 = fig.add_subplot(gs[1:, 0])     # Bottom 2 rows, first column
ax3 = fig.add_subplot(gs[1:, 1:])    # Bottom 2 rows, last 2 columns
```

### Publication-Quality Styling

#### SciencePlots Package

```bash
pip install SciencePlots
```

```python
import matplotlib.pyplot as plt
import scienceplots

# Apply journal-specific styles
plt.style.use(['science', 'nature'])  # Nature journal style
plt.style.use(['science', 'ieee'])    # IEEE style
plt.style.use(['science', 'scatter']) # For scatter plots
```

#### Manual rcParams Configuration

```python
# Define custom publication settings
custom_params = {
    'figure.figsize': (7, 5),
    'figure.dpi': 300,
    'font.size': 10,
    'font.family': 'sans-serif',
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'legend.frameon': False,
    'lines.linewidth': 1.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
}

plt.rcParams.update(custom_params)
```

### Adding Panel Labels

For multi-panel figures, add labels (A, B, C, D):

```python
fig, axes = plt.subplots(2, 2)

for i, ax in enumerate(axes.flat):
    label = chr(65 + i)  # A, B, C, D
    ax.text(-0.15, 1.1, label, 
            transform=ax.transAxes,
            fontsize=16, 
            fontweight='bold',
            va='top')
```

---

## <a name="seaborn"></a>3. Seaborn for Statistical Visualization

### Why Use Seaborn?

Seaborn is a high-level visualization library built on Matplotlib:

**Advantages:**
- Beautiful defaults out of the box
- Seamless pandas DataFrame integration
- Built-in statistical functions (CI, regression)
- Convenient themes and color palettes
- Less verbose code

**When to use Seaborn:**
- Quick exploratory data analysis
- Statistical comparisons with error bars
- Multi-dimensional data visualization
- Working with pandas DataFrames

### Setup and Configuration

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set theme and palette
sns.set_theme(style='whitegrid', palette='colorblind')

# Available styles: darkgrid, whitegrid, dark, white, ticks
# Available palettes: colorblind, Set2, husl, etc.
```

### Common Plot Types

#### Distribution Plots

```python
# Histogram with KDE
sns.histplot(data=df, x='variable', bins=20, kde=True)

# KDE plot
sns.kdeplot(data=df, x='variable', hue='group', fill=True)

# Box plot
sns.boxplot(data=df, x='condition', y='value', hue='group')

# Violin plot
sns.violinplot(data=df, x='condition', y='value', split=True, hue='group')
```

#### Categorical Plots

```python
# Bar plot with confidence intervals
sns.barplot(data=df, x='condition', y='value', hue='group', errorbar='ci')

# Point plot (shows means with lines)
sns.pointplot(data=df, x='condition', y='value', hue='group', errorbar='ci')

# Strip plot (individual points)
sns.stripplot(data=df, x='condition', y='value', hue='group', dodge=True)

# Swarm plot (non-overlapping points)
sns.swarmplot(data=df, x='condition', y='value', hue='group')
```

#### Relationship Plots

```python
# Scatter plot
sns.scatterplot(data=df, x='age', y='score', hue='group', style='sex')

# Regression plot with confidence interval
sns.regplot(data=df, x='age', y='score', 
            scatter_kws={'alpha': 0.5},
            line_kws={'color': 'red'})

# Line plot
sns.lineplot(data=df, x='trial', y='accuracy', hue='subject')
```

#### Matrix Plots

```python
# Correlation heatmap
correlation = df.corr()
sns.heatmap(correlation, annot=True, fmt='.2f', 
            cmap='RdBu_r', center=0, vmin=-1, vmax=1)

# Clustered heatmap
sns.clustermap(correlation, cmap='RdBu_r', center=0)
```

### Multi-Dimensional Visualization

#### Pairplot

```python
# All pairwise relationships
sns.pairplot(df, hue='species', diag_kind='kde')
```

Shows:
- **Diagonal**: Distribution of each variable
- **Off-diagonal**: Scatter plots of all pairs
- **Colors**: Separated by categorical variable

#### FacetGrid

```python
# Create conditional plots
g = sns.FacetGrid(df, col='condition', row='group', hue='sex',
                  height=4, aspect=1.2)
g.map(sns.histplot, 'value', kde=True)
g.add_legend()
```

Use FacetGrid when you want to split your data by categorical variables and create separate plots for each combination.

### Color Palettes

```python
# Qualitative (categorical data)
sns.set_palette('colorblind')  # Colorblind-safe
sns.set_palette('Set2')

# Sequential (ordered data)
sns.set_palette('viridis')
sns.set_palette('plasma')

# Diverging (data with a midpoint)
sns.set_palette('coolwarm')
sns.set_palette('RdYlBu')
```

**⚠️ Always use colorblind-safe palettes for publications!**

---

## <a name="plotly"></a>4. Interactive Visualization with Plotly

### When to Use Interactive Plots

**Use interactive plots for:**
- Data exploration (zoom, pan, hover)
- Large datasets with many points
- High-dimensional data (3D visualizations)
- Web sharing and dashboards
- Presentations with live data

**Avoid for:**
- Journal publications (use static Matplotlib)
- Print-only documents
- Simple plots where interactivity doesn't add value

### Plotly Express Basics

```python
import plotly.express as px

# Interactive scatter plot
fig = px.scatter(df, x='age', y='score', 
                 color='group', size='accuracy',
                 hover_data=['subject_id', 'trial'])
fig.show()
```

### Common Interactive Plots

```python
# Line plot
fig = px.line(df, x='trial', y='accuracy', color='subject')

# Box plot with points
fig = px.box(df, x='condition', y='value', 
             color='condition', points='all')

# Histogram with marginal
fig = px.histogram(df, x='value', color='group', 
                   marginal='box', opacity=0.6)

# Heatmap
fig = px.imshow(correlation_matrix, 
                text_auto='.2f',
                color_continuous_scale='RdBu_r')

# 3D scatter
fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3', color='cluster')
```

### Subplots with Plotly

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2,
                    subplot_titles=('Plot A', 'Plot B', 'Plot C', 'Plot D'))

fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers'), row=1, col=1)
fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines'), row=1, col=2)
fig.add_trace(go.Histogram(x=data), row=2, col=1)
fig.add_trace(go.Box(y=data), row=2, col=2)

fig.update_layout(height=700, title_text='Multi-Panel Interactive Plot')
fig.show()
```

### Animation

```python
# Animated scatter plot
fig = px.scatter(df, x='x', y='y', 
                 color='group',
                 animation_frame='time',  # Animate over time
                 range_x=[0, 10], 
                 range_y=[0, 100])
fig.show()
```

### Exporting

```python
# Export as interactive HTML
fig.write_html('outputs/interactive_plot.html')

# Export as static image (requires kaleido)
fig.write_image('static_plot.png', width=1200, height=600)
fig.write_image('static_plot.pdf')
```

---

## <a name="best-practices"></a>5. Best Practices for Scientific Figures

### Tufte's Design Principles

**Data-Ink Ratio:**
```
Data-ink ratio = Data ink / Total ink used
```

**Maximize information, minimize non-data elements.**

Key principles:
1. **Simplicity**: Remove unnecessary elements (chartjunk)
2. **Clarity**: One clear message per figure
3. **Accuracy**: Don't distort data (e.g., avoid truncated axes)
4. **Consistency**: Same style across all figures
5. **Legibility**: Readable at publication size

### Typography

- **Font size**: 8-10 pt minimum at final publication size
- **Font family**: Sans-serif (Arial, Helvetica) for clarity
- **Consistency**: Same sizes for all axis labels
- **Avoid**: Overly decorative fonts

### Layout Guidelines

**Journal figure sizes:**
- Single column: ~3.5 inches (9 cm)
- Double column: ~7 inches (18 cm)
- Height: Typically 4-6 inches

**Design checklist:**
- ✓ Remove top and right spines
- ✓ Use `bbox_inches='tight'` when saving
- ✓ Add panel labels (A, B, C, D) for multi-panel figures
- ✓ Keep legends frameless
- ✓ Ensure all text is readable at final size

### What to Avoid

**❌ Truncated Y-axis** (exaggerates differences)
```python
# Bad: Starting y-axis above zero
ax.set_ylim(95, 100)  # Exaggerates small differences

# Good: Include zero or clearly indicate truncation
ax.set_ylim(0, 100)
```

**❌ 3D effects** (distort perception)
**❌ Pie charts** for > 5 categories
**❌ Dual y-axes** (confusing comparisons)
**❌ Rainbow colormaps** (jet, rainbow create false gradients)

---

## <a name="color-accessibility"></a>6. Color Accessibility

### Colorblind Vision Deficiency

~8% of males and ~0.5% of females have color vision deficiency (CVD).

**Most common:** Red-green colorblindness

### Colorblind-Safe Palettes

**❌ AVOID:**
- Red-green combinations
- Color as the only distinguishing feature

**✅ USE:**
- **Sequential**: viridis, plasma, cividis
- **Diverging**: coolwarm, RdYlBu (with caution)
- **Categorical**: colorblind palette, tab10

```python
# Matplotlib
plt.set_cmap('viridis')

# Seaborn
sns.set_palette('colorblind')

# Plotly
fig = px.scatter(df, x='x', y='y', 
                 color='group',
                 color_discrete_sequence=px.colors.qualitative.Safe)
```

### Additional Strategies

Beyond color, use:
- **Line styles**: solid, dashed, dotted
- **Markers**: circles, squares, triangles
- **Texture/hatching**: for bar charts
- **Direct labels**: instead of legends

### Testing for Colorblindness

**Online simulators:**
- https://davidmathlogic.com/colorblind/
- https://www.color-blindness.com/coblis-color-blindness-simulator/

Always check your figures with a colorblind simulator before publication!

---

## <a name="export-formats"></a>7. Export Formats and Resolution

### Vector vs Raster Formats

| Format | Type | Best Use | Scalability |
|--------|------|----------|-------------|
| **PDF** | Vector | Publications, printing | ✓ Infinite |
| **SVG** | Vector | Web, Illustrator editing | ✓ Infinite |
| **EPS** | Vector | Legacy publications | ✓ Infinite |
| **PNG** | Raster | Web, presentations | ✗ Limited |
| **TIFF** | Raster | Some journals | ✗ Limited |
| **JPG** | Raster | Avoid (lossy compression) | ✗ Limited |

### DPI Requirements

**Journal requirements:**
- **Line art**: 1000-1200 DPI
- **Combination (line + halftone)**: 600 DPI
- **Halftone (photos)**: 300 DPI

### Exporting from Matplotlib

```python
# Vector formats (recommended)
fig.savefig('figure.pdf', dpi=300, bbox_inches='tight')
fig.savefig('figure.svg', format='svg', bbox_inches='tight')

# Raster format (if required)
fig.savefig('figure.png', dpi=600, bbox_inches='tight')

# TIFF for some journals
fig.savefig('figure.tiff', dpi=600, bbox_inches='tight', 
            pil_kwargs={'compression': 'tiff_lzw'})
```

**Key parameters:**
- `dpi=300` (or higher): Resolution
- `bbox_inches='tight'`: Remove whitespace
- `format`: Explicitly specify format

---

## <a name="common-mistakes"></a>8. Common Mistakes to Avoid

### 1. Truncated Y-Axis
**Problem**: Exaggerates small differences  
**Solution**: Start at zero or clearly indicate truncation

### 2. Inappropriate Chart Types
**Problems:**
- Pie charts for > 5 categories
- 3D charts (distort perception)
- Dual y-axes (confusing)

**Solutions:**
- Use bar charts instead of pie charts
- Stick to 2D visualizations
- Use separate panels instead of dual axes

### 3. Too Much Information
**Problems:**
- Overcrowded plots
- Too many colors/line styles
- Legends with > 8 items

**Solutions:**
- Simplify or split into multiple panels
- Limit to 5-7 distinguishable colors
- Use direct labeling when possible

### 4. Poor Labels and Units
**Problems:**
- Missing axis labels
- Missing units
- Unclear abbreviations

**Solutions:**
- Always include axis labels with units
- Spell out abbreviations or define them
- Use proper scientific notation

### 5. Rainbow Colormaps
**Problem**: Jet/rainbow colormaps create false perceptual gradients  
**Solution**: Use perceptually uniform colormaps (viridis, plasma, cividis)

```python
# Bad
plt.imshow(data, cmap='jet')

# Good
plt.imshow(data, cmap='viridis')
```

### 6. Inconsistent Styling
**Problem**: Different fonts, sizes, colors across figures  
**Solution**: Define global settings at the start

```python
# Define once, apply to all figures
plt.rcParams.update(custom_params)
```

---

## <a name="quick-reference"></a>9. Quick Reference

### Decision Tree for Visualization

```
Need a figure?
    ├─ For publication?
    │    ├─ Statistical comparison? → Seaborn
    │    └─ Custom/complex? → Matplotlib + SciencePlots
    │
    ├─ For data exploration?
    │    └─ Interactive needed? → Plotly
    │
    └─ For presentation?
         ├─ Static → Matplotlib/Seaborn
         └─ Interactive → Plotly
```

### Common Code Patterns

#### Matplotlib Multi-Panel

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for i, ax in enumerate(axes.flat):
    ax.plot(x, y[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # Add panel label
    ax.text(-0.15, 1.1, chr(65+i), transform=ax.transAxes,
            fontsize=16, fontweight='bold')

plt.tight_layout()
fig.savefig('figure.pdf', dpi=300, bbox_inches='tight')
```

#### Seaborn Statistical Plot

```python
sns.set_theme(style='whitegrid', palette='colorblind')

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(data=df, x='condition', y='value', 
            hue='group', errorbar='ci', ax=ax)
ax.set_ylabel('Mean Response (ms)')
ax.legend(frameon=False)

fig.savefig('figure.pdf', dpi=300, bbox_inches='tight')
```

#### Plotly Interactive

```python
fig = px.scatter(df, x='x', y='y', color='group',
                 hover_data=['subject', 'trial'])
fig.update_layout(template='plotly_white')
fig.write_html('interactive.html')
```

---

## <a name="resources"></a>10. Further Resources

### Documentation

- **Matplotlib**: https://matplotlib.org
- **Seaborn**: https://seaborn.pydata.org
- **Plotly**: https://plotly.com/python
- **SciencePlots**: https://github.com/garrettj403/SciencePlots

### Galleries and Examples

- **Python Graph Gallery**: https://python-graph-gallery.com
- **Seaborn Examples**: https://seaborn.pydata.org/examples/
- **Plotly Examples**: https://plotly.com/python/

### Color Tools

- **Colorblind simulator**: https://davidmathlogic.com/colorblind/
- **ColorBrewer** (palettes): https://colorbrewer2.org
- **Colorcet** (perceptually uniform): https://colorcet.holoviz.org

### Books and Articles

- **"The Visual Display of Quantitative Information"** by Edward Tufte
- **"Fundamentals of Data Visualization"** by Claus O. Wilke (free online)
- **Nature figure guidelines**: https://www.nature.com/nature/for-authors/final-submission

### Journal Guidelines

Always check your target journal's specific requirements:
- Figure file formats
- Resolution (DPI)
- Maximum file size
- Color mode (RGB vs CMYK)
- Font embedding requirements

---

## Summary Checklist

Before submitting a figure, verify:

- [ ] Clear axis labels with units
- [ ] Readable font sizes (≥ 8 pt at final size)
- [ ] Colorblind-safe palette
- [ ] Panel labels (A, B, C, D) for multi-panel figures
- [ ] Legend without frame (or minimal frame)
- [ ] Removed unnecessary spines (top, right)
- [ ] Appropriate file format (PDF/SVG for publications)
- [ ] Correct resolution (600 DPI for raster)
- [ ] No chartjunk or unnecessary elements
- [ ] Consistent styling across all figures
- [ ] Figure tells a clear story
- [ ] All elements visible at publication size

**Remember:** A figure should be understandable without reading the caption!

---
*This handout is part of the "Introduction to Scientific Programming" course at CNC-UC, University of Coimbra. For questions or clarifications, please contact the course instructor.*
**Document Version**: 1.0  
**License**: CC BY 4.0

