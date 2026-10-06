# Exercise 5 2 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

# a) Create additional datasets (code provided above)
np.random.seed(42)

demographics = pd.DataFrame({
    'subject_id': range(1, 31),
    'age': np.random.randint(20, 40, 30),
    'sex': np.random.choice(['M', 'F'], 30),
    'handedness': np.random.choice(['R', 'L'], 30, p=[0.9, 0.1])
})

genetics = pd.DataFrame({
    'subject_id': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
    'COMT_val158met': np.random.choice(['val/val', 'val/met', 'met/met'], 10),
    'BDNF_val66met': np.random.choice(['val/val', 'val/met', 'met/met'], 10)
})

print("=== DATASETS TO MERGE ===\n")
print(f"Behavioral data: {len(df)} rows, {df['subject_id'].nunique()} subjects")
print(f"Demographics: {len(demographics)} rows, {demographics['subject_id'].nunique()} subjects")
print(f"Genetics: {len(genetics)} rows, {genetics['subject_id'].nunique()} subjects")
print()

# b) Different types of merges
print("=== DIFFERENT MERGE TYPES ===\n")

# Get subject-level behavioral summary for cleaner examples
behavioral_summary = df.groupby('subject_id').agg({
    'reaction_time': 'mean',
    'accuracy': 'mean'
}).reset_index()

print("Behavioral summary:")
print(behavioral_summary.head())
print()

# Inner join
inner_merged = pd.merge(behavioral_summary, demographics, on='subject_id', how='inner')
print(f"Inner join (subjects in both datasets):")
print(f"  Rows: {len(inner_merged)}")
print(f"  Subjects: {inner_merged['subject_id'].nunique()}")
print(inner_merged.head())
print()

# Left join
left_merged = pd.merge(behavioral_summary, demographics, on='subject_id', how='left')
print(f"Left join (keep all behavioral data):")
print(f"  Rows: {len(left_merged)}")
print(f"  Missing demographics: {left_merged.isnull().sum().sum()}")
print()

# Right join
right_merged = pd.merge(behavioral_summary, demographics, on='subject_id', how='right')
print(f"Right join (keep all demographics):")
print(f"  Rows: {len(right_merged)}")
print(f"  Missing behavioral data: {right_merged['reaction_time'].isnull().sum()}")
print()

# Outer join
outer_merged = pd.merge(behavioral_summary, demographics, on='subject_id', how='outer')
print(f"Outer join (keep everything):")
print(f"  Rows: {len(outer_merged)}")
print(f"  Total missing values: {outer_merged.isnull().sum().sum()}")
print()

# Visualize merge types
print("=== MERGE TYPE COMPARISON ===\n")
merge_comparison = pd.DataFrame({
    'Merge Type': ['Inner', 'Left', 'Right', 'Outer'],
    'Rows': [len(inner_merged), len(left_merged), len(right_merged), len(outer_merged)],
    'Missing Values': [
        inner_merged.isnull().sum().sum(),
        left_merged.isnull().sum().sum(),
        right_merged.isnull().sum().sum(),
        outer_merged.isnull().sum().sum()
    ]
})
print(merge_comparison)
print()

# c) Concatenating data
print("=== CONCATENATING DATA ===\n")

# Create session 2 data
session2_data = df.sample(n=300, random_state=42).copy()
session2_data['session_num'] = 2
df_session1 = df.copy()
df_session1['session_num'] = 1

# Concatenate vertically
combined_sessions = pd.concat([df_session1, session2_data], ignore_index=True)

print(f"Session 1 rows: {len(df_session1)}")
print(f"Session 2 rows: {len(session2_data)}")
print(f"Combined rows: {len(combined_sessions)}")
print()

print("Session distribution:")
print(combined_sessions['session_num'].value_counts())
print()

# Concatenate with keys (to identify source)
combined_with_keys = pd.concat(
    [df_session1, session2_data],
    keys=['session_1', 'session_2'],
    names=['session_label', 'row_index']
)
print("Combined with hierarchical index:")
print(combined_with_keys.head())
print()

# Concatenate horizontally (add columns)
# First, get summary statistics
session1_summary = df_session1.groupby('subject_id')['reaction_time'].mean().rename('session1_rt')
session2_summary = session2_data.groupby('subject_id')['reaction_time'].mean().rename('session2_rt')

horizontal_concat = pd.concat([session1_summary, session2_summary], axis=1)
print("Horizontal concatenation (add columns):")
print(horizontal_concat.head(10))
print()

# d) Merge multiple datasets
print("=== MERGING MULTIPLE DATASETS ===\n")

# Method 1: Sequential merges
merged_all = pd.merge(behavioral_summary, demographics, on='subject_id', how='left')
merged_all = pd.merge(merged_all, genetics, on='subject_id', how='left')

print("Sequential merging (behavioral + demographics + genetics):")
print(f"  Rows: {len(merged_all)}")
print(f"  Subjects: {merged_all['subject_id'].nunique()}")
print(merged_all.head(15))
print()

print("Missing genetic data:")
print(f"  Subjects without COMT data: {merged_all['COMT_val158met'].isnull().sum()}")
print(f"  Subjects without BDNF data: {merged_all['BDNF_val66met'].isnull().sum()}")
print()

# Check which subjects have genetic data
has_genetic_data = merged_all['COMT_val158met'].notnull()
print(f"Subjects with genetic data: {has_genetic_data.sum()}")
print(f"Subjects without genetic data: {(~has_genetic_data).sum()}")
print()

# Compare RT by genotype (only subjects with genetic data)
print("=== GENOTYPE ANALYSIS ===\n")

# COMT genotype effect
comt_effect = merged_all.dropna(subset=['COMT_val158met']).groupby('COMT_val158met')['reaction_time'].agg(['mean', 'std', 'count'])
print("Reaction time by COMT genotype:")
print(comt_effect.round(2))
print()

# Statistical test
from scipy import stats
comt_groups = [
    merged_all[merged_all['COMT_val158met'] == geno]['reaction_time'].dropna()
    for geno in merged_all['COMT_val158met'].dropna().unique()
]
if len(comt_groups) >= 2:
    f_stat, p_val = stats.f_oneway(*comt_groups)
    print(f"ANOVA for COMT effect: F={f_stat:.3f}, p={p_val:.4f}")
    if p_val < 0.05:
        print("Significant effect of COMT genotype!")
    else:
        print("No significant effect of COMT genotype")
print()

# Age effect
print("=== AGE EFFECT ===\n")
age_corr, age_p = stats.pearsonr(merged_all['age'], merged_all['reaction_time'])
print(f"Correlation between age and RT: r={age_corr:.3f}, p={age_p:.4f}")

# Visualize
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Age effect
axes[0].scatter(merged_all['age'], merged_all['reaction_time'], alpha=0.5)
axes[0].set_xlabel('Age (years)')
axes[0].set_ylabel('Mean Reaction Time (ms)')
axes[0].set_title(f'Age Effect (r={age_corr:.3f})')

# Add regression line
z = np.polyfit(merged_all['age'], merged_all['reaction_time'], 1)
p = np.poly1d(z)
axes[0].plot(merged_all['age'].sort_values(), 
             p(merged_all['age'].sort_values()), 
             "r--", linewidth=2, label='Linear fit')
axes[0].legend()

# COMT effect
comt_data_for_plot = merged_all.dropna(subset=['COMT_val158met'])
comt_groups_plot = [
    comt_data_for_plot[comt_data_for_plot['COMT_val158met'] == geno]['reaction_time']
    for geno in comt_data_for_plot['COMT_val158met'].unique()
]
axes[1].boxplot(comt_groups_plot, tick_labels=comt_data_for_plot['COMT_val158met'].unique())
axes[1].set_ylabel('Mean Reaction Time (ms)')
axes[1].set_title('COMT Genotype Effect')
axes[1].set_xlabel('COMT val158met Genotype')

plt.tight_layout()
plt.show()

# Summary
print("\n=== SUMMARY OF MERGED DATASET ===")
print(f"Final dataset: {len(merged_all)} rows")
print(f"Columns: {list(merged_all.columns)}")
print(f"Complete cases (no missing data): {merged_all.dropna().shape[0]}")
print(f"Subjects with complete data: {merged_all.dropna()['subject_id'].nunique()}")
