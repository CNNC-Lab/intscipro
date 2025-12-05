"""
Exercise 5.3: Validation Curves
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for hyperparameter tuning using validation curves.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import validation_curve, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Data
# =============================================================================
print("=" * 60)
print("1. LOADING DATA")
print("=" * 60)

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

print(f"Samples: {X.shape[0]}")
print(f"Features: {X.shape[1]}")

# =============================================================================
# 2. Validation Curve for Decision Tree max_depth
# =============================================================================
print("\n" + "=" * 60)
print("2. VALIDATION CURVE: Decision Tree max_depth")
print("=" * 60)

param_range = range(1, 21)

train_scores, val_scores = validation_curve(
    DecisionTreeClassifier(random_state=42),
    X, y,
    param_name='max_depth',
    param_range=param_range,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
val_mean = val_scores.mean(axis=1)
val_std = val_scores.std(axis=1)

# Find optimal max_depth
optimal_depth = param_range[np.argmax(val_mean)]
optimal_score = val_mean[np.argmax(val_mean)]

print(f"\nOptimal max_depth: {optimal_depth}")
print(f"Best validation score: {optimal_score:.4f}")

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(param_range, train_mean, 'b-o', label='Training Score')
ax.fill_between(param_range, train_mean - train_std, train_mean + train_std, alpha=0.2, color='blue')
ax.plot(param_range, val_mean, 'r-o', label='Validation Score')
ax.fill_between(param_range, val_mean - val_std, val_mean + val_std, alpha=0.2, color='red')

ax.axvline(x=optimal_depth, color='green', linestyle='--', label=f'Optimal depth = {optimal_depth}')
ax.set_xlabel('max_depth')
ax.set_ylabel('Accuracy')
ax.set_title('Validation Curve: Decision Tree max_depth')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex5_3_validation_curve_tree.png', dpi=150)
plt.close()
print("Validation curve saved to ex5_3_validation_curve_tree.png")

# =============================================================================
# 3. Validation Curve for SVM C parameter
# =============================================================================
print("\n" + "=" * 60)
print("3. VALIDATION CURVE: SVM C parameter")
print("=" * 60)

# Scale data for SVM
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

param_range_C = np.logspace(-3, 3, 7)

train_scores_svm, val_scores_svm = validation_curve(
    SVC(kernel='rbf', random_state=42),
    X_scaled, y,
    param_name='C',
    param_range=param_range_C,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

train_mean_svm = train_scores_svm.mean(axis=1)
val_mean_svm = val_scores_svm.mean(axis=1)

optimal_C = param_range_C[np.argmax(val_mean_svm)]
optimal_score_svm = val_mean_svm[np.argmax(val_mean_svm)]

print(f"\nOptimal C: {optimal_C:.4f}")
print(f"Best validation score: {optimal_score_svm:.4f}")

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.semilogx(param_range_C, train_mean_svm, 'b-o', label='Training Score')
ax.semilogx(param_range_C, val_mean_svm, 'r-o', label='Validation Score')
ax.axvline(x=optimal_C, color='green', linestyle='--', label=f'Optimal C = {optimal_C:.3f}')
ax.set_xlabel('C (log scale)')
ax.set_ylabel('Accuracy')
ax.set_title('Validation Curve: SVM C Parameter')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex5_3_validation_curve_svm.png', dpi=150)
plt.close()
print("Validation curve saved to ex5_3_validation_curve_svm.png")

# =============================================================================
# 4. Multiple Parameters Validation Curves
# =============================================================================
print("\n" + "=" * 60)
print("4. MULTIPLE PARAMETERS VALIDATION CURVES")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Random Forest n_estimators
print("\nComputing validation curve for Random Forest n_estimators...")
param_range_n = [10, 25, 50, 100, 150, 200]
train_scores_rf, val_scores_rf = validation_curve(
    RandomForestClassifier(random_state=42),
    X, y,
    param_name='n_estimators',
    param_range=param_range_n,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

ax1 = axes[0, 0]
ax1.plot(param_range_n, train_scores_rf.mean(axis=1), 'b-o', label='Training')
ax1.plot(param_range_n, val_scores_rf.mean(axis=1), 'r-o', label='Validation')
ax1.set_xlabel('n_estimators')
ax1.set_ylabel('Accuracy')
ax1.set_title('Random Forest: n_estimators')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Random Forest max_depth
print("Computing validation curve for Random Forest max_depth...")
param_range_depth = [2, 5, 10, 15, 20, None]
train_scores_rf2, val_scores_rf2 = validation_curve(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X, y,
    param_name='max_depth',
    param_range=param_range_depth,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

ax2 = axes[0, 1]
x_labels = [str(d) if d is not None else 'None' for d in param_range_depth]
ax2.plot(range(len(param_range_depth)), train_scores_rf2.mean(axis=1), 'b-o', label='Training')
ax2.plot(range(len(param_range_depth)), val_scores_rf2.mean(axis=1), 'r-o', label='Validation')
ax2.set_xticks(range(len(param_range_depth)))
ax2.set_xticklabels(x_labels)
ax2.set_xlabel('max_depth')
ax2.set_ylabel('Accuracy')
ax2.set_title('Random Forest: max_depth')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Logistic Regression C
print("Computing validation curve for Logistic Regression C...")
param_range_lr = np.logspace(-4, 4, 9)
train_scores_lr, val_scores_lr = validation_curve(
    Pipeline([('scaler', StandardScaler()), 
              ('classifier', LogisticRegression(max_iter=1000, random_state=42))]),
    X, y,
    param_name='classifier__C',
    param_range=param_range_lr,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

ax3 = axes[1, 0]
ax3.semilogx(param_range_lr, train_scores_lr.mean(axis=1), 'b-o', label='Training')
ax3.semilogx(param_range_lr, val_scores_lr.mean(axis=1), 'r-o', label='Validation')
ax3.set_xlabel('C (log scale)')
ax3.set_ylabel('Accuracy')
ax3.set_title('Logistic Regression: C')
ax3.legend()
ax3.grid(True, alpha=0.3)

# SVM gamma
print("Computing validation curve for SVM gamma...")
param_range_gamma = np.logspace(-4, 1, 6)
train_scores_gamma, val_scores_gamma = validation_curve(
    SVC(kernel='rbf', random_state=42),
    X_scaled, y,
    param_name='gamma',
    param_range=param_range_gamma,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

ax4 = axes[1, 1]
ax4.semilogx(param_range_gamma, train_scores_gamma.mean(axis=1), 'b-o', label='Training')
ax4.semilogx(param_range_gamma, val_scores_gamma.mean(axis=1), 'r-o', label='Validation')
ax4.set_xlabel('gamma (log scale)')
ax4.set_ylabel('Accuracy')
ax4.set_title('SVM: gamma')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex5_3_multiple_validation_curves.png', dpi=150)
plt.close()
print("Multiple validation curves saved to ex5_3_multiple_validation_curves.png")

# =============================================================================
# 5. Compare to Grid Search
# =============================================================================
print("\n" + "=" * 60)
print("5. COMPARISON WITH GRID SEARCH")
print("=" * 60)

# Grid Search for Decision Tree
param_grid = {'max_depth': list(range(1, 21))}

grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    return_train_score=True
)
grid_search.fit(X, y)

print("\nGrid Search Results for Decision Tree max_depth:")
print(f"  Best max_depth: {grid_search.best_params_['max_depth']}")
print(f"  Best CV score: {grid_search.best_score_:.4f}")

print("\nValidation Curve Results:")
print(f"  Optimal max_depth: {optimal_depth}")
print(f"  Best validation score: {optimal_score:.4f}")

print(f"\nMatch: {grid_search.best_params_['max_depth'] == optimal_depth}")

# =============================================================================
# 6. Summary
# =============================================================================
print("\n" + "=" * 60)
print("6. SUMMARY")
print("=" * 60)

print("""
VALIDATION CURVE INTERPRETATION:
--------------------------------

1. WHAT VALIDATION CURVES SHOW:
   - How model performance changes with a single hyperparameter
   - Training score: How well model fits training data
   - Validation score: How well model generalizes

2. IDENTIFYING OPTIMAL VALUE:
   - Look for peak in validation score
   - Consider the gap between training and validation
   - Balance between underfitting and overfitting

3. PATTERNS TO RECOGNIZE:
   
   Underfitting region (left side):
   - Both scores are low
   - Model is too simple
   
   Optimal region (middle):
   - Validation score is highest
   - Reasonable gap between curves
   
   Overfitting region (right side):
   - Training score high, validation drops
   - Model is too complex

4. VALIDATION CURVE vs GRID SEARCH:
   - Validation curve: Visual, one parameter at a time
   - Grid Search: Automated, can handle multiple parameters
   - Both should give same optimal value for single parameter

5. PRACTICAL TIPS:
   - Start with validation curves to understand parameter effects
   - Use Grid Search for final tuning with multiple parameters
   - Consider computational cost for large parameter ranges
""")

print("=" * 60)
print("EXERCISE 5.3 COMPLETE")
print("=" * 60)
