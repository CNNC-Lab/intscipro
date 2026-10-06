# Exercise 6 1 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Prepare data
subject_means = df.groupby(['subject_id', 'condition'])['reaction_time'].mean().unstack()

print("=== HYPOTHESIS TESTING ===\n")

# a) Independent samples t-test
print("=== INDEPENDENT SAMPLES T-TEST ===\n")

control_rt = df[df['condition'] == 'control']['reaction_time']
drug_a_rt = df[df['condition'] == 'drug_a']['reaction_time']

print(f"Control: n={len(control_rt)}, mean={control_rt.mean():.2f}, std={control_rt.std():.2f}")
print(f"Drug A: n={len(drug_a_rt)}, mean={drug_a_rt.mean():.2f}, std={drug_a_rt.std():.2f}")
print()

# Check normality assumption
print("Checking normality assumption (Shapiro-Wilk test):")
stat_control, p_control = stats.shapiro(control_rt)
stat_drug_a, p_drug_a = stats.shapiro(drug_a_rt)

print(f"  Control: W={stat_control:.4f}, p={p_control:.4f}", 
      "✓ Normal" if p_control > 0.05 else "✗ Not normal")
print(f"  Drug A: W={stat_drug_a:.4f}, p={p_drug_a:.4f}",
      "✓ Normal" if p_drug_a > 0.05 else "✗ Not normal")
print()

# Check equal variances assumption
print("Checking equal variances (Levene's test):")
stat_levene, p_levene = stats.levene(control_rt, drug_a_rt)
print(f"  Levene's test: W={stat_levene:.4f}, p={p_levene:.4f}",
      "✓ Equal variances" if p_levene > 0.05 else "✗ Unequal variances")
print()

# Perform t-test
if p_levene > 0.05:
    print("Using standard t-test (equal variances):")
    t_stat, p_value = stats.ttest_ind(control_rt, drug_a_rt, equal_var=True)
else:
    print("Using Welch's t-test (unequal variances):")
    t_stat, p_value = stats.ttest_ind(control_rt, drug_a_rt, equal_var=False)

print(f"  t-statistic: {t_stat:.4f}")
print(f"  p-value: {p_value:.4f}")
print(f"  Conclusion: {'Significant difference' if p_value < 0.05 else 'No significant difference'} (α=0.05)")
print()

# Calculate Cohen's d
def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = group1.var(), group2.var()
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (group1.mean() - group2.mean()) / pooled_std

d = cohens_d(control_rt, drug_a_rt)
print(f"Effect size (Cohen's d): {d:.4f}")
if abs(d) < 0.2:
    interpretation = "negligible"
elif abs(d) < 0.5:
    interpretation = "small"
elif abs(d) < 0.8:
    interpretation = "medium"
else:
    interpretation = "large"
print(f"  Interpretation: {interpretation} effect")
print()

# b) Paired samples t-test
print("=== PAIRED SAMPLES T-TEST ===\n")

# Use subject means for cleaner paired comparison
control_paired = subject_means['control']
drug_a_paired = subject_means['drug_a']

print(f"Paired comparison (n={len(control_paired)} subjects)")
print(f"  Control mean: {control_paired.mean():.2f} ms")
print(f"  Drug A mean: {drug_a_paired.mean():.2f} ms")
print(f"  Mean difference: {(drug_a_paired - control_paired).mean():.2f} ms")
print()

# Paired t-test
t_stat_paired, p_paired = stats.ttest_rel(control_paired, drug_a_paired)

print(f"Paired t-test results:")
print(f"  t-statistic: {t_stat_paired:.4f}")
print(f"  p-value: {p_paired:.4f}")
print(f"  Conclusion: {'Significant difference' if p_paired < 0.05 else 'No significant difference'}")
print()

# Effect size for paired data
differences = drug_a_paired - control_paired
d_paired = differences.mean() / differences.std()
print(f"Effect size (Cohen's d for paired data): {d_paired:.4f}")
print()

# Visualize paired data
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Before-after plot
axes[0].plot([1, 2], [control_paired, drug_a_paired], 'o-', alpha=0.3, color='gray')
axes[0].plot([1, 2], [control_paired.mean(), drug_a_paired.mean()], 
             'o-', linewidth=3, markersize=10, color='red', label='Mean')
axes[0].set_xlim(0.5, 2.5)
axes[0].set_xticks([1, 2])
axes[0].set_xticklabels(['Control', 'Drug A'])
axes[0].set_ylabel('Reaction Time (ms)')
axes[0].set_title('Paired Comparison: Control vs Drug A')
axes[0].legend()

# Distribution of differences
axes[1].hist(differences, bins=20, edgecolor='black', alpha=0.7)
axes[1].axvline(0, color='red', linestyle='--', linewidth=2, label='No effect')
axes[1].axvline(differences.mean(), color='blue', linestyle='--', linewidth=2, label='Mean difference')
axes[1].set_xlabel('Difference (Drug A - Control) (ms)')
axes[1].set_ylabel('Number of Subjects')
axes[1].set_title('Distribution of Within-Subject Differences')
axes[1].legend()

plt.tight_layout()
plt.show()

# c) Non-parametric alternative
print("=== NON-PARAMETRIC TESTS ===\n")

# Mann-Whitney U test (independent samples)
u_stat, p_mann = stats.mannwhitneyu(control_rt, drug_a_rt, alternative='two-sided')
print("Mann-Whitney U test (non-parametric alternative to t-test):")
print(f"  U-statistic: {u_stat:.4f}")
print(f"  p-value: {p_mann:.4f}")
print(f"  Conclusion: {'Significant difference' if p_mann < 0.05 else 'No significant difference'}")
print()

# Wilcoxon signed-rank test (paired samples)
w_stat, p_wilcoxon = stats.wilcoxon(control_paired, drug_a_paired)
print("Wilcoxon signed-rank test (non-parametric alternative to paired t-test):")
print(f"  W-statistic: {w_stat:.4f}")
print(f"  p-value: {p_wilcoxon:.4f}")
print(f"  Conclusion: {'Significant difference' if p_wilcoxon < 0.05 else 'No significant difference'}")
print()

# Compare parametric vs non-parametric
print("Comparison of p-values:")
comparison_pvals = pd.DataFrame({
    'Test Type': ['Independent t-test', 'Mann-Whitney U', 'Paired t-test', 'Wilcoxon'],
    'p-value': [p_value, p_mann, p_paired, p_wilcoxon],
    'Significant (α=0.05)': [
        '✓' if p_value < 0.05 else '✗',
        '✓' if p_mann < 0.05 else '✗',
        '✓' if p_paired < 0.05 else '✗',
        '✓' if p_wilcoxon < 0.05 else '✗'
    ]
})
print(comparison_pvals.to_string(index=False))
print()

# d) ANOVA
print("=== ONE-WAY ANOVA ===\n")

control_all = df[df['condition'] == 'control']['reaction_time']
drug_a_all = df[df['condition'] == 'drug_a']['reaction_time']
drug_b_all = df[df['condition'] == 'drug_b']['reaction_time']

# Perform ANOVA
f_stat, p_anova = stats.f_oneway(control_all, drug_a_all, drug_b_all)

print(f"Comparing all three conditions:")
print(f"  Control: mean={control_all.mean():.2f}, n={len(control_all)}")
print(f"  Drug A: mean={drug_a_all.mean():.2f}, n={len(drug_a_all)}")
print(f"  Drug B: mean={drug_b_all.mean():.2f}, n={len(drug_b_all)}")
print()

print(f"ANOVA results:")
print(f"  F-statistic: {f_stat:.4f}")
print(f"  p-value: {p_anova:.4f}")
print(f"  Conclusion: {'Significant differences exist' if p_anova < 0.05 else 'No significant differences'}")
print()

# Post-hoc tests (if ANOVA is significant)
if p_anova < 0.05:
    print("POST-HOC PAIRWISE COMPARISONS (Bonferroni correction):")
    alpha_corrected = 0.05 / 3  # 3 comparisons
    print(f"  Corrected α = {alpha_corrected:.4f}")
    print()
    
    comparisons = [
        ('Control', 'Drug A', control_all, drug_a_all),
        ('Control', 'Drug B', control_all, drug_b_all),
        ('Drug A', 'Drug B', drug_a_all, drug_b_all)
    ]
    
    for name1, name2, group1, group2 in comparisons:
        t, p = stats.ttest_ind(group1, group2)
        sig = '✓ Significant' if p < alpha_corrected else '✗ Not significant'
        print(f"  {name1} vs {name2}: t={t:.3f}, p={p:.4f} {sig}")
    print()

# Visualize all three conditions
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([control_all, drug_a_all, drug_b_all], 
           tick_labels=['Control', 'Drug A', 'Drug B'])
ax.set_ylabel('Reaction Time (ms)')
ax.set_title(f'Comparison of All Conditions (ANOVA p={p_anova:.4f})')
plt.show()

# Summary report
print("=== STATISTICAL TESTING SUMMARY ===")
print(f"""
Experimental Question: Do drugs affect reaction time?

Method 1: Independent samples t-test
- Compares control vs drug_a
- Result: {'Significant' if p_value < 0.05 else 'Not significant'} (p={p_value:.4f})
- Effect size: d={d:.3f} ({interpretation})

Method 2: Paired samples t-test  
- Compares within-subject changes
- Result: {'Significant' if p_paired < 0.05 else 'Not significant'} (p={p_paired:.4f})
- More powerful due to within-subject design

Method 3: One-way ANOVA
- Compares all three conditions
- Result: {'Significant differences' if p_anova < 0.05 else 'No differences'} (p={p_anova:.4f})
- {'Post-hoc tests show specific pairwise differences' if p_anova < 0.05 else 'No post-hoc tests needed'}

Non-parametric alternatives:
- Mann-Whitney U: p={p_mann:.4f}
- Wilcoxon: p={p_wilcoxon:.4f}
- Similar conclusions to parametric tests
""")
