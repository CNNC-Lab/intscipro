"""
Exercise 11: Area Under a Curve (Riemann Sum)
Student: Solutions

Approximating integrals using the Riemann sum method.
"""

import os
os.makedirs("outputs", exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("EXERCISE 11: Riemann Sum Integration")
print("=" * 60)

# Part a: Visualizing the Riemann Sum
print("\nPart a: Visualizing rectangles under exp(x)")
print("-" * 60)

# Parameters
a = 0.0
b = 4.0
step = 0.1

# Generate x values and calculate y = exp(x)
x_values = np.arange(a, b, step)
y_values = np.exp(x_values)

# Create plot
plt.figure(figsize=(10, 6))

# Plot the curve
x_smooth = np.linspace(a, b, 1000)
y_smooth = np.exp(x_smooth)
plt.plot(x_smooth, y_smooth, 'b-', linewidth=2, label='y = exp(x)')

# Plot the rectangles
plt.bar(x_values, y_values, width=step, align='edge', 
        alpha=0.5, edgecolor='black', label='Riemann rectangles')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Riemann Sum Approximation of ∫exp(x)dx from 0 to 4')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('outputs/ex11_part_a.png', dpi=150, bbox_inches='tight')
plt.close()
print("Visualization saved as ex11_part_a.png")

# Part b: Calculating the total area
print("\n" + "=" * 60)
print("Part b: Calculating total area")
print("-" * 60)

total_area = 0
for i, x in enumerate(x_values):
    y = y_values[i]
    rectangle_area = y * step
    total_area += rectangle_area

print(f"Sum of rectangle areas: {total_area:.6f}")

# Analytical solution for comparison
analytical = np.exp(b) - np.exp(a)
print(f"Analytical solution: ∫₀⁴ exp(x)dx = exp(4) - exp(0) = {analytical:.6f}")
print(f"Error: {abs(total_area - analytical):.6f}")
print(f"Relative error: {abs(total_area - analytical)/analytical * 100:.4f}%")

# Part c: Finding the upper limit
print("\n" + "=" * 60)
print("Part c: Finding upper limit where area = 25")
print("-" * 60)

target_area = 25.0
total_area = 0
x = 0.0

# Store values for plotting
x_list = []
y_list = []

while total_area < target_area:
    y = np.exp(x)
    x_list.append(x)
    y_list.append(y)
    total_area += y * step
    x += step

print(f"Upper limit found: x ≈ {x:.2f}")
print(f"Total area: {total_area:.6f}")

# Analytical solution: ∫₀ᵃ exp(x)dx = 25
# exp(a) - 1 = 25 → exp(a) = 26 → a = ln(26)
analytical_limit = np.log(26)
print(f"Analytical solution: a = ln(26) ≈ {analytical_limit:.6f}")
print(f"Error: {abs(x - analytical_limit):.6f}")

# Visualize result
plt.figure(figsize=(10, 6))
x_smooth = np.linspace(0, x, 1000)
y_smooth = np.exp(x_smooth)
plt.plot(x_smooth, y_smooth, 'b-', linewidth=2, label='y = exp(x)')
plt.bar(x_list, y_list, width=step, align='edge', 
        alpha=0.5, edgecolor='black', label='Rectangles')
plt.axvline(x=x, color='r', linestyle='--', linewidth=2, label=f'Upper limit: x ≈ {x:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Riemann Sum ≈ {target_area} (Area under exp(x))')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('outputs/ex11_part_c.png', dpi=150, bbox_inches='tight')
plt.close()
print("Visualization saved as ex11_part_c.png")

# Part d: Alternative implementations
print("\n" + "=" * 60)
print("Part d: Alternative implementations")
print("-" * 60)

# Part b with while-loop
print("\nPart b using while-loop:")
total_area = 0
i = 0
x_values_b = np.arange(a, b, step)
while i < len(x_values_b):
    y = np.exp(x_values_b[i])
    total_area += y * step
    i += 1
print(f"Total area: {total_area:.6f}")

# Part c with for-loop and break
print("\nPart c using for-loop with break:")
target_area = 25.0
total_area = 0
max_x = 10.0  # Upper limit for range
x_values_c = np.arange(0.0, max_x, step)

for x in x_values_c:
    y = np.exp(x)
    total_area += y * step
    if total_area >= target_area:
        print(f"Upper limit found: x ≈ {x:.2f}")
        print(f"Total area: {total_area:.6f}")
        break

print("\n" + "=" * 60)
print("Discussion: Which is more natural?")
print("-" * 60)
print("Part b (calculating fixed area):")
print("  - for-loop is more natural")
print("  - We know the range (0 to 4)")
print("  - Simple iteration over known values")
print("\nPart c (finding threshold):")
print("  - while-loop is more natural")
print("  - We don't know how many iterations needed")
print("  - Condition-based termination")
print("  - Could use for-loop with break, but while is clearer")

# Summary
print("\n" + "=" * 60)
print("WHAT DID WE JUST DO?")
print("=" * 60)
print("We approximated the integral using Riemann sums:")
print()
print("  ∫₀ᵃ exp(x) dx ≈ Σ exp(xᵢ) Δx")
print()
print("where:")
print("  - Δx = 0.1 (step size)")
print("  - xᵢ are sample points")
print("  - Each term exp(xᵢ)Δx is the area of one rectangle")
print()
print("Part b: We calculated ∫₀⁴ exp(x) dx")
print("Part c: We found 'a' such that ∫₀ᵃ exp(x) dx = 25")
print()
print("This is a fundamental technique in numerical analysis!")
print("Used when:")
print("  - Analytical integration is difficult/impossible")
print("  - Working with experimental data")
print("  - Solving differential equations numerically")
