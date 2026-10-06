# Exercise 1.2: Array Attributes and Reshaping
import numpy as np

arr = np.arange(24)

# a) Array attributes
print("Shape:", arr.shape)        # (24,)
print("Size:", arr.size)          # 24
print("Dimensions:", arr.ndim)    # 1
print("Data type:", arr.dtype)    # int64

# b) Reshape to 4x6
arr_2d = arr.reshape(4, 6)
print("4x6 shape:", arr_2d.shape)

# c) Reshape to 2x3x4
arr_3d = arr.reshape(2, 3, 4)
print("3D shape:", arr_3d.shape)

# d) Flatten back to 1D
flat1 = arr_3d.flatten()  # Creates copy
flat2 = arr_3d.ravel()    # Returns view when possible
print("Flattened:", flat1.shape, flat2.shape)

# e) Auto-calculate columns
arr_auto = arr.reshape(3, -1)  # -1 means "calculate this dimension"
print("3x? shape:", arr_auto.shape)  # (3, 8)

# f) Transpose
matrix = np.arange(12).reshape(3, 4)
print("Original shape:", matrix.shape)   # (3, 4)
transposed = matrix.T
print("Transposed shape:", transposed.shape)  # (4, 3)
