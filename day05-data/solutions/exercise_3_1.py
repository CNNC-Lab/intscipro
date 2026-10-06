# Exercise 3 1 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# a) Count and compare
print("=== MISSING DATA ANALYSIS ===\n")

total_missing = df_missing.isnull().sum().sum()
print(f"Total missing values: {total_missing}")
print(f"Percentage of all data: {total_missing / (df_missing.shape[0] * df_missing.shape[1]) * 100:.2f}%\n")

# Mean RT with different handling
rt_with_nan = df_missing['reaction_time']
rt_without_nan = df_missing['reaction_time'].dropna()

print("Reaction time statistics:")
print(f"Mean (including NaN): {rt_with_nan.mean():.2f}ms")
print(f"Mean (excluding NaN): {rt_without_nan.mean():.2f}ms")
print(f"Difference: {abs(rt_with_nan.mean() - rt_without_nan.mean()):.2f}ms\n")

# b) Implement different strategies
print("=== IMPUTATION STRATEGIES ===\n")

# Strategy 1: Drop rows with any missing
df_dropped = df_missing.dropna()
print(f"Strategy 1 - Drop rows:")
print(f"  Original rows: {len(df_missing)}")
print(f"  After dropping: {len(df_dropped)}")
print(f"  Rows lost: {len(df_missing) - len(df_dropped)} ({(len(df_missing)-len(df_dropped))/len(df_missing)*100:.1f}%)")
print(f"  Mean RT: {df_dropped['reaction_time'].mean():.2f}ms\n")

# Strategy 2: Fill with overall median
df_median = df_missing.copy()
df_median['reaction_time'] = df_median['reaction_time'].fillna(
    df_median['reaction_time'].median()
)
df_median['accuracy'] = df_median['accuracy'].fillna(
    df_median['accuracy'].median()
)
print(f"Strategy 2 - Fill with median:")
print(f"  Missing values remaining: {df_median.isnull().sum().sum()}")
print(f"  Mean RT: {df_median['reaction_time'].mean():.2f}ms")
print(f"  Std RT: {df_median['reaction_time'].std():.2f}ms\n")

# Strategy 3: Fill with condition-specific medians
df_grouped = df_missing.copy()
df_grouped['reaction_time'] = df_grouped.groupby('condition')['reaction_time'].transform(
    lambda x: x.fillna(x.median())
)
df_grouped['accuracy'] = df_grouped.groupby('condition')['accuracy'].transform(
    lambda x: x.fillna(x.median())
)
print(f"Strategy 3 - Fill with condition-specific medians:")
print(f"  Missing values remaining: {df_grouped.isnull().sum().sum()}")
print(f"  Mean RT: {df_grouped['reaction_time'].mean():.2f}ms")
print(f"  Mean RT by condition:")
for condition in df_grouped['condition'].unique():
    cond_rt = df_grouped[df_grouped['condition'] == condition]['reaction_time'].mean()
    print(f"    {condition}: {cond_rt:.2f}ms")
print()

# Strategy 4: Forward fill (for time series)
df_ffill = df_missing.sort_values(['subject_id', 'trial']).copy()
df_ffill['reaction_time'] = df_ffill.groupby('subject_id')['reaction_time'].ffill()
df_ffill['accuracy'] = df_ffill.groupby('subject_id')['accuracy'].ffill()
remaining_missing = df_ffill.isnull().sum().sum()
print(f"Strategy 4 - Forward fill (within subject):")
print(f"  Missing values remaining: {remaining_missing}")
print(f"  Mean RT: {df_ffill['reaction_time'].mean():.2f}ms")
print(f"  Note: Forward fill can't fill first values in each group\n")

# c) Compare results
print("=== COMPARISON SUMMARY ===\n")

comparison = pd.DataFrame({
    'Strategy': ['Original', 'Drop rows', 'Median fill', 'Group median', 'Forward fill'],
    'N_rows': [
        len(df_missing),
        len(df_dropped),
        len(df_median),
        len(df_grouped),
        len(df_ffill)
    ],
    'Missing_values': [
        df_missing.isnull().sum().sum(),
        df_dropped.isnull().sum().sum(),
        df_median.isnull().sum().sum(),
        df_grouped.isnull().sum().sum(),
        df_ffill.isnull().sum().sum()
    ],
    'Mean_RT': [
        df_missing['reaction_time'].mean(),
        df_dropped['reaction_time'].mean(),
        df_median['reaction_time'].mean(),
        df_grouped['reaction_time'].mean(),
        df_ffill['reaction_time'].mean()
    ],
    'Std_RT': [
        df_missing['reaction_time'].std(),
        df_dropped['reaction_time'].std(),
        df_median['reaction_time'].std(),
        df_grouped['reaction_time'].std(),
        df_ffill['reaction_time'].std()
    ]
})

print(comparison.to_string(index=False))

# When to use each approach
print("\n=== WHEN TO USE EACH STRATEGY ===")
print("""
1. Drop rows:
   - When missing data is minimal (<5%)
   - When missing is completely random
   - When you have plenty of data

2. Median fill (overall):
   - Quick and simple
   - When groups are similar
   - When missing is random

3. Group-specific median:
   - When groups differ systematically
   - When you want to preserve group differences
   - More accurate than overall median

4. Forward fill:
   - Time series data
   - When values change smoothly
   - When previous value is good estimate
   
5. Other approaches (not shown):
   - Interpolation for smooth temporal data
   - Predictive models (regression, KNN)
   - Multiple imputation for inference
""")
