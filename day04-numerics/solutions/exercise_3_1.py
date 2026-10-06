# Exercise 3.1: Statistical Analysis
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
group1 = np.random.normal(100, 15, 30)
group2 = np.random.normal(110, 15, 30)

# a) Descriptive statistics
desc1 = stats.describe(group1)
desc2 = stats.describe(group2)
print("Group 1:", desc1)
print("Group 2:", desc2)

# b) T-test
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"\nT-test: t={t_stat:.3f}, p={p_value:.3f}")
if p_value < 0.05:
    print("Groups are significantly different")
else:
    print("No significant difference")

# c) Normality test
stat, p = stats.shapiro(group1)
print(f"\nShapiro-Wilk: W={stat:.3f}, p={p:.3f}")
if p > 0.05:
    print("Data appears normally distributed")

# d) Correlation
r, p = stats.pearsonr(group1, group2)
print(f"\nCorrelation: r={r:.3f}, p={p:.3f}")

# e) Theoretical PDF
x = np.linspace(40, 160, 200)
pdf = stats.norm.pdf(x, loc=100, scale=15)

# f) Histogram with theoretical PDF
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(group1, bins=15, density=True, alpha=0.7, label='Data')
plt.plot(x, pdf, 'r-', linewidth=2, label='Theoretical')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Group 1 vs Theoretical Distribution')
plt.legend()

# g) CDF calculation
prob_below_85 = stats.norm.cdf(85, loc=100, scale=15)
print(f"\nP(X < 85) = {prob_below_85:.3f} ({prob_below_85*100:.1f}%)")

# Bonus: Show CDF
plt.subplot(1, 2, 2)
cdf = stats.norm.cdf(x, loc=100, scale=15)
plt.plot(x, cdf, 'b-', linewidth=2)
plt.axvline(85, color='r', linestyle='--', label='x=85')
plt.axhline(prob_below_85, color='r', linestyle='--', 
            label=f'P={prob_below_85:.3f}')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
