# Exercise 2.1: Statistical Operations
import numpy as np

np.random.seed(42)
data = np.random.normal(100, 15, (50, 4))

# a) Overall statistics
print("Mean:", data.mean())
print("Median:", np.median(data))
print("Std:", data.std())
print("Variance:", data.var())

# b) Column means
col_means = data.mean(axis=0)
print("Column means:", col_means)

# c) Row standard deviations
row_stds = data.std(axis=1)
print("Row stds (first 5):", row_stds[:5])

# d) Min/max and positions
print("Min:", data.min())
print("Max:", data.max())
print("Min position:", np.unravel_index(data.argmin(), data.shape))
print("Max position:", np.unravel_index(data.argmax(), data.shape))

# e) Percentiles per column
percentiles = [25, 50, 75]
for p in percentiles:
    values = np.percentile(data, p, axis=0)
    print(f"{p}th percentile:", values)

# f) Count values > 100 per column
counts = np.sum(data > 100, axis=0)
print("Counts > 100:", counts)

# g) Correlation between columns 0 and 1
col0 = data[:, 0]
col1 = data[:, 1]
correlation = np.corrcoef(col0, col1)[0, 1]
print(f"Correlation: {correlation:.3f}")
