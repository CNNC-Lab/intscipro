"""
Exercise 4.1: Diabetes Regression
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for regression analysis with multiple models and regularization comparison.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load and Explore Diabetes Dataset
# =============================================================================
print("=" * 60)
print("1. DATA EXPLORATION")
print("=" * 60)

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Feature names: {feature_names}")
print(f"\nTarget statistics:")
print(f"  Mean: {y.mean():.2f}")
print(f"  Std:  {y.std():.2f}")
print(f"  Min:  {y.min():.2f}")
print(f"  Max:  {y.max():.2f}")

# =============================================================================
# 2. Check Feature Correlations
# =============================================================================
print("\n" + "=" * 60)
print("2. FEATURE CORRELATIONS")
print("=" * 60)

# Create DataFrame for correlation analysis
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Correlation with target
correlations = df.corr()['target'].drop('target').sort_values(ascending=False)
print("\nCorrelation with target:")
for feat, corr in correlations.items():
    print(f"  {feat:>6s}: {corr:+.4f}")

# Plot correlation heatmap
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Feature correlations
ax1 = axes[0]
corr_matrix = df.corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, ax=ax1, annot_kws={'size': 8})
ax1.set_title('Feature Correlation Matrix')

# Correlation with target
ax2 = axes[1]
colors = ['green' if c > 0 else 'red' for c in correlations.values]
ax2.barh(range(len(correlations)), correlations.values, color=colors)
ax2.set_yticks(range(len(correlations)))
ax2.set_yticklabels(correlations.index)
ax2.set_xlabel('Correlation with Target')
ax2.set_title('Feature Correlation with Target')
ax2.axvline(x=0, color='black', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.savefig('ex4_1_correlations.png', dpi=150)
plt.close()
print("\nCorrelation plots saved to ex4_1_correlations.png")

# =============================================================================
# 3. Split Data (80/20)
# =============================================================================
print("\n" + "=" * 60)
print("3. DATA SPLITTING")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# =============================================================================
# 4. Train Multiple Models
# =============================================================================
print("\n" + "=" * 60)
print("4. TRAINING MODELS")
print("=" * 60)

# Define alpha values for regularization
alpha_values = [0.1, 1.0, 10, 100]

# Define models
models = {
    'Linear Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ]),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

# Add Ridge models with different alphas
for alpha in alpha_values:
    models[f'Ridge (alpha={alpha})'] = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', Ridge(alpha=alpha))
    ])

# Add Lasso models with different alphas
for alpha in alpha_values:
    models[f'Lasso (alpha={alpha})'] = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', Lasso(alpha=alpha, max_iter=10000))
    ])

# Train and evaluate all models
results = {}

print("\nModel Performance:")
print("-" * 80)
print(f"{'Model':<30} {'R²':>10} {'RMSE':>10} {'MAE':>10}")
print("-" * 80)

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    
    results[name] = {'r2': r2, 'rmse': rmse, 'mae': mae, 'y_pred': y_pred}
    print(f"{name:<30} {r2:>10.4f} {rmse:>10.2f} {mae:>10.2f}")

# =============================================================================
# 5. Predicted vs Actual Plots
# =============================================================================
print("\n" + "=" * 60)
print("5. PREDICTED VS ACTUAL PLOTS")
print("=" * 60)

# Select key models for visualization
key_models = ['Linear Regression', 'Ridge (alpha=1.0)', 'Lasso (alpha=1.0)', 'Random Forest']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for ax, name in zip(axes, key_models):
    y_pred = results[name]['y_pred']
    r2 = results[name]['r2']
    
    ax.scatter(y_test, y_pred, alpha=0.6, edgecolors='k', linewidth=0.5)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.set_title(f'{name}\nR² = {r2:.4f}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Predicted vs Actual Values', fontsize=14)
plt.tight_layout()
plt.savefig('ex4_1_predicted_vs_actual.png', dpi=150)
plt.close()
print("Predicted vs Actual plots saved to ex4_1_predicted_vs_actual.png")

# =============================================================================
# 6. Residual Plots
# =============================================================================
print("\n" + "=" * 60)
print("6. RESIDUAL PLOTS")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for ax, name in zip(axes, key_models):
    y_pred = results[name]['y_pred']
    residuals = y_test - y_pred
    
    ax.scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5)
    ax.axhline(y=0, color='r', linestyle='--', lw=2)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Residuals')
    ax.set_title(f'{name}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Residual Plots', fontsize=14)
plt.tight_layout()
plt.savefig('ex4_1_residuals.png', dpi=150)
plt.close()
print("Residual plots saved to ex4_1_residuals.png")

# =============================================================================
# 7. Regularization Comparison - Coefficients
# =============================================================================
print("\n" + "=" * 60)
print("7. REGULARIZATION COMPARISON")
print("=" * 60)

# Get coefficients from Linear, Ridge, and Lasso
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Linear Regression coefficients
ax1 = axes[0, 0]
lr_coefs = models['Linear Regression'].named_steps['regressor'].coef_
ax1.bar(range(len(feature_names)), lr_coefs)
ax1.set_xticks(range(len(feature_names)))
ax1.set_xticklabels(feature_names, rotation=45, ha='right')
ax1.set_ylabel('Coefficient')
ax1.set_title('Linear Regression Coefficients')
ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

# Ridge coefficients for different alphas
ax2 = axes[0, 1]
for alpha in alpha_values:
    ridge_coefs = models[f'Ridge (alpha={alpha})'].named_steps['regressor'].coef_
    ax2.plot(range(len(feature_names)), ridge_coefs, marker='o', label=f'alpha={alpha}')
ax2.set_xticks(range(len(feature_names)))
ax2.set_xticklabels(feature_names, rotation=45, ha='right')
ax2.set_ylabel('Coefficient')
ax2.set_title('Ridge Coefficients by Alpha')
ax2.legend()
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

# Lasso coefficients for different alphas
ax3 = axes[1, 0]
for alpha in alpha_values:
    lasso_coefs = models[f'Lasso (alpha={alpha})'].named_steps['regressor'].coef_
    ax3.plot(range(len(feature_names)), lasso_coefs, marker='o', label=f'alpha={alpha}')
ax3.set_xticks(range(len(feature_names)))
ax3.set_xticklabels(feature_names, rotation=45, ha='right')
ax3.set_ylabel('Coefficient')
ax3.set_title('Lasso Coefficients by Alpha')
ax3.legend()
ax3.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

# Number of non-zero coefficients in Lasso
ax4 = axes[1, 1]
non_zero_counts = []
for alpha in alpha_values:
    lasso_coefs = models[f'Lasso (alpha={alpha})'].named_steps['regressor'].coef_
    non_zero = np.sum(np.abs(lasso_coefs) > 1e-10)
    non_zero_counts.append(non_zero)
ax4.bar(range(len(alpha_values)), non_zero_counts)
ax4.set_xticks(range(len(alpha_values)))
ax4.set_xticklabels([str(a) for a in alpha_values])
ax4.set_xlabel('Alpha')
ax4.set_ylabel('Number of Non-Zero Coefficients')
ax4.set_title('Lasso Feature Selection')

plt.tight_layout()
plt.savefig('ex4_1_regularization_comparison.png', dpi=150)
plt.close()
print("Regularization comparison saved to ex4_1_regularization_comparison.png")

# Print which features Lasso zeros out
print("\nLasso Feature Selection (alpha=1.0):")
lasso_coefs = models['Lasso (alpha=1.0)'].named_steps['regressor'].coef_
for i, (name, coef) in enumerate(zip(feature_names, lasso_coefs)):
    status = "KEPT" if np.abs(coef) > 1e-10 else "ZEROED"
    print(f"  {name:>6s}: {coef:+.4f} ({status})")

# =============================================================================
# 8. Learning Curves
# =============================================================================
print("\n" + "=" * 60)
print("8. LEARNING CURVES")
print("=" * 60)

# Select best model based on test R²
best_model_name = max(results.keys(), key=lambda k: results[k]['r2'])
best_model = models[best_model_name]

print(f"\nBest model: {best_model_name} (R² = {results[best_model_name]['r2']:.4f})")

# Create learning curves for key models
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for ax, name in zip(axes, key_models):
    model = models[name]
    
    train_sizes, train_scores, val_scores = learning_curve(
        model, X, y,
        train_sizes=np.linspace(0.1, 1.0, 10),
        cv=5,
        scoring='r2',
        random_state=42
    )
    
    train_mean = train_scores.mean(axis=1)
    train_std = train_scores.std(axis=1)
    val_mean = val_scores.mean(axis=1)
    val_std = val_scores.std(axis=1)
    
    ax.plot(train_sizes, train_mean, label='Training', color='blue')
    ax.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2, color='blue')
    ax.plot(train_sizes, val_mean, label='Validation', color='orange')
    ax.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.2, color='orange')
    
    ax.set_xlabel('Training Set Size')
    ax.set_ylabel('R² Score')
    ax.set_title(f'{name}')
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)

plt.suptitle('Learning Curves', fontsize=14)
plt.tight_layout()
plt.savefig('ex4_1_learning_curves.png', dpi=150)
plt.close()
print("Learning curves saved to ex4_1_learning_curves.png")

# =============================================================================
# 9. Summary
# =============================================================================
print("\n" + "=" * 60)
print("9. SUMMARY")
print("=" * 60)

print("\nBest performing models (by R²):")
sorted_models = sorted(results.items(), key=lambda x: x[1]['r2'], reverse=True)
for i, (name, metrics) in enumerate(sorted_models[:5]):
    print(f"  {i+1}. {name}: R²={metrics['r2']:.4f}, RMSE={metrics['rmse']:.2f}")

print("\nOverfitting/Underfitting Analysis:")
print("  - If training score >> validation score: Overfitting")
print("  - If both scores are low: Underfitting")
print("  - If both scores are high and close: Good fit")
print("\nBased on learning curves, the models show:")
print("  - Linear models: Slight underfitting (limited capacity)")
print("  - Random Forest: Good fit with some variance")

print("\n" + "=" * 60)
print("EXERCISE 4.1 COMPLETE")
print("=" * 60)
