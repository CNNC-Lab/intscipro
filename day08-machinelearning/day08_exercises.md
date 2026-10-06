# Day 8 Exercises: Machine Learning I
_PhD Course in Integrative Neurosciences - Introduction to Scientific Programming_

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Conceptual Questions](#conceptual-questions)
3. [Classification Exercises](#classification-exercises)
4. [Regression Exercises](#regression-exercises)
5. [Model Evaluation Exercises](#model-evaluation-exercises)
6. [Unsupervised Learning Exercises](#unsupervised-learning-exercises)
7. [Pipeline & Best Practices Exercises](#pipeline--best-practices-exercises)
8. [Neuroscience Application Projects](#neuroscience-application-projects)
9. [Challenge Problems](#challenge-problems)
10. [Solutions Guidance](#solutions-guidance)

---

## Getting Started

### Prerequisites
- Complete Week 8 lectures and notebooks
- Python 3.10+ installed
- Required packages: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`

### Setup
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, r2_score

# Set random seed
np.random.seed(42)
```

### Instructions
- Work through exercises sequentially
- Start with conceptual questions to test understanding
- Code exercises build on previous knowledge
- Check solutions guidance at end before looking at answers
- Focus on understanding, not just getting correct answers

---

## Conceptual Questions

### Section 1: Machine Learning Fundamentals

**Q1.1**: Explain in your own words the difference between supervised and unsupervised learning. Provide two examples of each from your field of interest.

**Q1.2**: What is the difference between classification and regression? Give one example of each from your field of interest.

**Q1.3**: Why is it crucial to split data into training and test sets BEFORE any preprocessing? What can go wrong if you don't?

**Q1.4**: Explain the bias-variance tradeoff. Draw or describe what high bias looks like vs high variance.

**Q1.5**: True or False (explain your answer):
- a) A model with 100% training accuracy is always the best model
- b) Cross-validation is only necessary for small datasets
- c) Feature scaling is required for all machine learning algorithms
- d) Test set performance is always lower than training set performance

### Section 2: Classification

**Q2.1**: You're building a medical diagnostic system. Would you prioritize precision or recall? Why? How would your answer change for a spam filter?

**Q2.2**: You have a binary classification problem with 95% negative class and 5% positive class. Your model achieves 95% accuracy. Is this good? What metric should you use instead?

**Q2.3**: Explain when you would use each of these algorithms:
- a) Logistic Regression
- b) Random Forest
- c) SVM
- d) KNN

**Q2.4**: Your decision tree achieves 99% training accuracy but only 60% test accuracy. What's happening? List three solutions.

**Q2.5**: What does an AUC (Area Under ROC Curve) of 0.5 indicate? What about 0.95?

### Section 3: Regression

**Q3.1**: You fit a linear regression model and get R² = -0.2. What does this mean? Is this possible?

**Q3.2**: When would you use Ridge regression instead of Lasso? When would you prefer Lasso?

**Q3.3**: Your regression model has high training R² (0.95) but low test R² (0.40). List three techniques to address this.

**Q3.4**: Explain the difference between RMSE and MAE. When would you prefer each?

**Q3.5**: True or False (explain):
- a) R² can be negative
- b) Lower MSE always means better model
- c) Regularization always improves test performance
- d) Tree-based regression requires feature scaling

### Section 4: Unsupervised Learning

**Q4.1**: You apply K-Means with K=3 but there are actually 5 true clusters in your data. What will happen?

**Q4.2**: Explain the Elbow Method for choosing K in K-Means. What are its limitations?

**Q4.3**: When would you use DBSCAN instead of K-Means?

**Q4.4**: Explain the difference between PCA and t-SNE. Can you use t-SNE output as input to a classifier? Why or why not?

**Q4.5**: You perform PCA and the first 3 components explain 95% of variance. Should you keep just these 3 components? What factors should you consider?

### Section 5: Best Practices

**Q5.1**: What is data leakage? Provide three examples of how it can occur.

**Q5.2**: Why should you never fit a scaler on the entire dataset before splitting?

**Q5.3**: Explain the purpose of a Pipeline in scikit-learn. Why is it crucial for cross-validation?

**Q5.4**: You use Grid Search to tune hyperparameters. Should you report the CV score or test set score as your model's performance? Why?

**Q5.5**: What's wrong with this workflow?
```python
# 1. Scale all data
X_scaled = StandardScaler().fit_transform(X)
# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
# 3. Try model A on test set -> 85% accuracy
# 4. Try model B on test set -> 87% accuracy
# 5. Try model C on test set -> 86% accuracy
# 6. Choose model B because it has highest test accuracy
```

---

## Classification Exercises

### Exercise 3.1: Breast Cancer Classification

**Dataset**: Load breast cancer dataset from scikit-learn

**Tasks**:
1. Load the data and explore it
   - How many features?
   - How many samples?
   - Is the dataset balanced?

2. Split into train/test (80/20), use `stratify=y`

3. Train three classifiers:
   - Logistic Regression
   - Random Forest
   - SVM (remember to scale!)

4. For each model:
   - Calculate accuracy, precision, recall, F1-score
   - Create confusion matrix
   - Plot ROC curve

5. Compare models:
   - Which performs best overall?
   - Which has highest recall? Why might this matter for medical diagnosis?

6. Feature importance:
   - For Random Forest, plot top 10 most important features
   - Compare to Logistic Regression coefficients

**Starter Code**:
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score
)

# 1. Load data
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# Your code here...
```

### Exercise 3.2: Multi-Class Iris Classification

**Dataset**: Iris dataset (3 classes)

**Tasks**:
1. Load Iris dataset and explore
2. Create train/test split (70/30)
3. Train at least 3 different classifiers
4. Use 5-fold cross-validation on training set
5. Report mean ± std of CV scores
6. Evaluate best model on test set
7. Create multi-class confusion matrix
8. Calculate per-class precision, recall, F1

**Questions**:
- Which class is easiest to predict?
- Which classes are most confused with each other?
- How do CV scores compare to test performance?

### Exercise 3.3: Handling Imbalanced Data

**Task**: Create an imbalanced version of breast cancer data

**Steps**:
1. Load breast cancer data
2. Subsample to create 90% malignant, 10% benign
3. Train classifiers on imbalanced data
4. Compare accuracy vs F1-score
5. Try `class_weight='balanced'` parameter
6. Use stratified cross-validation

**Goal**: Demonstrate why accuracy is misleading for imbalanced data

**Starter Code**:
```python
from sklearn.utils import resample

# Create imbalanced dataset
X_majority = X[y==0]
X_minority = X[y==1]
y_majority = y[y==0]
y_minority = y[y==1]

# Downsample minority to 10%
n_minority_samples = int(len(X_majority) * 0.1)
X_minority_downsampled, y_minority_downsampled = resample(
    X_minority, y_minority,
    n_samples=n_minority_samples,
    random_state=42
)

# Combine
X_imbalanced = np.vstack((X_majority, X_minority_downsampled))
y_imbalanced = np.hstack((y_majority, y_minority_downsampled))

# Your analysis here...
```

---

## Regression Exercises

### Exercise 4.1: Diabetes Regression

**Dataset**: Diabetes dataset from scikit-learn

**Tasks**:
1. Load diabetes dataset and explore
2. Check for correlations between features
3. Split data (80/20)
4. Train these models:
   - Linear Regression
   - Ridge (try different alpha values: 0.1, 1.0, 10, 100)
   - Lasso (try different alpha values)
   - Random Forest

5. For each model:
   - Calculate R², RMSE, MAE
   - Plot predicted vs actual
   - Plot residuals

6. Regularization comparison:
   - Plot coefficients for Linear, Ridge, Lasso
   - Which features does Lasso zero out?
   - How does regularization strength affect this?

7. Best model:
   - Which performs best on test set?
   - Create learning curves
   - Is model overfitting or underfitting?

### Exercise 4.2: Feature Engineering

**Dataset**: California Housing or Diabetes

**Tasks**:
1. Create polynomial features (degree=2)
2. Train linear regression on:
   - Original features
   - Polynomial features

3. Compare performance:
   - Does polynomial help?
   - Is model overfitting with polynomial features?

4. Try regularization with polynomial features:
   - Ridge with polynomials
   - Lasso with polynomials

5. Which approach works best?

**Starter Code**:
```python
from sklearn.preprocessing import PolynomialFeatures

# Create polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

print(f"Original features: {X.shape[1]}")
print(f"Polynomial features: {X_poly.shape[1]}")

# Your code here...
```

### Exercise 4.3: Residual Analysis

**Task**: Perform thorough residual analysis for regression models

**Steps**:
1. Train a regression model on diabetes data
2. Calculate residuals (y_true - y_pred)
3. Create these plots:
   - Residuals vs Predicted values
   - Residuals vs Each feature
   - Histogram of residuals
   - Q-Q plot of residuals

4. Interpret:
   - Are residuals randomly scattered?
   - Is there a pattern suggesting non-linearity?
   - Are residuals normally distributed?
   - Are there outliers?

---

## Model Evaluation Exercises

### Exercise 5.1: Cross-Validation Deep Dive

**Dataset**: Breast cancer (classification) or Diabetes (regression)

**Tasks**:
1. Implement K-Fold cross-validation manually:
   ```python
   from sklearn.model_selection import KFold
   
   kf = KFold(n_splits=5, shuffle=True, random_state=42)
   scores = []
   
   for train_idx, test_idx in kf.split(X):
       # Your code here
       # Train model on train_idx
       # Evaluate on test_idx
       # Append score to scores list
   ```

2. Compare manual implementation to `cross_val_score`

3. Try different K values (3, 5, 10, 20):
   - How does K affect mean score?
   - How does K affect std of scores?
   - What's the computational cost?

4. For classification:
   - Compare regular K-Fold vs Stratified K-Fold
   - Check class distribution in each fold

### Exercise 5.2: Learning Curves

**Task**: Create and interpret learning curves

**Steps**:
1. Choose a dataset and model
2. Use `learning_curve` to get training and validation scores at different training sizes
3. Plot learning curves
4. Experiment with model complexity:
   - High complexity (deep tree, low regularization)
   - Medium complexity
   - Low complexity (shallow tree, high regularization)

5. For each complexity level:
   - Is model overfitting?
   - Is model underfitting?
   - Would more data help?

**Starter Code**:
```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5,
    scoring='accuracy'  # or 'r2' for regression
)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores.mean(axis=1), label='Training')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Validation')
plt.fill_between(train_sizes, 
                 train_scores.mean(axis=1) - train_scores.std(axis=1),
                 train_scores.mean(axis=1) + train_scores.std(axis=1),
                 alpha=0.2)
plt.fill_between(train_sizes,
                 val_scores.mean(axis=1) - val_scores.std(axis=1),
                 val_scores.mean(axis=1) + val_scores.std(axis=1),
                 alpha=0.2)
plt.xlabel('Training Set Size')
plt.ylabel('Score')
plt.legend()
plt.title('Learning Curves')
plt.show()
```

### Exercise 5.3: Validation Curves

**Task**: Tune a single hyperparameter using validation curves

**Example**: Tune `max_depth` for Decision Tree

**Steps**:
1. Define range of parameter values
2. For each value:
   - Perform cross-validation
   - Record training and validation scores
3. Plot validation curve
4. Identify optimal parameter value
5. Compare to Grid Search results

**Starter Code**:
```python
from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeClassifier

param_range = range(1, 21)  # max_depth from 1 to 20

train_scores, val_scores = validation_curve(
    DecisionTreeClassifier(random_state=42),
    X, y,
    param_name='max_depth',
    param_range=param_range,
    cv=5
)

# Plot and identify optimal max_depth
```

---

## Unsupervised Learning Exercises

### Exercise 6.1: Clustering Analysis

**Dataset**: Iris dataset (but pretend you don't know the true labels)

**Tasks**:
1. Apply K-Means with K=2, 3, 4, 5
2. For each K:
   - Calculate silhouette score
   - Calculate Davies-Bouldin index
   - Visualize clusters (use PCA for 2D projection)

3. Use Elbow Method:
   - Plot inertia vs K
   - Identify elbow point

4. Compare with true labels:
   - Use Adjusted Rand Index
   - Create confusion matrix (predicted clusters vs true labels)

5. Try Hierarchical Clustering:
   - Create dendrogram
   - Cut at different heights
   - Compare to K-Means

6. Try DBSCAN:
   - Experiment with eps and min_samples
   - How many clusters does it find?
   - How many noise points?

**Bonus**: Which algorithm recovered the true structure best?

### Exercise 6.2: Dimensionality Reduction Comparison

**Dataset**: Digits dataset (64 dimensions)

**Tasks**:
1. Apply PCA:
   - Keep 2 components for visualization
   - Plot explained variance ratio
   - How many components for 95% variance?

2. Create scree plot:
   - Plot variance explained vs component number
   - Identify elbow point

3. Visualize original digits and reconstructed:
   - Project to N components
   - Reconstruct back to 64 dimensions
   - Compare reconstruction error for different N

4. Apply t-SNE:
   - Reduce to 2 dimensions
   - Try different perplexity values (5, 30, 50)
   - Color by digit class

5. Compare PCA vs t-SNE:
   - Which separates digits better visually?
   - Which is faster?
   - Which can transform new data?

**Starter Code**:
```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

digits = load_digits()
X = digits.data
y = digits.target

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# t-SNE (apply PCA first for speed)
pca_pre = PCA(n_components=50)
X_pca_pre = pca_pre.fit_transform(X)
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X_pca_pre)

# Visualize...
```

### Exercise 6.3: Clustering on High-Dimensional Data

**Dataset**: Breast cancer dataset

**Challenge**: Clustering often fails in high dimensions (curse of dimensionality)

**Tasks**:
1. Apply K-Means directly to raw features:
   - Try K=2 (should find two cancer types)
   - Calculate silhouette score
   - Visualize (use PCA for 2D)

2. Apply dimensionality reduction first:
   - PCA to 10 components
   - Then K-Means with K=2
   - Compare silhouette score

3. Try different numbers of PCA components:
   - 5, 10, 20, 30 components
   - For each, apply K-Means
   - Plot silhouette score vs num components

4. Compare to true labels:
   - How well do clusters match true classes?
   - Try both with and without PCA

**Goal**: Understand when dimensionality reduction helps clustering

---

## Pipeline & Best Practices Exercises

### Exercise 7.1: Build a Complete Pipeline

**Dataset**: Any classification dataset

**Tasks**:
1. Create pipeline with:
   - StandardScaler
   - PCA (10 components)
   - RandomForestClassifier

2. Use cross-validation to evaluate

3. Compare to NOT using pipeline:
   - Show data leakage problem
   - Demonstrate overly optimistic results

4. Save and load pipeline:
   ```python
   import joblib
   joblib.dump(pipeline, 'my_model.pkl')
   loaded_pipeline = joblib.load('my_model.pkl')
   ```

5. Use pipeline for predictions on new data

**Starter Code**:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Cross-validation
scores = cross_val_score(pipeline, X, y, cv=5)
print(f"CV Scores: {scores.mean():.4f} ± {scores.std():.4f}")

# Your code here...
```

### Exercise 7.2: Hyperparameter Tuning

**Dataset**: Any dataset

**Tasks**:
1. Create pipeline with classifier
2. Define parameter grid:
   ```python
   param_grid = {
       'classifier__n_estimators': [50, 100, 200],
       'classifier__max_depth': [5, 10, None],
       'classifier__min_samples_split': [2, 5, 10]
   }
   ```

3. Perform Grid Search with 5-fold CV
4. Analyze results:
   - Best parameters
   - Best CV score
   - Time taken

5. Try Random Search:
   - Define parameter distributions
   - Try 20 random combinations
   - Compare to Grid Search (performance vs time)

6. Create validation curve for one parameter:
   - How does performance change?
   - Where is optimal value?

### Exercise 7.3: Detecting and Fixing Data Leakage

**Task**: Identify and fix data leakage in bad code

**Bad Code Example**:
```python
# WRONG WAY - Multiple leakage points!

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC

# 1. Scale all data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Select features on all data
selector = SelectKBest(k=10)
X_selected = selector.fit_transform(X_scaled, y)

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X_selected, y)

# 4. Cross-validation
model = SVC()
cv_scores = cross_val_score(model, X_train, y_train, cv=5)

# 5. Try different models and pick best based on test set
# ... repeated testing on same test set ...
```

**Your Tasks**:
1. Identify ALL sources of data leakage in above code
2. Explain why each is problematic
3. Rewrite using proper pipeline
4. Demonstrate the difference in performance estimates

---

## Challenge Problems

### Challenge 8.1: Imbalanced Medical Diagnosis

**Difficulty**: ⭐⭐⭐

**Scenario**: Diagnose rare disease (1% prevalence)

**Setup**:
```python
# Create heavily imbalanced dataset
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=10000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    weights=[0.99, 0.01],  # 99% negative, 1% positive
    random_state=42
)
```

**Challenge**:
1. Demonstrate why accuracy is useless
2. Train models with and without class_weight='balanced'
3. Use stratified sampling
4. Try SMOTE (bonus - requires `imbalanced-learn` package)
5. Find optimal threshold (don't use default 0.5):
   - Plot precision-recall for different thresholds
   - Choose threshold based on clinical requirements

6. Report:
   - What recall can you achieve while maintaining reasonable precision?
   - What's the tradeoff?

### Challenge 8.2: High-Dimensional Low-Sample

**Difficulty**: ⭐⭐⭐⭐

**Scenario**: Common in neuroscience - many features, few samples

**Setup**:
```python
# Create high-dimensional dataset
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=100,      # Only 100 samples!
    n_features=1000,    # But 1000 features!
    n_informative=50,
    n_redundant=50,
    random_state=42
)
```

**Challenge**:
1. Show that overfitting is severe with standard models
2. Apply dimensionality reduction:
   - PCA
   - Feature selection (SelectKBest)
3. Use regularization (Ridge, Lasso)
4. Use nested cross-validation:
   - Outer loop for performance estimation
   - Inner loop for hyperparameter tuning
5. Compare:
   - Model with all features
   - Model with PCA
   - Model with feature selection
   - Model with regularization

6. Report:
   - Which approach works best?
   - Why?

### Challenge 8.3: Multi-Class Cell Type Classification

**Difficulty**: ⭐⭐⭐

**Dataset**: Iris (3 cell types)

**Challenge**:
1. Build pipeline with:
   - Feature scaling
   - Dimensionality reduction
   - Classification

2. Use Grid Search to optimize:
   - Number of PCA components
   - Classifier hyperparameters

3. Create one-vs-rest binary classifiers:
   - Class 0 vs rest
   - Class 1 vs rest
   - Class 2 vs rest
   - Compare to multi-class approach

4. Error analysis:
   - Which classes are confused?
   - Why?
   - Can you fix it?

5. Feature analysis:
   - Which features distinguish each class?
   - Visualize decision boundaries

### Challenge 8.4: Ensemble Learning

**Difficulty**: ⭐⭐⭐⭐

**Challenge**: Build ensemble of different models

**Tasks**:
1. Train multiple base models:
   - Logistic Regression
   - Random Forest
   - SVM
   - KNN

2. Create voting ensemble:
   ```python
   from sklearn.ensemble import VotingClassifier
   
   voting_clf = VotingClassifier(
       estimators=[
           ('lr', LogisticRegression()),
           ('rf', RandomForestClassifier()),
           ('svm', SVC(probability=True))
       ],
       voting='soft'  # Use probability estimates
   )
   ```

3. Compare:
   - Individual model performance
   - Ensemble performance
   - When does ensemble help?

4. Feature importance from ensemble:
   - Average importance across models
   - Which features are consistently important?

5. Bonus - Stacking:
   - Use predictions from base models as features
   - Train meta-model on these predictions

---

## Solutions Guidance

### Checking Your Work

For each exercise, ask yourself:
1. **Correctness**: Does code run without errors?
2. **Completeness**: Did I answer all parts?
3. **Understanding**: Can I explain what each line does?
4. **Interpretation**: Do I understand the results?
5. **Best Practices**: Did I use pipelines, cross-validation, proper splitting?

### Common Mistakes to Avoid

**Data Leakage**:
- ❌ Fitting scaler on all data before split
- ✅ Fit only on training data, or use Pipeline

**Metric Selection**:
- ❌ Using accuracy for imbalanced data
- ✅ Use F1-score, ROC-AUC, or appropriate metric

**Test Set Abuse**:
- ❌ Trying many models and picking best based on test set
- ✅ Use cross-validation for model selection

**Feature Scaling**:
- ❌ Forgetting to scale for SVM, KNN
- ✅ Always scale or use Pipeline

**Overfitting**:
- ❌ Very complex model with small dataset
- ✅ Use regularization, cross-validation, simpler models

### Solution Outline Templates

**Classification Exercise Template**:
```python
# 1. Load and explore data
# - Check shape, features, class balance
# - Visualize distributions

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', YourClassifier())
])

# 4. Cross-validation
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"CV: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# 5. Train on full training set
pipeline.fit(X_train, y_train)

# 6. Evaluate on test set
y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.3f}")

# 7. Confusion matrix and analysis
cm = confusion_matrix(y_test, y_pred)
# ... plot and interpret
```

**Regression Exercise Template**:
```python
# 1. Load and explore data
# - Check correlations
# - Visualize distributions

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', YourRegressor())
])

# 4. Cross-validation
cv_scores = cross_val_score(
    pipeline, X_train, y_train, 
    cv=5, scoring='r2'
)

# 5. Train and evaluate
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# 6. Residual analysis
residuals = y_test - y_pred
# ... plot and interpret
```

### Self-Assessment Questions

After completing exercises, verify understanding:

**Classification**:
- [ ] Can you explain confusion matrix components?
- [ ] Do you know when to use each metric?
- [ ] Can you interpret ROC curve and AUC?
- [ ] Do you understand the bias-variance tradeoff?

**Regression**:
- [ ] Can you interpret R² value?
- [ ] Do you know difference between RMSE and MAE?
- [ ] Can you explain regularization?
- [ ] Do you understand residual plots?

**Evaluation**:
- [ ] Can you explain cross-validation?
- [ ] Do you know how to detect overfitting?
- [ ] Can you interpret learning curves?
- [ ] Do you understand train/validation/test splits?

**Best Practices**:
- [ ] Can you identify data leakage?
- [ ] Do you know why pipelines are important?
- [ ] Can you perform proper hyperparameter tuning?
- [ ] Do you avoid test set abuse?

### Getting Unstuck

If you're stuck on an exercise:

1. **Review Theory**: Check handout or lecture notes
2. **Check Documentation**: Read scikit-learn docs for the function
3. **Start Simple**: Use simpler model or smaller dataset first
4. **Error Messages**: Read carefully and search online
5. **Compare Notebook**: Check provided notebooks for similar examples
6. **Ask for Help**: Discuss with classmates or instructor

### Next Steps After Exercises

Once comfortable with Week 8 exercises:

1. **Apply to Your Data**: Try these techniques on your research data
2. **Kaggle Competitions**: Practice on real competitions
3. **Read Papers**: Find neuroscience papers using these methods
4. **Build Portfolio**: Create projects showcasing your skills

---

## Additional Practice Resources

### Datasets for Practice

**Classification**:
- Wine Quality: https://archive.ics.uci.edu/ml/datasets/wine+quality
- Heart Disease: https://archive.ics.uci.edu/ml/datasets/heart+disease
- Breast Cancer: Built into scikit-learn

**Regression**:
- Boston Housing: `from sklearn.datasets import load_boston`
- California Housing: `from sklearn.datasets import fetch_california_housing`
- Diabetes: Built into scikit-learn

**Clustering**:
- MNIST digits: `from sklearn.datasets import load_digits`
- Iris: Built into scikit-learn

### Online Practice Platforms

1. **Kaggle**: https://www.kaggle.com/learn/intro-to-machine-learning
2. **DataCamp**: Machine Learning with scikit-learn track
3. **Coursera**: Andrew Ng's Machine Learning
4. **Google Colab**: Free Jupyter notebooks in cloud

### Books for Exercises

1. **"Python Machine Learning"** by Sebastian Raschka
   - Many practical exercises
   - Scikit-learn focused

2. **"Hands-On Machine Learning"** by Aurélien Géron
   - Extensive exercises at end of chapters
   - Covers scikit-learn thoroughly

3. **"Introduction to Statistical Learning"** (with Python)
   - Theory + practice
   - Excellent exercises

---
**Remember: The goal is understanding, not just completing exercises. Take your time, experiment, and ask questions!**

*Exercises prepared for CNC-UC Introduction to Scientific Programming*  
*University of Coimbra*