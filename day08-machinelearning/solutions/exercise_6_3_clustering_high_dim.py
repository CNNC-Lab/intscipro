"""
Exercise 6.3: Clustering on High-Dimensional Data
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for understanding when dimensionality reduction helps clustering.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, adjusted_rand_score, confusion_matrix

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Breast Cancer Dataset
# =============================================================================
print("=" * 60)
print("1. LOADING BREAST CANCER DATASET")
print("=" * 60)

cancer = load_breast_cancer()
X = cancer.data
y_true = cancer.target  # 0 = malignant, 1 = benign

print(f"Samples: {X.shape[0]}")
print(f"Features: {X.shape[1]}")
print(f"True classes: {cancer.target_names}")
print(f"Class distribution: {np.bincount(y_true)}")

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =============================================================================
# 2. K-Means on Raw Features
# =============================================================================
print("\n" + "=" * 60)
print("2. K-MEANS ON RAW FEATURES (30 dimensions)")
print("=" * 60)

kmeans_raw = KMeans(n_clusters=2, random_state=42, n_init=10)
labels_raw = kmeans_raw.fit_predict(X_scaled)

silhouette_raw = silhouette_score(X_scaled, labels_raw)
ari_raw = adjusted_rand_score(y_true, labels_raw)

print(f"\nK-Means on raw features:")
print(f"  Silhouette Score: {silhouette_raw:.4f}")
print(f"  Adjusted Rand Index: {ari_raw:.4f}")

# Confusion matrix
cm_raw = confusion_matrix(y_true, labels_raw)
print(f"\nConfusion Matrix (True vs Predicted):")
print(cm_raw)

# Visualize using PCA for 2D projection
pca_viz = PCA(n_components=2)
X_viz = pca_viz.fit_transform(X_scaled)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax1 = axes[0]
scatter1 = ax1.scatter(X_viz[:, 0], X_viz[:, 1], c=y_true, cmap='coolwarm', alpha=0.7)
ax1.set_xlabel('PC1')
ax1.set_ylabel('PC2')
ax1.set_title('True Labels')
ax1.grid(True, alpha=0.3)
plt.colorbar(scatter1, ax=ax1, label='Class')

ax2 = axes[1]
scatter2 = ax2.scatter(X_viz[:, 0], X_viz[:, 1], c=labels_raw, cmap='coolwarm', alpha=0.7)
ax2.set_xlabel('PC1')
ax2.set_ylabel('PC2')
ax2.set_title(f'K-Means on Raw Features\nSilhouette: {silhouette_raw:.3f}, ARI: {ari_raw:.3f}')
ax2.grid(True, alpha=0.3)
plt.colorbar(scatter2, ax=ax2, label='Cluster')

plt.tight_layout()
plt.savefig('ex6_3_raw_clustering.png', dpi=150)
plt.close()
print("Raw clustering visualization saved to ex6_3_raw_clustering.png")

# =============================================================================
# 3. K-Means with PCA (10 components)
# =============================================================================
print("\n" + "=" * 60)
print("3. K-MEANS WITH PCA (10 components)")
print("=" * 60)

pca_10 = PCA(n_components=10)
X_pca_10 = pca_10.fit_transform(X_scaled)

print(f"Variance explained by 10 components: {pca_10.explained_variance_ratio_.sum():.2%}")

kmeans_pca10 = KMeans(n_clusters=2, random_state=42, n_init=10)
labels_pca10 = kmeans_pca10.fit_predict(X_pca_10)

silhouette_pca10 = silhouette_score(X_pca_10, labels_pca10)
ari_pca10 = adjusted_rand_score(y_true, labels_pca10)

print(f"\nK-Means on PCA (10 components):")
print(f"  Silhouette Score: {silhouette_pca10:.4f}")
print(f"  Adjusted Rand Index: {ari_pca10:.4f}")

# =============================================================================
# 4. Different Numbers of PCA Components
# =============================================================================
print("\n" + "=" * 60)
print("4. EFFECT OF NUMBER OF PCA COMPONENTS")
print("=" * 60)

n_components_list = [2, 5, 10, 15, 20, 25, 30]
results = {
    'n_components': [],
    'variance_explained': [],
    'silhouette': [],
    'ari': []
}

print("\nResults for different numbers of PCA components:")
print("-" * 70)
print(f"{'N components':<15} {'Var Explained':>15} {'Silhouette':>12} {'ARI':>12}")
print("-" * 70)

for n in n_components_list:
    if n == 30:
        # Use all features
        X_reduced = X_scaled
        var_explained = 1.0
    else:
        pca = PCA(n_components=n)
        X_reduced = pca.fit_transform(X_scaled)
        var_explained = pca.explained_variance_ratio_.sum()
    
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_reduced)
    
    sil = silhouette_score(X_reduced, labels)
    ari = adjusted_rand_score(y_true, labels)
    
    results['n_components'].append(n)
    results['variance_explained'].append(var_explained)
    results['silhouette'].append(sil)
    results['ari'].append(ari)
    
    print(f"{n:<15} {var_explained:>15.2%} {sil:>12.4f} {ari:>12.4f}")

# Plot results
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

ax1 = axes[0]
ax1.plot(results['n_components'], results['variance_explained'], 'b-o')
ax1.set_xlabel('Number of PCA Components')
ax1.set_ylabel('Variance Explained')
ax1.set_title('Variance Explained vs Components')
ax1.grid(True, alpha=0.3)

ax2 = axes[1]
ax2.plot(results['n_components'], results['silhouette'], 'g-o')
ax2.set_xlabel('Number of PCA Components')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Score vs Components')
ax2.grid(True, alpha=0.3)

ax3 = axes[2]
ax3.plot(results['n_components'], results['ari'], 'r-o')
ax3.set_xlabel('Number of PCA Components')
ax3.set_ylabel('Adjusted Rand Index')
ax3.set_title('ARI vs Components')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex6_3_pca_components.png', dpi=150)
plt.close()
print("\nPCA components analysis saved to ex6_3_pca_components.png")

# =============================================================================
# 5. Comparison: With vs Without PCA
# =============================================================================
print("\n" + "=" * 60)
print("5. COMPARISON: WITH vs WITHOUT PCA")
print("=" * 60)

# Find best number of components
best_idx = np.argmax(results['ari'])
best_n = results['n_components'][best_idx]
best_ari = results['ari'][best_idx]
best_sil = results['silhouette'][best_idx]

print(f"\nBest configuration:")
print(f"  N components: {best_n}")
print(f"  Silhouette: {best_sil:.4f}")
print(f"  ARI: {best_ari:.4f}")

print(f"\nComparison:")
print(f"  Raw features (30D): Silhouette={silhouette_raw:.4f}, ARI={ari_raw:.4f}")
print(f"  Best PCA ({best_n}D):   Silhouette={best_sil:.4f}, ARI={best_ari:.4f}")

if best_ari > ari_raw:
    print(f"\n  PCA IMPROVED clustering by {best_ari - ari_raw:.4f} ARI points!")
else:
    print(f"\n  Raw features performed better or equal.")

# =============================================================================
# 6. Visualization Comparison
# =============================================================================
print("\n" + "=" * 60)
print("6. VISUALIZATION COMPARISON")
print("=" * 60)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Top row: Different PCA components
for ax, n in zip(axes[0], [2, 10, 30]):
    if n == 30:
        X_reduced = X_scaled
        title_suffix = "(Raw)"
    else:
        pca = PCA(n_components=n)
        X_reduced = pca.fit_transform(X_scaled)
        title_suffix = f"(PCA {n}D)"
    
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_reduced)
    ari = adjusted_rand_score(y_true, labels)
    
    # Project to 2D for visualization
    if n > 2:
        pca_2d = PCA(n_components=2)
        X_2d = pca_2d.fit_transform(X_reduced)
    else:
        X_2d = X_reduced
    
    scatter = ax.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap='coolwarm', alpha=0.7)
    ax.set_xlabel('Dim 1')
    ax.set_ylabel('Dim 2')
    ax.set_title(f'K-Means {title_suffix}\nARI: {ari:.3f}')
    ax.grid(True, alpha=0.3)

# Bottom row: True labels for comparison
for ax, n in zip(axes[1], [2, 10, 30]):
    if n == 30:
        X_reduced = X_scaled
    else:
        pca = PCA(n_components=n)
        X_reduced = pca.fit_transform(X_scaled)
    
    if n > 2:
        pca_2d = PCA(n_components=2)
        X_2d = pca_2d.fit_transform(X_reduced)
    else:
        X_2d = X_reduced
    
    scatter = ax.scatter(X_2d[:, 0], X_2d[:, 1], c=y_true, cmap='coolwarm', alpha=0.7)
    ax.set_xlabel('Dim 1')
    ax.set_ylabel('Dim 2')
    ax.set_title('True Labels')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex6_3_comparison.png', dpi=150)
plt.close()
print("Comparison visualization saved to ex6_3_comparison.png")

# =============================================================================
# 7. Summary
# =============================================================================
print("\n" + "=" * 60)
print("7. SUMMARY")
print("=" * 60)

print("""
WHEN DOES DIMENSIONALITY REDUCTION HELP CLUSTERING?
----------------------------------------------------

1. CURSE OF DIMENSIONALITY:
   - In high dimensions, distances become less meaningful
   - All points tend to be equidistant from each other
   - Clustering algorithms struggle to find structure

2. BENEFITS OF PCA BEFORE CLUSTERING:
   - Removes noise from low-variance dimensions
   - Reduces computational cost
   - Can improve cluster separation
   - Makes visualization possible

3. POTENTIAL DRAWBACKS:
   - May lose important information in discarded components
   - Linear assumption may not capture non-linear structure
   - Need to choose number of components

4. FOR THIS DATASET (Breast Cancer):
   - 30 features is not extremely high-dimensional
   - PCA with moderate components (5-15) works well
   - Too few components loses information
   - Too many components includes noise

5. PRACTICAL RECOMMENDATIONS:
   - Try clustering with and without PCA
   - Use explained variance to guide component selection
   - Validate with external metrics if labels available
   - Consider the trade-off between information and noise

6. WHEN PCA HELPS MOST:
   - Very high-dimensional data (hundreds/thousands of features)
   - Noisy data with many uninformative features
   - When clusters are defined by a few principal directions
   - When computational efficiency is important
""")

print("=" * 60)
print("EXERCISE 6.3 COMPLETE")
print("=" * 60)
