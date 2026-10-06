# Exercise 3 2 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

from scipy import stats
import matplotlib.pyplot as plt

# a) Add outliers (code provided above)
df_outliers = df.copy()
np.random.seed(42)
outlier_indices = np.random.choice(df_outliers.index, 15, replace=False)
df_outliers.loc[outlier_indices, 'reaction_time'] = np.random.uniform(800, 1200, 15)
fast_indices = np.random.choice(df_outliers.index, 10, replace=False)
df_outliers.loc[fast_indices, 'reaction_time'] = np.random.uniform(100, 150, 10)

print("=== OUTLIER DETECTION ===\n")

# b) Detect outliers - Method 1: Z-score
print("Method 1: Z-score (|z| > 3)")
z_scores = np.abs(stats.zscore(df_outliers['reaction_time']))
outliers_zscore = z_scores > 3
n_outliers_z = outliers_zscore.sum()

print(f"Outliers detected: {n_outliers_z} ({n_outliers_z/len(df_outliers)*100:.2f}%)")
print(f"Outlier RT range: {df_outliers.loc[outliers_zscore, 'reaction_time'].min():.1f} - "
      f"{df_outliers.loc[outliers_zscore, 'reaction_time'].max():.1f} ms\n")

# Method 2: IQR
print("Method 2: IQR (1.5 * IQR rule)")
Q1 = df_outliers['reaction_time'].quantile(0.25)
Q3 = df_outliers['reaction_time'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1: {Q1:.1f}, Q3: {Q3:.1f}, IQR: {IQR:.1f}")
print(f"Lower bound: {lower_bound:.1f}, Upper bound: {upper_bound:.1f}")

outliers_iqr = (df_outliers['reaction_time'] < lower_bound) | \
               (df_outliers['reaction_time'] > upper_bound)
n_outliers_iqr = outliers_iqr.sum()

print(f"Outliers detected: {n_outliers_iqr} ({n_outliers_iqr/len(df_outliers)*100:.2f}%)\n")

# Compare methods
print("Comparison of methods:")
print(f"Both methods agree: {(outliers_zscore & outliers_iqr).sum()} outliers")
print(f"Only Z-score: {(outliers_zscore & ~outliers_iqr).sum()} outliers")
print(f"Only IQR: {(~outliers_zscore & outliers_iqr).sum()} outliers\n")

# c) Visualize outliers
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Box plot
axes[0, 0].boxplot(df_outliers['reaction_time'])
axes[0, 0].set_ylabel('Reaction Time (ms)')
axes[0, 0].set_title('Box Plot - Outliers Visible')
axes[0, 0].axhline(lower_bound, color='r', linestyle='--', label='IQR bounds')
axes[0, 0].axhline(upper_bound, color='r', linestyle='--')
axes[0, 0].legend()

# Histogram with outliers
axes[0, 1].hist(df_outliers['reaction_time'], bins=50, edgecolor='black', alpha=0.7)
axes[0, 1].axvline(lower_bound, color='r', linestyle='--', label='IQR bounds')
axes[0, 1].axvline(upper_bound, color='r', linestyle='--')
axes[0, 1].set_xlabel('Reaction Time (ms)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution with Outliers')
axes[0, 1].legend()

# Histogram without outliers
df_no_outliers = df_outliers[~outliers_iqr]
axes[1, 0].hist(df_no_outliers['reaction_time'], bins=50, edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Reaction Time (ms)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Distribution without Outliers')

# Scatter plot showing outliers
axes[1, 1].scatter(df_outliers.index, df_outliers['reaction_time'], 
                   c=outliers_iqr, cmap='coolwarm', alpha=0.6)
axes[1, 1].axhline(lower_bound, color='r', linestyle='--')
axes[1, 1].axhline(upper_bound, color='r', linestyle='--')
axes[1, 1].set_xlabel('Index')
axes[1, 1].set_ylabel('Reaction Time (ms)')
axes[1, 1].set_title('Outliers Highlighted (Red)')

plt.tight_layout()
plt.show()

# d) Handle outliers - three approaches
print("\n=== HANDLING OUTLIERS ===\n")

# Approach 1: Remove outliers
df_removed = df_outliers[~outliers_iqr].copy()
print(f"Approach 1 - Remove outliers:")
print(f"  Original size: {len(df_outliers)}")
print(f"  After removal: {len(df_removed)}")
print(f"  Removed: {len(df_outliers) - len(df_removed)} ({(len(df_outliers)-len(df_removed))/len(df_outliers)*100:.1f}%)\n")

# Approach 2: Cap outliers (winsorization)
df_capped = df_outliers.copy()
df_capped.loc[df_capped['reaction_time'] < lower_bound, 'reaction_time'] = lower_bound
df_capped.loc[df_capped['reaction_time'] > upper_bound, 'reaction_time'] = upper_bound
print(f"Approach 2 - Cap outliers:")
print(f"  Values capped: {n_outliers_iqr}")
print(f"  New range: {df_capped['reaction_time'].min():.1f} - {df_capped['reaction_time'].max():.1f} ms\n")

# Approach 3: Flag outliers
df_flagged = df_outliers.copy()
df_flagged['is_outlier'] = outliers_iqr
print(f"Approach 3 - Flag outliers:")
print(f"  Outliers flagged: {df_flagged['is_outlier'].sum()}")
print(f"  Can analyze separately or exclude in specific analyses\n")

# e) Compare impact on statistics
print("=== IMPACT ON SUMMARY STATISTICS ===\n")

comparison = pd.DataFrame({
    'Measure': ['N', 'Mean', 'Median', 'Std', 'Min', 'Max'],
    'Original': [
        len(df_outliers),
        df_outliers['reaction_time'].mean(),
        df_outliers['reaction_time'].median(),
        df_outliers['reaction_time'].std(),
        df_outliers['reaction_time'].min(),
        df_outliers['reaction_time'].max()
    ],
    'Removed': [
        len(df_removed),
        df_removed['reaction_time'].mean(),
        df_removed['reaction_time'].median(),
        df_removed['reaction_time'].std(),
        df_removed['reaction_time'].min(),
        df_removed['reaction_time'].max()
    ],
    'Capped': [
        len(df_capped),
        df_capped['reaction_time'].mean(),
        df_capped['reaction_time'].median(),
        df_capped['reaction_time'].std(),
        df_capped['reaction_time'].min(),
        df_capped['reaction_time'].max()
    ]
})

print(comparison.round(2).to_string(index=False))

print("\n=== KEY INSIGHTS ===")
print(f"""
1. Outliers inflate mean more than median:
   - Original mean: {df_outliers['reaction_time'].mean():.1f} ms
   - Without outliers: {df_removed['reaction_time'].mean():.1f} ms
   - Difference: {df_outliers['reaction_time'].mean() - df_removed['reaction_time'].mean():.1f} ms

2. Outliers greatly increase standard deviation:
   - Original std: {df_outliers['reaction_time'].std():.1f} ms
   - Without outliers: {df_removed['reaction_time'].std():.1f} ms
   - Reduction: {((df_outliers['reaction_time'].std() - df_removed['reaction_time'].std()) / df_outliers['reaction_time'].std() * 100):.1f}%

3. Median is robust to outliers:
   - Original: {df_outliers['reaction_time'].median():.1f} ms
   - Without outliers: {df_removed['reaction_time'].median():.1f} ms
   - Almost unchanged!

Recommendations:
- Use IQR method (more robust than Z-score)
- Always visualize before deciding
- Remove clear errors (e.g., RT > 3 seconds)
- Flag/investigate borderline cases
- Document your decision and reasoning
""")
