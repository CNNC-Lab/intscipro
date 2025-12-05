"""
Challenge 8.3: Multi-Class Cell Type Classification
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for multi-class classification with pipeline optimization.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import (
    train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
)
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    ConfusionMatrixDisplay
)

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Iris Dataset (3 cell types)
# =============================================================================
print("=" * 60)
print("1. LOADING IRIS DATASET (3 cell types)")
print("=" * 60)

iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
feature_names = iris.feature_names

print(f"Samples: {X.shape[0]}")
print(f"Features: {X.shape[1]}")
print(f"Classes: {class_names}")
print(f"Class distribution: {np.bincount(y)}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"\nTraining samples: {len(y_train)}")
print(f"Test samples: {len(y_test)}")

# =============================================================================
# 2. Build Pipeline with Grid Search
# =============================================================================
print("\n" + "=" * 60)
print("2. PIPELINE WITH GRID SEARCH")
print("=" * 60)

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('classifier', SVC(random_state=42))
])

# Parameter grid
param_grid = {
    'pca__n_components': [2, 3, 4],  # Iris has 4 features
    'classifier__C': [0.1, 1.0, 10.0],
    'classifier__kernel': ['linear', 'rbf'],
    'classifier__gamma': ['scale', 'auto']
}

print("Parameter grid:")
for param, values in param_grid.items():
    print(f"  {param}: {values}")

# Grid Search
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(
    pipeline, param_grid, cv=cv, scoring='accuracy',
    return_train_score=True, n_jobs=-1, verbose=1
)
grid_search.fit(X_train, y_train)

print(f"\nBest parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")

# Test set evaluation
y_pred = grid_search.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {test_accuracy:.4f}")

# =============================================================================
# 3. One-vs-Rest Binary Classifiers
# =============================================================================
print("\n" + "=" * 60)
print("3. ONE-VS-REST BINARY CLASSIFIERS")
print("=" * 60)

# Create OvR classifiers for each class
ovr_results = {}

for class_idx, class_name in enumerate(class_names):
    print(f"\n--- {class_name} vs Rest ---")
    
    # Create binary labels
    y_binary = (y == class_idx).astype(int)
    y_train_binary = (y_train == class_idx).astype(int)
    y_test_binary = (y_test == class_idx).astype(int)
    
    # Train binary classifier
    pipeline_binary = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(random_state=42))
    ])
    
    cv_scores = cross_val_score(pipeline_binary, X_train, y_train_binary, cv=cv, scoring='accuracy')
    pipeline_binary.fit(X_train, y_train_binary)
    
    y_pred_binary = pipeline_binary.predict(X_test)
    test_acc = accuracy_score(y_test_binary, y_pred_binary)
    
    ovr_results[class_name] = {
        'cv_score': cv_scores.mean(),
        'test_acc': test_acc,
        'model': pipeline_binary
    }
    
    print(f"  CV Score: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")
    print(f"  Test Accuracy: {test_acc:.4f}")

# Compare to multi-class
print("\n--- Comparison ---")
print(f"Multi-class SVM: {test_accuracy:.4f}")
print("One-vs-Rest:")
for name, results in ovr_results.items():
    print(f"  {name}: {results['test_acc']:.4f}")

# =============================================================================
# 4. Error Analysis
# =============================================================================
print("\n" + "=" * 60)
print("4. ERROR ANALYSIS")
print("=" * 60)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

# Which classes are confused?
print("\nMisclassification Analysis:")
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

for i, class_i in enumerate(class_names):
    for j, class_j in enumerate(class_names):
        if i != j and cm[i, j] > 0:
            print(f"  {class_i} misclassified as {class_j}: {cm[i, j]} times ({cm_normalized[i, j]:.1%})")

# =============================================================================
# 5. Feature Analysis
# =============================================================================
print("\n" + "=" * 60)
print("5. FEATURE ANALYSIS")
print("=" * 60)

# Train a simple logistic regression for interpretability
lr_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(multi_class='multinomial', random_state=42))
])
lr_pipeline.fit(X_train, y_train)

# Get coefficients
coefs = lr_pipeline.named_steps['classifier'].coef_

print("\nFeature importance (Logistic Regression coefficients):")
print("-" * 60)
print(f"{'Feature':<20}", end='')
for name in class_names:
    print(f"{name:>12}", end='')
print()
print("-" * 60)

for i, feat in enumerate(feature_names):
    print(f"{feat:<20}", end='')
    for j in range(len(class_names)):
        print(f"{coefs[j, i]:>12.3f}", end='')
    print()

# Which features distinguish each class?
print("\nMost important feature for each class:")
for j, class_name in enumerate(class_names):
    most_important_idx = np.argmax(np.abs(coefs[j]))
    print(f"  {class_name}: {feature_names[most_important_idx]} (coef={coefs[j, most_important_idx]:.3f})")

# =============================================================================
# 6. Decision Boundary Visualization
# =============================================================================
print("\n" + "=" * 60)
print("6. DECISION BOUNDARY VISUALIZATION")
print("=" * 60)

# Use PCA to reduce to 2D for visualization
pca_2d = PCA(n_components=2)
X_train_2d = pca_2d.fit_transform(StandardScaler().fit_transform(X_train))
X_test_2d = pca_2d.transform(StandardScaler().fit_transform(X_test))

# Train SVM on 2D data
svm_2d = SVC(kernel='rbf', C=1.0, random_state=42)
svm_2d.fit(X_train_2d, y_train)

# Create mesh for decision boundary
h = 0.02
x_min, x_max = X_train_2d[:, 0].min() - 1, X_train_2d[:, 0].max() + 1
y_min, y_max = X_train_2d[:, 1].min() - 1, X_train_2d[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = svm_2d.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Decision boundary
ax1 = axes[0]
ax1.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
scatter = ax1.scatter(X_train_2d[:, 0], X_train_2d[:, 1], c=y_train, cmap='viridis', edgecolors='k')
ax1.set_xlabel('PC1')
ax1.set_ylabel('PC2')
ax1.set_title('Decision Boundaries (SVM on PCA)')
ax1.legend(handles=scatter.legend_elements()[0], labels=list(class_names))

# Confusion matrix heatmap
ax2 = axes[1]
ConfusionMatrixDisplay(cm, display_labels=class_names).plot(ax=ax2, cmap='Blues')
ax2.set_title('Confusion Matrix')

# Feature importance
ax3 = axes[2]
x_pos = np.arange(len(feature_names))
width = 0.25
for j, class_name in enumerate(class_names):
    ax3.bar(x_pos + j*width, np.abs(coefs[j]), width, label=class_name, alpha=0.7)
ax3.set_xticks(x_pos + width)
ax3.set_xticklabels([f.replace(' ', '\n') for f in feature_names], fontsize=8)
ax3.set_ylabel('|Coefficient|')
ax3.set_title('Feature Importance by Class')
ax3.legend()
ax3.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('challenge_8_3_multiclass.png', dpi=150)
plt.close()
print("Visualization saved to challenge_8_3_multiclass.png")

# =============================================================================
# 7. Why Classes Are Confused
# =============================================================================
print("\n" + "=" * 60)
print("7. WHY CLASSES ARE CONFUSED")
print("=" * 60)

# Pairwise feature analysis
print("\nPairwise class separation analysis:")
print("-" * 50)

for i in range(len(class_names)):
    for j in range(i+1, len(class_names)):
        class_i_data = X[y == i]
        class_j_data = X[y == j]
        
        # Calculate separation for each feature
        separations = []
        for f in range(X.shape[1]):
            mean_diff = np.abs(class_i_data[:, f].mean() - class_j_data[:, f].mean())
            pooled_std = np.sqrt((class_i_data[:, f].std()**2 + class_j_data[:, f].std()**2) / 2)
            separation = mean_diff / (pooled_std + 1e-10)
            separations.append(separation)
        
        best_feature = np.argmax(separations)
        print(f"\n{class_names[i]} vs {class_names[j]}:")
        print(f"  Best separating feature: {feature_names[best_feature]}")
        print(f"  Separation score: {separations[best_feature]:.2f}")
        
        if separations[best_feature] < 2:
            print(f"  WARNING: Low separation - classes may be confused!")

# =============================================================================
# 8. Summary
# =============================================================================
print("\n" + "=" * 60)
print("8. SUMMARY")
print("=" * 60)

print(f"""
MULTI-CLASS CLASSIFICATION RESULTS:
-----------------------------------

1. Best Pipeline Configuration:
   - PCA components: {grid_search.best_params_['pca__n_components']}
   - SVM kernel: {grid_search.best_params_['classifier__kernel']}
   - SVM C: {grid_search.best_params_['classifier__C']}
   - CV Score: {grid_search.best_score_:.4f}
   - Test Accuracy: {test_accuracy:.4f}

2. One-vs-Rest Performance:
   - Setosa vs Rest: {ovr_results['setosa']['test_acc']:.4f}
   - Versicolor vs Rest: {ovr_results['versicolor']['test_acc']:.4f}
   - Virginica vs Rest: {ovr_results['virginica']['test_acc']:.4f}

3. Class Confusion:
   - Setosa is easily separable (different petal dimensions)
   - Versicolor and Virginica are sometimes confused
   - Petal length/width are most discriminative

4. Key Features:
   - Petal length and width are most important
   - Sepal measurements are less discriminative
   - Feature scaling is essential for SVM

RECOMMENDATIONS:
----------------
1. For multi-class: Use native multi-class algorithms (SVM, RF)
2. For interpretability: Use One-vs-Rest with simple classifiers
3. Always analyze confusion matrix to understand errors
4. Feature importance helps explain model decisions
""")

print("=" * 60)
print("CHALLENGE 8.3 COMPLETE")
print("=" * 60)
