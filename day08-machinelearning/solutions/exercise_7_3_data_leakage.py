"""
Exercise 7.3: Detecting and Fixing Data Leakage
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for identifying and fixing data leakage in ML workflows.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

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
# 2. The BAD Code (with Data Leakage)
# =============================================================================
print("\n" + "=" * 60)
print("2. BAD CODE WITH DATA LEAKAGE")
print("=" * 60)

print("""
# WRONG WAY - Multiple leakage points!

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC

# 1. Scale all data                    <-- LEAKAGE POINT 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Select features on all data       <-- LEAKAGE POINT 2
selector = SelectKBest(k=10)
X_selected = selector.fit_transform(X_scaled, y)

# 3. Split data                        <-- TOO LATE!
X_train, X_test, y_train, y_test = train_test_split(X_selected, y)

# 4. Cross-validation                  <-- LEAKAGE POINT 3
model = SVC()
cv_scores = cross_val_score(model, X_train, y_train, cv=5)

# 5. Try different models on test set  <-- LEAKAGE POINT 4
# ... repeated testing on same test set ...
""")

# =============================================================================
# 3. Identify All Sources of Data Leakage
# =============================================================================
print("\n" + "=" * 60)
print("3. IDENTIFYING DATA LEAKAGE SOURCES")
print("=" * 60)

print("""
LEAKAGE POINT 1: Scaling all data before split
-----------------------------------------------
Problem: StandardScaler.fit_transform(X) computes mean and std from ALL data,
         including test samples. When we later split, the test data has already
         "seen" information from training data (and vice versa).
         
Why it's bad: The scaler's parameters are contaminated with test data info.
              This makes the model appear to generalize better than it will
              on truly unseen data.

LEAKAGE POINT 2: Feature selection on all data
----------------------------------------------
Problem: SelectKBest.fit_transform(X, y) uses ALL samples to determine which
         features are most predictive. The test data influences feature selection.
         
Why it's bad: Features are selected based on their relationship with ALL labels,
              including test labels. This is like "peeking" at the test answers.

LEAKAGE POINT 3: CV on already-transformed data
-----------------------------------------------
Problem: Cross-validation is performed on data that was already scaled and
         feature-selected using ALL data. Each CV fold is not independent.
         
Why it's bad: CV scores are overly optimistic because preprocessing was done
              on the full dataset, not within each fold.

LEAKAGE POINT 4: Repeated testing on test set
---------------------------------------------
Problem: Trying multiple models and selecting based on test performance
         effectively uses the test set for model selection.
         
Why it's bad: The test set should only be used ONCE for final evaluation.
              Using it for model selection makes it part of training.
""")

# =============================================================================
# 4. Demonstrate the Problem
# =============================================================================
print("\n" + "=" * 60)
print("4. DEMONSTRATING THE LEAKAGE PROBLEM")
print("=" * 60)

# BAD WAY (with leakage)
print("\n--- BAD WAY (with leakage) ---")

# Leakage 1: Scale all data
scaler_bad = StandardScaler()
X_scaled_bad = scaler_bad.fit_transform(X)

# Leakage 2: Feature selection on all data
selector_bad = SelectKBest(score_func=f_classif, k=10)
X_selected_bad = selector_bad.fit_transform(X_scaled_bad, y)

# Split (too late!)
X_train_bad, X_test_bad, y_train_bad, y_test_bad = train_test_split(
    X_selected_bad, y, test_size=0.2, random_state=42
)

# Train and evaluate
model_bad = SVC(kernel='rbf', random_state=42)
model_bad.fit(X_train_bad, y_train_bad)

# CV on leaked data
cv_scores_bad = cross_val_score(model_bad, X_selected_bad, y, cv=5)
test_accuracy_bad = accuracy_score(y_test_bad, model_bad.predict(X_test_bad))

print(f"CV Score (with leakage): {cv_scores_bad.mean():.4f} +/- {cv_scores_bad.std():.4f}")
print(f"Test Accuracy (with leakage): {test_accuracy_bad:.4f}")

# =============================================================================
# 5. The CORRECT Way (Using Pipeline)
# =============================================================================
print("\n" + "=" * 60)
print("5. CORRECT WAY (Using Pipeline)")
print("=" * 60)

# Split FIRST
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create pipeline with all preprocessing
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(score_func=f_classif, k=10)),
    ('classifier', SVC(kernel='rbf', random_state=42))
])

# Cross-validation on training data only
cv_scores_good = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"CV Score (no leakage): {cv_scores_good.mean():.4f} +/- {cv_scores_good.std():.4f}")

# Train on full training set
pipeline.fit(X_train, y_train)

# Evaluate on test set (only once!)
test_accuracy_good = accuracy_score(y_test, pipeline.predict(X_test))
print(f"Test Accuracy (no leakage): {test_accuracy_good:.4f}")

# =============================================================================
# 6. Compare Results
# =============================================================================
print("\n" + "=" * 60)
print("6. COMPARISON OF RESULTS")
print("=" * 60)

print("\n" + "-" * 50)
print(f"{'Metric':<25} {'With Leakage':>15} {'No Leakage':>15}")
print("-" * 50)
print(f"{'CV Score Mean':<25} {cv_scores_bad.mean():>15.4f} {cv_scores_good.mean():>15.4f}")
print(f"{'CV Score Std':<25} {cv_scores_bad.std():>15.4f} {cv_scores_good.std():>15.4f}")
print(f"{'Test Accuracy':<25} {test_accuracy_bad:>15.4f} {test_accuracy_good:>15.4f}")
print("-" * 50)

if cv_scores_bad.mean() > cv_scores_good.mean():
    print("\nWARNING: Leakage gives OVERLY OPTIMISTIC CV scores!")
    print(f"Difference: {cv_scores_bad.mean() - cv_scores_good.mean():.4f}")

# =============================================================================
# 7. Visualize the Difference
# =============================================================================
print("\n" + "=" * 60)
print("7. VISUALIZATION")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# CV Scores comparison
ax1 = axes[0]
positions = [1, 2]
bp = ax1.boxplot([cv_scores_bad, cv_scores_good], positions=positions, widths=0.6)
ax1.set_xticks(positions)
ax1.set_xticklabels(['With Leakage', 'No Leakage'])
ax1.set_ylabel('CV Score')
ax1.set_title('Cross-Validation Scores Comparison')
ax1.grid(True, alpha=0.3)

# Add mean lines
for i, scores in enumerate([cv_scores_bad, cv_scores_good]):
    ax1.hlines(scores.mean(), positions[i]-0.3, positions[i]+0.3, colors='red', linewidth=2)

# Bar chart comparison
ax2 = axes[1]
metrics = ['CV Score', 'Test Accuracy']
leakage_values = [cv_scores_bad.mean(), test_accuracy_bad]
no_leakage_values = [cv_scores_good.mean(), test_accuracy_good]

x = np.arange(len(metrics))
width = 0.35

bars1 = ax2.bar(x - width/2, leakage_values, width, label='With Leakage', color='red', alpha=0.7)
bars2 = ax2.bar(x + width/2, no_leakage_values, width, label='No Leakage', color='green', alpha=0.7)

ax2.set_ylabel('Score')
ax2.set_title('Performance Comparison')
ax2.set_xticks(x)
ax2.set_xticklabels(metrics)
ax2.legend()
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_ylim([0.9, 1.0])

plt.tight_layout()
plt.savefig('ex7_3_leakage_comparison.png', dpi=150)
plt.close()
print("Comparison plot saved to ex7_3_leakage_comparison.png")

# =============================================================================
# 8. Correct Code Template
# =============================================================================
print("\n" + "=" * 60)
print("8. CORRECT CODE TEMPLATE")
print("=" * 60)

print("""
# CORRECT WAY - No data leakage!

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# 1. Split data FIRST
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Create pipeline with ALL preprocessing
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(k=10)),
    ('classifier', SVC())
])

# 3. Cross-validation on TRAINING data only
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"CV Score: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

# 4. Use CV scores for model selection (NOT test set!)
# ... compare different models using CV scores ...

# 5. Train final model on full training set
pipeline.fit(X_train, y_train)

# 6. Evaluate on test set ONCE (final evaluation only)
test_score = pipeline.score(X_test, y_test)
print(f"Final Test Score: {test_score:.4f}")
""")

# =============================================================================
# 9. Summary
# =============================================================================
print("\n" + "=" * 60)
print("9. SUMMARY")
print("=" * 60)

print("""
DATA LEAKAGE CHECKLIST:
-----------------------

[ ] Split data BEFORE any preprocessing
[ ] Put ALL preprocessing in a Pipeline
[ ] Use cross_val_score with the Pipeline
[ ] Select models based on CV scores, NOT test scores
[ ] Use test set only ONCE for final evaluation
[ ] Never fit anything on the full dataset before splitting

COMMON LEAKAGE SOURCES:
-----------------------
1. Fitting scaler/normalizer on all data
2. Feature selection on all data
3. Imputing missing values using all data
4. Target encoding using all data
5. Using future information (time series)
6. Repeated testing on test set

CONSEQUENCES OF LEAKAGE:
------------------------
- Overly optimistic performance estimates
- Model fails on truly new data
- False confidence in model quality
- Wasted time and resources in production

PREVENTION:
-----------
- Always use Pipelines
- Think about information flow
- Ask: "Would I have this information in production?"
- Validate with truly held-out data
""")

print("=" * 60)
print("EXERCISE 7.3 COMPLETE")
print("=" * 60)
