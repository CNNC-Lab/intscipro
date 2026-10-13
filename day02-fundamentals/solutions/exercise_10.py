"""
Exercise 10: Function Analysis with Loops
Student: Solutions

Analyzing the function y = x² - 2x using numerical methods.
"""

print("=" * 60)
print("EXERCISE 10: Function Analysis")
print("=" * 60)

# Part a: Calculate and display function
print("\nPart a: Calculate and display y = x² - 2x")
print("-" * 60)

# Create x values from -5 to 5 in steps of 0.1.
# range() only works with integers, so loop over a counter and scale it.
start = -5.0
step = 0.1
n_points = 101

x_values = []
y_values = []
for i in range(n_points):
    x = round(start + i * step, 1)   # round() avoids 0.30000000000000004
    y = x**2 - 2*x
    x_values.append(x)
    y_values.append(y)

# Table (every 10th point)
print(f"{'x':>6} {'y':>10}")
for i in range(0, n_points, 10):
    print(f"{x_values[i]:6.1f} {y_values[i]:10.3f}")

# Text plot: one line per x, bar length proportional to y
print("\nText plot of y = x² - 2x (each '#' = 2 units, negative values shown with '-')")
for x, y in zip(x_values, y_values):
    if y >= 0:
        bar = "#" * int(y / 2)
    else:
        bar = "-" * int(-y * 4)      # y never goes below -1 here, so scale up
    print(f"{x:5.1f} | {bar}")

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
        roots.append((x_values[i], "negative to positive"))
        print(f"Root {len(roots)} at x ≈ {x_values[i]:.2f} (crossing from negative to positive)")
    elif (y_values[i-1] >= 0 and y_values[i] < 0):
        roots.append((x_values[i], "positive to negative"))
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

# Table with function and derivative side by side (every 10th point)
print(f"{'x':>6} {'y':>10} {'dy/dx':>10}")
for i in range(0, len(derivative), 10):
    print(f"{x_for_derivative[i]:6.1f} {y_values[i]:10.3f} {derivative[i]:10.3f}")

# Find where derivative crosses zero (critical points)
print("\nCritical points (where derivative = 0):")
for i in range(1, len(derivative)):
    if (derivative[i-1] < 0 and derivative[i] >= 0) or \
       (derivative[i-1] >= 0 and derivative[i] < 0):
        critical_x = x_for_derivative[i]
        critical_y = y_values[i]
        print(f"  Critical point at x ≈ {critical_x:.2f}, y ≈ {critical_y:.2f}")
        print(f"  This is a {'minimum' if derivative[i] > derivative[i-1] else 'maximum'}")

# Minimum and maximum of the function with a loop
min_y, min_x = y_values[0], x_values[0]
max_y, max_x = y_values[0], x_values[0]
for x, y in zip(x_values, y_values):
    if y < min_y:
        min_y, min_x = y, x
    if y > max_y:
        max_y, max_x = y, x
print(f"\nSmallest y on the grid: y({min_x:.1f}) = {min_y:.2f}")
print(f"Largest y on the grid:  y({max_x:.1f}) = {max_y:.2f}")

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
