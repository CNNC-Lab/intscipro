"""
Challenge 8.1: Imbalanced Medical Diagnosis
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for handling heavily imbalanced data (1% positive class).
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc,
    precision_recall_curve, average_precision_score
)

# Set random seed
np.random.seed(42)

# =============================================================================
# 1. Create Heavily Imbalanced Dataset
# =============================================================================
print("=" * 60)
print("1. CREATING IMBALANCED DATASET (1% positive)")
print("=" * 60)

X, y = make_classification(
    n_samples=10000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    weights=[0.99, 0.01],  # 99% negative, 1% positive
    random_state=42
)

print(f"Total samples: {len(y)}")
print(f"Negative class (0): {np.sum(y == 0)} ({100 * np.mean(y == 0):.1f}%)")
print(f"Positive class (1): {np.sum(y == 1)} ({100 * np.mean(y == 1):.1f}%)")

# Split data with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set: {len(y_train)} samples")
print(f"  Positive: {np.sum(y_train == 1)} ({100 * np.mean(y_train == 1):.1f}%)")
print(f"Test set: {len(y_test)} samples")
print(f"  Positive: {np.sum(y_test == 1)} ({100 * np.mean(y_test == 1):.1f}%)")

# =============================================================================
# 2. Demonstrate Why Accuracy is Useless
# =============================================================================
print("\n" + "=" * 60)
print("2. WHY ACCURACY IS USELESS")
print("=" * 60)

# Naive classifier that always predicts negative
y_pred_naive = np.zeros_like(y_test)
accuracy_naive = accuracy_score(y_test, y_pred_naive)
recall_naive = recall_score(y_test, y_pred_naive)

print("\nNaive classifier (always predicts negative):")
print(f"  Accuracy: {accuracy_naive:.2%}")
print(f"  Recall: {recall_naive:.2%}")
print(f"\n  This classifier has {accuracy_naive:.0%} accuracy but misses ALL positive cases!")
print("  In medical diagnosis, this would mean missing ALL disease cases.")

# =============================================================================
# 3. Train Models Without Class Balancing
# =============================================================================
print("\n" + "=" * 60)
print("3. MODELS WITHOUT CLASS BALANCING")
print("=" * 60)

pipeline_unbalanced = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

pipeline_unbalanced.fit(X_train, y_train)
y_pred_unbal = pipeline_unbalanced.predict(X_test)

print("\nLogistic Regression (no class_weight):")
print(f"  Accuracy:  {accuracy_score(y_test, y_pred_unbal):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_unbal):.4f}")
print(f"  Recall:    {recall_score(y_test, y_pred_unbal):.4f}")
print(f"  F1-Score:  {f1_score(y_test, y_pred_unbal):.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_unbal))

# =============================================================================
# 4. Train Models WITH Class Balancing
# =============================================================================
print("\n" + "=" * 60)
print("4. MODELS WITH class_weight='balanced'")
print("=" * 60)

pipeline_balanced = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'))
])

pipeline_balanced.fit(X_train, y_train)
y_pred_bal = pipeline_balanced.predict(X_test)

print("\nLogistic Regression (class_weight='balanced'):")
print(f"  Accuracy:  {accuracy_score(y_test, y_pred_bal):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_bal):.4f}")
print(f"  Recall:    {recall_score(y_test, y_pred_bal):.4f}")
print(f"  F1-Score:  {f1_score(y_test, y_pred_bal):.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_bal))

# =============================================================================
# 5. Stratified Cross-Validation
# =============================================================================
print("\n" + "=" * 60)
print("5. STRATIFIED CROSS-VALIDATION")
print("=" * 60)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Compare metrics
for name, pipeline in [('Unbalanced', pipeline_unbalanced), ('Balanced', pipeline_balanced)]:
    acc_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')
    f1_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='f1')
    recall_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='recall')
    
    print(f"\n{name}:")
    print(f"  Accuracy: {acc_scores.mean():.4f} +/- {acc_scores.std():.4f}")
    print(f"  F1-Score: {f1_scores.mean():.4f} +/- {f1_scores.std():.4f}")
    print(f"  Recall:   {recall_scores.mean():.4f} +/- {recall_scores.std():.4f}")

# =============================================================================
# 6. Find Optimal Threshold
# =============================================================================
print("\n" + "=" * 60)
print("6. FINDING OPTIMAL THRESHOLD")
print("=" * 60)

# Get probability predictions
y_prob = pipeline_balanced.predict_proba(X_test)[:, 1]

# Calculate precision-recall for different thresholds
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)

# Find threshold for different recall targets
print("\nThreshold analysis:")
print("-" * 60)
print(f"{'Target Recall':>15} {'Threshold':>12} {'Precision':>12} {'F1':>12}")
print("-" * 60)

for target_recall in [0.7, 0.8, 0.9, 0.95]:
    # Find threshold that achieves target recall
    idx = np.argmin(np.abs(recalls - target_recall))
    if idx < len(thresholds):
        thresh = thresholds[idx]
        prec = precisions[idx]
        rec = recalls[idx]
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        print(f"{target_recall:>15.0%} {thresh:>12.4f} {prec:>12.4f} {f1:>12.4f}")

# Find threshold that maximizes F1
f1_scores_thresh = 2 * precisions * recalls / (precisions + recalls + 1e-10)
best_idx = np.argmax(f1_scores_thresh[:-1])  # Exclude last element
best_threshold = thresholds[best_idx]
best_f1 = f1_scores_thresh[best_idx]

print(f"\nOptimal threshold (max F1): {best_threshold:.4f}")
print(f"F1 at optimal threshold: {best_f1:.4f}")

# Apply optimal threshold
y_pred_optimal = (y_prob >= best_threshold).astype(int)
print(f"\nWith optimal threshold ({best_threshold:.4f}):")
print(f"  Precision: {precision_score(y_test, y_pred_optimal):.4f}")
print(f"  Recall:    {recall_score(y_test, y_pred_optimal):.4f}")
print(f"  F1-Score:  {f1_score(y_test, y_pred_optimal):.4f}")

# =============================================================================
# 7. Visualization
# =============================================================================
print("\n" + "=" * 60)
print("7. VISUALIZATION")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# ROC Curve
ax1 = axes[0, 0]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
ax1.plot(fpr, tpr, 'b-', label=f'ROC (AUC = {roc_auc:.3f})')
ax1.plot([0, 1], [0, 1], 'k--', label='Random')
ax1.set_xlabel('False Positive Rate')
ax1.set_ylabel('True Positive Rate')
ax1.set_title('ROC Curve')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Precision-Recall Curve
ax2 = axes[0, 1]
ap = average_precision_score(y_test, y_prob)
ax2.plot(recalls, precisions, 'b-', label=f'PR (AP = {ap:.3f})')
ax2.axhline(y=np.mean(y_test), color='k', linestyle='--', label=f'Baseline ({np.mean(y_test):.3f})')
ax2.axvline(x=recalls[best_idx], color='r', linestyle='--', alpha=0.5)
ax2.axhline(y=precisions[best_idx], color='r', linestyle='--', alpha=0.5)
ax2.scatter([recalls[best_idx]], [precisions[best_idx]], color='red', s=100, zorder=5, label='Optimal')
ax2.set_xlabel('Recall')
ax2.set_ylabel('Precision')
ax2.set_title('Precision-Recall Curve')
ax2.legend()
ax2.grid(True, alpha=0.3)

# F1 vs Threshold
ax3 = axes[1, 0]
ax3.plot(thresholds, f1_scores_thresh[:-1], 'g-')
ax3.axvline(x=best_threshold, color='r', linestyle='--', label=f'Optimal ({best_threshold:.3f})')
ax3.axvline(x=0.5, color='k', linestyle='--', alpha=0.5, label='Default (0.5)')
ax3.set_xlabel('Threshold')
ax3.set_ylabel('F1 Score')
ax3.set_title('F1 Score vs Threshold')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Confusion Matrix Comparison
ax4 = axes[1, 1]
cm_default = confusion_matrix(y_test, y_pred_bal)
cm_optimal = confusion_matrix(y_test, y_pred_optimal)

labels = ['Default (0.5)', f'Optimal ({best_threshold:.2f})']
metrics = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
default_vals = [cm_default[0, 0], cm_default[0, 1], cm_default[1, 0], cm_default[1, 1]]
optimal_vals = [cm_optimal[0, 0], cm_optimal[0, 1], cm_optimal[1, 0], cm_optimal[1, 1]]

x = np.arange(len(metrics))
width = 0.35
ax4.bar(x - width/2, default_vals, width, label='Default', alpha=0.7)
ax4.bar(x + width/2, optimal_vals, width, label='Optimal', alpha=0.7)
ax4.set_xticks(x)
ax4.set_xticklabels(metrics, rotation=45)
ax4.set_ylabel('Count')
ax4.set_title('Confusion Matrix Comparison')
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('challenge_8_1_imbalanced.png', dpi=150)
plt.close()
print("Visualization saved to challenge_8_1_imbalanced.png")

# =============================================================================
# 8. Clinical Considerations
# =============================================================================
print("\n" + "=" * 60)
print("8. CLINICAL CONSIDERATIONS")
print("=" * 60)

print("""
TRADEOFF ANALYSIS:
------------------

For a rare disease diagnostic system:

HIGH RECALL (e.g., 95%):
  - Catches most disease cases
  - More false positives (healthy people flagged)
  - Good for: Screening tests, serious diseases
  - Cost: More follow-up tests, patient anxiety

HIGH PRECISION (e.g., 95%):
  - Few false alarms
  - May miss some disease cases
  - Good for: Confirmatory tests, expensive treatments
  - Cost: Missed diagnoses

RECOMMENDATION FOR MEDICAL DIAGNOSIS:
--------------------------------------
1. Use HIGH RECALL for initial screening
   - Better to have false alarms than miss cases
   - Follow up with more specific tests

2. Use HIGH PRECISION for treatment decisions
   - Avoid unnecessary treatments
   - Reduce side effects and costs

3. Consider the specific disease:
   - Life-threatening: Prioritize recall
   - Treatable with side effects: Balance both
   - Expensive treatment: Consider precision
""")

# Final summary
print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print(f"""
Results with 1% positive class:

1. Naive classifier (always negative): {accuracy_naive:.0%} accuracy, 0% recall
   - Useless despite high accuracy!

2. Without class balancing:
   - Accuracy: {accuracy_score(y_test, y_pred_unbal):.2%}
   - Recall: {recall_score(y_test, y_pred_unbal):.2%}

3. With class_weight='balanced':
   - Accuracy: {accuracy_score(y_test, y_pred_bal):.2%}
   - Recall: {recall_score(y_test, y_pred_bal):.2%}

4. With optimal threshold ({best_threshold:.3f}):
   - Recall: {recall_score(y_test, y_pred_optimal):.2%}
   - Precision: {precision_score(y_test, y_pred_optimal):.2%}
   - F1: {f1_score(y_test, y_pred_optimal):.2%}

KEY TAKEAWAY: For imbalanced medical data, NEVER use accuracy!
Use F1-score, precision-recall curves, and adjust thresholds based on
clinical requirements.
""")

print("=" * 60)
print("CHALLENGE 8.1 COMPLETE")
print("=" * 60)
