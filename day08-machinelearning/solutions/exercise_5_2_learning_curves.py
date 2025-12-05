"""
Exercise 5.2: Learning Curves
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for creating and interpreting learning curves.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
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
# 2. Define Models with Different Complexity
# =============================================================================
print("\n" + "=" * 60)
print("2. DEFINING MODELS WITH DIFFERENT COMPLEXITY")
print("=" * 60)

models = {
    # High complexity - prone to overfitting
    'High Complexity\n(Deep Tree)': DecisionTreeClassifier(max_depth=None, random_state=42),
    
    # Medium complexity
    'Medium Complexity\n(Depth=5 Tree)': DecisionTreeClassifier(max_depth=5, random_state=42),
    
    # Low complexity - prone to underfitting
    'Low Complexity\n(Depth=2 Tree)': DecisionTreeClassifier(max_depth=2, random_state=42),
    
    # Well-regularized model
    'Regularized\n(Logistic Reg)': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(C=0.1, max_iter=1000, random_state=42))
    ])
}

print("Models defined:")
for name in models.keys():
    print(f"  - {name.replace(chr(10), ' ')}")

# =============================================================================
# 3. Create Learning Curves
# =============================================================================
print("\n" + "=" * 60)
print("3. CREATING LEARNING CURVES")
print("=" * 60)

train_sizes = np.linspace(0.1, 1.0, 10)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

learning_curve_results = {}

for ax, (name, model) in zip(axes, models.items()):
    print(f"\nComputing learning curve for: {name.replace(chr(10), ' ')}")
    
    train_sizes_abs, train_scores, val_scores = learning_curve(
        model, X, y,
        train_sizes=train_sizes,
        cv=5,
        scoring='accuracy',
        random_state=42,
        n_jobs=-1
    )
    
    train_mean = train_scores.mean(axis=1)
    train_std = train_scores.std(axis=1)
    val_mean = val_scores.mean(axis=1)
    val_std = val_scores.std(axis=1)
    
    learning_curve_results[name] = {
        'train_sizes': train_sizes_abs,
        'train_mean': train_mean,
        'train_std': train_std,
        'val_mean': val_mean,
        'val_std': val_std
    }
    
    # Plot
    ax.plot(train_sizes_abs, train_mean, 'b-o', label='Training Score')
    ax.fill_between(train_sizes_abs, train_mean - train_std, train_mean + train_std, alpha=0.2, color='blue')
    ax.plot(train_sizes_abs, val_mean, 'r-o', label='Validation Score')
    ax.fill_between(train_sizes_abs, val_mean - val_std, val_mean + val_std, alpha=0.2, color='red')
    
    ax.set_xlabel('Training Set Size')
    ax.set_ylabel('Accuracy')
    ax.set_title(name)
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0.7, 1.05])
    
    # Add gap annotation
    final_gap = train_mean[-1] - val_mean[-1]
    ax.annotate(f'Gap: {final_gap:.3f}', 
                xy=(train_sizes_abs[-1], (train_mean[-1] + val_mean[-1])/2),
                fontsize=10, ha='right')

plt.tight_layout()
plt.savefig('ex5_2_learning_curves.png', dpi=150)
plt.close()
print("\nLearning curves saved to ex5_2_learning_curves.png")

# =============================================================================
# 4. Interpretation
# =============================================================================
print("\n" + "=" * 60)
print("4. LEARNING CURVE INTERPRETATION")
print("=" * 60)

for name, results in learning_curve_results.items():
    print(f"\n{name.replace(chr(10), ' ')}:")
    
    train_final = results['train_mean'][-1]
    val_final = results['val_mean'][-1]
    gap = train_final - val_final
    
    print(f"  Final Training Score: {train_final:.4f}")
    print(f"  Final Validation Score: {val_final:.4f}")
    print(f"  Gap (Train - Val): {gap:.4f}")
    
    # Diagnosis
    if gap > 0.1:
        print("  Diagnosis: OVERFITTING")
        print("  - Training score much higher than validation")
        print("  - Model is too complex for the data")
        print("  - Solutions: Regularization, simpler model, more data")
    elif val_final < 0.85:
        print("  Diagnosis: UNDERFITTING")
        print("  - Both scores are relatively low")
        print("  - Model is too simple to capture patterns")
        print("  - Solutions: More complex model, more features")
    else:
        print("  Diagnosis: GOOD FIT")
        print("  - Training and validation scores are close")
        print("  - Model generalizes well")
    
    # Would more data help?
    val_trend = results['val_mean'][-1] - results['val_mean'][-3]
    if val_trend > 0.01:
        print("  More data: Would likely help (validation still improving)")
    else:
        print("  More data: Unlikely to help much (validation plateaued)")

# =============================================================================
# 5. Additional Models Comparison
# =============================================================================
print("\n" + "=" * 60)
print("5. ADDITIONAL MODELS COMPARISON")
print("=" * 60)

additional_models = {
    'Random Forest (100 trees)': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM (RBF kernel)': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', random_state=42))
    ]),
    'Logistic Regression (C=1)': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(C=1.0, max_iter=1000, random_state=42))
    ])
}

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, (name, model) in zip(axes, additional_models.items()):
    train_sizes_abs, train_scores, val_scores = learning_curve(
        model, X, y,
        train_sizes=train_sizes,
        cv=5,
        scoring='accuracy',
        random_state=42,
        n_jobs=-1
    )
    
    train_mean = train_scores.mean(axis=1)
    val_mean = val_scores.mean(axis=1)
    
    ax.plot(train_sizes_abs, train_mean, 'b-o', label='Training')
    ax.plot(train_sizes_abs, val_mean, 'r-o', label='Validation')
    ax.set_xlabel('Training Set Size')
    ax.set_ylabel('Accuracy')
    ax.set_title(name)
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0.85, 1.02])

plt.tight_layout()
plt.savefig('ex5_2_additional_models.png', dpi=150)
plt.close()
print("Additional models plot saved to ex5_2_additional_models.png")

# =============================================================================
# 6. Summary
# =============================================================================
print("\n" + "=" * 60)
print("6. SUMMARY")
print("=" * 60)

print("""
LEARNING CURVE INTERPRETATION GUIDE:
------------------------------------

1. OVERFITTING (High Variance):
   - Training score: High (near 1.0)
   - Validation score: Much lower than training
   - Large gap between curves
   - Curves may converge with more data
   
   Solutions:
   - Reduce model complexity
   - Add regularization
   - Get more training data
   - Feature selection

2. UNDERFITTING (High Bias):
   - Training score: Low
   - Validation score: Low (similar to training)
   - Small gap between curves
   - Both curves plateau early
   
   Solutions:
   - Increase model complexity
   - Add more features
   - Reduce regularization
   - Use more powerful model

3. GOOD FIT:
   - Training score: High
   - Validation score: High (close to training)
   - Small gap between curves
   - Both curves plateau at high values

4. WOULD MORE DATA HELP?
   - If validation curve is still rising: YES
   - If validation curve has plateaued: NO
   - If large gap exists: YES (for overfitting)
   - If both curves are low: NO (need better model)
""")

print("=" * 60)
print("EXERCISE 5.2 COMPLETE")
print("=" * 60)
