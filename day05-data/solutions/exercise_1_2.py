# Exercise 1 2 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# b) Data quality checks
print("=== MISSING DATA ANALYSIS ===\n")

# Count missing values
missing_counts = df_missing.isnull().sum()
print("Missing values per column:")
print(missing_counts[missing_counts > 0])

# Percentage missing
missing_percent = (df_missing.isnull().sum() / len(df_missing)) * 100
print("\nPercentage missing per column:")
print(missing_percent[missing_percent > 0])

# Rows with any missing values
rows_with_missing = df_missing[df_missing.isnull().any(axis=1)]
print(f"\nRows with missing values: {len(rows_with_missing)}")

# Subjects with >5% missing data
subject_missing = df_missing.groupby('subject_id').apply(
    lambda x: (x.isnull().sum().sum() / (len(x) * len(x.columns))) * 100
)
problematic_subjects = subject_missing[subject_missing > 5]
print(f"\nSubjects with >5% missing data:")
print(problematic_subjects)

# c) Visualize missing data
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
missing_data = df_missing.isnull().sum()
missing_data = missing_data[missing_data > 0]

ax.bar(missing_data.index, missing_data.values, color='coral')
ax.set_xlabel('Column')
ax.set_ylabel('Number of Missing Values')
ax.set_title('Missing Data by Column')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Alternative: heatmap-style visualization
plt.figure(figsize=(12, 6))
plt.imshow(df_missing.isnull().T, aspect='auto', cmap='gray_r', interpolation='none')
plt.colorbar(label='Missing')
plt.xlabel('Row Index')
plt.ylabel('Column')
plt.yticks(range(len(df_missing.columns)), df_missing.columns)
plt.title('Missing Data Pattern (Black = Missing)')
plt.tight_layout()
plt.show()
