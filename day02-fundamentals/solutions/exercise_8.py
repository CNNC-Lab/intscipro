"""
Exercise 8: Logical Expressions and Comparisons
Student: Solutions

Working with boolean logic, comparisons, and chained comparisons.
"""

print("=" * 60)
print("EXERCISE 8: Logical Expressions and Comparisons")
print("=" * 60)

# Part a: Boolean Logic
print("\nPart a: Boolean Logic")
print("-" * 60)

x = 5
y = 10
z = 5

expressions = [
    ("x < y", x < y),
    ("x == z", x == z),
    ("x <= z", x <= z),
    ("y != z", y != z),
    ("x < y and y > z", x < y and y > z),
    ("x < y or y < z", x < y or y < z),
    ("not (x == z)", not (x == z)),
    ("x < y < 15", x < y < 15),
]

print(f"Variables: x={x}, y={y}, z={z}\n")
for expr_str, result in expressions:
    print(f"{expr_str:25} = {result}")

# Part b: Chained Comparisons
print("\n" + "=" * 60)
print("Part b: Chained Comparisons")
print("-" * 60)

ages = [15, 18, 25, 30, 35]

print("\nTesting age ranges:")
print(f"{'Age':<5} {'Traditional':<30} {'Chained':<20} {'Result'}")
print("-" * 70)

for age in ages:
    # Traditional way
    result1 = age >= 18 and age < 30
    # Chained comparison
    result2 = 18 <= age < 30
    
    print(f"{age:<5} {str(age >= 18) + ' and ' + str(age < 30):<30} "
          f"{str(result2):<20} {result2}")

print("\nConclusion: Chained comparisons are:")
print("  - More readable")
print("  - More concise")
print("  - Closer to mathematical notation")

# Part c: Neuroscience Application
print("\n" + "=" * 60)
print("Part c: Neuroscience Applications")
print("-" * 60)

# Example 1: Membrane potential check
print("\n1. Checking if voltage is in depolarization range")
print("   (Depolarization: -55 mV to -30 mV)")

test_voltages = [-70, -55, -45, -30, -20]
for voltage in test_voltages:
    is_depolarized = -55 <= voltage <= -30
    status = "DEPOLARIZED" if is_depolarized else "not depolarized"
    print(f"   Voltage: {voltage:4} mV  →  {status}")

# Example 2: Firing rate check
print("\n2. Checking if firing rate is abnormal")
print("   (Abnormal: >100 Hz or <1 Hz)")

test_rates = [0.5, 1.0, 12.5, 45.0, 100.0, 150.0]
for firing_rate in test_rates:
    is_abnormal = firing_rate > 100 or firing_rate < 1
    status = "ABNORMAL" if is_abnormal else "normal"
    print(f"   Rate: {firing_rate:6.1f} Hz  →  {status}")

# Example 3: Experiment validation
print("\n3. Validating experiment eligibility")
print("   (Valid: has consent AND age >= 18 AND no exclusion criteria)")

participants = [
    {"name": "Alice", "age": 22, "consent": True, "exclusion": False},
    {"name": "Bob", "age": 17, "consent": True, "exclusion": False},
    {"name": "Carol", "age": 25, "consent": False, "exclusion": False},
    {"name": "Dave", "age": 30, "consent": True, "exclusion": True},
    {"name": "Eve", "age": 28, "consent": True, "exclusion": False},
]

print("\n   Name      Age  Consent  Exclusion  Valid?")
print("   " + "-" * 50)
for p in participants:
    is_valid = p["consent"] and p["age"] >= 18 and not p["exclusion"]
    print(f"   {p['name']:<8} {p['age']:>3}  {str(p['consent']):<7}  "
          f"{str(p['exclusion']):<9}  {is_valid}")

# Bonus: Complex logical expressions
print("\n" + "=" * 60)
print("BONUS: Complex Logical Expressions")
print("-" * 60)

voltage = -45
threshold = -55
refractory = False
time_since_spike = 5.0  # ms

# Neuron will fire if:
# - voltage > threshold AND
# - not in refractory period AND
# - enough time has passed since last spike
will_fire = (voltage > threshold and 
             not refractory and 
             time_since_spike > 2.0)

print(f"\nNeuron State:")
print(f"  Voltage: {voltage} mV")
print(f"  Threshold: {threshold} mV")
print(f"  Refractory: {refractory}")
print(f"  Time since last spike: {time_since_spike} ms")
print(f"\n  Will fire: {will_fire}")

# Truth table for AND operation
print("\n" + "=" * 60)
print("Truth Tables Reference")
print("-" * 60)

print("\nAND operation:")
print("  True  and True  =", True and True)
print("  True  and False =", True and False)
print("  False and True  =", False and True)
print("  False and False =", False and False)

print("\nOR operation:")
print("  True  or True  =", True or True)
print("  True  or False =", True or False)
print("  False or True  =", False or True)
print("  False or False =", False or False)

print("\nNOT operation:")
print("  not True  =", not True)
print("  not False =", not False)
