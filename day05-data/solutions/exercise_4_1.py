# Exercise 4 1 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# Create copy to work with
df_transformed = df.copy()

# a) Derived numerical variables
print("=== CREATING DERIVED VARIABLES ===\n")

# RT in seconds
df_transformed['rt_seconds'] = df_transformed['reaction_time'] / 1000

# Efficiency (accuracy per second)
df_transformed['efficiency'] = df_transformed['accuracy'] / df_transformed['rt_seconds']

# Performance score
df_transformed['performance_score'] = (
    df_transformed['accuracy'] * 100 - df_transformed['rt_seconds']
)

print("New variables created:")
print(df_transformed[['reaction_time', 'rt_seconds', 'accuracy', 
                      'efficiency', 'performance_score']].head())
print()

print("Summary statistics for new variables:")
print(df_transformed[['rt_seconds', 'efficiency', 'performance_score']].describe())
print()

# b) Categorize continuous variables
print("=== CATEGORIZING VARIABLES ===\n")

# RT category using pd.cut with custom bins
df_transformed['rt_category'] = pd.cut(
    df_transformed['reaction_time'],
    bins=[0, 300, 450, float('inf')],
    labels=['fast', 'medium', 'slow']
)

# Accuracy level
df_transformed['accuracy_level'] = pd.cut(
    df_transformed['accuracy'],
    bins=[0, 0.7, 0.9, 1.0],
    labels=['low', 'medium', 'high']
)

print("RT category distribution:")
print(df_transformed['rt_category'].value_counts())
print(f"\nMean RT by category:")
print(df_transformed.groupby('rt_category')['reaction_time'].mean())
print()

print("Accuracy level distribution:")
print(df_transformed['accuracy_level'].value_counts())
print(f"\nMean accuracy by level:")
print(df_transformed.groupby('accuracy_level')['accuracy'].mean())
print()

# c) Z-scores
print("=== Z-SCORE NORMALIZATION ===\n")

df_transformed['rt_zscore'] = (
    (df_transformed['reaction_time'] - df_transformed['reaction_time'].mean()) / 
    df_transformed['reaction_time'].std()
)

df_transformed['accuracy_zscore'] = (
    (df_transformed['accuracy'] - df_transformed['accuracy'].mean()) / 
    df_transformed['accuracy'].std()
)

print("Z-score statistics (should have mean≈0, std≈1):")
print(df_transformed[['rt_zscore', 'accuracy_zscore']].describe())
print()

# Verify with scipy
from scipy import stats
rt_zscore_scipy = stats.zscore(df_transformed['reaction_time'])
print(f"Manual z-score matches scipy: {np.allclose(df_transformed['rt_zscore'], rt_zscore_scipy)}")
print()

# d) Binary indicators
print("=== BINARY INDICATORS ===\n")

df_transformed['is_correct'] = df_transformed['accuracy'] > 0.5
df_transformed['is_drug'] = df_transformed['condition'].str.contains('drug')

print("Correct trials:")
print(df_transformed['is_correct'].value_counts())
print(f"Percentage correct: {df_transformed['is_correct'].mean()*100:.1f}%")
print()

print("Drug vs control distribution:")
print(df_transformed['is_drug'].value_counts())
print()

# Alternative using np.where for multiple categories
df_transformed['trial_outcome'] = np.where(
    df_transformed['accuracy'] > 0.9,
    'excellent',
    np.where(
        df_transformed['accuracy'] > 0.7,
        'good',
        'poor'
    )
)

print("Trial outcome distribution:")
print(df_transformed['trial_outcome'].value_counts())
print()

# Summary of all new columns
print("=== SUMMARY OF NEW COLUMNS ===")
new_columns = ['rt_seconds', 'efficiency', 'performance_score', 'rt_category',
               'accuracy_level', 'rt_zscore', 'accuracy_zscore', 'is_correct',
               'is_drug', 'trial_outcome']
print(f"Added {len(new_columns)} new columns:")
for col in new_columns:
    print(f"  - {col}: {df_transformed[col].dtype}")
