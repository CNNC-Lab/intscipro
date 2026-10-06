# Exercise 2 2 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# a) Using .loc[]
print("=== USING .loc[] ===\n")

# Rows 0-9, specific columns
subset1 = df.loc[0:9, ['subject_id', 'reaction_time', 'accuracy']]
print("Rows 0-9, selected columns:")
print(subset1)
print()

# Control trials
control_trials = df.loc[df['condition'] == 'control']
print(f"Control trials: {len(control_trials)}")
print(control_trials.head())
print()

# RT for high accuracy trials
high_acc_rt = df.loc[df['accuracy'] > 0.85, 'reaction_time']
print(f"Reaction times for high accuracy trials (n={len(high_acc_rt)}):")
print(f"Mean: {high_acc_rt.mean():.1f}ms")
print(f"Std: {high_acc_rt.std():.1f}ms")
print()

# b) Using .iloc[]
print("=== USING .iloc[] ===\n")

# First 20 rows, first 4 columns
subset2 = df.iloc[0:20, 0:4]
print("First 20 rows, first 4 columns:")
print(subset2.head(10))
print()

# Every 10th row
every_10th = df.iloc[::10]
print(f"Every 10th row: {len(every_10th)} rows")
print(every_10th[['subject_id', 'condition', 'trial']].head())
print()

# Last 5 rows, last 2 columns
last_subset = df.iloc[-5:, -2:]
print("Last 5 rows, last 2 columns:")
print(last_subset)
print()

# c) Modify data using .loc[]
print("=== MODIFYING DATA WITH .loc[] ===\n")

# Create copy to avoid modifying original
df_modified = df.copy()

# Default value
df_modified['performance_category'] = 'medium'

# Set high performance
df_modified.loc[df_modified['accuracy'] > 0.9, 'performance_category'] = 'high'

# Set low performance
df_modified.loc[df_modified['accuracy'] < 0.7, 'performance_category'] = 'low'

# Check results
print("Performance category distribution:")
print(df_modified['performance_category'].value_counts())
print()

# Verify accuracy ranges
print("Accuracy by performance category:")
print(df_modified.groupby('performance_category')['accuracy'].describe())
