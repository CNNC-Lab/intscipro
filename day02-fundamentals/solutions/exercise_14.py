"""
Exercise 14: Function Fundamentals
Student: Solutions

Building functions progressively from simple loops.
"""

print("=" * 60)
print("EXERCISE 14: Function Fundamentals")
print("=" * 60)

# Part a: From loop to function
print("\nPart a: Sum of squares - Progressive development")
print("-" * 60)

# Step 1: Simple for-loop
print("\nStep 1: For-loop calculating sum of squares 1 to 20")
total = 0
for i in range(1, 21):
    total += i ** 2
print(f"Result: {total}")

# Step 2: Function without parameters
print("\nStep 2: Function sum_of_squares() - no parameters")
def sum_of_squares():
    """Calculate sum of squares from 1 to 20."""
    total = 0
    for i in range(1, 21):
        total += i ** 2
    return total

result = sum_of_squares()
print(f"Result: {result}")

# Step 3: Function with parameter
print("\nStep 3: Function sum_of_squares(n) - with parameter")
def sum_of_squares(n):
    """
    Calculate sum of squares from 1 to n.
    
    Parameters:
    -----------
    n : int
        Upper limit (inclusive)
    
    Returns:
    --------
    int
        Sum of squares from 1² to n²
    """
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

print(f"sum_of_squares(20) = {sum_of_squares(20)}")
print(f"sum_of_squares(10) = {sum_of_squares(10)}")
print(f"sum_of_squares(5) = {sum_of_squares(5)}")

# Verify with formula: n(n+1)(2n+1)/6
def sum_of_squares_formula(n):
    """Calculate sum of squares using mathematical formula."""
    return n * (n + 1) * (2 * n + 1) // 6

print(f"\nVerification using formula n(n+1)(2n+1)/6:")
print(f"sum_of_squares(20) = {sum_of_squares(20)}")
print(f"Formula result     = {sum_of_squares_formula(20)}")

# Part b: While-loop function
print("\n" + "=" * 60)
print("Part b: While-loop function")
print("-" * 60)

# Step 1: While-loop
print("\nStep 1: While-loop finding threshold")
total = 0
i = 1
while total <= 10000:
    total += i ** 2
    i += 1
print(f"Threshold exceeded at i = {i - 1}, total = {total}")

# Step 2: Function without parameter
print("\nStep 2: Function find_threshold() - no parameters")
def find_threshold():
    """Find number where sum of squares exceeds 10000."""
    total = 0
    i = 1
    while total <= 10000:
        total += i ** 2
        i += 1
    return i - 1  # Return the last number added

result = find_threshold()
print(f"Threshold exceeded at: {result}")

# Step 3: Function with parameter
print("\nStep 3: Function find_threshold(threshold) - with parameter")
def find_threshold(threshold):
    """
    Find number where sum of squares exceeds threshold.
    
    Parameters:
    -----------
    threshold : int
        The threshold value to exceed
    
    Returns:
    --------
    int
        The number at which sum of squares exceeds threshold
    """
    total = 0
    i = 1
    while total <= threshold:
        total += i ** 2
        i += 1
    return i - 1

print(f"find_threshold(10000) = {find_threshold(10000)}")
print(f"find_threshold(1000) = {find_threshold(1000)}")
print(f"find_threshold(100) = {find_threshold(100)}")

# Part c: Input Validation
print("\n" + "=" * 60)
print("Part c: Input validation")
print("-" * 60)

def find_threshold_validated(threshold):
    """
    Find number where sum of squares exceeds threshold (with validation).
    
    Parameters:
    -----------
    threshold : int
        The threshold value to exceed (must be positive integer)
    
    Returns:
    --------
    int or None
        The number at which sum exceeds threshold, or None if invalid input
    """
    # Check if threshold is an integer
    if not isinstance(threshold, int):
        print(f"Error: threshold must be an integer, not {type(threshold).__name__}")
        return None
    
    # Check if threshold is positive
    if threshold <= 0:
        print(f"Error: threshold must be positive, got {threshold}")
        return None
    
    # Valid input - perform calculation
    total = 0
    i = 1
    while total <= threshold:
        total += i ** 2
        i += 1
    
    return i - 1

# Test with valid and invalid inputs
print("\nTesting with valid input:")
result = find_threshold_validated(10000)
if result is not None:
    print(f"Result: {result}")

print("\nTesting with invalid inputs:")
result = find_threshold_validated(10.5)  # Float
result = find_threshold_validated("100")  # String
result = find_threshold_validated(-100)  # Negative
result = find_threshold_validated(0)  # Zero

# Bonus: Enhanced version with type coercion
print("\n" + "=" * 60)
print("BONUS: Enhanced validation with type coercion")
print("-" * 60)

def find_threshold_smart(threshold):
    """
    Find threshold with smart type handling.
    
    Attempts to convert input to int if possible.
    """
    # Try to convert to int
    try:
        threshold = int(threshold)
    except (ValueError, TypeError):
        print(f"Error: Cannot convert {threshold} to integer")
        return None
    
    # Check if positive
    if threshold <= 0:
        print(f"Error: threshold must be positive, got {threshold}")
        return None
    
    # Calculate
    total = 0
    i = 1
    while total <= threshold:
        total += i ** 2
        i += 1
    
    return i - 1

print("\nTesting smart version:")
print(f"find_threshold_smart(100) = {find_threshold_smart(100)}")      # int
print(f"find_threshold_smart(100.0) = {find_threshold_smart(100.0)}")  # float
print(f"find_threshold_smart('100') = {find_threshold_smart('100')}")  # string
print(f"find_threshold_smart('abc') = {find_threshold_smart('abc')}")  # invalid

# Summary
print("\n" + "=" * 60)
print("SUMMARY: Function Development Process")
print("=" * 60)
print("""
1. Start with working code (loop)
2. Wrap in function with descriptive name
3. Add parameters to make it general
4. Add docstring explaining purpose and parameters
5. Add input validation
6. Add error handling
7. Test with various inputs

Benefits of functions:
  • Code reusability - write once, use many times
  • Easier testing - test function independently
  • Better organization - logical units
  • Clearer code - descriptive function names
  • Easier maintenance - change in one place
""")
