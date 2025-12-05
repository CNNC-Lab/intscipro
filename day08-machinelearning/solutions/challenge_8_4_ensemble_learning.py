"""
Challenge 8.4: Ensemble Learning
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for building and comparing ensemble models.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, StackingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)

# Load data
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("=" * 60)
print("ENSEMBLE LEARNING")
print("=" * 60)
print(f"Training: {len(y_train)}, Test: {len(y_test)}")

# Define base models
base_models = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=1000, random_state=42))
    ]),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', SVC(probability=True, random_state=42))
    ]),
    'KNN': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', KNeighborsClassifier(n_neighbors=5))
    ])
}

# Train and evaluate base models
print("\n--- Base Models ---")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
base_results = {}

for name, model in base_models.items():
    cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    model.fit(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    base_results[name] = {'cv': cv_scores.mean(), 'test': test_acc}
    print(f"{name}: CV={cv_scores.mean():.4f}, Test={test_acc:.4f}")

# Voting Ensemble
print("\n--- Voting Ensemble ---")
voting_clf = VotingClassifier(
    estimators=[
        ('lr', base_models['Logistic Regression']),
        ('rf', base_models['Random Forest']),
        ('svm', base_models['SVM']),
        ('knn', base_models['KNN'])
    ],
    voting='soft'
)

cv_scores = cross_val_score(voting_clf, X_train, y_train, cv=cv, scoring='accuracy')
voting_clf.fit(X_train, y_train)
voting_acc = voting_clf.score(X_test, y_test)
print(f"Voting (soft): CV={cv_scores.mean():.4f}, Test={voting_acc:.4f}")

# Stacking Ensemble
print("\n--- Stacking Ensemble ---")
stacking_clf = StackingClassifier(
    estimators=[
        ('lr', base_models['Logistic Regression']),
        ('rf', base_models['Random Forest']),
        ('svm', base_models['SVM'])
    ],
    final_estimator=LogisticRegression(random_state=42),
    cv=5
)

cv_scores = cross_val_score(stacking_clf, X_train, y_train, cv=cv, scoring='accuracy')
stacking_clf.fit(X_train, y_train)
stacking_acc = stacking_clf.score(X_test, y_test)
print(f"Stacking: CV={cv_scores.mean():.4f}, Test={stacking_acc:.4f}")

# Feature importance analysis
print("\n--- Feature Importance ---")
rf = base_models['Random Forest']
importances = rf.feature_importances_
top_5 = np.argsort(importances)[::-1][:5]
print("Top 5 features (Random Forest):")
for i, idx in enumerate(top_5):
    print(f"  {i+1}. {cancer.feature_names[idx]}: {importances[idx]:.4f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Model comparison
ax1 = axes[0]
models = list(base_results.keys()) + ['Voting', 'Stacking']
test_scores = [base_results[m]['test'] for m in base_results.keys()] + [voting_acc, stacking_acc]
colors = ['blue']*4 + ['green', 'red']
ax1.bar(range(len(models)), test_scores, color=colors, alpha=0.7)
ax1.set_xticks(range(len(models)))
ax1.set_xticklabels(models, rotation=45, ha='right')
ax1.set_ylabel('Test Accuracy')
ax1.set_title('Model Comparison')
ax1.grid(True, alpha=0.3, axis='y')

# Feature importance
ax2 = axes[1]
ax2.barh(range(5), importances[top_5][::-1])
ax2.set_yticks(range(5))
ax2.set_yticklabels([cancer.feature_names[i] for i in top_5[::-1]])
ax2.set_xlabel('Importance')
ax2.set_title('Top 5 Features')

plt.tight_layout()
plt.savefig('challenge_8_4_ensemble.png', dpi=150)
plt.close()

print("\n--- Summary ---")
print(f"Best base model: {max(base_results, key=lambda x: base_results[x]['test'])}")
print(f"Voting ensemble: {voting_acc:.4f}")
print(f"Stacking ensemble: {stacking_acc:.4f}")
print("\nEnsembles often outperform individual models by combining diverse predictions.")
print("\n" + "=" * 60)
print("CHALLENGE 8.4 COMPLETE")
