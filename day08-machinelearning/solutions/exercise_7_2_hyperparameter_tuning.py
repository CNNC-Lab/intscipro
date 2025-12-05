"""
Exercise 7.2: Hyperparameter Tuning
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for Grid Search and Random Search hyperparameter tuning.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split, GridSearchCV, RandomizedSearchCV, 
    validation_curve, cross_val_score
)
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from scipy.stats import randint, uniform
import time

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

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# =============================================================================
# 2. Create Pipeline
# =============================================================================
print("\n" + "=" * 60)
print("2. CREATING PIPELINE")
print("=" * 60)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

print("Pipeline created with StandardScaler + RandomForestClassifier")

# =============================================================================
# 3. Grid Search
# =============================================================================
print("\n" + "=" * 60)
print("3. GRID SEARCH")
print("=" * 60)

# Define parameter grid
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_split': [2, 5, 10]
}

total_combinations = 1
for values in param_grid.values():
    total_combinations *= len(values)
print(f"\nParameter grid: {total_combinations} combinations")
for param, values in param_grid.items():
    print(f"  {param}: {values}")

# Perform Grid Search
print("\nRunning Grid Search with 5-fold CV...")
start_time = time.time()

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='accuracy',
    return_train_score=True,
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

grid_time = time.time() - start_time
print(f"\nGrid Search completed in {grid_time:.2f} seconds")

# Results
print("\n--- Grid Search Results ---")
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")

# Test set performance
y_pred_grid = grid_search.predict(X_test)
test_accuracy_grid = accuracy_score(y_test, y_pred_grid)
print(f"Test set accuracy: {test_accuracy_grid:.4f}")

# =============================================================================
# 4. Analyze Grid Search Results
# =============================================================================
print("\n" + "=" * 60)
print("4. GRID SEARCH ANALYSIS")
print("=" * 60)

import pandas as pd
results_df = pd.DataFrame(grid_search.cv_results_)

# Top 5 configurations
print("\nTop 5 configurations:")
top_5 = results_df.nsmallest(5, 'rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score', 'mean_train_score']
]
for i, row in top_5.iterrows():
    print(f"\n  Rank {results_df.loc[i, 'rank_test_score']}:")
    print(f"    Params: {row['params']}")
    print(f"    CV Score: {row['mean_test_score']:.4f} +/- {row['std_test_score']:.4f}")
    print(f"    Train Score: {row['mean_train_score']:.4f}")

# Visualize results
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Effect of n_estimators
ax1 = axes[0]
for max_depth in [5, 10, None]:
    mask = results_df['param_classifier__max_depth'] == max_depth
    subset = results_df[mask].groupby('param_classifier__n_estimators')['mean_test_score'].mean()
    label = f'max_depth={max_depth}' if max_depth else 'max_depth=None'
    ax1.plot(subset.index, subset.values, 'o-', label=label)
ax1.set_xlabel('n_estimators')
ax1.set_ylabel('Mean CV Score')
ax1.set_title('Effect of n_estimators')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Effect of max_depth
ax2 = axes[1]
depth_scores = results_df.groupby('param_classifier__max_depth')['mean_test_score'].mean()
x_labels = [str(d) if d else 'None' for d in depth_scores.index]
ax2.bar(range(len(depth_scores)), depth_scores.values)
ax2.set_xticks(range(len(depth_scores)))
ax2.set_xticklabels(x_labels)
ax2.set_xlabel('max_depth')
ax2.set_ylabel('Mean CV Score')
ax2.set_title('Effect of max_depth')
ax2.grid(True, alpha=0.3)

# Effect of min_samples_split
ax3 = axes[2]
split_scores = results_df.groupby('param_classifier__min_samples_split')['mean_test_score'].mean()
ax3.bar(range(len(split_scores)), split_scores.values)
ax3.set_xticks(range(len(split_scores)))
ax3.set_xticklabels(split_scores.index)
ax3.set_xlabel('min_samples_split')
ax3.set_ylabel('Mean CV Score')
ax3.set_title('Effect of min_samples_split')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex7_2_grid_search_analysis.png', dpi=150)
plt.close()
print("\nGrid search analysis saved to ex7_2_grid_search_analysis.png")

# =============================================================================
# 5. Random Search
# =============================================================================
print("\n" + "=" * 60)
print("5. RANDOM SEARCH")
print("=" * 60)

# Define parameter distributions
param_distributions = {
    'classifier__n_estimators': randint(50, 300),
    'classifier__max_depth': [3, 5, 7, 10, 15, 20, None],
    'classifier__min_samples_split': randint(2, 20),
    'classifier__min_samples_leaf': randint(1, 10),
    'classifier__max_features': ['sqrt', 'log2', None]
}

print("Parameter distributions:")
for param, dist in param_distributions.items():
    print(f"  {param}: {dist}")

# Perform Random Search with 20 iterations
print("\nRunning Random Search (20 iterations) with 5-fold CV...")
start_time = time.time()

random_search = RandomizedSearchCV(
    pipeline,
    param_distributions,
    n_iter=20,
    cv=5,
    scoring='accuracy',
    return_train_score=True,
    random_state=42,
    n_jobs=-1,
    verbose=1
)
random_search.fit(X_train, y_train)

random_time = time.time() - start_time
print(f"\nRandom Search completed in {random_time:.2f} seconds")

# Results
print("\n--- Random Search Results ---")
print(f"Best parameters: {random_search.best_params_}")
print(f"Best CV score: {random_search.best_score_:.4f}")

# Test set performance
y_pred_random = random_search.predict(X_test)
test_accuracy_random = accuracy_score(y_test, y_pred_random)
print(f"Test set accuracy: {test_accuracy_random:.4f}")

# =============================================================================
# 6. Compare Grid Search vs Random Search
# =============================================================================
print("\n" + "=" * 60)
print("6. COMPARISON: GRID SEARCH vs RANDOM SEARCH")
print("=" * 60)

print("\n" + "-" * 50)
print(f"{'Metric':<25} {'Grid Search':>12} {'Random Search':>14}")
print("-" * 50)
print(f"{'Time (seconds)':<25} {grid_time:>12.2f} {random_time:>14.2f}")
print(f"{'Combinations tried':<25} {total_combinations:>12} {20:>14}")
print(f"{'Best CV Score':<25} {grid_search.best_score_:>12.4f} {random_search.best_score_:>14.4f}")
print(f"{'Test Accuracy':<25} {test_accuracy_grid:>12.4f} {test_accuracy_random:>14.4f}")
print("-" * 50)

# =============================================================================
# 7. Validation Curve for Best Parameter
# =============================================================================
print("\n" + "=" * 60)
print("7. VALIDATION CURVE FOR n_estimators")
print("=" * 60)

# Get best other parameters
best_params = grid_search.best_params_.copy()
del best_params['classifier__n_estimators']

# Create pipeline with best params except n_estimators
pipeline_for_vc = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(
        max_depth=best_params.get('classifier__max_depth'),
        min_samples_split=best_params.get('classifier__min_samples_split', 2),
        random_state=42
    ))
])

param_range = [10, 25, 50, 75, 100, 150, 200, 250, 300]

train_scores, val_scores = validation_curve(
    pipeline_for_vc,
    X_train, y_train,
    param_name='classifier__n_estimators',
    param_range=param_range,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(param_range, train_scores.mean(axis=1), 'b-o', label='Training Score')
ax.fill_between(param_range, 
                train_scores.mean(axis=1) - train_scores.std(axis=1),
                train_scores.mean(axis=1) + train_scores.std(axis=1),
                alpha=0.2, color='blue')
ax.plot(param_range, val_scores.mean(axis=1), 'r-o', label='Validation Score')
ax.fill_between(param_range,
                val_scores.mean(axis=1) - val_scores.std(axis=1),
                val_scores.mean(axis=1) + val_scores.std(axis=1),
                alpha=0.2, color='red')

optimal_n = param_range[np.argmax(val_scores.mean(axis=1))]
ax.axvline(x=optimal_n, color='green', linestyle='--', label=f'Optimal: {optimal_n}')

ax.set_xlabel('n_estimators')
ax.set_ylabel('Accuracy')
ax.set_title('Validation Curve: n_estimators')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex7_2_validation_curve.png', dpi=150)
plt.close()
print("Validation curve saved to ex7_2_validation_curve.png")

# =============================================================================
# 8. Summary
# =============================================================================
print("\n" + "=" * 60)
print("8. SUMMARY")
print("=" * 60)

print("""
GRID SEARCH vs RANDOM SEARCH:
-----------------------------

GRID SEARCH:
  Pros:
    - Exhaustive search of parameter space
    - Guaranteed to find best in grid
    - Reproducible results
  Cons:
    - Computationally expensive
    - Curse of dimensionality
    - May miss optimal values between grid points

RANDOM SEARCH:
  Pros:
    - More efficient for large parameter spaces
    - Can explore continuous distributions
    - Often finds good solutions faster
  Cons:
    - May miss optimal configuration
    - Results vary with random seed
    - Need to choose n_iter wisely

WHEN TO USE WHICH:
------------------
- Grid Search: Small parameter space, need exhaustive search
- Random Search: Large parameter space, limited time
- Both: Start with Random Search, then Grid Search around best

BEST PRACTICES:
---------------
1. Always use cross-validation (cv parameter)
2. Use pipelines to prevent data leakage
3. Report CV score, not test score, for model selection
4. Use test set only for final evaluation
5. Consider computational budget when choosing method
""")

print("=" * 60)
print("EXERCISE 7.2 COMPLETE")
print("=" * 60)
