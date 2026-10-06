# Exercise 2.2: Linear Algebra
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# a) Element-wise multiplication
elem_mult = A * B
print("Element-wise:\n", elem_mult)

# b) Matrix multiplication
matrix_mult = A @ B
print("Matrix multiplication:\n", matrix_mult)

# c) Transpose
A_T = A.T
print("Transpose:\n", A_T)

# d) Non-singular matrix and inverse
C = np.array([[1, 2],
              [3, 4]])
C_inv = np.linalg.inv(C)
print("C:\n", C)
print("C inverse:\n", C_inv)

# e) Verify A × A⁻¹ = I
identity = C @ C_inv
print("C × C⁻¹:\n", identity)
print("Is identity?", np.allclose(identity, np.eye(2)))

# f) Determinant
det_A = np.linalg.det(A)
print("det(A):", det_A)  # Should be ~0 (singular)

det_C = np.linalg.det(C)
print("det(C):", det_C)  # Should be -2

# g) Solve linear system
# 2x + 3y = 8
# 4x -  y = 2
coefficients = np.array([[2, 3],
                         [4, -1]])
constants = np.array([8, 2])
solution = np.linalg.solve(coefficients, constants)
print("Solution: x =", solution[0], ", y =", solution[1])

# Verify
print("Verification:", coefficients @ solution)
print("Should equal:", constants)
