"""
Exercise 2: Understanding Variables and Identity
Student: Solutions

Exploring mutable vs immutable types and variable swapping.
"""

print("=" * 50)
print("EXERCISE 2a: Same or Different?")
print("=" * 50)

# Program 1: Strings (immutable)
print("\nProgram 1 (Strings):")
x = 'ab'
y = x
print(f"Initial: x='{x}', y='{y}'")
print(f"x id: {id(x)}, y id: {id(y)}")
x = 'ac'
print(f"After x='ac': x='{x}', y='{y}'")
print(f"x id: {id(x)}, y id: {id(y)}")
print("Result: y is still 'ab'")
print("Explanation: Strings are immutable. x = 'ac' creates")
print("a NEW string object, so y still refers to 'ab'")

# Program 2: Lists (mutable)
print("\nProgram 2 (Lists):")
x = ['a', 'b']
y = x
print(f"Initial: x={x}, y={y}")
print(f"x id: {id(x)}, y id: {id(y)}")
x[1] = 'c'
print(f"After x[1]='c': x={x}, y={y}")
print(f"x id: {id(x)}, y id: {id(y)}")
print("Result: y is now ['a', 'c']")
print("Explanation: Lists are mutable. Both x and y refer")
print("to the SAME list object, so modifying x affects y")

# Solution: Create independent copy
print("\nTo make y independent of x:")
x = ['a', 'b']
y = x.copy()  # or y = x[:]
print(f"Initial: x={x}, y={y}")
x[1] = 'c'
print(f"After x[1]='c': x={x}, y={y}")
print("Now y is independent!")

print("\n" + "=" * 50)
print("EXERCISE 2b: Swapping Values")
print("=" * 50)

# Method 1: Using temporary variable
print("\nMethod 1: Using temporary variable")
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
temp = a
a = b
b = temp
print(f"After swap: a={a}, b={b}")

# Method 2: Tuple unpacking (Pythonic way)
print("\nMethod 2: Tuple unpacking (Pythonic way)")
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Method 3: Arithmetic (works for numbers only)
print("\nMethod 3: Arithmetic (for numbers only)")
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
a = a + b
b = a - b
a = a - b
print(f"After swap: a={a}, b={b}")

# Method 4: XOR (works for integers only)
print("\nMethod 4: XOR bitwise operation (integers only)")
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swap: a={a}, b={b}")

print("\nRecommended: Use tuple unpacking (Method 2)")
print("It's the most Pythonic and works with any type!")
