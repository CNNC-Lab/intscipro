"""
Exercise 5: Temperature Conversion
Student: Solutions

Converting between Celsius and Fahrenheit with validation.
"""

print("=" * 60)
print("TEMPERATURE CONVERTER")
print("=" * 60)

# Basic version: Celsius to Fahrenheit only
print("\nBasic version (C to F only):")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.1f}°C is equal to {fahrenheit:.1f}°F")

# Advanced version: Both directions with validation
print("\n" + "=" * 60)
print("Advanced version (both directions):")
print("=" * 60)

while True:
    print("\nChoose conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        continue
    
    try:
        temp = float(input("Enter temperature: "))
        
        if choice == '1':
            # Check against absolute zero in Celsius
            if temp < -273.15:
                print("Error: Temperature cannot be below absolute zero (-273.15°C)")
                continue
            
            result = (temp * 9/5) + 32
            print(f"\n{temp:.1f}°C = {result:.1f}°F")
            
        else:  # choice == '2'
            # Check against absolute zero in Fahrenheit
            if temp < -459.67:
                print("Error: Temperature cannot be below absolute zero (-459.67°F)")
                continue
            
            result = (temp - 32) * 5/9
            print(f"\n{temp:.1f}°F = {result:.1f}°C")
        
        break
        
    except ValueError:
        print("Error: Please enter a valid number.")

# Bonus: Scientific context
print("\n" + "=" * 60)
print("SCIENTIFIC REFERENCE TEMPERATURES")
print("=" * 60)
print(f"Absolute zero:      -273.15°C = -459.67°F")
print(f"Water freezes:         0.00°C =   32.00°F")
print(f"Room temperature:     20.00°C =   68.00°F")
print(f"Body temperature:     37.00°C =   98.60°F")
print(f"Water boils:         100.00°C =  212.00°F")
