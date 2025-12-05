"""
Exercise 4.2: Feature Engineering
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for polynomial feature engineering and regularization.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Data
# =============================================================================
print("=" * 60)
print("1. LOADING DATA")
print("=" * 60)

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

print(f"Original features: {X.shape[1]}")
print(f"Samples: {X.shape[0]}")

# =============================================================================
# 2. Create Polynomial Features
# =============================================================================
print("\n" + "=" * 60)
print("2. CREATING POLYNOMIAL FEATURES")
print("=" * 60)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

print(f"Original features: {X.shape[1]}")
print(f"Polynomial features (degree=2): {X_poly.shape[1]}")
print(f"\nFeature expansion: {X.shape[1]} -> {X_poly.shape[1]} features")

# Get polynomial feature names
poly_feature_names = poly.get_feature_names_out(feature_names)
print(f"\nSample polynomial features:")
for i in range(min(10, len(poly_feature_names))):
    print(f"  {i+1}. {poly_feature_names[i]}")
print(f"  ... ({len(poly_feature_names) - 10} more features)")

# =============================================================================
# 3. Split Data
# =============================================================================
print("\n" + "=" * 60)
print("3. DATA SPLITTING")
print("=" * 60)

# Split original data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Split polynomial data
X_poly_train, X_poly_test, _, _ = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# =============================================================================
# 4. Train Linear Regression on Original vs Polynomial
# =============================================================================
print("\n" + "=" * 60)
print("4. LINEAR REGRESSION: ORIGINAL vs POLYNOMIAL")
print("=" * 60)

# Original features
lr_original = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
lr_original.fit(X_train, y_train)
y_pred_original = lr_original.predict(X_test)
r2_original = r2_score(y_test, y_pred_original)
rmse_original = np.sqrt(mean_squared_error(y_test, y_pred_original))

# Polynomial features
lr_poly = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
lr_poly.fit(X_poly_train, y_train)
y_pred_poly = lr_poly.predict(X_poly_test)
r2_poly = r2_score(y_test, y_pred_poly)
rmse_poly = np.sqrt(mean_squared_error(y_test, y_pred_poly))

# Training scores
y_train_pred_original = lr_original.predict(X_train)
y_train_pred_poly = lr_poly.predict(X_poly_train)
r2_train_original = r2_score(y_train, y_train_pred_original)
r2_train_poly = r2_score(y_train, y_train_pred_poly)

print("\nLinear Regression Results:")
print("-" * 60)
print(f"{'Features':<20} {'Train R²':>12} {'Test R²':>12} {'Test RMSE':>12}")
print("-" * 60)
print(f"{'Original':<20} {r2_train_original:>12.4f} {r2_original:>12.4f} {rmse_original:>12.2f}")
print(f"{'Polynomial':<20} {r2_train_poly:>12.4f} {r2_poly:>12.4f} {rmse_poly:>12.2f}")

# Check for overfitting
print("\nOverfitting Analysis:")
gap_original = r2_train_original - r2_original
gap_poly = r2_train_poly - r2_poly
print(f"  Original features gap (train - test): {gap_original:.4f}")
print(f"  Polynomial features gap (train - test): {gap_poly:.4f}")

if gap_poly > gap_original + 0.1:
    print("\n  WARNING: Polynomial features show signs of overfitting!")
    print("  The model fits training data much better than test data.")

# =============================================================================
# 5. Cross-Validation Comparison
# =============================================================================
print("\n" + "=" * 60)
print("5. CROSS-VALIDATION COMPARISON")
print("=" * 60)

# CV for original features
cv_original = cross_val_score(lr_original, X, y, cv=5, scoring='r2')

# CV for polynomial features
cv_poly = cross_val_score(lr_poly, X_poly, y, cv=5, scoring='r2')

print("\n5-Fold Cross-Validation R² Scores:")
print("-" * 50)
print(f"Original:   {cv_original.mean():.4f} +/- {cv_original.std():.4f}")
print(f"Polynomial: {cv_poly.mean():.4f} +/- {cv_poly.std():.4f}")

# =============================================================================
# 6. Regularization with Polynomial Features
# =============================================================================
print("\n" + "=" * 60)
print("6. REGULARIZATION WITH POLYNOMIAL FEATURES")
print("=" * 60)

alpha_values = [0.01, 0.1, 1.0, 10, 100, 1000]

results = {'alpha': alpha_values, 'ridge_train': [], 'ridge_test': [],
           'lasso_train': [], 'lasso_test': [], 'lasso_nonzero': []}

print("\nRidge and Lasso with Polynomial Features:")
print("-" * 80)
print(f"{'Alpha':<10} {'Ridge Train':>12} {'Ridge Test':>12} {'Lasso Train':>12} {'Lasso Test':>12} {'Lasso NZ':>10}")
print("-" * 80)

for alpha in alpha_values:
    # Ridge
    ridge = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', Ridge(alpha=alpha))
    ])
    ridge.fit(X_poly_train, y_train)
    ridge_train = r2_score(y_train, ridge.predict(X_poly_train))
    ridge_test = r2_score(y_test, ridge.predict(X_poly_test))
    
    # Lasso
    lasso = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', Lasso(alpha=alpha, max_iter=10000))
    ])
    lasso.fit(X_poly_train, y_train)
    lasso_train = r2_score(y_train, lasso.predict(X_poly_train))
    lasso_test = r2_score(y_test, lasso.predict(X_poly_test))
    lasso_nonzero = np.sum(np.abs(lasso.named_steps['regressor'].coef_) > 1e-10)
    
    results['ridge_train'].append(ridge_train)
    results['ridge_test'].append(ridge_test)
    results['lasso_train'].append(lasso_train)
    results['lasso_test'].append(lasso_test)
    results['lasso_nonzero'].append(lasso_nonzero)
    
    print(f"{alpha:<10} {ridge_train:>12.4f} {ridge_test:>12.4f} {lasso_train:>12.4f} {lasso_test:>12.4f} {lasso_nonzero:>10}")

# =============================================================================
# 7. Visualization
# =============================================================================
print("\n" + "=" * 60)
print("7. VISUALIZATION")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Ridge performance vs alpha
ax1 = axes[0, 0]
ax1.semilogx(alpha_values, results['ridge_train'], 'b-o', label='Train')
ax1.semilogx(alpha_values, results['ridge_test'], 'r-o', label='Test')
ax1.set_xlabel('Alpha (log scale)')
ax1.set_ylabel('R² Score')
ax1.set_title('Ridge Regression: R² vs Alpha')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Lasso performance vs alpha
ax2 = axes[0, 1]
ax2.semilogx(alpha_values, results['lasso_train'], 'b-o', label='Train')
ax2.semilogx(alpha_values, results['lasso_test'], 'r-o', label='Test')
ax2.set_xlabel('Alpha (log scale)')
ax2.set_ylabel('R² Score')
ax2.set_title('Lasso Regression: R² vs Alpha')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Lasso feature selection
ax3 = axes[1, 0]
ax3.semilogx(alpha_values, results['lasso_nonzero'], 'g-o')
ax3.set_xlabel('Alpha (log scale)')
ax3.set_ylabel('Number of Non-Zero Coefficients')
ax3.set_title('Lasso Feature Selection')
ax3.axhline(y=X_poly.shape[1], color='k', linestyle='--', label=f'Total features ({X_poly.shape[1]})')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Plot 4: Comparison of best models
ax4 = axes[1, 1]
models_comparison = {
    'Linear\n(Original)': r2_original,
    'Linear\n(Poly)': r2_poly,
    'Ridge\n(Poly, best)': max(results['ridge_test']),
    'Lasso\n(Poly, best)': max(results['lasso_test'])
}
bars = ax4.bar(range(len(models_comparison)), list(models_comparison.values()))
ax4.set_xticks(range(len(models_comparison)))
ax4.set_xticklabels(list(models_comparison.keys()))
ax4.set_ylabel('Test R² Score')
ax4.set_title('Model Comparison')
ax4.grid(True, alpha=0.3, axis='y')

# Color best bar
best_idx = np.argmax(list(models_comparison.values()))
bars[best_idx].set_color('green')

plt.tight_layout()
plt.savefig('ex4_2_feature_engineering.png', dpi=150)
plt.close()
print("Plots saved to ex4_2_feature_engineering.png")

# =============================================================================
# 8. Summary
# =============================================================================
print("\n" + "=" * 60)
print("8. SUMMARY")
print("=" * 60)

# Find best configurations
best_ridge_alpha = alpha_values[np.argmax(results['ridge_test'])]
best_lasso_alpha = alpha_values[np.argmax(results['lasso_test'])]

print("\nBest Configurations:")
print(f"  Ridge: alpha={best_ridge_alpha}, Test R²={max(results['ridge_test']):.4f}")
print(f"  Lasso: alpha={best_lasso_alpha}, Test R²={max(results['lasso_test']):.4f}")

print("\nKey Findings:")
print(f"  1. Original features Linear Regression: R²={r2_original:.4f}")
print(f"  2. Polynomial features without regularization: R²={r2_poly:.4f}")
print(f"  3. Polynomial + Ridge (best): R²={max(results['ridge_test']):.4f}")
print(f"  4. Polynomial + Lasso (best): R²={max(results['lasso_test']):.4f}")

if max(results['ridge_test']) > r2_poly or max(results['lasso_test']) > r2_poly:
    print("\n  CONCLUSION: Regularization helps when using polynomial features!")
    print("  It prevents overfitting by constraining coefficient magnitudes.")
else:
    print("\n  CONCLUSION: Polynomial features may not help for this dataset.")
    print("  The relationship might already be well-captured by linear features.")

print("\n" + "=" * 60)
print("EXERCISE 4.2 COMPLETE")
print("=" * 60)
