"""
Exercise 3.3: Handling Imbalanced Data
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution demonstrating why accuracy is misleading for imbalanced data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils import resample
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, ConfusionMatrixDisplay
)

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load and Create Imbalanced Dataset
# =============================================================================
print("=" * 60)
print("1. CREATING IMBALANCED DATASET")
print("=" * 60)

# Load original data
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

print("Original dataset:")
print(f"  - Malignant (0): {np.sum(y == 0)} ({100 * np.sum(y == 0) / len(y):.1f}%)")
print(f"  - Benign (1): {np.sum(y == 1)} ({100 * np.sum(y == 1) / len(y):.1f}%)")

# Create imbalanced dataset (90% malignant, 10% benign)
X_majority = X[y == 0]  # Malignant
X_minority = X[y == 1]  # Benign
y_majority = y[y == 0]
y_minority = y[y == 1]

# Downsample minority to 10% of majority
n_minority_samples = int(len(X_majority) * 0.1)
X_minority_downsampled, y_minority_downsampled = resample(
    X_minority, y_minority,
    n_samples=n_minority_samples,
    random_state=42
)

# Combine
X_imbalanced = np.vstack((X_majority, X_minority_downsampled))
y_imbalanced = np.hstack((y_majority, y_minority_downsampled))

print("\nImbalanced dataset:")
print(f"  - Malignant (0): {np.sum(y_imbalanced == 0)} ({100 * np.sum(y_imbalanced == 0) / len(y_imbalanced):.1f}%)")
print(f"  - Benign (1): {np.sum(y_imbalanced == 1)} ({100 * np.sum(y_imbalanced == 1) / len(y_imbalanced):.1f}%)")

# =============================================================================
# 2. Split Data
# =============================================================================
print("\n" + "=" * 60)
print("2. DATA SPLITTING")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X_imbalanced, y_imbalanced, test_size=0.2, random_state=42, stratify=y_imbalanced
)

print(f"Training set: {len(X_train)} samples")
print(f"  - Class 0: {np.sum(y_train == 0)} ({100 * np.sum(y_train == 0) / len(y_train):.1f}%)")
print(f"  - Class 1: {np.sum(y_train == 1)} ({100 * np.sum(y_train == 1) / len(y_train):.1f}%)")

print(f"\nTest set: {len(X_test)} samples")
print(f"  - Class 0: {np.sum(y_test == 0)} ({100 * np.sum(y_test == 0) / len(y_test):.1f}%)")
print(f"  - Class 1: {np.sum(y_test == 1)} ({100 * np.sum(y_test == 1) / len(y_test):.1f}%)")

# =============================================================================
# 3. Train Classifiers WITHOUT Class Balancing
# =============================================================================
print("\n" + "=" * 60)
print("3. CLASSIFIERS WITHOUT CLASS BALANCING")
print("=" * 60)

# Define models without class_weight
models_unbalanced = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ]),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', random_state=42))
    ])
}

print("\nResults WITHOUT class balancing:")
print("-" * 70)
print(f"{'Model':<25} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
print("-" * 70)

results_unbalanced = {}
for name, model in models_unbalanced.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    
    results_unbalanced[name] = {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1}
    print(f"{name:<25} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f}")

# =============================================================================
# 4. Train Classifiers WITH Class Balancing
# =============================================================================
print("\n" + "=" * 60)
print("4. CLASSIFIERS WITH class_weight='balanced'")
print("=" * 60)

# Define models with class_weight='balanced'
models_balanced = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'))
    ]),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced'),
    'SVM': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', random_state=42, class_weight='balanced'))
    ])
}

print("\nResults WITH class_weight='balanced':")
print("-" * 70)
print(f"{'Model':<25} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
print("-" * 70)

results_balanced = {}
for name, model in models_balanced.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    
    results_balanced[name] = {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1}
    print(f"{name:<25} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f}")

# =============================================================================
# 5. Compare Accuracy vs F1-Score
# =============================================================================
print("\n" + "=" * 60)
print("5. ACCURACY vs F1-SCORE COMPARISON")
print("=" * 60)

print("\nComparison (Unbalanced vs Balanced):")
print("-" * 80)
print(f"{'Model':<25} {'Acc (Unbal)':>12} {'Acc (Bal)':>12} {'F1 (Unbal)':>12} {'F1 (Bal)':>12}")
print("-" * 80)

for name in models_unbalanced.keys():
    acc_unbal = results_unbalanced[name]['accuracy']
    acc_bal = results_balanced[name]['accuracy']
    f1_unbal = results_unbalanced[name]['f1']
    f1_bal = results_balanced[name]['f1']
    print(f"{name:<25} {acc_unbal:>12.4f} {acc_bal:>12.4f} {f1_unbal:>12.4f} {f1_bal:>12.4f}")

# =============================================================================
# 6. Stratified Cross-Validation
# =============================================================================
print("\n" + "=" * 60)
print("6. STRATIFIED CROSS-VALIDATION")
print("=" * 60)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("\nStratified 5-Fold CV Results (with class_weight='balanced'):")
print("-" * 60)

for name, model in models_balanced.items():
    # CV with accuracy
    acc_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    # CV with F1
    f1_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='f1')
    
    print(f"\n{name}:")
    print(f"  Accuracy: {acc_scores.mean():.4f} +/- {acc_scores.std():.4f}")
    print(f"  F1-Score: {f1_scores.mean():.4f} +/- {f1_scores.std():.4f}")

# =============================================================================
# 7. Confusion Matrix Comparison
# =============================================================================
print("\n" + "=" * 60)
print("7. CONFUSION MATRIX COMPARISON")
print("=" * 60)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Top row: Unbalanced
for ax, (name, model) in zip(axes[0], models_unbalanced.items()):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm, display_labels=['Malignant', 'Benign']).plot(ax=ax)
    ax.set_title(f'{name}\n(No Balancing)')

# Bottom row: Balanced
for ax, (name, model) in zip(axes[1], models_balanced.items()):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm, display_labels=['Malignant', 'Benign']).plot(ax=ax)
    ax.set_title(f'{name}\n(class_weight=balanced)')

plt.suptitle('Confusion Matrices: Unbalanced vs Balanced Models', fontsize=14)
plt.tight_layout()
plt.savefig('ex3_3_confusion_comparison.png', dpi=150)
plt.close()
print("Confusion matrix comparison saved to ex3_3_confusion_comparison.png")

# =============================================================================
# 8. Key Takeaways
# =============================================================================
print("\n" + "=" * 60)
print("8. KEY TAKEAWAYS")
print("=" * 60)

print("""
WHY ACCURACY IS MISLEADING FOR IMBALANCED DATA:
------------------------------------------------
1. A naive classifier that always predicts the majority class would achieve
   ~90% accuracy on this dataset, but would completely miss all minority
   class samples (0% recall for minority class).

2. High accuracy can hide poor performance on the minority class, which is
   often the class of interest (e.g., detecting rare diseases).

3. F1-score balances precision and recall, making it more informative for
   imbalanced datasets.

SOLUTIONS FOR IMBALANCED DATA:
------------------------------
1. Use class_weight='balanced' to give more importance to minority class
2. Use stratified sampling to maintain class proportions in train/test splits
3. Use appropriate metrics (F1, precision, recall, AUC-ROC) instead of accuracy
4. Consider resampling techniques (SMOTE, undersampling, oversampling)
5. Adjust decision threshold based on cost of false positives vs false negatives
""")

print("=" * 60)
print("EXERCISE 3.3 COMPLETE")
print("=" * 60)
