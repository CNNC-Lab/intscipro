"""
Exercise 3.2: Multi-Class Iris Classification
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for multi-class classification with cross-validation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    ConfusionMatrixDisplay
)

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load and Explore Iris Dataset
# =============================================================================
print("=" * 60)
print("1. DATA EXPLORATION")
print("=" * 60)

iris = load_iris()
X = iris.data
y = iris.target

print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Feature names: {iris.feature_names}")
print(f"Target names: {iris.target_names}")
print(f"\nClass distribution:")
for i, name in enumerate(iris.target_names):
    print(f"  - {name}: {np.sum(y == i)} samples")

# Visualize pairwise relationships
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.flatten()

feature_pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
for ax, (i, j) in zip(axes, feature_pairs):
    for class_idx, class_name in enumerate(iris.target_names):
        mask = y == class_idx
        ax.scatter(X[mask, i], X[mask, j], label=class_name, alpha=0.7)
    ax.set_xlabel(iris.feature_names[i])
    ax.set_ylabel(iris.feature_names[j])
    ax.legend(fontsize=8)

plt.suptitle('Iris Dataset: Pairwise Feature Plots')
plt.tight_layout()
plt.savefig('ex3_2_iris_exploration.png', dpi=150)
plt.close()
print("\nExploration plot saved to ex3_2_iris_exploration.png")

# =============================================================================
# 2. Train/Test Split (70/30)
# =============================================================================
print("\n" + "=" * 60)
print("2. DATA SPLITTING")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")
print(f"Training class distribution: {np.bincount(y_train)}")
print(f"Test class distribution: {np.bincount(y_test)}")

# =============================================================================
# 3. Train Multiple Classifiers with 5-Fold CV
# =============================================================================
print("\n" + "=" * 60)
print("3. TRAINING WITH 5-FOLD CROSS-VALIDATION")
print("=" * 60)

# Define models
models = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ]),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', random_state=42))
    ]),
    'KNN': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', KNeighborsClassifier(n_neighbors=5))
    ]),
    'Decision Tree': DecisionTreeClassifier(random_state=42)
}

# Cross-validation results
cv_results = {}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("\nCross-Validation Results (on training set):")
print("-" * 50)

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    cv_results[name] = {
        'mean': scores.mean(),
        'std': scores.std(),
        'scores': scores
    }
    print(f"{name:25s}: {scores.mean():.4f} +/- {scores.std():.4f}")

# =============================================================================
# 4. Evaluate Best Model on Test Set
# =============================================================================
print("\n" + "=" * 60)
print("4. BEST MODEL EVALUATION ON TEST SET")
print("=" * 60)

# Find best model based on CV mean score
best_model_name = max(cv_results.keys(), key=lambda k: cv_results[k]['mean'])
best_model = models[best_model_name]

print(f"\nBest model by CV score: {best_model_name}")
print(f"CV Score: {cv_results[best_model_name]['mean']:.4f} +/- {cv_results[best_model_name]['std']:.4f}")

# Train on full training set and evaluate on test set
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

print(f"\nTest Set Accuracy: {test_accuracy:.4f}")

# Compare CV score to test performance
print(f"\nCV Score vs Test Score:")
print(f"  CV Score:   {cv_results[best_model_name]['mean']:.4f}")
print(f"  Test Score: {test_accuracy:.4f}")
print(f"  Difference: {cv_results[best_model_name]['mean'] - test_accuracy:.4f}")

# =============================================================================
# 5. Multi-Class Confusion Matrix
# =============================================================================
print("\n" + "=" * 60)
print("5. MULTI-CLASS CONFUSION MATRIX")
print("=" * 60)

# Train all models and create confusion matrices
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for ax, (name, model) in zip(axes[:-1], models.items()):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm, display_labels=iris.target_names).plot(ax=ax)
    ax.set_title(f'{name}')

# Hide last empty subplot
axes[-1].axis('off')

plt.suptitle('Confusion Matrices for All Models')
plt.tight_layout()
plt.savefig('ex3_2_confusion_matrices.png', dpi=150)
plt.close()
print("Confusion matrices saved to ex3_2_confusion_matrices.png")

# =============================================================================
# 6. Per-Class Precision, Recall, F1
# =============================================================================
print("\n" + "=" * 60)
print("6. PER-CLASS METRICS")
print("=" * 60)

# Use best model
y_pred_best = best_model.predict(X_test)

print(f"\nClassification Report for {best_model_name}:")
print(classification_report(y_test, y_pred_best, target_names=iris.target_names))

# Analyze confusion matrix
cm = confusion_matrix(y_test, y_pred_best)
print("Confusion Matrix Analysis:")
print(cm)

# =============================================================================
# 7. Answer Questions
# =============================================================================
print("\n" + "=" * 60)
print("7. ANALYSIS QUESTIONS")
print("=" * 60)

# Which class is easiest to predict?
print("\n--- Which class is easiest to predict? ---")
per_class_accuracy = cm.diagonal() / cm.sum(axis=1)
for i, name in enumerate(iris.target_names):
    print(f"  {name}: {per_class_accuracy[i]:.2%} accuracy")
easiest_class = iris.target_names[np.argmax(per_class_accuracy)]
print(f"\nEasiest class: {easiest_class}")

# Which classes are most confused?
print("\n--- Which classes are most confused with each other? ---")
# Look at off-diagonal elements
cm_no_diag = cm.copy()
np.fill_diagonal(cm_no_diag, 0)
max_confusion_idx = np.unravel_index(np.argmax(cm_no_diag), cm_no_diag.shape)
print(f"Most confused pair: {iris.target_names[max_confusion_idx[0]]} <-> {iris.target_names[max_confusion_idx[1]]}")
print(f"  {cm_no_diag[max_confusion_idx[0], max_confusion_idx[1]]} samples misclassified")

# CV vs Test comparison
print("\n--- How do CV scores compare to test performance? ---")
print("Model comparison (CV vs Test):")
for name, model in models.items():
    model.fit(X_train, y_train)
    test_acc = accuracy_score(y_test, model.predict(X_test))
    cv_mean = cv_results[name]['mean']
    diff = cv_mean - test_acc
    print(f"  {name:25s}: CV={cv_mean:.4f}, Test={test_acc:.4f}, Diff={diff:+.4f}")

print("\n" + "=" * 60)
print("EXERCISE 3.2 COMPLETE")
print("=" * 60)
