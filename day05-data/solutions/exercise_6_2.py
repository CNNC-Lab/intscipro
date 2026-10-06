# Exercise 6 2 - Solution

from _setup import *  # noqa: F401,F403 - data built in the exercise text

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare data with demographics
subject_summary = df.groupby('subject_id').agg({
    'reaction_time': 'mean',
    'accuracy': 'mean'
}).reset_index()

# Add simulated demographics
np.random.seed(42)
subject_summary['age'] = np.random.randint(20, 40, len(subject_summary))
subject_summary['iq'] = np.random.normal(100, 15, len(subject_summary))

# Add some correlation between age and RT
subject_summary['reaction_time'] += subject_summary['age'] * 2

print("=== CORRELATION ANALYSIS ===\n")

# a) Correlation analysis
print("Pearson Correlation (age vs RT):")
r_pearson, p_pearson = stats.pearsonr(subject_summary['age'], subject_summary['reaction_time'])
print(f"  r = {r_pearson:.4f}")
print(f"  p-value = {p_pearson:.4f}")
if abs(r_pearson) < 0.3:
    strength = "weak"
elif abs(r_pearson) < 0.7:
    strength = "moderate"
else:
    strength = "strong"
direction = "positive" if r_pearson > 0 else "negative"
print(f"  Interpretation: {strength} {direction} correlation")
print()

print("Spearman Correlation (age vs RT):")
rho_spearman, p_spearman = stats.spearmanr(subject_summary['age'], subject_summary['reaction_time'])
print(f"  ρ = {rho_spearman:.4f}")
print(f"  p-value = {p_spearman:.4f}")
print()

print("Comparison:")
print(f"  Pearson r = {r_pearson:.4f}")
print(f"  Spearman ρ = {rho_spearman:.4f}")
print(f"  Difference = {abs(r_pearson - rho_spearman):.4f}")
print(f"  → {'Similar values suggest linear relationship' if abs(r_pearson - rho_spearman) < 0.1 else 'Different values suggest non-linear relationship'}")
print()

# Correlation matrix
print("Correlation Matrix (all numeric variables):")
corr_matrix = subject_summary[['age', 'reaction_time', 'accuracy', 'iq']].corr()
print(corr_matrix.round(4))
print()

# Visualize correlation matrix
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            vmin=-1, vmax=1, square=True, linewidths=1, ax=axes[0])
axes[0].set_title('Correlation Matrix Heatmap')

# Scatter plot: age vs RT
axes[1].scatter(subject_summary['age'], subject_summary['reaction_time'], alpha=0.6)
axes[1].set_xlabel('Age (years)')
axes[1].set_ylabel('Mean Reaction Time (ms)')
axes[1].set_title(f'Age vs RT (r={r_pearson:.3f}, p={p_pearson:.4f})')

# Add regression line
z = np.polyfit(subject_summary['age'], subject_summary['reaction_time'], 1)
p = np.poly1d(z)
x_line = np.linspace(subject_summary['age'].min(), subject_summary['age'].max(), 100)
axes[1].plot(x_line, p(x_line), "r--", linewidth=2, label='Linear fit')
axes[1].legend()

plt.tight_layout()
plt.show()

# b) Fit distributions
print("\n=== DISTRIBUTION FITTING ===\n")

# Fit normal distribution to RT
rt_data = df['reaction_time'].dropna()

mu, sigma = stats.norm.fit(rt_data)
print("Normal Distribution Fit:")
print(f"  μ (mean) = {mu:.2f} ms")
print(f"  σ (std) = {sigma:.2f} ms")
print()

# Kolmogorov-Smirnov test
ks_stat, ks_p = stats.kstest(rt_data, stats.norm(mu, sigma).cdf)
print("Kolmogorov-Smirnov test (goodness of fit):")
print(f"  KS statistic = {ks_stat:.4f}")
print(f"  p-value = {ks_p:.4f}")
print(f"  Conclusion: {'Data consistent with normal' if ks_p > 0.05 else 'Data NOT normal'}")
print()

# Visualize fit
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram with fitted normal
x = np.linspace(rt_data.min(), rt_data.max(), 1000)
pdf_normal = stats.norm.pdf(x, mu, sigma)

axes[0, 0].hist(rt_data, bins=50, density=True, alpha=0.6, edgecolor='black', label='Data')
axes[0, 0].plot(x, pdf_normal, 'r-', linewidth=2, label='Fitted normal')
axes[0, 0].set_xlabel('Reaction Time (ms)')
axes[0, 0].set_ylabel('Probability Density')
axes[0, 0].set_title('Normal Distribution Fit')
axes[0, 0].legend()

# Q-Q plot for normality
stats.probplot(rt_data, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot: RT vs Normal Distribution')
axes[0, 1].get_lines()[0].set_markerfacecolor('steelblue')
axes[0, 1].get_lines()[0].set_markersize(4)

# Try log-normal fit
shape, loc, scale = stats.lognorm.fit(rt_data, floc=0)
pdf_lognorm = stats.lognorm.pdf(x, shape, loc, scale)

axes[1, 0].hist(rt_data, bins=50, density=True, alpha=0.6, edgecolor='black', label='Data')
axes[1, 0].plot(x, pdf_normal, 'r-', linewidth=2, label='Normal', alpha=0.7)
axes[1, 0].plot(x, pdf_lognorm, 'g-', linewidth=2, label='Log-normal', alpha=0.7)
axes[1, 0].set_xlabel('Reaction Time (ms)')
axes[1, 0].set_ylabel('Probability Density')
axes[1, 0].set_title('Comparing Distribution Fits')
axes[1, 0].legend()

# Goodness of fit comparison
ks_normal = stats.kstest(rt_data, stats.norm(mu, sigma).cdf)
ks_lognorm = stats.kstest(rt_data, stats.lognorm(shape, loc, scale).cdf)

axes[1, 1].bar(['Normal', 'Log-normal'], [ks_normal[0], ks_lognorm[0]], color=['red', 'green'], alpha=0.7)
axes[1, 1].set_ylabel('KS Statistic')
axes[1, 1].set_title('Goodness of Fit Comparison (lower is better)')
axes[1, 1].axhline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()

print("Comparison of fits:")
print(f"  Normal: KS={ks_normal[0]:.4f}, p={ks_normal[1]:.4f}")
print(f"  Log-normal: KS={ks_lognorm[0]:.4f}, p={ks_lognorm[1]:.4f}")
print(f"  → {'Log-normal' if ks_lognorm[0] < ks_normal[0] else 'Normal'} fits better (lower KS statistic)")
print()

# c) Q-Q plot interpretation
print("=== Q-Q PLOT INTERPRETATION ===\n")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Normal data (for comparison)
normal_data = np.random.normal(350, 50, 1000)
stats.probplot(normal_data, dist="norm", plot=axes[0])
axes[0].set_title('Q-Q Plot: Perfect Normal Data\n(points on line)')

# Skewed data
skewed_data = np.random.gamma(2, 50, 1000) + 200
stats.probplot(skewed_data, dist="norm", plot=axes[1])
axes[1].set_title('Q-Q Plot: Right-Skewed Data\n(curve above line on right)')

# Heavy-tailed data
heavy_tail_data = np.random.standard_t(3, 1000) * 50 + 350
stats.probplot(heavy_tail_data, dist="norm", plot=axes[2])
axes[2].set_title('Q-Q Plot: Heavy-Tailed Data\n(S-shape)')

for ax in axes:
    ax.get_lines()[0].set_markerfacecolor('steelblue')
    ax.get_lines()[0].set_markersize(3)
    ax.get_lines()[0].set_alpha(0.6)

plt.tight_layout()
plt.show()

print("""
Q-Q Plot Interpretation Guide:

1. Points on the line:
   → Data follows normal distribution
   
2. Points curve above line on right:
   → Right-skewed distribution (long tail to the right)
   
3. Points curve below line on right:
   → Left-skewed distribution (long tail to the left)
   
4. S-shaped pattern:
   → Heavy-tailed distribution (more extreme values than normal)
   
5. Upside-down S-shape:
   → Light-tailed distribution (fewer extreme values than normal)

For our RT data:
""")

# Create Q-Q plot for our RT data with interpretation
fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(rt_data, dist="norm", plot=ax)
ax.set_title('Q-Q Plot: Reaction Time Data')
ax.get_lines()[0].set_markerfacecolor('steelblue')
ax.get_lines()[0].set_markersize(4)
ax.get_lines()[0].set_alpha(0.6)
plt.show()

# Detailed interpretation
if ks_p > 0.05:
    print("  ✓ Data appears normally distributed (KS test p>0.05)")
    print("  → Can safely use parametric tests (t-test, ANOVA, etc.)")
else:
    print("  ✗ Data deviates from normality (KS test p<0.05)")
    print("  → Consider:")
    print("    1. Transform data (log, square root)")
    print("    2. Use non-parametric tests")
    print("    3. Use robust statistics (median, IQR)")

print("\n=== SUMMARY ===")
print(f"""
Correlation Analysis:
- Age vs RT: r={r_pearson:.3f}, p={p_pearson:.4f} ({strength} {direction})
- Spearman ρ={rho_spearman:.3f} (similar to Pearson → linear relationship)

Distribution Fitting:
- RT data {'appears' if ks_p > 0.05 else 'does NOT appear'} normally distributed
- {'Normal' if ks_normal[0] < ks_lognorm[0] else 'Log-normal'} distribution provides better fit
- Use Q-Q plots for visual assessment of normality

Recommendations:
- {'Proceed with parametric tests' if ks_p > 0.05 else 'Consider non-parametric alternatives'}
- Report both Pearson and Spearman for correlations
- Always visualize distributions before analysis
""")
