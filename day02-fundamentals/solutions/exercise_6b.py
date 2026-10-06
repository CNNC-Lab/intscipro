"""
Exercise 6b: Exploring String Methods
Student: Solutions

Discovering string methods to format names.
"""

print("=" * 60)
print("EXERCISE 6b: Name Reverser")
print("=" * 60)

# Basic version
print("\nBasic version:")
full_name = input("Enter your full name (firstname lastname): ")

# Method discovered: split()
parts = full_name.split()
first_name = parts[0]
last_name = parts[1]

# Method discovered: title()
result = f"{last_name.title()}, {first_name.title()}"
print(f"Output: {result}")

# Advanced version with error handling
print("\n" + "=" * 60)
print("Advanced version:")
print("=" * 60)

full_name = input("\nEnter your full name: ")

# Strip whitespace from ends
full_name = full_name.strip()

# Split into parts
parts = full_name.split()

if len(parts) < 2:
    print("Error: Please enter at least first and last name")
elif len(parts) == 2:
    # Simple case: firstname lastname
    first_name = parts[0].title()
    last_name = parts[1].title()
    print(f"Output: {last_name}, {first_name}")
else:
    # Handle middle names
    first_name = parts[0].title()
    middle_names = [name.title() for name in parts[1:-1]]
    last_name = parts[-1].title()
    
    middle_initials = ' '.join([name[0] + '.' for name in middle_names])
    print(f"Output: {last_name}, {first_name} {middle_initials}")

# Demonstrate string methods
print("\n" + "=" * 60)
print("USEFUL STRING METHODS DISCOVERED")
print("=" * 60)

demo_string = "  maria silva santos  "
print(f"Original: '{demo_string}'")

print(f"\nstrip():       '{demo_string.strip()}'")
print(f"split():       {demo_string.split()}")
print(f"upper():       '{demo_string.upper()}'")
print(f"lower():       '{demo_string.lower()}'")
print(f"title():       '{demo_string.title()}'")
print(f"capitalize():  '{demo_string.capitalize()}'")

# More advanced string methods
print("\n" + "=" * 60)
print("MORE STRING METHODS")
print("=" * 60)

test = "hello world"
print(f"Original: '{test}'")
print(f"replace('world', 'Python'): '{test.replace('world', 'Python')}'")
print(f"startswith('hello'): {test.startswith('hello')}")
print(f"endswith('world'): {test.endswith('world')}")
print(f"count('l'): {test.count('l')}")
print(f"find('world'): {test.find('world')}")
print(f"join with '-': '{'-'.join(test.split())}'")

# Checking string properties
print("\n" + "=" * 60)
print("STRING CHECKING METHODS")
print("=" * 60)

test_cases = ["Hello123", "12345", "hello", "HELLO", "Hello World"]
for s in test_cases:
    print(f"\n'{s}':")
    print(f"  isalnum():  {s.isalnum()}")
    print(f"  isalpha():  {s.isalpha()}")
    print(f"  isdigit():  {s.isdigit()}")
    print(f"  islower():  {s.islower()}")
    print(f"  isupper():  {s.isupper()}")
    print(f"  isspace():  {s.isspace()}")
