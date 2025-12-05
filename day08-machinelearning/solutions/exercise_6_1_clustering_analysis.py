"""
Exercise 6.1: Clustering Analysis
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for clustering analysis with multiple algorithms.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    silhouette_score, davies_bouldin_score, 
    adjusted_rand_score, confusion_matrix
)
from scipy.cluster.hierarchy import dendrogram, linkage

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Data (pretend we don't know true labels)
# =============================================================================
print("=" * 60)
print("1. LOADING DATA")
print("=" * 60)

iris = load_iris()
X = iris.data
y_true = iris.target  # We'll use this only for evaluation, not for clustering

print(f"Samples: {X.shape[0]}")
print(f"Features: {X.shape[1]}")
print("(Pretending we don't know the true labels for clustering)")

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# =============================================================================
# 2. K-Means with Different K Values
# =============================================================================
print("\n" + "=" * 60)
print("2. K-MEANS CLUSTERING (K = 2, 3, 4, 5)")
print("=" * 60)

k_values = [2, 3, 4, 5]
kmeans_results = {}

print("\nK-Means Results:")
print("-" * 60)
print(f"{'K':<5} {'Silhouette':>12} {'Davies-Bouldin':>15} {'Inertia':>12}")
print("-" * 60)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    silhouette = silhouette_score(X_scaled, labels)
    db_score = davies_bouldin_score(X_scaled, labels)
    inertia = kmeans.inertia_
    
    kmeans_results[k] = {
        'labels': labels,
        'silhouette': silhouette,
        'davies_bouldin': db_score,
        'inertia': inertia,
        'model': kmeans
    }
    
    print(f"{k:<5} {silhouette:>12.4f} {db_score:>15.4f} {inertia:>12.2f}")

# =============================================================================
# 3. Visualize K-Means Clusters
# =============================================================================
print("\n" + "=" * 60)
print("3. VISUALIZING K-MEANS CLUSTERS")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for ax, k in zip(axes, k_values):
    labels = kmeans_results[k]['labels']
    
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', alpha=0.7)
    
    # Plot centroids
    centroids_pca = pca.transform(kmeans_results[k]['model'].cluster_centers_)
    ax.scatter(centroids_pca[:, 0], centroids_pca[:, 1], 
               c='red', marker='X', s=200, edgecolors='black', linewidths=2)
    
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_title(f'K-Means (K={k})\nSilhouette: {kmeans_results[k]["silhouette"]:.3f}')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex6_1_kmeans_clusters.png', dpi=150)
plt.close()
print("K-Means clusters saved to ex6_1_kmeans_clusters.png")

# =============================================================================
# 4. Elbow Method
# =============================================================================
print("\n" + "=" * 60)
print("4. ELBOW METHOD")
print("=" * 60)

k_range = range(1, 11)
inertias = []
silhouettes = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    if k > 1:
        silhouettes.append(silhouette_score(X_scaled, kmeans.labels_))
    else:
        silhouettes.append(0)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Elbow plot
ax1 = axes[0]
ax1.plot(k_range, inertias, 'b-o')
ax1.set_xlabel('Number of Clusters (K)')
ax1.set_ylabel('Inertia')
ax1.set_title('Elbow Method')
ax1.axvline(x=3, color='r', linestyle='--', label='Elbow at K=3')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Silhouette plot
ax2 = axes[1]
ax2.plot(list(k_range)[1:], silhouettes[1:], 'g-o')
ax2.set_xlabel('Number of Clusters (K)')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Score vs K')
ax2.axvline(x=2, color='r', linestyle='--', label=f'Best at K=2')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex6_1_elbow_method.png', dpi=150)
plt.close()
print("Elbow method plot saved to ex6_1_elbow_method.png")

print("\nElbow Analysis:")
print("  - Inertia decreases as K increases")
print("  - Elbow point appears around K=3")
print("  - Silhouette score is highest at K=2, but K=3 is also good")

# =============================================================================
# 5. Compare with True Labels
# =============================================================================
print("\n" + "=" * 60)
print("5. COMPARISON WITH TRUE LABELS")
print("=" * 60)

print("\nAdjusted Rand Index (ARI) - measures agreement with true labels:")
for k in k_values:
    labels = kmeans_results[k]['labels']
    ari = adjusted_rand_score(y_true, labels)
    print(f"  K={k}: ARI = {ari:.4f}")

# Confusion matrix for K=3
print("\nConfusion Matrix (K=3 vs True Labels):")
labels_k3 = kmeans_results[3]['labels']
cm = confusion_matrix(y_true, labels_k3)
print(cm)

# =============================================================================
# 6. Hierarchical Clustering
# =============================================================================
print("\n" + "=" * 60)
print("6. HIERARCHICAL CLUSTERING")
print("=" * 60)

# Create dendrogram
fig, ax = plt.subplots(figsize=(12, 6))
linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix, ax=ax, truncate_mode='level', p=5)
ax.set_xlabel('Sample Index')
ax.set_ylabel('Distance')
ax.set_title('Hierarchical Clustering Dendrogram')
ax.axhline(y=10, color='r', linestyle='--', label='Cut at height=10')
ax.legend()

plt.tight_layout()
plt.savefig('ex6_1_dendrogram.png', dpi=150)
plt.close()
print("Dendrogram saved to ex6_1_dendrogram.png")

# Agglomerative clustering with different numbers of clusters
print("\nAgglomerative Clustering Results:")
print("-" * 50)
print(f"{'n_clusters':<12} {'Silhouette':>12} {'ARI':>12}")
print("-" * 50)

for n in [2, 3, 4]:
    agg = AgglomerativeClustering(n_clusters=n, linkage='ward')
    labels = agg.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels)
    ari = adjusted_rand_score(y_true, labels)
    print(f"{n:<12} {sil:>12.4f} {ari:>12.4f}")

# =============================================================================
# 7. DBSCAN
# =============================================================================
print("\n" + "=" * 60)
print("7. DBSCAN CLUSTERING")
print("=" * 60)

# Try different eps and min_samples
eps_values = [0.3, 0.5, 0.7, 1.0]
min_samples_values = [3, 5, 10]

print("\nDBSCAN Results:")
print("-" * 70)
print(f"{'eps':<8} {'min_samples':<12} {'n_clusters':>12} {'n_noise':>10} {'Silhouette':>12}")
print("-" * 70)

best_dbscan = None
best_sil = -1

for eps in eps_values:
    for min_samples in min_samples_values:
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        labels = dbscan.fit_predict(X_scaled)
        
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = np.sum(labels == -1)
        
        if n_clusters > 1:
            # Exclude noise points for silhouette
            mask = labels != -1
            if np.sum(mask) > n_clusters:
                sil = silhouette_score(X_scaled[mask], labels[mask])
            else:
                sil = -1
        else:
            sil = -1
        
        print(f"{eps:<8} {min_samples:<12} {n_clusters:>12} {n_noise:>10} {sil:>12.4f}")
        
        if sil > best_sil:
            best_sil = sil
            best_dbscan = {'eps': eps, 'min_samples': min_samples, 'labels': labels}

print(f"\nBest DBSCAN: eps={best_dbscan['eps']}, min_samples={best_dbscan['min_samples']}")

# Visualize best DBSCAN
fig, ax = plt.subplots(figsize=(8, 6))
labels = best_dbscan['labels']
unique_labels = set(labels)

colors = plt.cm.viridis(np.linspace(0, 1, len(unique_labels)))

for label, color in zip(unique_labels, colors):
    if label == -1:
        color = 'gray'
        marker = 'x'
        label_name = 'Noise'
    else:
        marker = 'o'
        label_name = f'Cluster {label}'
    
    mask = labels == label
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], c=[color], marker=marker, 
               label=label_name, alpha=0.7, s=50)

ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_title(f'DBSCAN (eps={best_dbscan["eps"]}, min_samples={best_dbscan["min_samples"]})')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex6_1_dbscan.png', dpi=150)
plt.close()
print("DBSCAN plot saved to ex6_1_dbscan.png")

# =============================================================================
# 8. Algorithm Comparison
# =============================================================================
print("\n" + "=" * 60)
print("8. ALGORITHM COMPARISON")
print("=" * 60)

# Best results from each algorithm
kmeans_best = kmeans_results[3]
agg_labels = AgglomerativeClustering(n_clusters=3, linkage='ward').fit_predict(X_scaled)
dbscan_labels = best_dbscan['labels']

print("\nComparison (using K=3 for K-Means and Hierarchical):")
print("-" * 50)
print(f"{'Algorithm':<20} {'ARI':>12} {'Silhouette':>12}")
print("-" * 50)

# K-Means
ari_km = adjusted_rand_score(y_true, kmeans_best['labels'])
sil_km = kmeans_best['silhouette']
print(f"{'K-Means':<20} {ari_km:>12.4f} {sil_km:>12.4f}")

# Hierarchical
ari_agg = adjusted_rand_score(y_true, agg_labels)
sil_agg = silhouette_score(X_scaled, agg_labels)
print(f"{'Hierarchical':<20} {ari_agg:>12.4f} {sil_agg:>12.4f}")

# DBSCAN
mask = dbscan_labels != -1
if np.sum(mask) > 1:
    ari_db = adjusted_rand_score(y_true[mask], dbscan_labels[mask])
    sil_db = silhouette_score(X_scaled[mask], dbscan_labels[mask]) if len(set(dbscan_labels[mask])) > 1 else -1
else:
    ari_db = -1
    sil_db = -1
print(f"{'DBSCAN':<20} {ari_db:>12.4f} {sil_db:>12.4f}")

# =============================================================================
# 9. Summary
# =============================================================================
print("\n" + "=" * 60)
print("9. SUMMARY")
print("=" * 60)

print("""
KEY FINDINGS:
-------------

1. K-MEANS:
   - Works well when clusters are spherical and similar size
   - Elbow method suggests K=3 (matching true number of classes)
   - ARI shows good agreement with true labels at K=3

2. HIERARCHICAL CLUSTERING:
   - Dendrogram helps visualize cluster hierarchy
   - Can cut at different heights for different granularity
   - Similar performance to K-Means for this dataset

3. DBSCAN:
   - Finds clusters of arbitrary shape
   - Automatically identifies noise points
   - Sensitive to eps and min_samples parameters
   - May not work well when clusters have varying densities

4. WHICH ALGORITHM RECOVERED TRUE STRUCTURE BEST?
   - For Iris dataset: K-Means and Hierarchical perform similarly
   - Both achieve high ARI when K=3
   - DBSCAN may struggle due to overlapping clusters

5. PRACTICAL RECOMMENDATIONS:
   - Start with K-Means for initial exploration
   - Use silhouette score and elbow method to choose K
   - Try hierarchical for understanding cluster hierarchy
   - Use DBSCAN when clusters have irregular shapes or noise
""")

print("=" * 60)
print("EXERCISE 6.1 COMPLETE")
print("=" * 60)
