"""
Exercise 11: Area Under a Curve (Riemann Sum)
Student: Solutions

Approximating integrals using the Riemann sum method.
"""

import math

print("=" * 60)
print("EXERCISE 11: Riemann Sum Integration")
print("=" * 60)

# Part a: Visualizing the Riemann Sum
print("\nPart a: Visualizing rectangles under exp(x)")
print("-" * 60)

# Parameters (a coarse step keeps the text picture readable)
a = 0.0
b = 4.0
step = 0.5
n_rectangles = int((b - a) / step)

print(f"{'x':>5} {'height':>9} {'area':>8}  rectangle (1 '#' = 1 unit of height)")
for i in range(n_rectangles):
    x = a + i * step
    height = math.exp(x)
    area = height * step
    print(f"{x:5.1f} {height:9.3f} {area:8.3f}  {'#' * int(height)}")

# Part b: Calculating the total area
print("\n" + "=" * 60)
print("Part b: Calculating total area")
print("-" * 60)

step = 0.1
n_rectangles = int(round((b - a) / step))

total_area = 0
for i in range(n_rectangles):
    x = a + i * step
    y = math.exp(x)
    rectangle_area = y * step
    total_area += rectangle_area

print(f"Sum of rectangle areas: {total_area:.6f}")

# Analytical solution for comparison
analytical = math.exp(b) - math.exp(a)
print(f"Analytical solution: ∫₀⁴ exp(x)dx = exp(4) - exp(0) = {analytical:.6f}")
print(f"Error: {abs(total_area - analytical):.6f}")
print(f"Relative error: {abs(total_area - analytical)/analytical * 100:.4f}%")

# Extension: left, right and midpoint rules for increasing numbers of rectangles
print("\nLeft / right / midpoint rules for increasing numbers of rectangles:")
print(f"{'n':>7} {'rule':<9} {'approximation':>14} {'exact':>12} {'error':>12}")
for n in [10, 100, 1000, 10000]:
    width = (b - a) / n
    for rule, offset in [("left", 0.0), ("right", 1.0), ("midpoint", 0.5)]:
        approx = 0.0
        for i in range(n):
            approx += math.exp(a + (i + offset) * width) * width
        print(f"{n:7d} {rule:<9} {approx:14.6f} {analytical:12.6f} {abs(approx - analytical):12.6f}")
print("The error shrinks roughly like 1/n for left/right and like 1/n² for midpoint.")

# Part c: Finding the upper limit
print("\n" + "=" * 60)
print("Part c: Finding upper limit where area = 25")
print("-" * 60)

target_area = 25.0
total_area = 0
x = 0.0

while total_area < target_area:
    y = math.exp(x)
    total_area += y * step
    x += step

print(f"Upper limit found: x ≈ {x:.2f}")
print(f"Total area: {total_area:.6f}")

# Analytical solution: ∫₀ᵃ exp(x)dx = 25
# exp(a) - 1 = 25 → exp(a) = 26 → a = ln(26)
analytical_limit = math.log(26)
print(f"Analytical solution: a = ln(26) ≈ {analytical_limit:.6f}")
print(f"Error: {abs(x - analytical_limit):.6f}")

# Part d: Alternative implementations
print("\n" + "=" * 60)
print("Part d: Alternative implementations")
print("-" * 60)

# Part b with while-loop
print("\nPart b using while-loop:")
total_area = 0
i = 0
while i < n_rectangles:
    y = math.exp(a + i * step)
    total_area += y * step
    i += 1
print(f"Total area: {total_area:.6f}")

# Part c with for-loop and break
print("\nPart c using for-loop with break:")
target_area = 25.0
total_area = 0
max_steps = 100  # Safety limit: at most 100 steps of 0.1 (x up to 10)

for i in range(max_steps):
    x = i * step
    y = math.exp(x)
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
