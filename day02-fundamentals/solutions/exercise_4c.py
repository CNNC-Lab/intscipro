"""
Exercise 4c: Reading Numeric Input
Student: Solutions

Reading numeric input with error handling.
"""

from datetime import datetime

print("=" * 50)
print("EXERCISE 4c: Age Calculator")
print("=" * 50)

# Basic version (without error handling)
print("\nBasic version:")
age_str = input("What is your age? ")
age = int(age_str)

if age >= 100:
    print("You are already 100 or over!")
elif age == 100:
    print("You are exactly 100! Congratulations!")
else:
    years_to_go = 100 - age
    print(f"You will turn 100 in {years_to_go} years!")

# Advanced version with error handling
print("\n" + "=" * 50)
print("Advanced version with error handling:")
print("=" * 50)

while True:
    try:
        age_str = input("\nWhat is your age? ")
        age = int(age_str)
        
        # Validate age is reasonable
        if age < 0:
            print("Age cannot be negative. Please try again.")
            continue
        if age > 120:
            print("Age seems unrealistic. Please enter a valid age.")
            continue
        
        # Valid age - process it
        break
        
    except ValueError:
        print("That's not a valid number. Please enter your age as a number.")

# Display result
print(f"\nYou entered: {age} years old")

if age >= 100:
    years_over = age - 100
    print(f"You are already {years_over} years over 100!")
elif age == 100:
    print("You are exactly 100! Congratulations on this milestone!")
else:
    years_to_go = 100 - age
    print(f"You will turn 100 in {years_to_go} years!")
    print(f"That will be in the year {datetime.now().year + years_to_go}.")
