"""
Exercise 1: Value and Type of Expressions
Student: Solutions

Testing different types of expressions and their results.
"""

# Define initial variables
i = 10
j = 3
f = 3.0
c = 4.0 + 3.5j
s = 'hello'

print("=" * 50)
print("EXERCISE 1: Value and Type of Expressions")
print("=" * 50)

# Test each expression
print("\n1. 2 * i")
result = 2 * i
print(f"   Result: {result}, Type: {type(result)}")

print("\n2. i + f")
result = i + f
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: int + float returns float")

print("\n3. s + ' world'")
result = s + ' world'
print(f"   Result: {result}, Type: {type(result)}")

print("\n4. s + i")
print("   This causes a TypeError!")
try:
    result = s + i
except TypeError as e:
    print(f"   Error: {e}")
    print("   Cannot concatenate str and int directly")

print("\n5. s + str(i)")
result = s + str(i)
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: Must convert int to str first")

print("\n6. i / j")
result = i / j
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: / always returns float (true division)")

print("\n7. i / float(j)")
result = i / float(j)
print(f"   Result: {result}, Type: {type(result)}")

print("\n8. i / f")
result = i / f
print(f"   Result: {result}, Type: {type(result)}")

print("\n9. i // j")
result = i // j
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: // is floor division (rounds down)")

print("\n10. i // f")
result = i // f
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: // with float operand returns float")

print("\n11. c * f")
result = c * f
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: complex * float returns complex")

print("\n12. f ** 2")
result = f ** 2
print(f"   Result: {result}, Type: {type(result)}")

print("\n13. i ** 0.5")
result = i ** 0.5
print(f"   Result: {result}, Type: {type(result)}")
print("   Note: Square root returns float")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("- Mixing int and float returns float")
print("- / always returns float")
print("- // returns int if both operands are int, else float")
print("- Cannot directly add string and number")
print("- Use str() to convert numbers to strings")
