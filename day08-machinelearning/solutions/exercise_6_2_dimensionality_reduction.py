"""
Exercise 6.2: Dimensionality Reduction Comparison
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for comparing PCA and t-SNE on digits dataset.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import time

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Digits Dataset
# =============================================================================
print("=" * 60)
print("1. LOADING DIGITS DATASET")
print("=" * 60)

digits = load_digits()
X = digits.data
y = digits.target

print(f"Samples: {X.shape[0]}")
print(f"Features (pixels): {X.shape[1]} (8x8 images)")
print(f"Classes: {len(np.unique(y))} (digits 0-9)")

# Visualize some digits
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(X[i].reshape(8, 8), cmap='gray')
    ax.set_title(f'Digit: {y[i]}')
    ax.axis('off')
plt.suptitle('Sample Digits from Dataset')
plt.tight_layout()
plt.savefig('ex6_2_sample_digits.png', dpi=150)
plt.close()
print("Sample digits saved to ex6_2_sample_digits.png")

# =============================================================================
# 2. PCA Analysis
# =============================================================================
print("\n" + "=" * 60)
print("2. PCA ANALYSIS")
print("=" * 60)

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Full PCA to analyze variance
pca_full = PCA()
pca_full.fit(X_scaled)

# Explained variance
explained_variance = pca_full.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

print(f"\nVariance explained by first 10 components:")
for i in range(10):
    print(f"  PC{i+1}: {explained_variance[i]:.4f} (cumulative: {cumulative_variance[i]:.4f})")

# How many components for 95% variance?
n_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(f"\nComponents needed for 95% variance: {n_components_95}")

# PCA with 2 components for visualization
start_time = time.time()
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)
pca_time = time.time() - start_time
print(f"\nPCA (2D) computation time: {pca_time:.4f} seconds")

# =============================================================================
# 3. Scree Plot
# =============================================================================
print("\n" + "=" * 60)
print("3. SCREE PLOT")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Individual variance
ax1 = axes[0]
ax1.bar(range(1, 21), explained_variance[:20], alpha=0.7)
ax1.set_xlabel('Principal Component')
ax1.set_ylabel('Variance Explained')
ax1.set_title('Scree Plot')
ax1.grid(True, alpha=0.3)

# Cumulative variance
ax2 = axes[1]
ax2.plot(range(1, len(cumulative_variance)+1), cumulative_variance, 'b-o', markersize=3)
ax2.axhline(y=0.95, color='r', linestyle='--', label='95% variance')
ax2.axvline(x=n_components_95, color='g', linestyle='--', label=f'{n_components_95} components')
ax2.set_xlabel('Number of Components')
ax2.set_ylabel('Cumulative Variance Explained')
ax2.set_title('Cumulative Variance Explained')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex6_2_scree_plot.png', dpi=150)
plt.close()
print("Scree plot saved to ex6_2_scree_plot.png")

# =============================================================================
# 4. Reconstruction Error
# =============================================================================
print("\n" + "=" * 60)
print("4. RECONSTRUCTION ERROR")
print("=" * 60)

n_components_list = [2, 5, 10, 20, 30, 40, 50]
reconstruction_errors = []

print("\nReconstruction error for different N:")
print("-" * 40)
print(f"{'N components':<15} {'MSE':>12}")
print("-" * 40)

for n in n_components_list:
    pca_n = PCA(n_components=n)
    X_reduced = pca_n.fit_transform(X_scaled)
    X_reconstructed = pca_n.inverse_transform(X_reduced)
    mse = np.mean((X_scaled - X_reconstructed) ** 2)
    reconstruction_errors.append(mse)
    print(f"{n:<15} {mse:>12.4f}")

# Visualize reconstruction
fig, axes = plt.subplots(3, 6, figsize=(15, 8))

sample_idx = 0
original = X[sample_idx].reshape(8, 8)

for row, n in enumerate([2, 10, 30]):
    pca_n = PCA(n_components=n)
    X_reduced = pca_n.fit_transform(X_scaled)
    X_reconstructed = scaler.inverse_transform(pca_n.inverse_transform(X_reduced))
    
    for col in range(6):
        ax = axes[row, col]
        if col == 0:
            ax.imshow(X[col].reshape(8, 8), cmap='gray')
            ax.set_ylabel(f'N={n}')
        else:
            ax.imshow(X_reconstructed[col].reshape(8, 8), cmap='gray')
        ax.axis('off')
        if row == 0:
            ax.set_title(f'Digit {y[col]}')

plt.suptitle('Original (col 0) vs Reconstructed Digits')
plt.tight_layout()
plt.savefig('ex6_2_reconstruction.png', dpi=150)
plt.close()
print("Reconstruction comparison saved to ex6_2_reconstruction.png")

# =============================================================================
# 5. t-SNE with Different Perplexity
# =============================================================================
print("\n" + "=" * 60)
print("5. t-SNE WITH DIFFERENT PERPLEXITY")
print("=" * 60)

# First reduce with PCA for speed
pca_pre = PCA(n_components=50)
X_pca_pre = pca_pre.fit_transform(X_scaled)

perplexity_values = [5, 30, 50]
tsne_results = {}

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, perp in zip(axes, perplexity_values):
    print(f"\nComputing t-SNE with perplexity={perp}...")
    start_time = time.time()
    
    tsne = TSNE(n_components=2, perplexity=perp, random_state=42, max_iter=1000)
    X_tsne = tsne.fit_transform(X_pca_pre)
    
    elapsed = time.time() - start_time
    print(f"  Time: {elapsed:.2f} seconds")
    
    tsne_results[perp] = X_tsne
    
    scatter = ax.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', alpha=0.7, s=10)
    ax.set_xlabel('t-SNE 1')
    ax.set_ylabel('t-SNE 2')
    ax.set_title(f't-SNE (perplexity={perp})')
    ax.grid(True, alpha=0.3)

plt.colorbar(scatter, ax=axes[-1], label='Digit')
plt.tight_layout()
plt.savefig('ex6_2_tsne_perplexity.png', dpi=150)
plt.close()
print("t-SNE perplexity comparison saved to ex6_2_tsne_perplexity.png")

# =============================================================================
# 6. PCA vs t-SNE Comparison
# =============================================================================
print("\n" + "=" * 60)
print("6. PCA vs t-SNE COMPARISON")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# PCA
ax1 = axes[0]
scatter1 = ax1.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y, cmap='tab10', alpha=0.7, s=10)
ax1.set_xlabel('PC1')
ax1.set_ylabel('PC2')
ax1.set_title(f'PCA (2 components)\nVariance explained: {pca_2d.explained_variance_ratio_.sum():.2%}')
ax1.grid(True, alpha=0.3)
plt.colorbar(scatter1, ax=ax1, label='Digit')

# t-SNE (perplexity=30)
ax2 = axes[1]
X_tsne_30 = tsne_results[30]
scatter2 = ax2.scatter(X_tsne_30[:, 0], X_tsne_30[:, 1], c=y, cmap='tab10', alpha=0.7, s=10)
ax2.set_xlabel('t-SNE 1')
ax2.set_ylabel('t-SNE 2')
ax2.set_title('t-SNE (perplexity=30)')
ax2.grid(True, alpha=0.3)
plt.colorbar(scatter2, ax=ax2, label='Digit')

plt.tight_layout()
plt.savefig('ex6_2_pca_vs_tsne.png', dpi=150)
plt.close()
print("PCA vs t-SNE comparison saved to ex6_2_pca_vs_tsne.png")

# =============================================================================
# 7. Comparison Summary
# =============================================================================
print("\n" + "=" * 60)
print("7. COMPARISON SUMMARY")
print("=" * 60)

print("""
PCA vs t-SNE COMPARISON:
------------------------

1. VISUAL SEPARATION:
   - PCA: Some overlap between digit classes
   - t-SNE: Much clearer separation of digit clusters
   - t-SNE is better for visualization of high-dimensional data

2. COMPUTATION TIME:
   - PCA: Very fast (< 0.1 seconds)
   - t-SNE: Much slower (several seconds to minutes)
   - PCA scales better to large datasets

3. INTERPRETABILITY:
   - PCA: Components have meaning (linear combinations)
   - t-SNE: No interpretable meaning for axes
   - PCA preserves global structure, t-SNE preserves local

4. TRANSFORMING NEW DATA:
   - PCA: Can transform new data with same transformation
   - t-SNE: Cannot transform new data (must refit)
   - PCA is better for preprocessing in ML pipelines

5. USE CASES:
   - PCA: Preprocessing, feature extraction, noise reduction
   - t-SNE: Visualization, exploring cluster structure
   - Often use PCA first, then t-SNE for visualization

6. PERPLEXITY EFFECT (t-SNE):
   - Low perplexity (5): Focus on local structure
   - High perplexity (50): More global structure
   - Typical range: 5-50, default 30 works well

RECOMMENDATIONS:
----------------
- Use PCA for dimensionality reduction in ML pipelines
- Use t-SNE for visualization and exploration
- Apply PCA before t-SNE to speed up computation
- Don't use t-SNE output as features for classification
""")

print("=" * 60)
print("EXERCISE 6.2 COMPLETE")
print("=" * 60)
