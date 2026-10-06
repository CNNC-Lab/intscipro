# Exercise 4.1: Basic Plotting
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.exp(-x/10)

plt.figure(figsize=(12, 10))

# a) Line plot with three functions
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
plt.plot(x, y3, 'g-.', linewidth=2, label='sin(x)·exp(-x/10)')
plt.xlabel('x', fontsize=11)
plt.ylabel('y', fontsize=11)
plt.title('Multiple Functions', fontsize=12, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# b) Scatter plot
plt.subplot(2, 2, 2)
np.random.seed(42)
scatter_x = np.random.randn(100)
scatter_y = np.random.randn(100)
distances = np.sqrt(scatter_x**2 + scatter_y**2)
colors = scatter_y

scatter = plt.scatter(scatter_x, scatter_y, 
                     c=colors, s=distances*50, 
                     alpha=0.6, cmap='viridis', edgecolors='black')
plt.colorbar(scatter, label='Y value')
plt.xlabel('x', fontsize=11)
plt.ylabel('y', fontsize=11)
plt.title('Scatter Plot', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# c) Bar chart with error bars
plt.subplot(2, 2, 3)
data1 = np.random.normal(20, 5, 50)
data2 = np.random.normal(25, 6, 50)
data3 = np.random.normal(22, 4, 50)

categories = ['Group A', 'Group B', 'Group C']
means = [data1.mean(), data2.mean(), data3.mean()]
stds = [data1.std(), data2.std(), data3.std()]

x_pos = np.arange(len(categories))
plt.bar(x_pos, means, yerr=stds, capsize=5, 
        alpha=0.7, color=['#1f77b4', '#ff7f0e', '#2ca02c'],
        edgecolor='black')
plt.xticks(x_pos, categories)
plt.xlabel('Category', fontsize=11)
plt.ylabel('Mean Value', fontsize=11)
plt.title('Bar Chart with Error Bars', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# d) Histogram with mean line
plt.subplot(2, 2, 4)
data = np.random.normal(100, 15, 1000)
mean_val = data.mean()

plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2,
            label=f'Mean = {mean_val:.1f}')
plt.xlabel('Value', fontsize=11)
plt.ylabel('Frequency', fontsize=11)
plt.title('Histogram', fontsize=12, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
