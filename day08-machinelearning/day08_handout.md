# Day 8 Handout: Machine Learning I
*PhD Course in Integrative Neurosciences - Introduction to Scientific Programming*

---

## Table of Contents

1. [Introduction to Machine Learning](#1-introduction-to-machine-learning)
2. [ML vs Traditional Statistics](#2-ml-vs-traditional-statistics)
3. [Supervised Learning: Classification](#3-supervised-learning-classification)
4. [Supervised Learning: Regression](#4-supervised-learning-regression)
5. [Model Evaluation](#5-model-evaluation)
6. [Unsupervised Learning](#6-unsupervised-learning)
7. [Pipelines and Best Practices](#7-pipelines-and-best-practices)
8. [Practical Guidelines](#8-practical-guidelines)
9. [Neuroscience Applications](#9-neuroscience-applications)
10. [Further Resources](#10-further-resources)

---

## 1. Introduction to Machine Learning

### 1.1 What is Machine Learning?

**Machine Learning (ML)** is a field of artificial intelligence that enables computers to learn patterns from data without being explicitly programmed for specific tasks.

**Core Idea**: Instead of writing rules manually, we let the algorithm discover patterns from examples.

**Traditional Programming vs Machine Learning**:

```
Traditional Programming:
Data + Program → Output

Machine Learning:
Data + Output → Program (Model)
```

### 1.2 Types of Machine Learning

#### **Supervised Learning**
- Learn from labeled data (input-output pairs)
- Goal: Predict output for new inputs
- **Classification**: Predict discrete categories (e.g., disease vs healthy)
- **Regression**: Predict continuous values (e.g., disease progression score)

#### **Unsupervised Learning**
- Learn from unlabeled data
- Goal: Discover hidden patterns or structure
- **Clustering**: Group similar data points
- **Dimensionality Reduction**: Reduce feature count while preserving information

#### **Reinforcement Learning** (not covered in this course)
- Learn through trial and error
- Goal: Maximize rewards over time
- Applications: Robotics, game playing

### 1.3 Key Concepts

#### **Features (X)**
Input variables or attributes used for prediction.
- Example: In brain imaging, features might be voxel intensities, brain region volumes, connectivity measures

#### **Target (y)**
Output variable we want to predict.
- Classification: Categories (e.g., patient vs control)
- Regression: Continuous values (e.g., cognitive score)

#### **Training vs Testing**
- **Training Set**: Data used to learn patterns (~70-80% of data)
- **Test Set**: Data used to evaluate performance (~20-30% of data)
- **Critical**: Never train on test data!

#### **Overfitting vs Underfitting**
- **Overfitting**: Model learns training data too well, including noise; poor generalization
- **Underfitting**: Model is too simple to capture patterns; poor performance on all data
- **Goal**: Find the sweet spot - good generalization to new data

---

## 2. ML vs Traditional Statistics

### 2.1 Key Differences

| Aspect | Traditional Statistics | Machine Learning |
|--------|------------------------|------------------|
| **Goal** | Inference & interpretation | Prediction & pattern discovery |
| **Focus** | Parameter estimation, p-values | Predictive accuracy |
| **Assumptions** | Explicit (normality, linearity) | Minimal (data-driven) |
| **Model Complexity** | Simple, interpretable | Can be complex (black boxes) |
| **Sample Size** | Works with small samples | Often needs large samples |
| **Features** | Few, carefully selected | Many, automatically selected |

### 2.2 When to Use Which?

**Use Traditional Statistics when**:
- Establishing causal relationships
- Need interpretability for scientific publication
- Small sample sizes (<100 samples)
- Testing specific hypotheses
- Need confidence intervals and p-values

**Use Machine Learning when**:
- Primary goal is accurate prediction
- Many potential features (high-dimensional)
- Complex, non-linear relationships
- Large datasets available
- Pattern discovery is the goal

### 2.3 The Bias-Variance Tradeoff

A fundamental concept in ML that doesn't exist in traditional statistics.

**Bias**: Error from overly simplistic assumptions
- High bias → Underfitting
- Example: Using linear model for non-linear relationship

**Variance**: Error from sensitivity to training data fluctuations
- High variance → Overfitting
- Example: Overly complex model fitting noise

**Total Error** = Bias² + Variance + Irreducible Error

**Goal**: Balance bias and variance to minimize total error

**Visual Understanding**:
- High Bias, Low Variance: Consistently wrong (underfitting)
- Low Bias, High Variance: Inconsistently correct (overfitting)
- Low Bias, Low Variance: Consistently correct (ideal)

---

## 3. Supervised Learning: Classification

### 3.1 What is Classification?

**Classification** assigns data points to predefined categories.

**Binary Classification**: Two classes (e.g., disease vs healthy)
**Multi-class Classification**: More than two classes (e.g., cell types A, B, C)

### 3.2 Classification Algorithms

#### **3.2.1 Logistic Regression**

Despite its name, logistic regression is a **classification** algorithm.

**How it works**:
- Uses sigmoid function to map predictions to probabilities (0 to 1)
- Formula: P(y=1|X) = 1 / (1 + e^(-(β₀ + β₁x₁ + β₂x₂ + ...)))
- Decision boundary is linear

**Advantages**:
- Fast and interpretable
- Provides probability estimates
- Works well for linearly separable data
- Good baseline model

**Limitations**:
- Assumes linear decision boundary
- May underperform with complex patterns

**When to use**:
- Quick baseline
- Need probability estimates
- Interpretability important
- Data is roughly linearly separable

**Scikit-learn Example**:
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)  # Get probabilities
```

#### **3.2.2 Support Vector Machines (SVM)**

**How it works**:
- Finds optimal hyperplane that maximizes margin between classes
- Uses support vectors (data points closest to boundary)
- Can use kernels for non-linear boundaries

**Key Parameters**:
- `C`: Regularization (smaller = more regularization)
- `kernel`: 'linear', 'rbf', 'poly', 'sigmoid'
- `gamma`: Kernel coefficient (higher = more complex boundary)

**Advantages**:
- Effective in high-dimensional spaces
- Memory efficient (only uses support vectors)
- Versatile with different kernels

**Limitations**:
- Slow on large datasets
- Requires feature scaling
- Less intuitive than other methods

**When to use**:
- High-dimensional data
- Clear margin of separation exists
- Dataset not too large (< 10,000 samples)

**Scikit-learn Example**:
```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# SVM requires scaling!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel='rbf', C=1.0, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
```

#### **3.2.3 Decision Trees**

**How it works**:
- Learns a series of if-then-else rules
- Recursively splits data based on features
- Each split maximizes information gain or decreases impurity

**Key Parameters**:
- `max_depth`: Maximum tree depth (limits complexity)
- `min_samples_split`: Minimum samples to split a node
- `min_samples_leaf`: Minimum samples in leaf node

**Advantages**:
- Highly interpretable (can visualize tree)
- No feature scaling needed
- Handles non-linear relationships
- Works with mixed data types

**Limitations**:
- Prone to overfitting without pruning
- Small data changes can alter tree significantly
- Biased toward dominant classes

**When to use**:
- Interpretability crucial
- No time for feature scaling
- Need feature importance estimates

**Scikit-learn Example**:
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Visualize tree
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=feature_names, class_names=class_names, filled=True)
plt.show()

# Feature importance
importances = model.feature_importances_
```

#### **3.2.4 Random Forests**

**How it works**:
- Ensemble of many decision trees
- Each tree trained on random subset of data (bootstrap sample)
- Each split considers random subset of features
- Final prediction by majority vote (classification) or average (regression)

**Key Parameters**:
- `n_estimators`: Number of trees (more is better, but slower)
- `max_depth`: Maximum depth of each tree
- `max_features`: Number of features to consider for each split

**Advantages**:
- Robust to overfitting (compared to single trees)
- Works well out-of-the-box with default parameters
- Provides feature importance
- Handles non-linear relationships

**Limitations**:
- Less interpretable than single trees
- Slower to train and predict
- Can be memory-intensive

**When to use**:
- Want robust, accurate predictions
- Have enough data for ensemble methods
- Feature importance needed
- Don't need to interpret individual decisions

**Scikit-learn Example**:
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,  # Number of trees
    max_depth=10,
    random_state=42,
    n_jobs=-1  # Use all CPU cores
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Feature importance from ensemble
importances = model.feature_importances_
```

#### **3.2.5 K-Nearest Neighbors (KNN)**

**How it works**:
- Classifies based on majority class of K nearest neighbors
- "Lazy learning" - no explicit training phase
- Distance metric (usually Euclidean) determines neighbors

**Key Parameters**:
- `n_neighbors`: Number of neighbors to consider (K)
- `metric`: Distance metric ('euclidean', 'manhattan', etc.)
- `weights`: 'uniform' or 'distance' (closer neighbors have more influence)

**Advantages**:
- Simple and intuitive
- No training phase (instant)
- Naturally handles multi-class problems

**Limitations**:
- Slow prediction on large datasets
- Sensitive to irrelevant features
- Requires feature scaling
- Struggles in high dimensions (curse of dimensionality)

**When to use**:
- Small to medium datasets
- Need simple, interpretable method
- Irregular decision boundaries expected

**Scikit-learn Example**:
```python
from sklearn.neighbors import KNeighborsClassifier

# KNN requires scaling!
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
```

### 3.3 Classification Metrics

#### **Confusion Matrix**

Foundation of classification metrics:

```
                Predicted
              Negative  Positive
Actual Negative    TN       FP
       Positive    FN       TP
```

- **True Positive (TP)**: Correctly predicted positive
- **True Negative (TN)**: Correctly predicted negative
- **False Positive (FP)**: Incorrectly predicted positive (Type I error)
- **False Negative (FN)**: Incorrectly predicted negative (Type II error)

#### **Accuracy**

**Formula**: (TP + TN) / (TP + TN + FP + FN)

**Interpretation**: Proportion of correct predictions

**Caution**: Misleading with imbalanced classes!
- Example: 95% negative class → always predict negative → 95% accuracy but useless model

**When to use**: Balanced classes only

#### **Precision**

**Formula**: TP / (TP + FP)

**Interpretation**: Of predicted positives, how many are truly positive?

**High precision needed when**: False positives are costly
- Example: Spam filter (don't want to mark legitimate emails as spam)

#### **Recall (Sensitivity)**

**Formula**: TP / (TP + FN)

**Interpretation**: Of actual positives, how many did we detect?

**High recall needed when**: False negatives are costly
- Example: Disease screening (don't want to miss sick patients)

#### **F1-Score**

**Formula**: 2 × (Precision × Recall) / (Precision + Recall)

**Interpretation**: Harmonic mean of precision and recall

**When to use**: Need balance between precision and recall, or classes are imbalanced

#### **ROC Curve and AUC**

**ROC (Receiver Operating Characteristic)** curve:
- X-axis: False Positive Rate (FPR) = FP / (FP + TN)
- Y-axis: True Positive Rate (TPR) = Recall = TP / (TP + FN)
- Shows tradeoff between sensitivity and specificity at various thresholds

**AUC (Area Under Curve)**:
- Range: 0 to 1
- AUC = 0.5: Random classifier
- AUC = 1.0: Perfect classifier
- AUC > 0.9: Excellent
- AUC 0.8-0.9: Good
- AUC 0.7-0.8: Fair

**Scikit-learn Example**:
```python
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score, roc_curve, roc_auc_score,
    classification_report
)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Complete report
print(classification_report(y_test, y_pred))

# ROC curve (need probabilities)
y_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)
```

---

## 4. Supervised Learning: Regression

### 4.1 What is Regression?

**Regression** predicts continuous numerical values.

**Examples**:
- Predicting cognitive test scores
- Estimating disease progression rates
- Forecasting neural activity amplitude

### 4.2 Regression Algorithms

#### **4.2.1 Linear Regression**

**How it works**:
- Fits a straight line (or hyperplane) through data
- Minimizes sum of squared residuals (OLS - Ordinary Least Squares)
- Formula: ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

**Assumptions**:
1. **Linearity**: Relationship between X and y is linear
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of residuals
4. **Normality**: Residuals are normally distributed (for inference)

**Advantages**:
- Fast and simple
- Highly interpretable (coefficients show feature importance)
- Works well when assumptions met

**Limitations**:
- Assumes linear relationship
- Sensitive to outliers
- Can overfit with many features

**Scikit-learn Example**:
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Examine coefficients
coefficients = model.coef_
intercept = model.intercept_
```

#### **4.2.2 Ridge Regression (L2 Regularization)**

**How it works**:
- Linear regression + penalty on coefficient magnitude
- Penalty term: λ Σ βᵢ²
- Shrinks coefficients toward zero (but not exactly zero)

**Key Parameter**:
- `alpha`: Regularization strength (higher = more shrinkage)

**Advantages**:
- Prevents overfitting
- Handles multicollinearity well
- Keeps all features (no feature selection)

**When to use**:
- Many correlated features
- Overfitting with standard linear regression
- Want to keep all features

**Scikit-learn Example**:
```python
from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)  # Try different alphas
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

#### **4.2.3 Lasso Regression (L1 Regularization)**

**How it works**:
- Linear regression + penalty on absolute coefficient values
- Penalty term: λ Σ |βᵢ|
- Can set coefficients exactly to zero (automatic feature selection)

**Key Parameter**:
- `alpha`: Regularization strength

**Advantages**:
- Automatic feature selection
- Interpretable (sparse solutions)
- Handles multicollinearity

**When to use**:
- Suspect many features are irrelevant
- Want automatic feature selection
- Need sparse solution

**Scikit-learn Example**:
```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=0.5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Count zero coefficients
n_zero = np.sum(model.coef_ == 0)
print(f"Features eliminated: {n_zero}")
```

#### **4.2.4 ElasticNet (L1 + L2)**

**How it works**:
- Combines Ridge and Lasso penalties
- Penalty: λ₁ Σ |βᵢ| + λ₂ Σ βᵢ²

**Key Parameters**:
- `alpha`: Overall regularization strength
- `l1_ratio`: Balance between L1 and L2 (0=Ridge, 1=Lasso)

**Advantages**:
- Best of both Ridge and Lasso
- More stable than Lasso with correlated features

**When to use**:
- Correlated features + want feature selection
- Lasso is too aggressive

**Scikit-learn Example**:
```python
from sklearn.linear_model import ElasticNet

model = ElasticNet(alpha=0.5, l1_ratio=0.5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

#### **4.2.5 Support Vector Regression (SVR)**

**How it works**:
- Extension of SVM for regression
- Fits hyperplane within epsilon-tube
- Points outside tube contribute to loss

**Key Parameters**:
- `kernel`: 'linear', 'rbf', 'poly'
- `C`: Regularization
- `epsilon`: Width of epsilon-tube

**Advantages**:
- Effective in high dimensions
- Robust to outliers (in tube)
- Can capture non-linear relationships

**Limitations**:
- Requires feature scaling
- Sensitive to parameter choices
- Computationally expensive

**Scikit-learn Example**:
```python
from sklearn.svm import SVR

# SVR requires scaling!
model = SVR(kernel='rbf', C=1.0, epsilon=0.1)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
```

#### **4.2.6 Tree-Based Regression**

**Decision Tree Regressor**:
- Same concept as classification trees
- Predicts mean value of samples in leaf node

**Random Forest Regressor**:
- Ensemble of regression trees
- Predictions averaged across trees

**Advantages** (both):
- No feature scaling needed
- Handles non-linear relationships
- Provides feature importance

**Scikit-learn Example**:
```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Decision tree
tree_model = DecisionTreeRegressor(max_depth=5, random_state=42)
tree_model.fit(X_train, y_train)

# Random forest
rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)
```

### 4.3 Regression Metrics

#### **R² Score (Coefficient of Determination)**

**Formula**: R² = 1 - (SS_res / SS_tot)
- SS_res: Sum of squared residuals
- SS_tot: Total sum of squares

**Interpretation**:
- Proportion of variance in y explained by model
- Range: -∞ to 1
- R² = 1: Perfect predictions
- R² = 0: Model no better than predicting mean
- R² < 0: Model worse than predicting mean

**When to use**: Standard metric for regression

#### **Mean Squared Error (MSE)**

**Formula**: MSE = (1/n) Σ (yᵢ - ŷᵢ)²

**Interpretation**:
- Average squared difference between predictions and actual
- Penalizes large errors more (due to squaring)

**Units**: Squared units of target variable

#### **Root Mean Squared Error (RMSE)**

**Formula**: RMSE = √MSE

**Interpretation**:
- Average prediction error
- Same units as target variable
- More interpretable than MSE

**When to use**: When you want error in original units

#### **Mean Absolute Error (MAE)**

**Formula**: MAE = (1/n) Σ |yᵢ - ŷᵢ|

**Interpretation**:
- Average absolute difference
- More robust to outliers than RMSE

**When to use**: When outliers shouldn't dominate error metric

**Scikit-learn Example**:
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
```

---

## 5. Model Evaluation

### 5.1 Train/Test Split

**Problem**: How to evaluate model performance?

**Solution**: Reserve portion of data for testing.

**Best Practices**:
- Use 70-80% for training, 20-30% for testing
- Use `random_state` for reproducibility
- Use `stratify` parameter for classification (maintains class balance)

**Scikit-learn Example**:
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing
    random_state=42,    # Reproducibility
    stratify=y          # For classification
)
```

### 5.2 Cross-Validation

**Problem**: Single train/test split gives variable results depending on which data ends up where.

**Solution**: Cross-Validation - Split data multiple times and average results.

#### **K-Fold Cross-Validation**

**How it works**:
1. Split data into K equal-sized folds
2. For each fold:
   - Train on K-1 folds
   - Test on remaining fold
3. Average performance across K folds

**Typical K values**: 5 or 10

**Advantages**:
- More reliable performance estimates
- All data used for both training and testing
- Reduces variance in estimates

**Scikit-learn Example**:
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    model, X, y,
    cv=5,              # 5-fold CV
    scoring='accuracy' # Metric
)

print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.4f}")
print(f"Std: {scores.std():.4f}")
```

#### **Stratified K-Fold**

For classification with imbalanced classes - maintains class proportions in each fold.

**Scikit-learn Example**:
```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

stratified_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=stratified_cv)
```

### 5.3 Learning Curves

**Purpose**: Diagnose overfitting vs underfitting

**How to interpret**:
- **Overfitting**: Large gap between training and validation curves
- **Underfitting**: Both curves plateau at low performance
- **Good fit**: Curves converge to high performance
- **More data helpful**: Curves still improving (not plateaued)

**Scikit-learn Example**:
```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5
)

# Plot
plt.plot(train_sizes, train_scores.mean(axis=1), label='Training')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Validation')
plt.xlabel('Training Set Size')
plt.ylabel('Score')
plt.legend()
```

---

## 6. Unsupervised Learning

### 6.1 Clustering

**Goal**: Group similar data points without predefined labels.

#### **6.1.1 K-Means Clustering**

**How it works**:
1. Randomly initialize K cluster centers
2. Assign each point to nearest center
3. Update centers as mean of assigned points
4. Repeat until convergence

**Key Parameter**:
- `n_clusters`: Number of clusters (must specify)

**Advantages**:
- Fast and scalable
- Simple to understand

**Limitations**:
- Must specify K in advance
- Assumes spherical clusters
- Sensitive to initialization
- Sensitive to outliers

**Choosing K (Elbow Method)**:
1. Try different K values
2. Plot inertia (within-cluster sum of squares) vs K
3. Look for "elbow" where improvement slows

**Scikit-learn Example**:
```python
from sklearn.cluster import KMeans

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)

# Get cluster centers
centers = kmeans.cluster_centers_

# Evaluate
inertia = kmeans.inertia_
```

#### **6.1.2 Hierarchical Clustering**

**How it works (Agglomerative)**:
1. Start with each point as own cluster
2. Repeatedly merge closest clusters
3. Creates dendrogram (tree of merges)

**Key Parameters**:
- `n_clusters`: Number of clusters (can be determined from dendrogram)
- `linkage`: How to measure cluster distance
  - 'ward': Minimizes within-cluster variance (most common)
  - 'complete': Maximum distance between clusters
  - 'average': Average distance between clusters

**Advantages**:
- Don't need to specify K in advance
- Creates hierarchy of clusters
- Deterministic (no random initialization)

**Limitations**:
- Computationally expensive (O(n²) or O(n³))
- Not scalable to large datasets

**Scikit-learn Example**:
```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Apply hierarchical clustering
hier = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = hier.fit_predict(X)

# Create dendrogram
linkage_matrix = linkage(X, method='ward')
dendrogram(linkage_matrix)
plt.show()
```

#### **6.1.3 DBSCAN**

**How it works**:
- Density-based: finds clusters of arbitrary shape
- Core points: ≥ min_samples neighbors within eps
- Border points: Within eps of core point
- Noise: Neither core nor border (labeled -1)

**Key Parameters**:
- `eps`: Maximum distance between neighbors
- `min_samples`: Minimum neighbors to be core point

**Advantages**:
- Finds arbitrary-shaped clusters
- Identifies outliers
- Don't need to specify number of clusters

**Limitations**:
- Sensitive to parameters
- Struggles with varying density
- Not suitable for high dimensions

**Scikit-learn Example**:
```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)

# Count clusters (excluding noise)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
```

#### **6.1.4 Clustering Evaluation**

**Internal Metrics** (no ground truth needed):

**Silhouette Score**:
- Measures how similar points are to own cluster vs others
- Range: -1 to 1 (higher is better)
- > 0.5: Good clustering

**Davies-Bouldin Index**:
- Average similarity between clusters
- Lower is better

**External Metrics** (require ground truth):

**Adjusted Rand Index (ARI)**:
- Similarity between predicted and true clusters
- Range: 0 to 1 (higher is better)
- Adjusted for chance

**Normalized Mutual Information (NMI)**:
- Shared information between clusterings
- Range: 0 to 1 (higher is better)

**Scikit-learn Example**:
```python
from sklearn.metrics import (
    silhouette_score, davies_bouldin_score,
    adjusted_rand_score, normalized_mutual_info_score
)

# Internal metrics
silhouette = silhouette_score(X, labels)
davies_bouldin = davies_bouldin_score(X, labels)

# External metrics (if ground truth available)
ari = adjusted_rand_score(y_true, labels)
nmi = normalized_mutual_info_score(y_true, labels)
```

### 6.2 Dimensionality Reduction

**Goal**: Reduce number of features while preserving information.

#### **6.2.1 Principal Component Analysis (PCA)**

**How it works**:
- Finds orthogonal directions of maximum variance
- Projects data onto these directions (principal components)
- First PC explains most variance, second PC second most, etc.

**Key Parameter**:
- `n_components`: Number of components to keep
  - Can specify integer (e.g., 2 for visualization)
  - Can specify float (e.g., 0.95 for 95% variance)

**Advantages**:
- Linear and fast
- Interpretable (variance explained)
- Works for downstream algorithms
- Reversible (can reconstruct data)

**Limitations**:
- Only captures linear relationships
- Components may not be interpretable
- Sensitive to scaling

**Use Cases**:
- Visualization (2D or 3D)
- Noise reduction
- Feature extraction
- Speeding up algorithms

**Scikit-learn Example**:
```python
from sklearn.decomposition import PCA

# Reduce to 2 components
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)

# Check variance explained
explained_var = pca.explained_variance_ratio_
print(f"Variance explained: {explained_var.sum():.2%}")

# Or specify variance to retain
pca_95 = PCA(n_components=0.95)  # Keep 95% variance
X_pca_95 = pca_95.fit_transform(X)
print(f"Components needed: {pca_95.n_components_}")
```

#### **6.2.2 t-SNE**

**How it works**:
- Non-linear dimensionality reduction
- Preserves local structure (neighbor relationships)
- Uses probabilities to model similarities

**Key Parameters**:
- `n_components`: Usually 2 or 3 (for visualization)
- `perplexity`: Balance between local and global structure (5-50)
- `random_state`: For reproducibility

**Advantages**:
- Captures non-linear relationships
- Excellent for visualization
- Reveals hidden structure

**Limitations**:
- Slow (especially for large datasets)
- Non-deterministic (different runs give different results)
- **Visualization only** - don't use for preprocessing
- Distances between clusters are not meaningful
- Cannot transform new data (no inverse)

**Best Practices**:
1. Apply PCA first (to ~50 dimensions) for speed
2. Try different perplexity values
3. Don't overinterpret cluster distances

**Scikit-learn Example**:
```python
from sklearn.manifold import TSNE

# Usually apply PCA first for large datasets
pca_pre = PCA(n_components=50, random_state=42)
X_pca = pca_pre.fit_transform(X)

# Then t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X_pca)

# Visualize
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis')
plt.title('t-SNE Visualization')
```

---

## 7. Pipelines and Best Practices

### 7.1 Scikit-learn Pipelines

**Why use Pipelines?**

1. **Prevents data leakage**: Preprocessing applied correctly in cross-validation
2. **Cleaner code**: One object instead of multiple steps
3. **Easier deployment**: Save entire workflow as one object
4. **Cross-validation safe**: Each fold preprocessed independently

**Pipeline Structure**:
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('step1_name', transformer1),
    ('step2_name', transformer2),
    ('model_name', estimator)
])
```

**Example with Scaling and Classification**:
```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Predict (automatically scales!)
y_pred = pipeline.predict(X_test)
```

**Complex Pipeline Example**:
```python
from sklearn.decomposition import PCA

pipeline = Pipeline([
    ('scaler', StandardScaler()),          # Step 1: Scale
    ('pca', PCA(n_components=10)),         # Step 2: Reduce dimensions
    ('classifier', RandomForestClassifier()) # Step 3: Classify
])

pipeline.fit(X_train, y_train)
```

**Accessing Pipeline Components**:
```python
# Get specific component
pca_component = pipeline.named_steps['pca']

# Check PCA variance
variance_explained = pca_component.explained_variance_ratio_.sum()
```

### 7.2 Hyperparameter Tuning

**What are Hyperparameters?**
- Parameters NOT learned from data
- Set before training
- Examples: tree depth, learning rate, number of neighbors

#### **7.2.1 Grid Search**

**How it works**:
- Try all combinations of specified parameter values
- Evaluate each with cross-validation
- Select best combination

**Advantages**:
- Exhaustive search
- Guaranteed to find best in grid

**Limitations**:
- Slow (tries all combinations)
- Exponential growth with parameters

**Scikit-learn Example**:
```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_split': [2, 5, 10]
}

# Grid search
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1  # Use all CPUs
)

grid_search.fit(X_train, y_train)

# Best parameters
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")

# Use best model
best_model = grid_search.best_estimator_
```

#### **7.2.2 Random Search**

**How it works**:
- Try random combinations of parameters
- Sample from parameter distributions
- Often finds good solutions faster than grid search

**Advantages**:
- Much faster than grid search
- Often finds good parameters quickly
- Better for large parameter spaces

**Limitations**:
- Not exhaustive
- Might miss optimal combination

**When to use**:
- Large parameter space
- Time constraints
- As initial exploration before refined grid search

**Scikit-learn Example**:
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Define parameter distributions
param_distributions = {
    'classifier__n_estimators': randint(50, 200),
    'classifier__max_depth': [5, 10, 15, 20, None],
    'classifier__min_samples_split': randint(2, 20)
}

# Random search
random_search = RandomizedSearchCV(
    pipeline,
    param_distributions,
    n_iter=20,  # Try 20 random combinations
    cv=5,
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)
```

### 7.3 Common Pitfalls and Solutions

#### **Pitfall 1: Data Leakage**

**Problem**: Test information leaks into training

**Common Causes**:
1. Fitting scaler on entire dataset before splitting
2. Feature selection on entire dataset
3. Using test set for model selection

**Example of WRONG approach**:
```python
# WRONG!
X_scaled = StandardScaler().fit_transform(X)  # Uses test data!
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

**Example of CORRECT approach**:
```python
# CORRECT!
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Only transform, not fit!

# Or better, use Pipeline:
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
# Pipeline handles this automatically in cross-validation!
```

#### **Pitfall 2: Test Set Abuse**

**Problem**: Using test set repeatedly for model selection

**Why it's bad**: Test performance becomes overly optimistic

**Solution**: Three-way split

```python
# Split into train, validation, test
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42
)

# Use validation for model selection
# Use test ONLY for final evaluation (once!)
```

#### **Pitfall 3: Forgetting Feature Scaling**

**Problem**: Some algorithms require scaled features

**Algorithms that NEED scaling**:
- SVM
- KNN
- Neural Networks
- Algorithms with regularization (Ridge, Lasso)
- PCA

**Algorithms that DON'T need scaling**:
- Tree-based methods (Decision Trees, Random Forests)
- Naive Bayes

**Solution**: Always scale when in doubt, use pipelines

#### **Pitfall 4: Class Imbalance**

**Problem**: Accuracy is misleading with imbalanced classes

**Example**: 95% negative class
- Always predict negative → 95% accuracy
- But completely useless model!

**Solutions**:
1. **Use appropriate metrics**: F1-score, ROC-AUC, not just accuracy
2. **Stratified splitting**: Maintains class proportions
3. **Class weights**: `class_weight='balanced'` parameter
4. **Resampling**: SMOTE, undersampling (advanced topic)

```python
# Use stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y
)

# Use class weights
model = RandomForestClassifier(class_weight='balanced')

# Use appropriate metrics
f1 = f1_score(y_test, y_pred)  # Better than accuracy for imbalanced
```

#### **Pitfall 5: Overfitting**

**Signs of overfitting**:
- High training accuracy, low test accuracy
- Large gap in learning curves
- Model performs well on training but fails on new data

**Solutions**:
1. **Regularization**: Use Ridge, Lasso, or L2 penalties
2. **Cross-validation**: Get reliable performance estimates
3. **More data**: If possible
4. **Feature selection**: Remove irrelevant features
5. **Reduce model complexity**: Lower tree depth, fewer layers
6. **Early stopping**: For iterative algorithms

---

## 8. Practical Guidelines

### 8.1 Workflow Checklist

#### **Before Starting**:
- [ ] Understand the problem (classification or regression?)
- [ ] Check data quality (missing values, outliers)
- [ ] Explore data distribution and class balance
- [ ] Set random seeds for reproducibility

#### **Data Preparation**:
- [ ] Split data BEFORE any preprocessing (train/test)
- [ ] Handle missing values
- [ ] Scale features (if needed for algorithm)
- [ ] Consider dimensionality reduction for high-dimensional data
- [ ] Use pipelines to prevent data leakage

#### **Model Selection**:
- [ ] Start with simple baseline (logistic regression, linear regression)
- [ ] Try 2-3 different algorithms
- [ ] Use cross-validation for all evaluations
- [ ] Choose metric appropriate for problem

#### **Hyperparameter Tuning**:
- [ ] Start with random search for exploration
- [ ] Refine with grid search if needed
- [ ] Use validation set or cross-validation
- [ ] Never tune on test set!

#### **Final Evaluation**:
- [ ] Evaluate ONCE on test set
- [ ] Report multiple metrics (not just accuracy)
- [ ] Check confusion matrix for classification
- [ ] Plot residuals for regression
- [ ] Assess practical significance, not just statistical

#### **Documentation**:
- [ ] Record all parameters and random seeds
- [ ] Document preprocessing steps
- [ ] Save final model
- [ ] Create reproducible script

### 8.2 Algorithm Selection Guide

#### **For Classification**:

**Start with**: Logistic Regression (simple baseline)

**Try next**:
- Random Forest (robust, works well out-of-box)
- SVM (if < 10,000 samples and features scaled)

**When interpretability matters**: Decision Tree or Logistic Regression

**When accuracy is paramount**: Random Forest or Gradient Boosting

#### **For Regression**:

**Start with**: Linear Regression (simple baseline)

**If overfitting**: Ridge or Lasso

**If many irrelevant features**: Lasso (feature selection)

**If non-linear**: Random Forest or SVR

#### **For Clustering**:

**Start with**: K-Means (if you know K)

**If K unknown**: Hierarchical Clustering or DBSCAN

**If arbitrary shapes**: DBSCAN

**If need hierarchy**: Hierarchical Clustering

### 8.3 Computing Resources

**Memory Considerations**:
- Random Forests: Memory-intensive
- SVM: Moderate memory
- Logistic Regression: Minimal memory

**Speed Considerations**:
- Fast: Logistic Regression, Naive Bayes
- Moderate: Random Forests, Decision Trees
- Slow: SVM (large datasets), t-SNE

**Parallelization**:
- Use `n_jobs=-1` to use all CPU cores
- Available for: Random Forests, cross-validation, grid search

---

## 9. Further Resources

### 9.1 Books

1. **"An Introduction to Statistical Learning"** by James, Witten, Hastie, Tibshirani
   - Accessible introduction to ML
   - Focuses on intuition
   - R code examples (but concepts apply to Python)
   - Free PDF available

2. **"Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow"** by Aurélien Géron
   - Practical Python examples
   - Covers scikit-learn thoroughly
   - Good for implementation

3. **"The Elements of Statistical Learning"** by Hastie, Tibshirani, Friedman
   - More mathematical/theoretical
   - Comprehensive reference
   - Free PDF available

### 9.2 Online Resources

**Scikit-learn Documentation**:
- Official docs: https://scikit-learn.org
- User guide with examples
- API reference

**Tutorials**:
- Scikit-learn tutorials: https://scikit-learn.org/stable/tutorial/
- Kaggle Learn: https://www.kaggle.com/learn
- Fast.ai: https://www.fast.ai

**Courses**:
- Andrew Ng's Machine Learning (Coursera)
- Fast.ai Practical Deep Learning
- Google's Machine Learning Crash Course

### 9.3 Practice Datasets

**Built-in Scikit-learn**:
- `load_iris()`, `load_breast_cancer()`, `load_digits()`: Classification
- `load_diabetes()`, `load_boston()`: Regression

**OpenML**: https://www.openml.org
- Thousands of datasets
- Accessible via scikit-learn

**Kaggle**: https://www.kaggle.com/datasets
- Real-world datasets
- Competitions for practice

---

## Appendix: Quick Reference

### Key Terminology

- **Feature**: Input variable (X)
- **Target**: Output variable (y)
- **Training**: Learning from data
- **Testing**: Evaluating on new data
- **Overfitting**: Model too complex, poor generalization
- **Underfitting**: Model too simple, poor performance
- **Hyperparameter**: Setting not learned from data
- **Cross-validation**: Multiple train/test splits
- **Pipeline**: Chain of preprocessing and modeling steps
- **Regularization**: Penalty to prevent overfitting

### Common Scikit-learn Patterns

```python
# Basic workflow
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Train model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 4. Predict and evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
```

### Metric Selection Guide

| Problem Type | Primary Metric | When to Use |
|--------------|----------------|-------------|
| Balanced Classification | Accuracy | Classes roughly equal |
| Imbalanced Classification | F1-Score, ROC-AUC | Classes unequal |
| Medical Diagnosis | Recall (Sensitivity) | Don't miss positives |
| Spam Detection | Precision | Avoid false positives |
| Regression | R², RMSE | Standard regression |
| Regression with Outliers | MAE | Robust to outliers |

---
*This handout is part of the "Introduction to Scientific Programming" course at CNC-UC, University of Coimbra. For questions or clarifications, please contact the course instructor.*
**Document Version**: 1.0  
**License**: CC BY 4.0

