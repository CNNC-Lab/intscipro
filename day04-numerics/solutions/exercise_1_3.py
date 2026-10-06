# Exercise 1.3: Indexing and Slicing
import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

arr_2d = np.array([[1,  2,  3,  4,  5],
                   [6,  7,  8,  9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

# a) Last element
print("Last:", arr_1d[-1])  # 100

# b) Multiple indices (fancy indexing)
print("Indices 2,4,7:", arr_1d[[2, 4, 7]])  # [30 50 80]

# c) Every third
print("Every 3rd:", arr_1d[::3])  # [10 40 70 100]

# d) First two rows
print("First 2 rows:\n", arr_2d[:2])

# e) Last column
print("Last column:", arr_2d[:, -1])  # [ 5 10 15 20]

# f) Subarray rows 1-2, columns 2-4
print("Subarray:\n", arr_2d[1:3, 2:5])
# [[ 8  9 10]
#  [13 14 15]]

# g) Boolean indexing (values > 10)
print("Values > 10:", arr_2d[arr_2d > 10])
# [11 12 13 14 15 16 17 18 19 20]

# h) Replace values > 50 with 50
arr_1d[arr_1d > 50] = 50
print("Clipped:", arr_1d)  # [10 20 30 40 50 50 50 50 50 50]
