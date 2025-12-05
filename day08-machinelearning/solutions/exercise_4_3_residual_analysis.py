"""
Exercise 4.3: Residual Analysis
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for thorough residual analysis of regression models.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Load Data and Train Model
# =============================================================================
print("=" * 60)
print("1. LOADING DATA AND TRAINING MODEL")
print("=" * 60)

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Train multiple models for comparison
models = {
    'Linear Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ]),
    'Ridge Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', Ridge(alpha=1.0))
    ]),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    r2 = r2_score(y_test, model.predict(X_test))
    print(f"{name}: R² = {r2:.4f}")

# =============================================================================
# 2. Calculate Residuals
# =============================================================================
print("\n" + "=" * 60)
print("2. CALCULATING RESIDUALS")
print("=" * 60)

# Use Linear Regression for detailed analysis
model = models['Linear Regression']
y_pred = model.predict(X_test)
residuals = y_test - y_pred

print(f"\nResidual Statistics:")
print(f"  Mean: {residuals.mean():.4f} (should be ~0)")
print(f"  Std:  {residuals.std():.2f}")
print(f"  Min:  {residuals.min():.2f}")
print(f"  Max:  {residuals.max():.2f}")

# =============================================================================
# 3. Residual Plots
# =============================================================================
print("\n" + "=" * 60)
print("3. CREATING RESIDUAL PLOTS")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Residuals vs Predicted Values
ax1 = axes[0, 0]
ax1.scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5)
ax1.axhline(y=0, color='r', linestyle='--', lw=2)
ax1.set_xlabel('Predicted Values')
ax1.set_ylabel('Residuals')
ax1.set_title('Residuals vs Predicted Values')
ax1.grid(True, alpha=0.3)

# Add LOWESS smoothing line
try:
    from statsmodels.nonparametric.smoothers_lowess import lowess
    smoothed = lowess(residuals, y_pred, frac=0.3)
    ax1.plot(smoothed[:, 0], smoothed[:, 1], 'g-', lw=2, label='LOWESS')
    ax1.legend()
except ImportError:
    pass

# Plot 2: Histogram of Residuals
ax2 = axes[0, 1]
ax2.hist(residuals, bins=20, edgecolor='black', alpha=0.7, density=True)
# Overlay normal distribution
x_norm = np.linspace(residuals.min(), residuals.max(), 100)
ax2.plot(x_norm, stats.norm.pdf(x_norm, residuals.mean(), residuals.std()),
         'r-', lw=2, label='Normal Distribution')
ax2.set_xlabel('Residuals')
ax2.set_ylabel('Density')
ax2.set_title('Histogram of Residuals')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Q-Q Plot
ax3 = axes[1, 0]
stats.probplot(residuals, dist="norm", plot=ax3)
ax3.set_title('Q-Q Plot of Residuals')
ax3.grid(True, alpha=0.3)

# Plot 4: Scale-Location Plot (sqrt of standardized residuals vs predicted)
ax4 = axes[1, 1]
standardized_residuals = residuals / residuals.std()
ax4.scatter(y_pred, np.sqrt(np.abs(standardized_residuals)), alpha=0.6, edgecolors='k', linewidth=0.5)
ax4.set_xlabel('Predicted Values')
ax4.set_ylabel('√|Standardized Residuals|')
ax4.set_title('Scale-Location Plot')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex4_3_residual_plots.png', dpi=150)
plt.close()
print("Main residual plots saved to ex4_3_residual_plots.png")

# =============================================================================
# 4. Residuals vs Each Feature
# =============================================================================
print("\n" + "=" * 60)
print("4. RESIDUALS VS EACH FEATURE")
print("=" * 60)

n_features = X.shape[1]
n_cols = 5
n_rows = (n_features + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 6))
axes = axes.flatten()

for i, (ax, fname) in enumerate(zip(axes[:n_features], feature_names)):
    ax.scatter(X_test[:, i], residuals, alpha=0.6, s=30)
    ax.axhline(y=0, color='r', linestyle='--', lw=1)
    ax.set_xlabel(fname)
    ax.set_ylabel('Residuals')
    ax.set_title(f'Residuals vs {fname}')
    ax.grid(True, alpha=0.3)

# Hide unused subplots
for ax in axes[n_features:]:
    ax.axis('off')

plt.tight_layout()
plt.savefig('ex4_3_residuals_vs_features.png', dpi=150)
plt.close()
print("Residuals vs features plot saved to ex4_3_residuals_vs_features.png")

# =============================================================================
# 5. Statistical Tests
# =============================================================================
print("\n" + "=" * 60)
print("5. STATISTICAL TESTS FOR RESIDUALS")
print("=" * 60)

# Shapiro-Wilk test for normality
stat, p_value = stats.shapiro(residuals)
print(f"\nShapiro-Wilk Test for Normality:")
print(f"  Statistic: {stat:.4f}")
print(f"  P-value: {p_value:.4f}")
if p_value > 0.05:
    print("  Conclusion: Residuals appear normally distributed (p > 0.05)")
else:
    print("  Conclusion: Residuals may not be normally distributed (p < 0.05)")

# Durbin-Watson test for autocorrelation (if samples are ordered)
# Note: This is more relevant for time series data
from scipy.stats import pearsonr
if len(residuals) > 2:
    autocorr, _ = pearsonr(residuals[:-1], residuals[1:])
    print(f"\nAutocorrelation (lag-1):")
    print(f"  Correlation: {autocorr:.4f}")
    if abs(autocorr) < 0.2:
        print("  Conclusion: No significant autocorrelation")
    else:
        print("  Conclusion: Some autocorrelation present")

# Check for heteroscedasticity (Breusch-Pagan-like visual check)
print("\nHeteroscedasticity Check:")
# Divide predictions into quartiles and check residual variance
quartiles = np.percentile(y_pred, [25, 50, 75])
q_labels = ['Q1', 'Q2', 'Q3', 'Q4']
q_vars = []
for i in range(4):
    if i == 0:
        mask = y_pred <= quartiles[0]
    elif i == 3:
        mask = y_pred > quartiles[2]
    else:
        mask = (y_pred > quartiles[i-1]) & (y_pred <= quartiles[i])
    q_vars.append(residuals[mask].var())
    print(f"  {q_labels[i]} variance: {q_vars[-1]:.2f}")

if max(q_vars) / min(q_vars) > 3:
    print("  Conclusion: Possible heteroscedasticity (variance ratio > 3)")
else:
    print("  Conclusion: Variance appears relatively constant")

# =============================================================================
# 6. Outlier Detection
# =============================================================================
print("\n" + "=" * 60)
print("6. OUTLIER DETECTION")
print("=" * 60)

# Standardized residuals
std_residuals = (residuals - residuals.mean()) / residuals.std()

# Identify outliers (|z| > 2 or |z| > 3)
outliers_2 = np.abs(std_residuals) > 2
outliers_3 = np.abs(std_residuals) > 3

print(f"\nOutliers (|standardized residual| > 2): {np.sum(outliers_2)} ({100*np.mean(outliers_2):.1f}%)")
print(f"Outliers (|standardized residual| > 3): {np.sum(outliers_3)} ({100*np.mean(outliers_3):.1f}%)")

if np.sum(outliers_3) > 0:
    print("\nExtreme outliers (|z| > 3):")
    outlier_indices = np.where(outliers_3)[0]
    for idx in outlier_indices:
        print(f"  Sample {idx}: y_true={y_test[idx]:.1f}, y_pred={y_pred[idx]:.1f}, residual={residuals[idx]:.1f}")

# =============================================================================
# 7. Model Comparison Residual Analysis
# =============================================================================
print("\n" + "=" * 60)
print("7. MODEL COMPARISON")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, (name, model) in zip(axes, models.items()):
    y_pred_model = model.predict(X_test)
    residuals_model = y_test - y_pred_model
    
    ax.scatter(y_pred_model, residuals_model, alpha=0.6, edgecolors='k', linewidth=0.5)
    ax.axhline(y=0, color='r', linestyle='--', lw=2)
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Residuals')
    ax.set_title(f'{name}\nResidual Std: {residuals_model.std():.2f}')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex4_3_model_comparison.png', dpi=150)
plt.close()
print("Model comparison plot saved to ex4_3_model_comparison.png")

# =============================================================================
# 8. Interpretation Summary
# =============================================================================
print("\n" + "=" * 60)
print("8. INTERPRETATION SUMMARY")
print("=" * 60)

print("""
RESIDUAL ANALYSIS INTERPRETATION:
---------------------------------

1. RESIDUALS VS PREDICTED VALUES:
   - Look for: Random scatter around zero
   - Problem signs: Funnel shape (heteroscedasticity), curves (non-linearity)
   
2. HISTOGRAM OF RESIDUALS:
   - Look for: Bell-shaped, centered at zero
   - Problem signs: Skewness, multiple peaks, heavy tails

3. Q-Q PLOT:
   - Look for: Points following the diagonal line
   - Problem signs: S-curves (heavy tails), deviations at ends

4. RESIDUALS VS FEATURES:
   - Look for: Random scatter, no patterns
   - Problem signs: Curves suggest missing polynomial terms

5. OUTLIERS:
   - A few outliers (< 5%) are normal
   - Many outliers may indicate model problems or data issues

WHAT TO DO IF PROBLEMS ARE FOUND:
---------------------------------
- Non-linearity: Add polynomial features or use non-linear models
- Heteroscedasticity: Transform target variable or use weighted regression
- Non-normality: May affect confidence intervals but not predictions
- Outliers: Investigate data quality, consider robust regression
""")

print("=" * 60)
print("EXERCISE 4.3 COMPLETE")
print("=" * 60)
