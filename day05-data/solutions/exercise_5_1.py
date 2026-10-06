# Exercise 5 1 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# a) Basic pivot table
print("=== BASIC PIVOT TABLE ===\n")

pivot_basic = df.pivot_table(
    values='reaction_time',
    index='subject_id',
    columns='condition',
    aggfunc='mean'
)

print("Mean RT by subject and condition:")
print(pivot_basic.head(10).round(2))
print()

print("Shape:", pivot_basic.shape)
print("Missing values:", pivot_basic.isnull().sum().sum())
print()

# b) Complex pivot table
print("=== COMPLEX PIVOT TABLE ===\n")

pivot_complex = df.pivot_table(
    values='reaction_time',
    index='subject_id',
    columns='condition',
    aggfunc=['mean', 'std', 'count'],
    margins=True,  # Add row/column totals
    margins_name='Overall'
)

print("Pivot with multiple aggregations and margins:")
print(pivot_complex.head(10).round(2))
print()

# Just the margins row (overall statistics)
print("Overall statistics (margins row):")
print(pivot_complex.loc['Overall'].round(2))
print()

# Multiple values in pivot
pivot_multi = df.pivot_table(
    values=['reaction_time', 'accuracy'],
    index='subject_id',
    columns='condition',
    aggfunc='mean'
)

print("Pivot with multiple value columns:")
print(pivot_multi.head(10).round(3))
print()

# c) Melting data
print("=== MELTING DATA (WIDE TO LONG) ===\n")

# Create wide format first
wide_data = pivot_basic.reset_index()
print("Wide format data:")
print(wide_data.head())
print(f"Shape: {wide_data.shape}")
print()

# Melt to long format
long_data = wide_data.melt(
    id_vars=['subject_id'],
    value_vars=['control', 'drug_a', 'drug_b'],
    var_name='condition',
    value_name='reaction_time'
)

print("After melting to long format:")
print(long_data.head(15))
print(f"Shape: {long_data.shape}")
print()

# Verify it matches original structure
print("Comparison with original data:")
original_summary = df.groupby(['subject_id', 'condition'])['reaction_time'].mean().reset_index()
print(f"Original grouped data shape: {original_summary.shape}")
print(f"Melted data shape: {long_data.shape}")
print()

# d) Calculate condition differences
print("=== CALCULATING CONDITION DIFFERENCES ===\n")

# Method 1: Using pivot table
pivot_for_diff = df.groupby(['subject_id', 'condition'])['reaction_time'].mean().unstack()

# Calculate differences
pivot_for_diff['drug_a_vs_control'] = pivot_for_diff['drug_a'] - pivot_for_diff['control']
pivot_for_diff['drug_b_vs_control'] = pivot_for_diff['drug_b'] - pivot_for_diff['control']
pivot_for_diff['drug_a_vs_drug_b'] = pivot_for_diff['drug_a'] - pivot_for_diff['drug_b']

print("RT differences between conditions (per subject):")
print(pivot_for_diff[['control', 'drug_a', 'drug_b', 
                       'drug_a_vs_control', 'drug_b_vs_control']].head(10).round(2))
print()

# Summary of differences
print("Summary of condition effects:")
print(f"Mean drug_a effect (vs control): {pivot_for_diff['drug_a_vs_control'].mean():.2f}ms")
print(f"Mean drug_b effect (vs control): {pivot_for_diff['drug_b_vs_control'].mean():.2f}ms")
print()

# Test if differences are significant
from scipy import stats

t_stat_a, p_val_a = stats.ttest_1samp(pivot_for_diff['drug_a_vs_control'].dropna(), 0)
t_stat_b, p_val_b = stats.ttest_1samp(pivot_for_diff['drug_b_vs_control'].dropna(), 0)

print("Statistical tests (is the difference different from 0?):")
print(f"Drug A vs Control: t={t_stat_a:.3f}, p={p_val_a:.4f}")
print(f"Drug B vs Control: t={t_stat_b:.3f}, p={p_val_b:.4f}")
print()

# Visualize differences
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot of differences
axes[0].boxplot([
    pivot_for_diff['drug_a_vs_control'].dropna(),
    pivot_for_diff['drug_b_vs_control'].dropna()
], tick_labels=['Drug A', 'Drug B'])
axes[0].axhline(0, color='red', linestyle='--', label='No effect')
axes[0].set_ylabel('RT Difference vs Control (ms)')
axes[0].set_title('Distribution of Drug Effects')
axes[0].legend()

# Histogram of Drug A effect
axes[1].hist(pivot_for_diff['drug_a_vs_control'].dropna(), bins=20, 
             edgecolor='black', alpha=0.7)
axes[1].axvline(0, color='red', linestyle='--', linewidth=2, label='No effect')
axes[1].axvline(pivot_for_diff['drug_a_vs_control'].mean(), 
                color='blue', linestyle='--', linewidth=2, label='Mean effect')
axes[1].set_xlabel('RT Difference (ms)')
axes[1].set_ylabel('Number of Subjects')
axes[1].set_title('Drug A Effect Distribution')
axes[1].legend()

plt.tight_layout()
plt.show()
