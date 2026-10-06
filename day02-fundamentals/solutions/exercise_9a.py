"""
Exercise 9a: For-Loop Sum
Student: Solutions

Using a for-loop to sum numbers from 1 to 100.
"""

print("=" * 60)
print("EXERCISE 9a: Sum of Numbers 1 to 100")
print("=" * 60)

# Method 1: Using a for-loop
print("\nMethod 1: Using for-loop")
total = 0
for i in range(1, 101):  # 101 because range is exclusive at the end
    total += i

print(f"Sum of numbers 1 to 100: {total}")

# Verify with formula: n(n+1)/2
n = 100
formula_result = n * (n + 1) // 2
print(f"Verification using formula n(n+1)/2: {formula_result}")
print(f"Results match: {total == formula_result}")

# Method 2: Using Python's built-in sum()
print("\nMethod 2: Using built-in sum()")
total_builtin = sum(range(1, 101))
print(f"Sum using sum(range(1, 101)): {total_builtin}")

# Demonstration with smaller number for visibility
print("\n" + "-" * 60)
print("Demonstration with n=10:")
print("-" * 60)
total = 0
for i in range(1, 11):
    total += i
    print(f"  Step {i:2}: Adding {i:2}, total = {total:2}")

print(f"\nFinal sum: {total}")
print(f"Formula check: 10 * 11 / 2 = {10 * 11 // 2}")
