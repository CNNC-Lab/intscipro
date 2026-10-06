"""
Exercise 12: Control Flow Mastery
Student: Solutions

Advanced control flow with if-elif-else and input validation.
"""

print("=" * 60)
print("EXERCISE 12: Control Flow Mastery")
print("=" * 60)

# Part a: Grade Calculator
print("\nPart a: Grade Calculator")
print("-" * 60)

def calculate_grade(score):
    """Convert numerical score to letter grade."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test with interactive input
while True:
    try:
        score = float(input("\nEnter score (0-100): "))
        
        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100")
            continue
        
        grade = calculate_grade(score)
        print(f"Score: {score:.1f} → Grade: {grade}")
        
        # Add descriptive feedback
        if grade == 'A':
            print("Excellent work!")
        elif grade == 'B':
            print("Good job!")
        elif grade == 'C':
            print("Satisfactory.")
        elif grade == 'D':
            print("Needs improvement.")
        else:
            print("Please see instructor.")
        
        break
        
    except ValueError:
        print("Error: Please enter a valid number")

# Part b: Spike Train Classifier
print("\n" + "=" * 60)
print("Part b: Spike Train Classifier")
print("-" * 60)

def classify_firing_rate(rate):
    """Classify neural firing pattern based on rate."""
    if rate < 1:
        return "Silent"
    elif rate < 10:
        return "Low"
    elif rate < 50:
        return "Moderate"
    elif rate < 100:
        return "High"
    else:
        return "Hyperactive"

# Test with various firing rates
test_rates = [0.5, 5.2, 25.0, 75.5, 150.0]
print("\nFiring Rate Classification:")
print(f"{'Rate (Hz)':<15} {'Classification'}")
print("-" * 35)
for rate in test_rates:
    classification = classify_firing_rate(rate)
    print(f"{rate:<15.1f} {classification}")

# Interactive version
while True:
    try:
        firing_rate = float(input("\nEnter firing rate (Hz): "))
        
        if firing_rate < 0:
            print("Error: Firing rate cannot be negative")
            continue
        
        classification = classify_firing_rate(firing_rate)
        print(f"\nFiring rate: {firing_rate:.2f} Hz")
        print(f"Classification: {classification}")
        
        # Add interpretation
        if classification == "Silent":
            print("Interpretation: Neuron is not active or below detection threshold")
        elif classification == "Low":
            print("Interpretation: Baseline activity")
        elif classification == "Moderate":
            print("Interpretation: Normal active state")
        elif classification == "High":
            print("Interpretation: Strong response to stimulus")
        else:
            print("Interpretation: Potentially pathological or burst firing")
        
        break
        
    except ValueError:
        print("Error: Please enter a valid number")

# Part c: Password Validator
print("\n" + "=" * 60)
print("Part c: Password Validator")
print("-" * 60)

def validate_password(password):
    """
    Validate password meets security criteria.
    Returns (is_valid, error_message)
    """
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for digit
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Password must contain at least one digit"
    
    # Check for uppercase
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    
    return True, "Password meets all requirements"

print("\nPassword Requirements:")
print("  - At least 8 characters long")
print("  - Contains at least one digit")
print("  - Contains at least one uppercase letter")

max_attempts = 3
for attempt in range(1, max_attempts + 1):
    print(f"\nAttempt {attempt} of {max_attempts}")
    password = input("Enter password: ")
    
    is_valid, message = validate_password(password)
    print(message)
    
    if is_valid:
        print("✓ Password accepted!")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Please try again. {remaining} attempts remaining.")
        else:
            print("✗ Too many failed attempts. Account locked.")

# Bonus: Enhanced password validator
print("\n" + "=" * 60)
print("BONUS: Enhanced Password Strength Checker")
print("-" * 60)

def check_password_strength(password):
    """Check password strength and return score."""
    score = 0
    feedback = []
    
    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (min 8 characters)")
    
    if len(password) >= 12:
        score += 1
        feedback.append("Good length")
    
    # Digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Missing digit")
    
    # Uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Missing uppercase letter")
    
    # Lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Missing lowercase letter")
    
    # Special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(char in special_chars for char in password):
        score += 1
        feedback.append("Contains special character")
    else:
        feedback.append("No special character")
    
    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, score, feedback

# Test password strength
test_passwords = ["pass", "password", "Password1", "MyP@ssw0rd!", "12345678"]
print("\nPassword Strength Analysis:")
print("-" * 60)
for pwd in test_passwords:
    strength, score, feedback = check_password_strength(pwd)
    print(f"\nPassword: {'*' * len(pwd)} (length: {len(pwd)})")
    print(f"Strength: {strength} ({score}/6 points)")
    for item in feedback:
        print(f"  • {item}")
