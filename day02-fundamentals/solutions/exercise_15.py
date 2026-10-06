"""
Exercise 15: Riemann Sum Function
Student: Solutions

Building progressively sophisticated Riemann sum calculators.
"""

import os
os.makedirs("outputs", exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt

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
    x_values = np.arange(a, b, step)
    y_values = np.exp(x_values)
    
    # Calculate sum
    total = 0.0
    for y in y_values:
        total += y * step
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, width=step, alpha=0.5, 
            edgecolor='black', label='Riemann rectangles')
    x_smooth = np.linspace(a, b, 1000)
    plt.plot(x_smooth, np.exp(x_smooth), 'b-', linewidth=2, label='y = exp(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Riemann Sum ≈ {total:.4f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/ex15_basic.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return total

result = riemann_sum_basic()
print(f"Riemann sum (0 to 4): {result:.6f}")
print(f"Analytical value: {np.exp(4) - np.exp(0):.6f}")
print("Plot saved as ex15_basic.png")

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
    x_values = np.arange(a, b, step)
    y_values = np.exp(x_values)
    
    # Calculate sum
    total = sum(y * step for y in y_values)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, width=step, alpha=0.5, 
            edgecolor='black', label='Riemann rectangles')
    x_smooth = np.linspace(a, b, 1000)
    plt.plot(x_smooth, np.exp(x_smooth), 'b-', linewidth=2, label='y = exp(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Riemann Sum from {a} to {b} ≈ {total:.4f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('outputs/ex15_bounds.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return total

# Test with different bounds
test_cases = [(0, 4), (1, 3), (-1, 1), (0, 2)]
print("\nTesting different bounds:")
for a, b in test_cases:
    result = riemann_sum_bounds(a, b)
    analytical = np.exp(b) - np.exp(a)
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
    x_values = np.arange(a, b, step)
    y_values = np.exp(x_values)
    
    # Calculate sum
    total = sum(y * step for y in y_values)
    
    return total

# Test with different step sizes
print("\nEffect of step size on accuracy:")
print(f"{'Step':<10} {'Result':<12} {'Analytical':<12} {'Error':<12} {'Rectangles'}")
print("-" * 60)

a, b = 0, 4
analytical = np.exp(b) - np.exp(a)

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

def riemann_sum_generic(func, a, b, step=0.1, plot=False):
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
    plot : bool, optional
        Whether to create a plot (default: False)
    
    Returns:
    --------
    float
        Approximation of integral
    """
    # Generate points
    x_values = np.arange(a, b, step)
    y_values = np.array([func(x) for x in x_values])
    
    # Calculate sum
    total = sum(y * step for y in y_values)
    
    # Optional plotting
    if plot:
        plt.figure(figsize=(10, 6))
        plt.bar(x_values, y_values, width=step, alpha=0.5, 
                edgecolor='black', label='Riemann rectangles')
        x_smooth = np.linspace(a, b, 1000)
        y_smooth = np.array([func(x) for x in x_smooth])
        plt.plot(x_smooth, y_smooth, 'b-', linewidth=2, 
                 label=f'{func.__name__}(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Riemann Sum ≈ {total:.4f}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('outputs/ex15_generic.png', dpi=150, bbox_inches='tight')
        plt.close()
    
    return total

# Define test functions
def quadratic(x):
    """Calculate x² - 2x"""
    return x**2 - 2*x

def exponential(x):
    """Calculate exp(x)"""
    return np.exp(x)

def gaussian(x):
    """Calculate Gaussian function"""
    return np.exp(-x**2)

# Test with different functions
print("\nTesting with different functions:")
print(f"{'Function':<20} {'Bounds':<12} {'Result':<15} {'Analytical (if known)'}")
print("-" * 70)

# Exponential
result = riemann_sum_generic(exponential, 0, 4, step=0.01)
analytical = np.exp(4) - np.exp(0)
print(f"{'exp(x)':<20} {'[0, 4]':<12} {result:<15.6f} {analytical:.6f}")

# Quadratic (∫(x²-2x)dx = x³/3 - x²)
result = riemann_sum_generic(quadratic, 0, 2, step=0.01)
analytical = (2**3/3 - 2**2) - (0**3/3 - 0**2)
print(f"{'x² - 2x':<20} {'[0, 2]':<12} {result:<15.6f} {analytical:.6f}")

# Sine
result = riemann_sum_generic(np.sin, 0, np.pi, step=0.01)
analytical = -np.cos(np.pi) - (-np.cos(0))  # = 2
print(f"{'sin(x)':<20} {'[0, π]':<12} {result:<15.6f} {analytical:.6f}")

# Gaussian (no simple analytical solution)
result = riemann_sum_generic(gaussian, -3, 3, step=0.01, plot=True)
print(f"{'exp(-x²)':<20} {'[-3, 3]':<12} {result:<15.6f} {'√π ≈ 1.772'}")

print("\nPlot saved as ex15_generic.png")

# Bonus: Comparison of integration methods
print("\n" + "=" * 60)
print("BONUS: Comparison with scipy.integrate")
print("-" * 60)

from scipy import integrate

def compare_methods(func, a, b, func_name="f(x)"):
    """Compare Riemann sum with scipy integration."""
    # Riemann sum
    riemann = riemann_sum_generic(func, a, b, step=0.01)
    
    # Scipy integration
    scipy_result, error = integrate.quad(func, a, b)
    
    # Compare
    difference = abs(riemann - scipy_result)
    
    print(f"\nFunction: {func_name}, bounds: [{a}, {b}]")
    print(f"  Riemann sum (step=0.01): {riemann:.8f}")
    print(f"  scipy.integrate.quad:    {scipy_result:.8f}")
    print(f"  Difference:              {difference:.8e}")
    print(f"  Scipy estimated error:   {error:.8e}")

compare_methods(np.exp, 0, 1, "exp(x)")
compare_methods(lambda x: x**2, 0, 1, "x²")
compare_methods(np.sin, 0, np.pi, "sin(x)")

print("\n" + "=" * 60)
print("SUMMARY")
print("-" * 60)
print("""
Progressive function development:
  1. Start with hardcoded values
  2. Add parameters for flexibility
  3. Add default parameters for convenience
  4. Make it generic (accept functions as parameters)
  5. Add optional features (plotting, verbosity)

This Riemann sum function can now integrate ANY function!
""")
