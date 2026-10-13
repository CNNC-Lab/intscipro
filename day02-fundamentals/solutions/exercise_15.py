"""
Exercise 15: Riemann Sum Function
Student: Solutions

Building progressively sophisticated Riemann sum calculators.
"""

import math

print("=" * 60)
print("EXERCISE 15: Riemann Sum Function")
print("=" * 60)

# Part a: Basic Riemann Sum Function
print("\nPart a: Basic Riemann sum function")
print("-" * 60)

def riemann_sum_basic():
    """
    Calculate Riemann sum for exp(x) from 0 to 4.
    
    Returns:
    --------
    float
        Approximation of integral
    """
    a = 0.0
    b = 4.0
    step = 0.1
    
    # Calculate values
    n_rectangles = int(round((b - a) / step))
    
    # Calculate sum
    total = 0.0
    print("  Rectangles (every 4th shown, 1 '#' = 1 unit of height):")
    for i in range(n_rectangles):
        x = a + i * step
        y = math.exp(x)
        total += y * step
        
        # Text bar chart
        if i % 4 == 0:
            print(f"  x = {x:4.1f} {'#' * int(y)}")
    
    return total

result = riemann_sum_basic()
print(f"Riemann sum (0 to 4): {result:.6f}")
print(f"Analytical value: {math.exp(4) - math.exp(0):.6f}")

# Part b: Parameterized boundaries
print("\n" + "=" * 60)
print("Part b: Parameterized boundaries")
print("-" * 60)

def riemann_sum_bounds(a, b):
    """
    Calculate Riemann sum for exp(x) from a to b.
    
    Parameters:
    -----------
    a : float
        Lower bound of integration
    b : float
        Upper bound of integration
    
    Returns:
    --------
    float
        Approximation of integral
    """
    step = 0.1
    
    # Calculate values
    n_rectangles = int(round((b - a) / step))
    
    # Calculate sum
    total = sum(math.exp(a + i * step) * step for i in range(n_rectangles))
    
    return total

# Test with different bounds
test_cases = [(0, 4), (1, 3), (-1, 1), (0, 2)]
print("\nTesting different bounds:")
for a, b in test_cases:
    result = riemann_sum_bounds(a, b)
    analytical = math.exp(b) - math.exp(a)
    error = abs(result - analytical)
    print(f"  [{a:2}, {b:2}]: {result:8.4f} (error: {error:.6f})")

# Part c: Default step size
print("\n" + "=" * 60)
print("Part c: Default step size")
print("-" * 60)

def riemann_sum(a, b, step=0.1):
    """
    Calculate Riemann sum for exp(x) from a to b.
    
    Parameters:
    -----------
    a : float
        Lower bound of integration
    b : float
        Upper bound of integration
    step : float, optional
        Integration step size (default: 0.1)
    
    Returns:
    --------
    float
        Approximation of integral
    """
    # Calculate values
    n_rectangles = int(round((b - a) / step))
    
    # Calculate sum
    total = sum(math.exp(a + i * step) * step for i in range(n_rectangles))
    
    return total

# Test with different step sizes
print("\nEffect of step size on accuracy:")
print(f"{'Step':<10} {'Result':<12} {'Analytical':<12} {'Error':<12} {'Rectangles'}")
print("-" * 60)

a, b = 0, 4
analytical = math.exp(b) - math.exp(a)

for step in [1.0, 0.5, 0.1, 0.01]:
    result = riemann_sum(a, b, step)
    error = abs(result - analytical)
    n_rects = int((b - a) / step)
    print(f"{step:<10.2f} {result:<12.6f} {analytical:<12.6f} {error:<12.6f} {n_rects}")

print("\nConclusion: Smaller step size → more accurate, but more computations")

# Part d: Generic function integration
print("\n" + "=" * 60)
print("Part d: Generic function integration")
print("-" * 60)

def riemann_sum_generic(func, a, b, step=0.1, show_bars=False):
    """
    Calculate Riemann sum for any function.
    
    Parameters:
    -----------
    func : function
        Function to integrate (must accept single numeric argument)
    a : float
        Lower bound
    b : float
        Upper bound
    step : float, optional
        Step size (default: 0.1)
    show_bars : bool, optional
        Whether to print a text bar chart of the rectangles (default: False)
    
    Returns:
    --------
    float
        Approximation of integral
    """
    n_rectangles = int(round((b - a) / step))
    
    total = 0.0
    for i in range(n_rectangles):
        x = a + i * step
        y = func(x)
        total += y * step
        
        # Optional text bar chart (every 10th rectangle, bar length = height * 10)
        if show_bars and i % 10 == 0 and y > 0:
            print(f"  x = {x:5.2f} {'#' * int(y * 10)}")
    
    return total

# Define test functions
def quadratic(x):
    """Calculate x² - 2x"""
    return x**2 - 2*x

def exponential(x):
    """Calculate exp(x)"""
    return math.exp(x)

def gaussian(x):
    """Calculate Gaussian function"""
    return math.exp(-x**2)

# Test with different functions
print("\nTesting with different functions:")
print(f"{'Function':<20} {'Bounds':<12} {'Result':<15} {'Analytical (if known)'}")
print("-" * 70)

# Exponential
result = riemann_sum_generic(exponential, 0, 4, step=0.01)
analytical = math.exp(4) - math.exp(0)
print(f"{'exp(x)':<20} {'[0, 4]':<12} {result:<15.6f} {analytical:.6f}")

# Quadratic (∫(x²-2x)dx = x³/3 - x²)
result = riemann_sum_generic(quadratic, 0, 2, step=0.01)
analytical = (2**3/3 - 2**2) - (0**3/3 - 0**2)
print(f"{'x² - 2x':<20} {'[0, 2]':<12} {result:<15.6f} {analytical:.6f}")

# Sine
result = riemann_sum_generic(math.sin, 0, math.pi, step=0.01)
analytical = -math.cos(math.pi) - (-math.cos(0))  # = 2
print(f"{'sin(x)':<20} {'[0, π]':<12} {result:<15.6f} {analytical:.6f}")

# Gaussian (no simple analytical solution)
result = riemann_sum_generic(gaussian, -3, 3, step=0.01, show_bars=True)
print(f"{'exp(-x²)':<20} {'[-3, 3]':<12} {result:<15.6f} {'√π ≈ 1.772'}")


# Bonus: Comparison of step sizes against the exact value
print("\n" + "=" * 60)
print("BONUS: Convergence with decreasing step size")
print("-" * 60)

def compare_steps(func, a, b, exact, func_name="f(x)"):
    """Compare Riemann sums for several step sizes with the exact value."""
    print(f"\nFunction: {func_name}, bounds: [{a}, {b}], exact = {exact:.8f}")
    for step in [0.1, 0.01, 0.001]:
        riemann = riemann_sum_generic(func, a, b, step=step)
        print(f"  step={step:<6} sum={riemann:.8f}  error={abs(riemann - exact):.2e}")

compare_steps(math.exp, 0, 1, math.e - 1, "exp(x)")
compare_steps(lambda x: x**2, 0, 1, 1/3, "x²")
compare_steps(math.sin, 0, math.pi, 2.0, "sin(x)")

print("\n" + "=" * 60)
print("SUMMARY")
print("-" * 60)
print("""
Progressive function development:
  1. Start with hardcoded values
  2. Add parameters for flexibility
  3. Add default parameters for convenience
  4. Make it generic (accept functions as parameters)
  5. Add optional features (text output, verbosity)

This Riemann sum function can now integrate ANY function!
""")
