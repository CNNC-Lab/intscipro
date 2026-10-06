# Exercise 1 1 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# b) Initial inspection
print("First 10 rows:")
print(df.head(10))

print("\nDataFrame shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\nColumn information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nData types:")
print(df.dtypes)

# c) Answer questions
print("\n=== ANSWERS ===")
print(f"Total observations: {len(df)}")
print(f"Unique subjects: {df['subject_id'].nunique()}")
print(f"Experimental conditions: {df['condition'].unique()}")
print(f"Reaction time range: {df['reaction_time'].min():.1f} - {df['reaction_time'].max():.1f} ms")
print(f"Mean reaction time: {df['reaction_time'].mean():.1f} ms")
print(f"Mean accuracy: {df['accuracy'].mean():.3f}")
