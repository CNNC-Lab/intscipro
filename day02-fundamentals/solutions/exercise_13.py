"""
Exercise 13: Exception Handling
Student: Solutions

Handling errors gracefully with try-except blocks.
"""

print("=" * 60)
print("EXERCISE 13: Exception Handling")
print("=" * 60)

# Part a: Safe Division
print("\nPart a: Safe Division")
print("-" * 60)

def safe_divide():
    """Perform division with error handling."""
    while True:
        try:
            numerator = float(input("Enter numerator: "))
            denominator = float(input("Enter denominator: "))
            
            result = numerator / denominator
            print(f"\nResult: {numerator} / {denominator} = {result:.4f}")
            return result
            
        except ValueError:
            print("Error: Please enter valid numbers!\n")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

# Run safe division
safe_divide()

# Part b: Robust Age Input
print("\n" + "=" * 60)
print("Part b: Robust Age Input")
print("-" * 60)

def get_valid_age():
    """Get age with comprehensive validation."""
    while True:
        try:
            age_str = input("\nEnter your age: ")
            age = int(age_str)
            
            # Validate range
            if age < 0:
                print("Error: Age cannot be negative. Please try again.")
                continue
            
            if age > 120:
                print("Error: Age must be less than 120. Please try again.")
                continue
            
            # Valid age
            print(f"✓ Valid age: {age}")
            return age
            
        except ValueError:
            print("Error: Please enter a whole number for age.")

# Get and use age
user_age = get_valid_age()
print(f"\nYou are {user_age} years old.")
if user_age < 18:
    print("You are a minor.")
elif user_age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Part c: File-Safe Calculator
print("\n" + "=" * 60)
print("Part c: File-Safe Calculator")
print("-" * 60)

def calculate(expression):
    """
    Safely evaluate a simple arithmetic expression.
    Returns (success, result_or_error_message)
    """
    try:
        # Parse the expression
        parts = expression.split()
        
        if len(parts) != 3:
            return False, "Invalid format. Use: number operator number"
        
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        # Perform operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return False, "Cannot divide by zero"
            result = num1 / num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '%':
            if num2 == 0:
                return False, "Cannot calculate modulo with zero"
            result = num1 % num2
        else:
            return False, f"Unknown operator: {operator}"
        
        return True, result
        
    except ValueError:
        return False, "Invalid number format"
    except Exception as e:
        return False, f"Unexpected error: {e}"

# Calculator loop
print("\nSimple Calculator")
print("Format: number operator number")
print("Operators: +, -, *, /, **, %")
print("Type 'quit' to exit\n")

calculation_history = []

while True:
    expression = input("Enter calculation (or 'quit'): ").strip()
    
    if expression.lower() == 'quit':
        print("\nCalculation History:")
        for calc in calculation_history:
            print(f"  {calc}")
        print("\nGoodbye!")
        break
    
    success, result = calculate(expression)
    
    if success:
        print(f"Result: {result}")
        calculation_history.append(f"{expression} = {result}")
    else:
        print(f"Error: {result}")

# Bonus: Advanced exception handling
print("\n" + "=" * 60)
print("BONUS: Multiple Exception Types")
print("-" * 60)

def advanced_operation():
    """Demonstrate handling multiple exception types."""
    try:
        print("\nTesting various error conditions:")
        
        # Test 1: Type error
        print("Test 1: String + Integer")
        try:
            result = "hello" + 5
        except TypeError as e:
            print(f"  TypeError caught: {e}")
        
        # Test 2: Index error
        print("\nTest 2: Index out of range")
        try:
            my_list = [1, 2, 3]
            value = my_list[10]
        except IndexError as e:
            print(f"  IndexError caught: {e}")
        
        # Test 3: Key error
        print("\nTest 3: Dictionary key not found")
        try:
            my_dict = {'a': 1, 'b': 2}
            value = my_dict['c']
        except KeyError as e:
            print(f"  KeyError caught: {e}")
        
        # Test 4: Name error
        print("\nTest 4: Undefined variable")
        try:
            print(undefined_variable)
        except NameError as e:
            print(f"  NameError caught: {e}")
        
        # Test 5: Attribute error
        print("\nTest 5: Invalid attribute")
        try:
            x = 5
            x.append(3)
        except AttributeError as e:
            print(f"  AttributeError caught: {e}")
        
        print("\nAll error conditions handled successfully!")
        
    except Exception as e:
        print(f"Unexpected error in advanced_operation: {e}")

advanced_operation()

# Summary
print("\n" + "=" * 60)
print("EXCEPTION HANDLING SUMMARY")
print("=" * 60)
print("""
Key exception types:
  ValueError      - Invalid value (e.g., int("hello"))
  ZeroDivisionError - Division by zero
  TypeError       - Wrong type for operation
  IndexError      - Invalid index
  KeyError        - Invalid dictionary key
  NameError       - Undefined variable
  AttributeError  - Invalid attribute
  IOError/OSError - File operation errors

Best practices:
  1. Catch specific exceptions first, general ones last
  2. Provide helpful error messages to users
  3. Use try-except-else-finally for complex cases
  4. Don't catch exceptions you can't handle
  5. Log errors for debugging
  6. Clean up resources in finally block
""")
