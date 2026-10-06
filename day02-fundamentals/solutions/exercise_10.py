"""
Exercise 10: Function Analysis with Loops
Student: Solutions

Analyzing the function y = x² - 2x using numerical methods.
"""

import os
os.makedirs("outputs", exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("EXERCISE 10: Function Analysis")
print("=" * 60)

# Part a: Calculate and display function
print("\nPart a: Calculate and display y = x² - 2x")
print("-" * 60)

# Create x values from -5 to 5 in steps of 0.1
x_values = np.arange(-5.0, 5.1, 0.1)

# Calculate y values
y_values = []
for x in x_values:
    y = x**2 - 2*x
    y_values.append(y)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'b-', linewidth=2, label='y = x² - 2x')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Plot: y = x² - 2x')
plt.legend()
plt.savefig('outputs/ex10_part_a.png', dpi=150, bbox_inches='tight')
plt.close()
print("Plot saved as ex10_part_a.png")

# Part b: Finding first root
print("\n" + "=" * 60)
print("Part b: Finding the first root")
print("-" * 60)

for i in range(1, len(y_values)):
    # Check if sign changes (indicating a root)
    if (y_values[i-1] < 0 and y_values[i] >= 0) or \
       (y_values[i-1] >= 0 and y_values[i] < 0):
        root_x = x_values[i]
        print(f"First root found at x ≈ {root_x:.2f}")
        print(f"  y({x_values[i-1]:.2f}) = {y_values[i-1]:.4f}")
        print(f"  y({x_values[i]:.2f}) = {y_values[i]:.4f}")
        break

# Part c: Finding all roots
print("\n" + "=" * 60)
print("Part c: Finding all roots")
print("-" * 60)

roots = []
for i in range(1, len(y_values)):
    if (y_values[i-1] < 0 and y_values[i] >= 0):
        roots.append((x_values[i], "positive to zero"))
        print(f"Root {len(roots)} at x ≈ {x_values[i]:.2f} (crossing from negative to positive)")
    elif (y_values[i-1] >= 0 and y_values[i] < 0):
        roots.append((x_values[i], "negative to zero"))
        print(f"Root {len(roots)} at x ≈ {x_values[i]:.2f} (crossing from positive to negative)")

print(f"\nTotal roots found: {len(roots)}")
print("Analytical roots: x = 0 and x = 2")

# Part d: Calculating the derivative
print("\n" + "=" * 60)
print("Part d: Calculating the derivative")
print("-" * 60)

# Derivative approximation: dy/dx ≈ (y[i+1] - y[i]) / (x[i+1] - x[i])
derivative = []
for i in range(len(y_values) - 1):
    dy = y_values[i+1] - y_values[i]
    dx = x_values[i+1] - x_values[i]
    derivative.append(dy / dx)

# Note: derivative has one fewer element, so we use x_values[:-1]
x_for_derivative = x_values[:-1]

# Find where derivative crosses zero (critical points)
print("\nCritical points (where derivative = 0):")
for i in range(1, len(derivative)):
    if (derivative[i-1] < 0 and derivative[i] >= 0) or \
       (derivative[i-1] >= 0 and derivative[i] < 0):
        critical_x = x_for_derivative[i]
        critical_y = y_values[i]
        print(f"  Critical point at x ≈ {critical_x:.2f}, y ≈ {critical_y:.2f}")
        print(f"  This is a {'minimum' if derivative[i] > derivative[i-1] else 'maximum'}")

# Plot function and derivative together
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, 'b-', linewidth=2, label='y = x² - 2x')
plt.plot(x_for_derivative, derivative, 'r-', linewidth=2, label="y' = 2x - 2")
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

# Mark roots
for root_x, _ in roots:
    plt.plot(root_x, 0, 'go', markersize=10, label='Root' if roots.index((root_x, _)) == 0 else '')

# Mark critical point
plt.plot(1, -1, 'rs', markersize=10, label='Critical Point')

plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and its Derivative')
plt.legend()
plt.savefig('outputs/ex10_all_parts.png', dpi=150, bbox_inches='tight')
plt.close()
print("\nCombined plot saved as ex10_all_parts.png")

# Analytical verification
print("\n" + "=" * 60)
print("Analytical Verification")
print("-" * 60)
print("Function: y = x² - 2x")
print("Derivative: dy/dx = 2x - 2")
print("Roots (y = 0): x² - 2x = 0 → x(x - 2) = 0 → x = 0 or x = 2")
print("Critical point (dy/dx = 0): 2x - 2 = 0 → x = 1")
print("At x = 1: y = 1² - 2(1) = -1 (minimum)")

print("\n" + "=" * 60)
print("What we observed:")
print("-" * 60)
print("- The derivative crosses zero where the function has a minimum")
print("- The derivative is negative where the function is decreasing")
print("- The derivative is positive where the function is increasing")
print("- The derivative is a straight line (2x - 2) for this quadratic")
