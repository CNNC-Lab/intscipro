"""
Exercise 9b: While-Loop Sum
Student: Solutions

Using a while-loop to find when sum exceeds 1000.
"""

print("=" * 60)
print("EXERCISE 9b: While-Loop Sum Until Threshold")
print("=" * 60)

# Initialize variables
total = 0
number = 1
count = 0

print("\nAdding consecutive numbers until total exceeds 1000...")
print("Number  Total")
print("-" * 20)

# While loop continues until total exceeds 1000
while total <= 1000:
    total += number
    count += 1
    
    # Print first few and last few steps
    if count <= 5 or total > 980:
        print(f"{number:4}    {total:5}")
    elif count == 6:
        print("  ...       ...")
    
    number += 1

# number is now one more than the last number added
last_number_added = number - 1

print("-" * 20)
print(f"\nThe sum exceeded 1000 at number: {last_number_added}")
print(f"Final total: {total}")
print(f"Numbers added: {count}")

# Verification
print("\n" + "-" * 60)
print("Verification:")
print("-" * 60)
sum_formula = last_number_added * (last_number_added + 1) // 2
print(f"Sum using formula: {sum_formula}")
print(f"Difference from target (1000): {total - 1000}")
print(f"Previous sum would have been: {total - last_number_added}")
