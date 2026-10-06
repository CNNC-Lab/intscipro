"""
Exercise 7: Arithmetic Operations on Different Types
Student: Solutions

Testing arithmetic operations with different numeric types.
"""

print("=" * 60)
print("EXERCISE 7: Arithmetic Operations on Different Types")
print("=" * 60)

# Part a: Type Mixing
print("\nPart a: Type Mixing")
print("-" * 60)

a = 2       # int
b = 3.75    # float

print(f"a = {a} (type: {type(a).__name__})")
print(f"b = {b} (type: {type(b).__name__})")

operations = [
    ("a + b", a + b),
    ("a - b", a - b),
    ("a * b", a * b),
    ("a / b", a / b),
    ("a // b", a // b),
    ("a % b", a % b),
    ("a ** b", a ** b),
]

print("\nOperation Results:")
for op_str, result in operations:
    print(f"{op_str:10} = {result:10.4f}    (type: {type(result).__name__})")

print("\nConclusion:")
print("  - Mixing int and float always returns float")
print("  - This is sensible to preserve precision")
print("  - Python automatically promotes to more general type")

# Part b: Division Behavior
print("\n" + "=" * 60)
print("Part b: Division Behavior")
print("-" * 60)

test_cases = [
    ("10 / 3", 10 / 3),
    ("10 // 3", 10 // 3),
    ("10.0 // 3.0", 10.0 // 3.0),
    ("10 % 3", 10 % 3),
    ("10.5 / 2", 10.5 / 2),
    ("10.5 // 2", 10.5 // 2),
    ("10.5 % 2", 10.5 % 2),
]

print("\nDivision Operations:")
for op_str, result in test_cases:
    print(f"{op_str:15} = {result:10}    (type: {type(result).__name__})")

print("\nKey Differences:")
print("  / (true division)   - Always returns float, exact division")
print("  // (floor division) - Returns floor of division")
print("                        (int if both operands int, else float)")
print("  % (modulo)          - Returns remainder of division")

# Part c: Modulo Applications
print("\n" + "=" * 60)
print("Part c: Modulo Applications")
print("-" * 60)

# 1. Check if number is even or odd
print("\n1. Check if number is even or odd:")
test_numbers = [10, 17, 24, 33]
for num in test_numbers:
    if num % 2 == 0:
        print(f"  {num} is EVEN")
    else:
        print(f"  {num} is ODD")

# 2. Check if a is a factor of b
print("\n2. Check if 'a' is a factor of 'b':")
test_pairs = [(3, 15), (4, 15), (5, 25), (7, 30)]
for a, b in test_pairs:
    if b % a == 0:
        print(f"  {a} IS a factor of {b}")
    else:
        print(f"  {a} is NOT a factor of {b}")

# 3. Extract last digit
print("\n3. Extract last digit of a number:")
numbers = [12345, 9876, 1024, 7]
for num in numbers:
    last_digit = num % 10
    print(f"  Last digit of {num}: {last_digit}")

# 4. Convert seconds to minutes and seconds
print("\n4. Convert seconds to minutes:seconds:")
total_seconds_list = [185, 3665, 90, 45]
for total_seconds in total_seconds_list:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print(f"  {total_seconds} seconds = {minutes} minutes and {seconds} seconds")

# Advanced: Convert to hours:minutes:seconds
print("\n5. Bonus - Convert to hours:minutes:seconds:")
total_seconds = 7385
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print(f"  {total_seconds} seconds = {hours}h {minutes}m {seconds}s")

# Summary
print("\n" + "=" * 60)
print("SUMMARY: Modulo (%) Uses")
print("=" * 60)
print("  1. Check even/odd: num % 2 == 0")
print("  2. Check divisibility: b % a == 0")
print("  3. Extract last digit: num % 10")
print("  4. Wrap around values: (x % max) gives 0 to max-1")
print("  5. Time conversions: seconds % 60, minutes % 60")
