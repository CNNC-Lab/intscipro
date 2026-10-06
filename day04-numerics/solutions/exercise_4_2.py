# Exercise 4.2: Subplots and Customization
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

np.random.seed(42)
x = np.random.randn(1000)
y = 2*x + np.random.randn(1000)

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Comprehensive Data Visualization', 
             fontsize=16, fontweight='bold', y=0.995)

# Top-left: Scatter with trend line
ax1 = axes[0, 0]
ax1.scatter(x, y, alpha=0.5, s=20, edgecolors='black', linewidths=0.5)

# Add trend line
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line_x = np.array([x.min(), x.max()])
line_y = slope * line_x + intercept
ax1.plot(line_x, line_y, 'r-', linewidth=2, 
         label=f'y = {slope:.2f}x + {intercept:.2f}\n$R^2$ = {r_value**2:.3f}')

ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.set_title('Scatter Plot with Trend Line', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Top-right: Overlapping histograms
ax2 = axes[0, 1]
ax2.hist(x, bins=30, alpha=0.5, label='x', color='blue', edgecolor='black')
ax2.hist(y, bins=30, alpha=0.5, label='y', color='red', edgecolor='black')
ax2.set_xlabel('Value', fontsize=11)
ax2.set_ylabel('Frequency', fontsize=11)
ax2.set_title('Distributions', fontsize=12, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3, axis='y')

# Bottom-left: Box plots
ax3 = axes[1, 0]
box_data = [x, y]
bp = ax3.boxplot(box_data, patch_artist=True)
ax3.set_xticks([1, 2], ['x', 'y'])

# Customize box colors
colors = ['lightblue', 'lightcoral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax3.set_ylabel('Value', fontsize=11)
ax3.set_title('Box Plots', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, axis='y')

# Bottom-right: 2D histogram (hexbin)
ax4 = axes[1, 1]
hb = ax4.hexbin(x, y, gridsize=30, cmap='YlOrRd', mincnt=1)
cb = plt.colorbar(hb, ax=ax4, label='Count')
ax4.set_xlabel('x', fontsize=11)
ax4.set_ylabel('y', fontsize=11)
ax4.set_title('2D Histogram (Hexbin)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# Print statistics
print(f"Correlation coefficient: {np.corrcoef(x, y)[0,1]:.3f}")
print(f"Linear regression: y = {slope:.2f}x + {intercept:.2f}")
print(f"R²: {r_value**2:.3f}")
