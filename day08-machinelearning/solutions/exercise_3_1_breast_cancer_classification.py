"""
Exercise 3.1: Breast Cancer Classification
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for breast cancer classification using multiple classifiers.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score, classification_report,
    ConfusionMatrixDisplay, RocCurveDisplay
)

# Set random seed for reproducibility
np.random.seed(42)

# =============================================================================
# 1. Load and Explore Data
# =============================================================================
print("=" * 60)
print("1. DATA EXPLORATION")
print("=" * 60)

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

print(f"Number of features: {X.shape[1]}")
print(f"Number of samples: {X.shape[0]}")
print(f"\nFeature names:\n{cancer.feature_names}")
print(f"\nTarget names: {cancer.target_names}")
print(f"\nClass distribution:")
print(f"  - Malignant (0): {np.sum(y == 0)} ({100 * np.sum(y == 0) / len(y):.1f}%)")
print(f"  - Benign (1): {np.sum(y == 1)} ({100 * np.sum(y == 1) / len(y):.1f}%)")
print(f"\nDataset is {'balanced' if 0.4 < np.mean(y) < 0.6 else 'slightly imbalanced'}")

# =============================================================================
# 2. Split Data (80/20 with stratification)
# =============================================================================
print("\n" + "=" * 60)
print("2. DATA SPLITTING")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")
print(f"Training class distribution: {np.bincount(y_train)}")
print(f"Test class distribution: {np.bincount(y_test)}")

# =============================================================================
# 3. Train Three Classifiers
# =============================================================================
print("\n" + "=" * 60)
print("3. TRAINING CLASSIFIERS")
print("=" * 60)

# Define models with pipelines (SVM needs scaling)
models = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=10000, random_state=42))
    ]),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', probability=True, random_state=42))
    ])
}

# Train all models
for name, model in models.items():
    model.fit(X_train, y_train)
    print(f"{name} trained successfully.")

# =============================================================================
# 4. Evaluate Each Model
# =============================================================================
print("\n" + "=" * 60)
print("4. MODEL EVALUATION")
print("=" * 60)

results = {}

for name, model in models.items():
    print(f"\n--- {name} ---")
    
    # Predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    
    results[name] = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'auc': auc,
        'y_pred': y_pred,
        'y_prob': y_prob
    }
    
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print(f"AUC-ROC:   {auc:.4f}")
    
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=cancer.target_names))

# =============================================================================
# 4b. Confusion Matrices
# =============================================================================
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, (name, model) in zip(axes, models.items()):
    y_pred = results[name]['y_pred']
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm, display_labels=cancer.target_names).plot(ax=ax)
    ax.set_title(f'{name}\nConfusion Matrix')

plt.tight_layout()
plt.savefig('ex3_1_confusion_matrices.png', dpi=150)
plt.close()
print("\nConfusion matrices saved to ex3_1_confusion_matrices.png")

# =============================================================================
# 4c. ROC Curves
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 6))

for name in models.keys():
    y_prob = results[name]['y_prob']
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    auc = results[name]['auc']
    ax.plot(fpr, tpr, label=f'{name} (AUC = {auc:.3f})')

ax.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('ROC Curves Comparison')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex3_1_roc_curves.png', dpi=150)
plt.close()
print("ROC curves saved to ex3_1_roc_curves.png")

# =============================================================================
# 5. Compare Models
# =============================================================================
print("\n" + "=" * 60)
print("5. MODEL COMPARISON")
print("=" * 60)

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    name: {metric: results[name][metric] for metric in ['accuracy', 'precision', 'recall', 'f1', 'auc']}
    for name in models.keys()
}).T

print("\nModel Comparison:")
print(comparison_df.round(4))

# Find best model for each metric
print("\nBest model by metric:")
for metric in ['accuracy', 'precision', 'recall', 'f1', 'auc']:
    best_model = comparison_df[metric].idxmax()
    best_score = comparison_df[metric].max()
    print(f"  {metric.capitalize():10s}: {best_model} ({best_score:.4f})")

print("\n--- Medical Diagnosis Considerations ---")
print("For medical diagnosis (cancer detection), RECALL is crucial because:")
print("  - High recall means fewer false negatives (missed cancers)")
print("  - Missing a cancer diagnosis (false negative) is more dangerous")
print("    than a false alarm (false positive)")
print(f"\nHighest recall model: {comparison_df['recall'].idxmax()} "
      f"(recall = {comparison_df['recall'].max():.4f})")

# =============================================================================
# 6. Feature Importance
# =============================================================================
print("\n" + "=" * 60)
print("6. FEATURE IMPORTANCE")
print("=" * 60)

# Random Forest feature importance
rf_model = models['Random Forest']
feature_importance = rf_model.feature_importances_
feature_names = cancer.feature_names

# Sort features by importance
sorted_idx = np.argsort(feature_importance)[::-1]

# Plot top 10 features
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Random Forest importance
ax1 = axes[0]
top_10_idx = sorted_idx[:10]
ax1.barh(range(10), feature_importance[top_10_idx][::-1])
ax1.set_yticks(range(10))
ax1.set_yticklabels([feature_names[i] for i in top_10_idx[::-1]])
ax1.set_xlabel('Feature Importance')
ax1.set_title('Random Forest: Top 10 Features')

# Logistic Regression coefficients
lr_pipeline = models['Logistic Regression']
lr_coefs = lr_pipeline.named_steps['classifier'].coef_[0]
sorted_coef_idx = np.argsort(np.abs(lr_coefs))[::-1]

ax2 = axes[1]
top_10_coef_idx = sorted_coef_idx[:10]
colors = ['green' if lr_coefs[i] > 0 else 'red' for i in top_10_coef_idx[::-1]]
ax2.barh(range(10), np.abs(lr_coefs[top_10_coef_idx])[::-1], color=colors)
ax2.set_yticks(range(10))
ax2.set_yticklabels([feature_names[i] for i in top_10_coef_idx[::-1]])
ax2.set_xlabel('|Coefficient| (green=positive, red=negative)')
ax2.set_title('Logistic Regression: Top 10 Features by |Coefficient|')

plt.tight_layout()
plt.savefig('ex3_1_feature_importance.png', dpi=150)
plt.close()
print("Feature importance plot saved to ex3_1_feature_importance.png")

print("\nTop 10 Random Forest Features:")
for i, idx in enumerate(sorted_idx[:10]):
    print(f"  {i+1}. {feature_names[idx]}: {feature_importance[idx]:.4f}")

print("\nTop 10 Logistic Regression Features (by |coefficient|):")
for i, idx in enumerate(sorted_coef_idx[:10]):
    sign = "+" if lr_coefs[idx] > 0 else "-"
    print(f"  {i+1}. {feature_names[idx]}: {sign}{np.abs(lr_coefs[idx]):.4f}")

print("\n" + "=" * 60)
print("EXERCISE 3.1 COMPLETE")
print("=" * 60)
