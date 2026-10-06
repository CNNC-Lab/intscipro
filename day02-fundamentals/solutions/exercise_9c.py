"""
Exercise 9c: Nested Loops - Multiplication Table
Student: Solutions

Creating a multiplication table using nested loops.
"""

print("=" * 80)
print("EXERCISE 9c: Multiplication Table")
print("=" * 80)

# Simple version - basic output
print("\nBasic Version:")
print("-" * 40)

for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}", end="    ")
        if j == 5:  # Line break in middle for readability
            print()
    print("\n")

# Formatted version - aligned columns
print("\n" + "=" * 80)
print("Formatted Version (Aligned Columns):")
print("=" * 80)

# Print header row
print("   ", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print("\n" + "   " + "-" * 40)

# Print table
for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        product = i * j
        print(f"{product:4}", end="")
    print()

# Compact version - all on one row
print("\n" + "=" * 80)
print("Compact Version (Each Row on One Line):")
print("=" * 80)

for i in range(1, 11):
    row = f"{i:2}:"
    for j in range(1, 11):
        product = i * j
        row += f" {product:3}"
    print(row)

# Grid version - nice formatting
print("\n" + "=" * 80)
print("Grid Version (Enhanced Formatting):")
print("=" * 80)

# Header
print("     ", end="")
for j in range(1, 11):
    print(f"{j:5}", end="")
print("\n     " + "=" * 50)

# Table with row labels
for i in range(1, 11):
    print(f"{i:3} |", end="")
    for j in range(1, 11):
        product = i * j
        print(f"{product:5}", end="")
    print()

# Bonus: Times tables up to 12
print("\n" + "=" * 80)
print("Bonus: Extended Table (1-12)")
print("=" * 80)

print("     ", end="")
for j in range(1, 13):
    print(f"{j:5}", end="")
print("\n     " + "=" * 60)

for i in range(1, 13):
    print(f"{i:3} |", end="")
    for j in range(1, 13):
        product = i * j
        print(f"{product:5}", end="")
    print()

# Highlight specific times table
print("\n" + "=" * 80)
print("Specific Times Table (e.g., 7 times table):")
print("=" * 80)

multiplier = 7
for i in range(1, 13):
    result = multiplier * i
    print(f"{multiplier} × {i:2} = {result:3}")
