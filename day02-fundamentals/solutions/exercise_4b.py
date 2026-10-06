"""
Exercise 4b: Reading Input
Student: Solutions

Reading user input and creating personalized greetings.
"""

print("=" * 50)
print("EXERCISE 4b: Reading Input")
print("=" * 50)

# Read user information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Create personalized greeting
full_name = f"{first_name} {last_name}"
print(f"\nHello, {full_name}!")
print(f"Welcome to the Scientific Programming course.")

# Additional personalization
print(f"\nIt's a pleasure to meet you, {first_name}!")
print(f"We hope you enjoy learning Python, {last_name} family!")

# Bonus: Title case formatting
print(f"\nFormatted properly: {full_name.title()}")
