"""
Exercise 5.1: Cross-Validation Deep Dive
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for manual K-Fold implementation and comparison.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, r2_score
import time

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Data
# =============================================================================
print("=" * 60)
print("1. LOADING DATA")
print("=" * 60)

# Classification dataset
cancer = load_breast_cancer()
X_clf = cancer.data
y_clf = cancer.target

# Regression dataset
diabetes = load_diabetes()
X_reg = diabetes.data
y_reg = diabetes.target

print(f"Classification dataset: {X_clf.shape[0]} samples, {X_clf.shape[1]} features")
print(f"Regression dataset: {X_reg.shape[0]} samples, {X_reg.shape[1]} features")

# =============================================================================
# 2. Manual K-Fold Implementation
# =============================================================================
print("\n" + "=" * 60)
print("2. MANUAL K-FOLD IMPLEMENTATION")
print("=" * 60)

def manual_kfold_cv(X, y, model, n_splits=5, scoring='accuracy', random_state=42):
    """
    Manual implementation of K-Fold cross-validation.
    
    Parameters:
    -----------
    X : array-like, features
    y : array-like, target
    model : sklearn estimator
    n_splits : int, number of folds
    scoring : str, 'accuracy' for classification, 'r2' for regression
    random_state : int, for reproducibility
    
    Returns:
    --------
    scores : list of scores for each fold
    """
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    scores = []
    
    for fold, (train_idx, test_idx) in enumerate(kf.split(X)):
        # Split data
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        # Clone model to avoid fitting issues
        from sklearn.base import clone
        model_clone = clone(model)
        
        # Train model
        model_clone.fit(X_train, y_train)
        
        # Predict
        y_pred = model_clone.predict(X_test)
        
        # Score
        if scoring == 'accuracy':
            score = accuracy_score(y_test, y_pred)
        elif scoring == 'r2':
            score = r2_score(y_test, y_pred)
        else:
            raise ValueError(f"Unknown scoring: {scoring}")
        
        scores.append(score)
        print(f"  Fold {fold + 1}: {score:.4f}")
    
    return scores

# Test manual implementation
print("\nManual K-Fold (Classification, k=5):")
model_clf = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])
manual_scores = manual_kfold_cv(X_clf, y_clf, model_clf, n_splits=5, scoring='accuracy')
print(f"Mean: {np.mean(manual_scores):.4f} +/- {np.std(manual_scores):.4f}")

# =============================================================================
# 3. Compare to cross_val_score
# =============================================================================
print("\n" + "=" * 60)
print("3. COMPARISON WITH cross_val_score")
print("=" * 60)

# Using cross_val_score
sklearn_scores = cross_val_score(
    model_clf, X_clf, y_clf, 
    cv=KFold(n_splits=5, shuffle=True, random_state=42),
    scoring='accuracy'
)

print("\nSklearn cross_val_score (Classification, k=5):")
for i, score in enumerate(sklearn_scores):
    print(f"  Fold {i + 1}: {score:.4f}")
print(f"Mean: {np.mean(sklearn_scores):.4f} +/- {np.std(sklearn_scores):.4f}")

print("\nComparison:")
print(f"  Manual:  {np.mean(manual_scores):.4f} +/- {np.std(manual_scores):.4f}")
print(f"  Sklearn: {np.mean(sklearn_scores):.4f} +/- {np.std(sklearn_scores):.4f}")
print(f"  Match: {np.allclose(manual_scores, sklearn_scores)}")

# =============================================================================
# 4. Different K Values
# =============================================================================
print("\n" + "=" * 60)
print("4. EFFECT OF DIFFERENT K VALUES")
print("=" * 60)

k_values = [3, 5, 10, 20]
results = {'k': [], 'mean': [], 'std': [], 'time': []}

print("\nClassification (Logistic Regression):")
print("-" * 50)
print(f"{'K':<5} {'Mean':>10} {'Std':>10} {'Time (s)':>10}")
print("-" * 50)

for k in k_values:
    start_time = time.time()
    scores = cross_val_score(
        model_clf, X_clf, y_clf,
        cv=KFold(n_splits=k, shuffle=True, random_state=42),
        scoring='accuracy'
    )
    elapsed = time.time() - start_time
    
    results['k'].append(k)
    results['mean'].append(scores.mean())
    results['std'].append(scores.std())
    results['time'].append(elapsed)
    
    print(f"{k:<5} {scores.mean():>10.4f} {scores.std():>10.4f} {elapsed:>10.4f}")

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Mean score vs K
ax1 = axes[0]
ax1.plot(results['k'], results['mean'], 'b-o', markersize=8)
ax1.fill_between(results['k'], 
                  np.array(results['mean']) - np.array(results['std']),
                  np.array(results['mean']) + np.array(results['std']),
                  alpha=0.2)
ax1.set_xlabel('K (Number of Folds)')
ax1.set_ylabel('Mean CV Score')
ax1.set_title('Mean Score vs K')
ax1.grid(True, alpha=0.3)

# Std vs K
ax2 = axes[1]
ax2.plot(results['k'], results['std'], 'r-o', markersize=8)
ax2.set_xlabel('K (Number of Folds)')
ax2.set_ylabel('Std of CV Scores')
ax2.set_title('Score Variability vs K')
ax2.grid(True, alpha=0.3)

# Time vs K
ax3 = axes[2]
ax3.plot(results['k'], results['time'], 'g-o', markersize=8)
ax3.set_xlabel('K (Number of Folds)')
ax3.set_ylabel('Time (seconds)')
ax3.set_title('Computational Cost vs K')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex5_1_k_comparison.png', dpi=150)
plt.close()
print("\nK comparison plot saved to ex5_1_k_comparison.png")

# =============================================================================
# 5. Regular K-Fold vs Stratified K-Fold
# =============================================================================
print("\n" + "=" * 60)
print("5. REGULAR K-FOLD vs STRATIFIED K-FOLD")
print("=" * 60)

# Create imbalanced dataset for demonstration
from sklearn.utils import resample
X_majority = X_clf[y_clf == 1]
X_minority = X_clf[y_clf == 0]
y_majority = y_clf[y_clf == 1]
y_minority = y_clf[y_clf == 0]

# Downsample to create imbalance
X_minority_down, y_minority_down = resample(X_minority, y_minority, n_samples=50, random_state=42)
X_imb = np.vstack([X_majority, X_minority_down])
y_imb = np.hstack([y_majority, y_minority_down])

print(f"\nImbalanced dataset:")
print(f"  Class 0: {np.sum(y_imb == 0)} ({100*np.mean(y_imb == 0):.1f}%)")
print(f"  Class 1: {np.sum(y_imb == 1)} ({100*np.mean(y_imb == 1):.1f}%)")

# Compare class distribution in folds
print("\nClass distribution in each fold:")
print("\nRegular K-Fold:")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for fold, (train_idx, test_idx) in enumerate(kf.split(X_imb)):
    train_ratio = np.mean(y_imb[train_idx] == 0)
    test_ratio = np.mean(y_imb[test_idx] == 0)
    print(f"  Fold {fold+1}: Train class 0 = {100*train_ratio:.1f}%, Test class 0 = {100*test_ratio:.1f}%")

print("\nStratified K-Fold:")
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for fold, (train_idx, test_idx) in enumerate(skf.split(X_imb, y_imb)):
    train_ratio = np.mean(y_imb[train_idx] == 0)
    test_ratio = np.mean(y_imb[test_idx] == 0)
    print(f"  Fold {fold+1}: Train class 0 = {100*train_ratio:.1f}%, Test class 0 = {100*test_ratio:.1f}%")

# Compare CV scores
print("\nCV Score Comparison:")
kf_scores = cross_val_score(model_clf, X_imb, y_imb, cv=kf, scoring='accuracy')
skf_scores = cross_val_score(model_clf, X_imb, y_imb, cv=skf, scoring='accuracy')

print(f"  Regular K-Fold:    {kf_scores.mean():.4f} +/- {kf_scores.std():.4f}")
print(f"  Stratified K-Fold: {skf_scores.mean():.4f} +/- {skf_scores.std():.4f}")

# =============================================================================
# 6. Regression Cross-Validation
# =============================================================================
print("\n" + "=" * 60)
print("6. REGRESSION CROSS-VALIDATION")
print("=" * 60)

model_reg = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', Ridge(alpha=1.0))
])

print("\nRegression CV with different K values:")
print("-" * 50)
print(f"{'K':<5} {'Mean R²':>12} {'Std':>10}")
print("-" * 50)

for k in k_values:
    scores = cross_val_score(
        model_reg, X_reg, y_reg,
        cv=KFold(n_splits=k, shuffle=True, random_state=42),
        scoring='r2'
    )
    print(f"{k:<5} {scores.mean():>12.4f} {scores.std():>10.4f}")

# =============================================================================
# 7. Summary
# =============================================================================
print("\n" + "=" * 60)
print("7. SUMMARY")
print("=" * 60)

print("""
KEY FINDINGS:
-------------

1. MANUAL vs SKLEARN:
   - Manual implementation matches sklearn's cross_val_score
   - Sklearn is more efficient and handles edge cases

2. EFFECT OF K:
   - Higher K: More training data per fold, lower bias, higher variance
   - Lower K: Less training data, higher bias, lower variance
   - K=5 or K=10 are common choices (good balance)
   - K=N (Leave-One-Out): Highest variance, computationally expensive

3. REGULAR vs STRATIFIED K-FOLD:
   - Stratified maintains class proportions in each fold
   - Essential for imbalanced datasets
   - Reduces variance in CV scores
   - Always use StratifiedKFold for classification!

4. COMPUTATIONAL COST:
   - Increases linearly with K
   - For large datasets, K=5 is often sufficient
   - For small datasets, K=10 or LOOCV may be needed

RECOMMENDATIONS:
----------------
- Classification: Use StratifiedKFold with K=5 or K=10
- Regression: Use KFold with K=5 or K=10
- Small datasets (<100): Consider K=10 or LOOCV
- Large datasets (>10000): K=5 is usually sufficient
""")

print("=" * 60)
print("EXERCISE 5.1 COMPLETE")
print("=" * 60)
