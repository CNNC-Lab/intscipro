"""
Exercise 7.1: Build a Complete Pipeline
PhD Course in Integrative Neurosciences - Introduction to Scientific Programming

Solution for building ML pipelines and demonstrating data leakage.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

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

# Split data
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
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

print("Pipeline steps:")
for name, step in pipeline.steps:
    print(f"  - {name}: {step.__class__.__name__}")

# =============================================================================
# 3. Cross-Validation with Pipeline
# =============================================================================
print("\n" + "=" * 60)
print("3. CROSS-VALIDATION WITH PIPELINE")
print("=" * 60)

cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='accuracy')
print(f"\n5-Fold CV Scores: {cv_scores}")
print(f"Mean CV Score: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

# =============================================================================
# 4. Demonstrate Data Leakage Problem
# =============================================================================
print("\n" + "=" * 60)
print("4. DEMONSTRATING DATA LEAKAGE PROBLEM")
print("=" * 60)

print("\n--- WRONG WAY (Data Leakage) ---")

# WRONG: Fit scaler on ALL data before splitting
scaler_wrong = StandardScaler()
X_scaled_wrong = scaler_wrong.fit_transform(X)  # Leakage!

# WRONG: Fit PCA on ALL data
pca_wrong = PCA(n_components=10)
X_pca_wrong = pca_wrong.fit_transform(X_scaled_wrong)  # Leakage!

# Now split
X_train_wrong, X_test_wrong, y_train_wrong, y_test_wrong = train_test_split(
    X_pca_wrong, y, test_size=0.2, random_state=42, stratify=y
)

# Train classifier
clf_wrong = RandomForestClassifier(n_estimators=100, random_state=42)
clf_wrong.fit(X_train_wrong, y_train_wrong)

# Evaluate
accuracy_wrong = accuracy_score(y_test_wrong, clf_wrong.predict(X_test_wrong))
print(f"Test Accuracy (with leakage): {accuracy_wrong:.4f}")

# CV on already-transformed data (also wrong!)
cv_scores_wrong = cross_val_score(clf_wrong, X_pca_wrong, y, cv=5, scoring='accuracy')
print(f"CV Score (with leakage): {cv_scores_wrong.mean():.4f} +/- {cv_scores_wrong.std():.4f}")

print("\n--- CORRECT WAY (Using Pipeline) ---")

# Train pipeline on training data only
pipeline.fit(X_train, y_train)

# Evaluate on test set
y_pred = pipeline.predict(X_test)
accuracy_correct = accuracy_score(y_test, y_pred)
print(f"Test Accuracy (no leakage): {accuracy_correct:.4f}")
print(f"CV Score (no leakage): {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

print("\n--- COMPARISON ---")
print(f"Accuracy with leakage:    {accuracy_wrong:.4f}")
print(f"Accuracy without leakage: {accuracy_correct:.4f}")

if accuracy_wrong > accuracy_correct:
    print("\nWARNING: Leakage gives OVERLY OPTIMISTIC results!")
    print("The model appears better than it actually is.")
else:
    print("\nIn this case, the difference is small, but leakage is still wrong!")
    print("It can lead to models that fail in production.")

# =============================================================================
# 5. Save and Load Pipeline
# =============================================================================
print("\n" + "=" * 60)
print("5. SAVE AND LOAD PIPELINE")
print("=" * 60)

# Save pipeline
save_path = 'my_pipeline.pkl'
joblib.dump(pipeline, save_path)
print(f"Pipeline saved to: {save_path}")

# Load pipeline
loaded_pipeline = joblib.load(save_path)
print("Pipeline loaded successfully!")

# Verify loaded pipeline works
y_pred_loaded = loaded_pipeline.predict(X_test)
accuracy_loaded = accuracy_score(y_test, y_pred_loaded)
print(f"Loaded pipeline accuracy: {accuracy_loaded:.4f}")
print(f"Original pipeline accuracy: {accuracy_correct:.4f}")
print(f"Match: {np.allclose(y_pred, y_pred_loaded)}")

# Clean up
os.remove(save_path)
print(f"Cleaned up: removed {save_path}")

# =============================================================================
# 6. Use Pipeline for New Data Predictions
# =============================================================================
print("\n" + "=" * 60)
print("6. PREDICTIONS ON NEW DATA")
print("=" * 60)

# Simulate new data (using test set as example)
new_samples = X_test[:5]

print("\nPredicting on 5 new samples:")
predictions = pipeline.predict(new_samples)
probabilities = pipeline.predict_proba(new_samples)

for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
    class_name = cancer.target_names[pred]
    confidence = prob[pred]
    print(f"  Sample {i+1}: {class_name} (confidence: {confidence:.2%})")

# =============================================================================
# 7. Accessing Pipeline Components
# =============================================================================
print("\n" + "=" * 60)
print("7. ACCESSING PIPELINE COMPONENTS")
print("=" * 60)

# Access individual steps
scaler = pipeline.named_steps['scaler']
pca = pipeline.named_steps['pca']
classifier = pipeline.named_steps['classifier']

print(f"\nScaler mean (first 5 features): {scaler.mean_[:5]}")
print(f"PCA explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance explained: {pca.explained_variance_ratio_.sum():.2%}")
print(f"Random Forest n_estimators: {classifier.n_estimators}")

# Feature importance from Random Forest
feature_importance = classifier.feature_importances_
print(f"\nTop 5 important PCA components:")
top_5 = np.argsort(feature_importance)[::-1][:5]
for i, idx in enumerate(top_5):
    print(f"  PC{idx+1}: {feature_importance[idx]:.4f}")

# =============================================================================
# 8. Summary
# =============================================================================
print("\n" + "=" * 60)
print("8. SUMMARY")
print("=" * 60)

print("""
WHY USE PIPELINES?
------------------

1. PREVENTS DATA LEAKAGE:
   - All preprocessing is fit only on training data
   - Test data is transformed using training parameters
   - Cross-validation handles this automatically

2. CLEANER CODE:
   - All steps in one object
   - Easy to save and load
   - Reproducible predictions

3. PROPER CROSS-VALIDATION:
   - Each fold fits preprocessing from scratch
   - No information leaks between folds
   - Gives realistic performance estimates

4. PRODUCTION READY:
   - Single object to deploy
   - Handles all preprocessing automatically
   - Consistent predictions on new data

DATA LEAKAGE SOURCES:
---------------------
1. Fitting scaler on all data before split
2. Fitting PCA/feature selection on all data
3. Using future information (in time series)
4. Target leakage (features derived from target)

PIPELINE BEST PRACTICES:
------------------------
1. Put ALL preprocessing in the pipeline
2. Use cross_val_score with the pipeline
3. Only fit pipeline on training data
4. Save entire pipeline for deployment
""")

print("=" * 60)
print("EXERCISE 7.1 COMPLETE")
print("=" * 60)
