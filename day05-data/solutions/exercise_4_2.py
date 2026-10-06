# Exercise 4 2 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# a) Basic group means
print("=== BASIC GROUP AGGREGATIONS ===\n")

# Mean RT by condition
rt_by_condition = df.groupby('condition')['reaction_time'].mean()
print("Mean reaction time by condition:")
print(rt_by_condition.round(2))
print()

# Mean accuracy by condition and session
acc_by_cond_session = df.groupby(['condition', 'session'])['accuracy'].mean()
print("Mean accuracy by condition and session:")
print(acc_by_cond_session.round(3))
print()

# Count trials per subject
trials_per_subject = df.groupby('subject_id').size()
print(f"Trials per subject (first 10 subjects):")
print(trials_per_subject.head(10))
print(f"Mean trials per subject: {trials_per_subject.mean():.1f}")
print()

# b) Multiple aggregations
print("=== MULTIPLE AGGREGATIONS ===\n")

# Multiple stats for RT by condition
rt_stats = df.groupby('condition')['reaction_time'].agg([
    'mean', 'std', 'min', 'max', 'count'
])
print("Reaction time statistics by condition:")
print(rt_stats.round(2))
print()

# Different aggregations for different columns
subject_stats = df.groupby('subject_id').agg({
    'reaction_time': ['mean', 'std'],
    'accuracy': ['mean', 'std'],
    'trial': 'count'
})
subject_stats.columns = ['_'.join(col) for col in subject_stats.columns]
print("Subject-level statistics (first 10 subjects):")
print(subject_stats.head(10).round(3))
print()

# Named aggregations (cleaner)
subject_summary = df.groupby('subject_id').agg(
    mean_rt=('reaction_time', 'mean'),
    std_rt=('reaction_time', 'std'),
    mean_acc=('accuracy', 'mean'),
    n_trials=('trial', 'count')
)
print("Subject summary with named aggregations (first 10):")
print(subject_summary.head(10).round(3))
print()

# c) Custom aggregations
print("=== CUSTOM AGGREGATIONS ===\n")

# Coefficient of variation
def coeff_variation(x):
    return x.std() / x.mean()

cv_by_condition = df.groupby('condition')['reaction_time'].agg(coeff_variation)
print("Coefficient of variation (CV) by condition:")
print(cv_by_condition.round(4))
print("(Higher CV = more variable performance)")
print()

# Percentage accurate trials
def pct_accurate(x):
    return (x > 0.5).mean() * 100

acc_pct = df.groupby(['subject_id', 'condition'])['accuracy'].agg(pct_accurate)
print("Percentage of accurate trials (first 20):")
print(acc_pct.head(20).round(1))
print()

# Multiple custom functions
def range_func(x):
    return x.max() - x.min()

custom_agg = df.groupby('condition')['reaction_time'].agg([
    ('mean', 'mean'),
    ('cv', coeff_variation),
    ('range', range_func),
    ('count', 'count')
])
print("Multiple custom aggregations:")
print(custom_agg.round(2))
print()

# d) Transform operations
print("=== TRANSFORM OPERATIONS ===\n")

df_transformed = df.copy()

# Within-subject z-scores
df_transformed['rt_zscore_within_subject'] = df_transformed.groupby('subject_id')['reaction_time'].transform(
    lambda x: (x - x.mean()) / x.std()
)

print("Within-subject z-scores (sample):")
sample_subject = df_transformed[df_transformed['subject_id'] == 1][
    ['subject_id', 'trial', 'reaction_time', 'rt_zscore_within_subject']
]
print(sample_subject.head(10))
print()

# Verify: mean should be ~0, std should be ~1 for each subject
verification = df_transformed.groupby('subject_id')['rt_zscore_within_subject'].agg(['mean', 'std'])
print("Verification (mean≈0, std≈1 for each subject):")
print(verification.head(10).round(6))
print()

# Percent of subject's mean
df_transformed['rt_pct_of_subject_mean'] = df_transformed.groupby('subject_id')['reaction_time'].transform(
    lambda x: (x / x.mean()) * 100
)

print("RT as percentage of subject mean:")
print(df_transformed[df_transformed['subject_id'] == 1][
    ['subject_id', 'trial', 'reaction_time', 'rt_pct_of_subject_mean']
].head(10))
print()

# Rank within group
df_transformed['rt_rank_in_condition'] = df_transformed.groupby('condition')['reaction_time'].rank()

print("RT rank within condition (sample):")
print(df_transformed[['condition', 'reaction_time', 'rt_rank_in_condition']].head(15))
print()

# e) Filtering groups
print("=== FILTERING GROUPS ===\n")

# Filter 1: Keep subjects with >85% accuracy
subject_acc = df.groupby('subject_id')['accuracy'].mean()
good_performers = subject_acc[subject_acc > 0.85].index
df_good_performers = df[df['subject_id'].isin(good_performers)]

print(f"Subjects with >85% accuracy:")
print(f"  Original subjects: {df['subject_id'].nunique()}")
print(f"  High performers: {len(good_performers)}")
print(f"  Original rows: {len(df)}")
print(f"  After filtering: {len(df_good_performers)}")
print()

# Alternative using filter
df_filtered_alt = df.groupby('subject_id').filter(lambda x: x['accuracy'].mean() > 0.85)
print(f"Using .filter() method: {len(df_filtered_alt)} rows")
print()

# Filter 2: Keep fast conditions
condition_rt = df.groupby('condition')['reaction_time'].mean()
fast_conditions = condition_rt[condition_rt < 400].index
df_fast_conditions = df[df['condition'].isin(fast_conditions)]

print(f"Conditions with mean RT < 400ms:")
print(f"  Fast conditions: {list(fast_conditions)}")
print(f"  Mean RT by condition:")
for cond in condition_rt.index:
    is_fast = "✓" if cond in fast_conditions else "✗"
    print(f"    {is_fast} {cond}: {condition_rt[cond]:.1f}ms")
print()

# Combined filtering
df_filtered_combined = df[
    (df['subject_id'].isin(good_performers)) &
    (df['condition'].isin(fast_conditions))
]
print(f"Combined filtering (high performers AND fast conditions):")
print(f"  Rows retained: {len(df_filtered_combined)}")
print(f"  Percentage of original: {len(df_filtered_combined)/len(df)*100:.1f}%")
