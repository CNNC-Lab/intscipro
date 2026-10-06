# Exercise 1.4: Array Operations and Broadcasting
import numpy as np

# a) Element-wise operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print("Sum:", a + b)        # [ 6  6  6  6  6]
print("Difference:", a - b) # [-4 -2  0  2  4]
print("Product:", a * b)    # [5 8 9 8 5]

# b) Sum of squares
result = a**2 + b**2
print("a² + b²:", result)   # [26 20 18 20 26]

# c) Mathematical functions
print("sqrt(a):", np.sqrt(a))  # [1.   1.41 1.73 2.   2.24]
print("exp(a):", np.exp(a))    # [  2.72   7.39  20.09  54.60 148.41]
print("log(a):", np.log(a))    # [0.   0.69 1.10 1.39 1.61]

# d) Broadcasting with scalar
matrix = np.arange(12).reshape(4, 3)
result = matrix + 10
print("Matrix + 10:\n", result)

# e) Subtract column means
matrix = np.arange(12).reshape(3, 4)
col_means = matrix.mean(axis=0)  # Mean of each column
centered = matrix - col_means    # Broadcasting
print("Original:\n", matrix)
print("Column means:", col_means)
print("Centered:\n", centered)

# f) Normalize rows
matrix = np.random.randn(4, 5)
row_means = matrix.mean(axis=1, keepdims=True)  # Shape: (4, 1)
row_stds = matrix.std(axis=1, keepdims=True)    # Shape: (4, 1)
normalized = (matrix - row_means) / row_stds
print("Normalized row means:", normalized.mean(axis=1))  # ~[0 0 0 0]
print("Normalized row stds:", normalized.std(axis=1))    # ~[1 1 1 1]

# g) 1D + 2D broadcasting
a = np.array([1, 2, 3])      # Shape: (3,)
b = np.array([[10],
              [20],
              [30]])         # Shape: (3, 1)

result = a + b
print("Broadcasting result:\n", result)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]
# Each row of b is added to a
