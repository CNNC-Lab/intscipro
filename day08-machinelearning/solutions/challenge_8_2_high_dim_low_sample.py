"""
Challenge 8.2: High-Dimensional Low-Sample Problem
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for handling many features with few samples (common in neuroscience).
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import (
    train_test_split, cross_val_score, StratifiedKFold,
    GridSearchCV
)
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Create High-Dimensional Low-Sample Dataset
# =============================================================================
print("=" * 60)
print("1. CREATING HIGH-DIMENSIONAL LOW-SAMPLE DATASET")
print("=" * 60)

X, y = make_classification(
    n_samples=100,      # Only 100 samples!
    n_features=1000,    # But 1000 features!
    n_informative=50,
    n_redundant=50,
    n_classes=2,
    random_state=42
)

print(f"Samples: {X.shape[0]}")
print(f"Features: {X.shape[1]}")
print(f"Ratio (samples/features): {X.shape[0]/X.shape[1]:.2f}")
print("\nThis is a challenging scenario common in:")
print("  - Neuroimaging (many voxels, few subjects)")
print("  - Genomics (many genes, few samples)")
print("  - EEG/MEG (many channels x timepoints)")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining samples: {len(y_train)}")
print(f"Test samples: {len(y_test)}")

# =============================================================================
# 2. Show Severe Overfitting with Standard Models
# =============================================================================
print("\n" + "=" * 60)
print("2. DEMONSTRATING SEVERE OVERFITTING")
print("=" * 60)

# Standard models without regularization
models_standard = {
    'Logistic Regression (no reg)': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(penalty=None, max_iter=1000, random_state=42))
    ]),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM (linear)': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='linear', random_state=42))
    ])
}

print("\nStandard models (no dimensionality reduction):")
print("-" * 60)
print(f"{'Model':<30} {'Train Acc':>12} {'Test Acc':>12} {'Overfit':>10}")
print("-" * 60)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models_standard.items():
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    overfit = train_acc - test_acc
    print(f"{name:<30} {train_acc:>12.4f} {test_acc:>12.4f} {overfit:>10.4f}")

print("\nSEVERE OVERFITTING: Training accuracy is much higher than test accuracy!")

# =============================================================================
# 3. Apply Dimensionality Reduction (PCA)
# =============================================================================
print("\n" + "=" * 60)
print("3. DIMENSIONALITY REDUCTION WITH PCA")
print("=" * 60)

n_components_list = [5, 10, 20, 50]
pca_results = {}

print("\nLogistic Regression with PCA:")
print("-" * 60)
print(f"{'N Components':>15} {'CV Score':>15} {'Test Acc':>12}")
print("-" * 60)

for n_comp in n_components_list:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=n_comp)),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ])
    
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')
    pipeline.fit(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)
    
    pca_results[n_comp] = {'cv_mean': cv_scores.mean(), 'cv_std': cv_scores.std(), 'test': test_acc}
    print(f"{n_comp:>15} {cv_scores.mean():>12.4f} +/- {cv_scores.std():.4f} {test_acc:>12.4f}")

# =============================================================================
# 4. Apply Feature Selection (SelectKBest)
# =============================================================================
print("\n" + "=" * 60)
print("4. FEATURE SELECTION WITH SelectKBest")
print("=" * 60)

k_values = [10, 25, 50, 100]
select_results = {}

print("\nLogistic Regression with SelectKBest:")
print("-" * 60)
print(f"{'K Features':>15} {'CV Score':>15} {'Test Acc':>12}")
print("-" * 60)

for k in k_values:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif, k=k)),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ])
    
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')
    pipeline.fit(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)
    
    select_results[k] = {'cv_mean': cv_scores.mean(), 'cv_std': cv_scores.std(), 'test': test_acc}
    print(f"{k:>15} {cv_scores.mean():>12.4f} +/- {cv_scores.std():.4f} {test_acc:>12.4f}")

# =============================================================================
# 5. Apply Regularization (Ridge, Lasso)
# =============================================================================
print("\n" + "=" * 60)
print("5. REGULARIZATION (Ridge, L1)")
print("=" * 60)

alpha_values = [0.01, 0.1, 1.0, 10.0, 100.0]
reg_results = {'ridge': {}, 'l1': {}}

print("\nRidge Classifier:")
print("-" * 50)
print(f"{'Alpha':>10} {'CV Score':>15} {'Test Acc':>12}")
print("-" * 50)

for alpha in alpha_values:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RidgeClassifier(alpha=alpha, random_state=42))
    ])
    
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')
    pipeline.fit(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)
    
    reg_results['ridge'][alpha] = {'cv_mean': cv_scores.mean(), 'test': test_acc}
    print(f"{alpha:>10} {cv_scores.mean():>12.4f} +/- {cv_scores.std():.4f} {test_acc:>12.4f}")

print("\nLogistic Regression with L1 (Lasso):")
print("-" * 50)
print(f"{'C (1/alpha)':>10} {'CV Score':>15} {'Test Acc':>12}")
print("-" * 50)

for C in [0.01, 0.1, 1.0, 10.0]:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(penalty='l1', solver='saga', C=C, max_iter=1000, random_state=42))
    ])
    
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')
    pipeline.fit(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)
    
    reg_results['l1'][C] = {'cv_mean': cv_scores.mean(), 'test': test_acc}
    print(f"{C:>10} {cv_scores.mean():>12.4f} +/- {cv_scores.std():.4f} {test_acc:>12.4f}")

# =============================================================================
# 6. Nested Cross-Validation
# =============================================================================
print("\n" + "=" * 60)
print("6. NESTED CROSS-VALIDATION")
print("=" * 60)

print("\nNested CV: Outer loop for performance, inner loop for tuning")

# Define pipeline
pipeline_nested = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

# Parameter grid for inner loop
param_grid = {
    'pca__n_components': [5, 10, 20],
    'classifier__C': [0.1, 1.0, 10.0]
}

# Outer CV
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
# Inner CV
inner_cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

nested_scores = []

print("\nRunning nested CV...")
for fold, (train_idx, test_idx) in enumerate(outer_cv.split(X_train, y_train)):
    X_train_fold = X_train[train_idx]
    y_train_fold = y_train[train_idx]
    X_test_fold = X_train[test_idx]
    y_test_fold = y_train[test_idx]
    
    # Inner CV for hyperparameter tuning
    grid_search = GridSearchCV(
        pipeline_nested, param_grid, cv=inner_cv, scoring='accuracy', n_jobs=-1
    )
    grid_search.fit(X_train_fold, y_train_fold)
    
    # Evaluate on outer fold
    score = grid_search.score(X_test_fold, y_test_fold)
    nested_scores.append(score)
    print(f"  Fold {fold+1}: {score:.4f} (best params: {grid_search.best_params_})")

print(f"\nNested CV Score: {np.mean(nested_scores):.4f} +/- {np.std(nested_scores):.4f}")

# =============================================================================
# 7. Compare All Approaches
# =============================================================================
print("\n" + "=" * 60)
print("7. COMPARISON OF ALL APPROACHES")
print("=" * 60)

# Best from each approach
best_pca = max(pca_results.items(), key=lambda x: x[1]['cv_mean'])
best_select = max(select_results.items(), key=lambda x: x[1]['cv_mean'])
best_ridge = max(reg_results['ridge'].items(), key=lambda x: x[1]['cv_mean'])
best_l1 = max(reg_results['l1'].items(), key=lambda x: x[1]['cv_mean'])

print("\nBest configuration from each approach:")
print("-" * 70)
print(f"{'Approach':<25} {'Config':>15} {'CV Score':>12} {'Test Acc':>12}")
print("-" * 70)
print(f"{'No reduction (RF)':<25} {'-':>15} {'-':>12} {models_standard['Random Forest'].score(X_test, y_test):>12.4f}")
print(f"{'PCA':<25} {f'n={best_pca[0]}':>15} {best_pca[1]['cv_mean']:>12.4f} {best_pca[1]['test']:>12.4f}")
print(f"{'SelectKBest':<25} {f'k={best_select[0]}':>15} {best_select[1]['cv_mean']:>12.4f} {best_select[1]['test']:>12.4f}")
print(f"{'Ridge':<25} {f'alpha={best_ridge[0]}':>15} {best_ridge[1]['cv_mean']:>12.4f} {best_ridge[1]['test']:>12.4f}")
print(f"{'L1 (Lasso)':<25} {f'C={best_l1[0]}':>15} {best_l1[1]['cv_mean']:>12.4f} {best_l1[1]['test']:>12.4f}")
print(f"{'Nested CV (PCA+LR)':<25} {'tuned':>15} {np.mean(nested_scores):>12.4f} {'-':>12}")
print("-" * 70)

# =============================================================================
# 8. Visualization
# =============================================================================
print("\n" + "=" * 60)
print("8. VISUALIZATION")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# PCA components effect
ax1 = axes[0, 0]
n_comps = list(pca_results.keys())
cv_scores = [pca_results[n]['cv_mean'] for n in n_comps]
test_scores = [pca_results[n]['test'] for n in n_comps]
ax1.plot(n_comps, cv_scores, 'b-o', label='CV Score')
ax1.plot(n_comps, test_scores, 'r-o', label='Test Score')
ax1.set_xlabel('Number of PCA Components')
ax1.set_ylabel('Accuracy')
ax1.set_title('Effect of PCA Components')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Feature selection effect
ax2 = axes[0, 1]
k_vals = list(select_results.keys())
cv_scores = [select_results[k]['cv_mean'] for k in k_vals]
test_scores = [select_results[k]['test'] for k in k_vals]
ax2.plot(k_vals, cv_scores, 'b-o', label='CV Score')
ax2.plot(k_vals, test_scores, 'r-o', label='Test Score')
ax2.set_xlabel('Number of Selected Features')
ax2.set_ylabel('Accuracy')
ax2.set_title('Effect of Feature Selection')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Ridge regularization effect
ax3 = axes[1, 0]
alphas = list(reg_results['ridge'].keys())
cv_scores = [reg_results['ridge'][a]['cv_mean'] for a in alphas]
test_scores = [reg_results['ridge'][a]['test'] for a in alphas]
ax3.semilogx(alphas, cv_scores, 'b-o', label='CV Score')
ax3.semilogx(alphas, test_scores, 'r-o', label='Test Score')
ax3.set_xlabel('Alpha (regularization strength)')
ax3.set_ylabel('Accuracy')
ax3.set_title('Effect of Ridge Regularization')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Comparison bar chart
ax4 = axes[1, 1]
approaches = ['No Reduction', 'PCA', 'SelectKBest', 'Ridge', 'L1']
cv_scores = [
    0.5,  # Placeholder for no reduction
    best_pca[1]['cv_mean'],
    best_select[1]['cv_mean'],
    best_ridge[1]['cv_mean'],
    best_l1[1]['cv_mean']
]
test_scores = [
    models_standard['Random Forest'].score(X_test, y_test),
    best_pca[1]['test'],
    best_select[1]['test'],
    best_ridge[1]['test'],
    best_l1[1]['test']
]

x = np.arange(len(approaches))
width = 0.35
ax4.bar(x - width/2, cv_scores, width, label='CV Score', alpha=0.7)
ax4.bar(x + width/2, test_scores, width, label='Test Score', alpha=0.7)
ax4.set_xticks(x)
ax4.set_xticklabels(approaches, rotation=45, ha='right')
ax4.set_ylabel('Accuracy')
ax4.set_title('Approach Comparison')
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('challenge_8_2_high_dim.png', dpi=150)
plt.close()
print("Visualization saved to challenge_8_2_high_dim.png")

# =============================================================================
# 9. Summary
# =============================================================================
print("\n" + "=" * 60)
print("9. SUMMARY")
print("=" * 60)

print("""
HIGH-DIMENSIONAL LOW-SAMPLE PROBLEM:
------------------------------------

CHALLENGES:
1. Curse of dimensionality
2. Severe overfitting
3. Unreliable feature importance
4. Computational cost

SOLUTIONS THAT WORK:
1. Dimensionality Reduction (PCA)
   - Reduces noise
   - Captures main variance
   - Works well when features are correlated

2. Feature Selection (SelectKBest)
   - Keeps interpretable features
   - Removes irrelevant features
   - Risk: may miss feature interactions

3. Regularization (Ridge, Lasso)
   - Shrinks coefficients
   - Lasso can zero out features
   - Doesn't require explicit feature reduction

4. Nested Cross-Validation
   - Unbiased performance estimate
   - Proper hyperparameter tuning
   - Essential for small samples

RECOMMENDATIONS FOR NEUROSCIENCE:
---------------------------------
1. Always use cross-validation (preferably nested)
2. Start with strong regularization
3. Consider PCA for correlated features (e.g., neighboring voxels)
4. Use feature selection for interpretability
5. Be skeptical of high training accuracy
6. Report confidence intervals on performance
""")

print("=" * 60)
print("CHALLENGE 8.2 COMPLETE")
print("=" * 60)
