# Exercise 4.3: Advanced Visualization
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

np.random.seed(42)
n_samples = 100
n_features = 4

# Generate data
time = np.linspace(0, 10, n_samples)
data = np.zeros((n_samples, n_features))
feature_names = ['Feature A', 'Feature B', 'Feature C', 'Feature D']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i in range(n_features):
    trend = np.sin(2*np.pi*0.5*time + i)
    noise = 0.3 * np.random.randn(n_samples)
    data[:, i] = trend + noise

# Create figure
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# 1. Time series with confidence intervals
ax1 = fig.add_subplot(gs[0, :])  # Top row, full width

for i in range(n_features):
    # Calculate rolling mean and std
    window = 10
    rolling_mean = np.convolve(data[:, i], np.ones(window)/window, mode='same')
    rolling_std = np.array([data[max(0,j-window):min(n_samples,j+window), i].std() 
                           for j in range(n_samples)])
    
    ax1.plot(time, rolling_mean, color=colors[i], 
            linewidth=2, label=feature_names[i])
    ax1.fill_between(time, 
                     rolling_mean - rolling_std,
                     rolling_mean + rolling_std,
                     color=colors[i], alpha=0.2)

ax1.set_xlabel('Time', fontsize=12, fontweight='bold')
ax1.set_ylabel('Value', fontsize=12, fontweight='bold')
ax1.set_title('Time Series with Confidence Intervals', 
             fontsize=14, fontweight='bold')
ax1.legend(loc='upper right', fontsize=10, framealpha=0.9)
ax1.grid(True, alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# 2. Correlation heatmap
ax2 = fig.add_subplot(gs[1, 0])

# Compute correlation matrix
corr_matrix = np.corrcoef(data.T)

# Plot heatmap
im = ax2.imshow(corr_matrix, cmap='coolwarm', aspect='auto',
               vmin=-1, vmax=1)

# Add colorbar
cbar = plt.colorbar(im, ax=ax2)
cbar.set_label('Correlation', fontsize=11, fontweight='bold')

# Set ticks and labels
ax2.set_xticks(range(n_features))
ax2.set_yticks(range(n_features))
ax2.set_xticklabels(feature_names, rotation=45, ha='right')
ax2.set_yticklabels(feature_names)

# Add correlation values as text
for i in range(n_features):
    for j in range(n_features):
        text = ax2.text(j, i, f'{corr_matrix[i, j]:.2f}',
                       ha='center', va='center',
                       color='white' if abs(corr_matrix[i, j]) > 0.5 else 'black',
                       fontsize=10, fontweight='bold')

ax2.set_title('Correlation Matrix', fontsize=12, fontweight='bold')

# 3. Distribution comparisons (violin plot)
ax3 = fig.add_subplot(gs[1, 1])

positions = np.arange(1, n_features + 1)
parts = ax3.violinplot([data[:, i] for i in range(n_features)],
                       positions=positions,
                       showmeans=True,
                       showmedians=True)

# Color the violin plots
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.7)

ax3.set_xticks(positions)
ax3.set_xticklabels(feature_names, rotation=45, ha='right')
ax3.set_ylabel('Value', fontsize=12, fontweight='bold')
ax3.set_title('Distribution Comparison', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, axis='y')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# 4. Statistical summary
ax4 = fig.add_subplot(gs[2, :])
ax4.axis('off')

# Create summary statistics table
summary_data = []
for i, name in enumerate(feature_names):
    mean = data[:, i].mean()
    std = data[:, i].std()
    min_val = data[:, i].min()
    max_val = data[:, i].max()
    summary_data.append([name, f'{mean:.3f}', f'{std:.3f}', 
                        f'{min_val:.3f}', f'{max_val:.3f}'])

table = ax4.table(cellText=summary_data,
                 colLabels=['Feature', 'Mean', 'Std Dev', 'Min', 'Max'],
                 cellLoc='center',
                 loc='center',
                 bbox=[0.2, 0.2, 0.6, 0.6])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

# Style header
for i in range(5):
    table[(0, i)].set_facecolor('#40466e')
    table[(0, i)].set_text_props(weight='bold', color='white')

# Alternate row colors
for i in range(1, n_features + 1):
    color = '#f0f0f0' if i % 2 == 0 else 'white'
    for j in range(5):
        table[(i, j)].set_facecolor(color)

ax4.set_title('Summary Statistics', fontsize=12, 
             fontweight='bold', pad=20)

# Overall figure title
fig.suptitle('Comprehensive Data Analysis', 
            fontsize=16, fontweight='bold', y=0.995)

plt.show()

# Print additional statistics
print("\n=== Statistical Summary ===")
for i, name in enumerate(feature_names):
    print(f"\n{name}:")
    print(f"  Mean: {data[:, i].mean():.3f}")
    print(f"  Median: {np.median(data[:, i]):.3f}")
    print(f"  Std: {data[:, i].std():.3f}")
    print(f"  Range: [{data[:, i].min():.3f}, {data[:, i].max():.3f}]")

print("\n=== Pairwise Correlations ===")
for i in range(n_features):
    for j in range(i+1, n_features):
        r = corr_matrix[i, j]
        print(f"{feature_names[i]} vs {feature_names[j]}: r = {r:.3f}")
