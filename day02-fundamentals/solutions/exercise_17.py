"""
Exercise 17: Recursive Functions
Student: Solutions

Exploring recursion with mathematical functions.
"""

print("=" * 60)
print("EXERCISE 17: Recursive Functions")
print("=" * 60)

# Part a: Factorial
print("\nPart a: Factorial")
print("-" * 60)

def factorial(n):
    """
    Calculate n! recursively.
    
    n! = n × (n-1)!
    Base case: 0! = 1, 1! = 1
    
    Parameters:
    -----------
    n : int
        Non-negative integer
    
    Returns:
    --------
    int
        n!
    """
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Test factorial
print("\nFactorial values:")
for n in [0, 1, 5, 10]:
    result = factorial(n)
    print(f"  {n}! = {result}")

# Show recursion process
print("\nRecursion visualization for factorial(5):")
print("  factorial(5)")
print("  = 5 × factorial(4)")
print("    = 5 × (4 × factorial(3))")
print("      = 5 × (4 × (3 × factorial(2)))")
print("        = 5 × (4 × (3 × (2 × factorial(1))))")
print("          = 5 × (4 × (3 × (2 × 1)))")
print("          = 5 × (4 × (3 × 2))")
print("          = 5 × (4 × 6)")
print("          = 5 × 24")
print("          = 120")

# Iterative version for comparison
def factorial_iterative(n):
    """Calculate n! iteratively."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\nComparison with iterative version:")
for n in [5, 10, 15]:
    rec = factorial(n)
    it = factorial_iterative(n)
    print(f"  {n}!: recursive={rec}, iterative={it}, match={rec==it}")

# Part b: Fibonacci
print("\n" + "=" * 60)
print("Part b: Fibonacci Sequence")
print("-" * 60)

def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    
    Parameters:
    -----------
    n : int
        Position in sequence (0-indexed)
    
    Returns:
    --------
    int
        nth Fibonacci number
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Generate Fibonacci sequence
print("\nFirst 15 Fibonacci numbers:")
for i in range(15):
    fib = fibonacci(i)
    print(f"  F({i:2}) = {fib:4}")

# Visualize recursion for small n
print("\nRecursion tree for fibonacci(5):")
print("""
                    fib(5)
                   /      \\
              fib(4)        fib(3)
             /     \\       /     \\
        fib(3)   fib(2)  fib(2)  fib(1)
       /    \\    /   \\   /   \\
   fib(2) fib(1) f(1) f(0) f(1) f(0)
   /   \\
fib(1) fib(0)

Notice: Many repeated calculations!
""")

# Improved version with memoization
def fibonacci_memo(n, memo=None):
    """Fibonacci with memoization (caching results)."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("\nComparison: naive vs memoized (larger n):")
import time

n = 30
start = time.time()
result1 = fibonacci(n)
time1 = time.time() - start

start = time.time()
result2 = fibonacci_memo(n)
time2 = time.time() - start

print(f"  fibonacci({n}) = {result1}")
print(f"  Naive recursive: {time1:.4f} seconds")
print(f"  With memoization: {time2:.6f} seconds")
print(f"  Speedup: {time1/time2:.0f}x faster!")

# Part c: List Sum
print("\n" + "=" * 60)
print("Part c: Recursive List Sum")
print("-" * 60)

def recursive_sum(numbers):
    """
    Sum all numbers in a list recursively.
    
    Base case: empty list sums to 0
    Recursive case: sum = first + sum(rest)
    
    Parameters:
    -----------
    numbers : list
        List of numbers
    
    Returns:
    --------
    float
        Sum of all numbers
    """
    # Base case: empty list
    if len(numbers) == 0:
        return 0
    
    # Recursive case: first element + sum of rest
    return numbers[0] + recursive_sum(numbers[1:])

# Test recursive sum
test_lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30],
    [],
    [100],
    [1.5, 2.5, 3.5, 4.5],
]

print("\nRecursive sum examples:")
for lst in test_lists:
    result = recursive_sum(lst)
    builtin = sum(lst)
    print(f"  {lst}: recursive={result}, built-in={builtin}")

# Visualize recursion
print("\nRecursion visualization for [1, 2, 3, 4, 5]:")
print("  recursive_sum([1, 2, 3, 4, 5])")
print("  = 1 + recursive_sum([2, 3, 4, 5])")
print("    = 1 + (2 + recursive_sum([3, 4, 5]))")
print("      = 1 + (2 + (3 + recursive_sum([4, 5])))")
print("        = 1 + (2 + (3 + (4 + recursive_sum([5]))))")
print("          = 1 + (2 + (3 + (4 + (5 + recursive_sum([])))))")
print("            = 1 + (2 + (3 + (4 + (5 + 0))))")
print("            = 1 + (2 + (3 + 9))")
print("            = 1 + (2 + 12)")
print("            = 1 + 14")
print("            = 15")

# Bonus: More recursive examples
print("\n" + "=" * 60)
print("BONUS: Additional Recursive Functions")
print("-" * 60)

def power(base, exponent):
    """Calculate base^exponent recursively."""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def count_digits(n):
    """Count digits in a number recursively."""
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

def reverse_string(s):
    """Reverse a string recursively."""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

def gcd(a, b):
    """Calculate greatest common divisor recursively (Euclidean algorithm)."""
    if b == 0:
        return a
    return gcd(b, a % b)

# Test bonus functions
print("\nPower function:")
print(f"  2^10 = {power(2, 10)}")
print(f"  5^3 = {power(5, 3)}")

print("\nCount digits:")
print(f"  12345 has {count_digits(12345)} digits")
print(f"  9 has {count_digits(9)} digit")

print("\nReverse string:")
print(f"  'hello' reversed: '{reverse_string('hello')}'")
print(f"  'Python' reversed: '{reverse_string('Python')}'")

print("\nGreatest Common Divisor:")
print(f"  gcd(48, 18) = {gcd(48, 18)}")
print(f"  gcd(100, 35) = {gcd(100, 35)}")

# Warning about recursion depth
print("\n" + "=" * 60)
print("WARNING: Recursion Depth Limit")
print("-" * 60)

import sys
print(f"Python recursion limit: {sys.getrecursionlimit()}")
print("\nTrying to exceed recursion limit:")
try:
    factorial(2000)
except RecursionError as e:
    print(f"  RecursionError: {e}")
    print("  Use iterative approach for deep recursion!")

# Summary
print("\n" + "=" * 60)
print("SUMMARY: Recursion")
print("-" * 60)
print("""
Key concepts:
  • Every recursive function needs a BASE CASE to stop
  • Recursive case calls the function with a simpler problem
  • Each call creates a new "frame" on the call stack
  
When to use recursion:
  ✓ Naturally recursive problems (trees, graphs)
  ✓ Divide-and-conquer algorithms
  ✓ When it makes the code clearer
  
When NOT to use recursion:
  ✗ Deep recursion (can exceed stack limit)
  ✗ Problems with many repeated subproblems (unless memoized)
  ✗ Simple iteration is clearer
  
Optimization:
  • Use memoization to cache results
  • Consider iterative alternatives
  • Tail recursion optimization (in some languages, not Python)
""")
