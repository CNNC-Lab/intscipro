import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Linear Algebra (numpy.linalg)
# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Determinant
det_A = np.linalg.det(A)

# Matrix inverse
A_inv = np.linalg.inv(A)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
# This matrix has real eigenvalues; recent NumPy versions may return a complex dtype
eigenvalues, eigenvectors = np.real_if_close(eigenvalues), np.real_if_close(eigenvectors)

# Solve linear system Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)

# Singular Value Decomposition (SVD)
U, s, Vt = np.linalg.svd(A)

# Matrix rank
rank = np.linalg.matrix_rank(A)

# Norm of a vector/matrix
norm = np.linalg.norm(A)

# ============================================================================
# VISUALIZATIONS
# ============================================================================

# Figure 1: Matrix Heatmaps
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

matrices = [A, A_inv, A @ B]
titles = [f'Matrix A\ndet={det_A:.2f}', f'Inverse A⁻¹\n(A·A⁻¹=I)', 'Product A·B']

for ax, mat, title in zip(axes, matrices, titles):
    im = ax.imshow(mat, cmap='RdBu_r', aspect='auto')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    
    # Annotate values
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, f'{mat[i, j]:.2f}', ha='center', va='center', 
                   color='white' if abs(mat[i, j]) > mat.max()/2 else 'black',
                   fontsize=11, fontweight='bold')
    
    cbar = plt.colorbar(im, ax=ax)

plt.tight_layout()
plt.savefig('06_matrix_operations.png', dpi=300, bbox_inches='tight')
plt.close()
print('Saved: 06_matrix_operations.png')

# Figure 2: Eigenvector Visualization
fig, ax = plt.subplots(figsize=(8, 8))

# Plot eigenvectors before and after transformation
colors = ['red', 'blue']
for i in range(2):
    v = eigenvectors[:, i]
    v_transformed = A @ v
    
    # Original eigenvector
    ax.arrow(0, 0, v[0], v[1], head_width=0.15, head_length=0.15, 
             fc=colors[i], ec=colors[i], alpha=0.5, linewidth=2,
             label=f'v{i+1}')
    
    # Transformed eigenvector (should be scaled by eigenvalue)
    ax.arrow(0, 0, v_transformed[0], v_transformed[1], 
             head_width=0.15, head_length=0.15,
             fc=colors[i], ec=colors[i], linewidth=3, linestyle='--',
             label=f'A·v{i+1} (λ={eigenvalues[i]:.2f})')

# Plot some other vectors to show general transformation
test_vectors = np.array([[1, 0], [0, 1], [1, 1], [-1, 1]]).T
for i in range(test_vectors.shape[1]):
    v = test_vectors[:, i]
    v_transformed = A @ v
    ax.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1,
             fc='gray', ec='gray', alpha=0.3, linewidth=1)
    ax.arrow(0, 0, v_transformed[0], v_transformed[1], head_width=0.1, head_length=0.1,
             fc='black', ec='black', alpha=0.3, linewidth=1, linestyle=':')

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Eigenvectors and Matrix Transformation\n(Solid=original, Dashed=transformed)', 
             fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=9)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('07_eigenvectors.png', dpi=300, bbox_inches='tight')
plt.close()
print('Saved: 07_eigenvectors.png')

# Figure 3: Linear System Solution Ax = b
fig, ax = plt.subplots(figsize=(8, 8))

# The system Ax = b represents two equations:
# 1*x1 + 2*x2 = 1
# 3*x1 + 4*x2 = 2

# Plot the lines
x1_range = np.linspace(-2, 2, 100)

# Line 1: x2 = (1 - 1*x1) / 2
x2_line1 = (b[0] - A[0, 0] * x1_range) / A[0, 1]

# Line 2: x2 = (2 - 3*x1) / 4
x2_line2 = (b[1] - A[1, 0] * x1_range) / A[1, 1]

ax.plot(x1_range, x2_line1, 'b-', linewidth=2, label=f'{A[0,0]}x₁ + {A[0,1]}x₂ = {b[0]}')
ax.plot(x1_range, x2_line2, 'r-', linewidth=2, label=f'{A[1,0]}x₁ + {A[1,1]}x₂ = {b[1]}')

# Plot the solution
ax.plot(x[0], x[1], 'go', markersize=15, label=f'Solution x=({x[0]:.2f}, {x[1]:.2f})', 
        zorder=5)
ax.plot(x[0], x[1], 'g*', markersize=20, zorder=6)

ax.set_xlim(-1, 1.5)
ax.set_ylim(-1, 1.5)
ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xlabel('x₁', fontsize=12)
ax.set_ylabel('x₂', fontsize=12)
ax.set_title('Linear System Solution: Ax = b\n(Intersection of two lines)', 
             fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('08_linear_system.png', dpi=300, bbox_inches='tight')
plt.close()
print('Saved: 08_linear_system.png')

# Figure 4: SVD Decomposition
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

# Create diagonal matrix from singular values
S = np.zeros_like(A)
S[:len(s), :len(s)] = np.diag(s)

svd_matrices = [A, U, S, Vt]
svd_titles = ['A (original)', 'U (left singular)', 'Σ (singular values)', 'Vᵀ (right singular)']
svd_subtitles = ['', f'orthogonal\n(UᵀU=I)', f's=[{s[0]:.2f}, {s[1]:.2f}]', 'orthogonal\n(VVᵀ=I)']

for ax, mat, title, subtitle in zip(axes, svd_matrices, svd_titles, svd_subtitles):
    im = ax.imshow(mat, cmap='RdBu_r', aspect='auto', vmin=-8, vmax=8)
    ax.set_title(f'{title}\n{subtitle}', fontsize=11, fontweight='bold')
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    
    # Annotate values
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, f'{mat[i, j]:.2f}', ha='center', va='center',
                   color='white' if abs(mat[i, j]) > 4 else 'black',
                   fontsize=10, fontweight='bold')
    
    cbar = plt.colorbar(im, ax=ax)

fig.suptitle('Singular Value Decomposition: A = U·Σ·Vᵀ', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('09_svd_decomposition.png', dpi=300, bbox_inches='tight')
plt.close()
print('Saved: 09_svd_decomposition.png')

# Figure 5: Grid Transformation
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Create a grid
grid_range = np.linspace(-2, 2, 9)
grid_points = []

# Vertical lines
for x in grid_range:
    y_vals = grid_range
    points = np.array([[x] * len(y_vals), y_vals])
    grid_points.append(points)

# Horizontal lines
for y in grid_range:
    x_vals = grid_range
    points = np.array([x_vals, [y] * len(x_vals)])
    grid_points.append(points)

# Plot original grid
for points in grid_points:
    axes[0].plot(points[0], points[1], 'b-', linewidth=1, alpha=0.6)

axes[0].set_xlim(-3, 3)
axes[0].set_ylim(-3, 3)
axes[0].axhline(y=0, color='k', linewidth=1)
axes[0].axvline(x=0, color='k', linewidth=1)
axes[0].grid(True, alpha=0.3, linestyle='--')
axes[0].set_xlabel('x', fontsize=12)
axes[0].set_ylabel('y', fontsize=12)
axes[0].set_title('Original Grid', fontsize=13, fontweight='bold')
axes[0].set_aspect('equal')

# Plot transformed grid
for points in grid_points:
    transformed = A @ points
    axes[1].plot(transformed[0], transformed[1], 'r-', linewidth=1, alpha=0.6)

axes[1].set_xlim(-10, 10)
axes[1].set_ylim(-10, 10)
axes[1].axhline(y=0, color='k', linewidth=1)
axes[1].axvline(x=0, color='k', linewidth=1)
axes[1].grid(True, alpha=0.3, linestyle='--')
axes[1].set_xlabel('x', fontsize=12)
axes[1].set_ylabel('y', fontsize=12)
axes[1].set_title(f'Transformed Grid (by matrix A)\ndet(A)={det_A:.2f}', 
                  fontsize=13, fontweight='bold')
axes[1].set_aspect('equal')

fig.suptitle('Linear Transformation: How Matrix A Transforms Space', 
             fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('10_grid_transformation.png', dpi=300, bbox_inches='tight')
plt.close()
print('Saved: 10_grid_transformation.png')

print(f'\nSummary:')
print(f'  Matrix A determinant: {det_A:.2f}')
print(f'  Matrix rank: {rank}')
print(f'  Matrix norm: {norm:.2f}')
print(f'  Eigenvalues: {eigenvalues}')
print(f'  Singular values: {s}')
print(f'  Solution to Ax=b: x = {x}')
