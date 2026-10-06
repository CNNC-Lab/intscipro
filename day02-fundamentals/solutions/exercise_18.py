"""
Exercise 18: Scope and Namespace
Student: Solutions

Understanding variable scope and namespace in Python.
"""

print("=" * 60)
print("EXERCISE 18: Scope and Namespace")
print("=" * 60)

# Part a: Understanding Scope
print("\nPart a: Understanding Scope")
print("-" * 60)

x = "global"

def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(f"Inner x: {x}")
    
    inner()
    print(f"Outer x: {x}")

outer()
print(f"Global x: {x}")

print("\nExplanation:")
print("  - Each function creates its own local scope")
print("  - Variables in inner scopes shadow outer scopes")
print("  - Assignments create local variables by default")
print("  - The global x is never modified")

# Demonstrating the LEGB rule
print("\n" + "-" * 60)
print("LEGB Rule: Local, Enclosing, Global, Built-in")
print("-" * 60)

x = "global x"

def outer_func():
    x = "enclosing x"
    
    def inner_func():
        # x = "local x"  # Uncomment to see local scope
        print(f"  Accessing x: {x}")
        print(f"  This is the enclosing x")
    
    inner_func()
    print(f"  In outer_func: {x}")

outer_func()
print(f"At global level: {x}")

# Built-in scope example
print("\nBuilt-in scope:")
print(f"  len is a built-in function: {len([1, 2, 3])}")

# Don't shadow built-ins!
print("\nWarning: Don't shadow built-in names:")
len_original = len
len = "I shadowed len!"  # BAD PRACTICE!
print(f"  Now len = '{len}'")
try:
    result = len([1, 2, 3])
except TypeError as e:
    print(f"  Error: {e}")
len = len_original  # Restore
print(f"  Restored: len([1, 2, 3]) = {len([1, 2, 3])}")

# Part b: Modifying Global Variables
print("\n" + "=" * 60)
print("Part b: Modifying Global Variables")
print("-" * 60)

# Problem version
print("\nProblem version (doesn't work):")
counter = 0

def increment_wrong():
    """This doesn't work as expected."""
    # This creates a LOCAL variable named counter
    # counter = counter + 1  # UnboundLocalError!
    pass

print(f"  Initial counter: {counter}")
increment_wrong()
print(f"  After increment_wrong(): {counter}")
print("  Counter unchanged because we didn't modify the global")

# Solution 1: Using global keyword (not recommended)
print("\nSolution 1: Using global keyword (not recommended):")
counter = 0

def increment_with_global():
    """Use global keyword to modify global variable."""
    global counter
    counter = counter + 1

print(f"  Initial counter: {counter}")
increment_with_global()
print(f"  After increment: {counter}")
increment_with_global()
print(f"  After another increment: {counter}")
print("  Works, but makes code harder to test and reason about")

# Solution 2: Return new value (recommended)
print("\nSolution 2: Return new value (recommended):")
counter = 0

def increment(value):
    """Return incremented value."""
    return value + 1

print(f"  Initial counter: {counter}")
counter = increment(counter)
print(f"  After increment: {counter}")
counter = increment(counter)
print(f"  After another increment: {counter}")
print("  Better: Explicit, testable, no hidden dependencies")

# Part c: Function Closures
print("\n" + "=" * 60)
print("Part c: Function Closures")
print("-" * 60)

def make_multiplier(factor):
    """Create a function that multiplies by factor."""
    def multiply(x):
        return x * factor
    return multiply

times_two = make_multiplier(2)
times_ten = make_multiplier(10)

print("\nClosure behavior:")
print(f"  times_two(5) = {times_two(5)}")
print(f"  times_ten(5) = {times_ten(5)}")
print(f"  times_two(10) = {times_two(10)}")
print(f"  times_ten(10) = {times_ten(10)}")

print("\nExplanation:")
print("  - make_multiplier returns a function")
print("  - The returned function 'remembers' the factor")
print("  - This is called a 'closure'")
print("  - Each closure has its own factor value")

# More closure examples
print("\n" + "-" * 60)
print("More Closure Examples")
print("-" * 60)

def make_counter():
    """Create a counter function."""
    count = 0
    
    def counter():
        nonlocal count  # Modify enclosing scope variable
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print("\nIndependent counters:")
print(f"  counter1(): {counter1()}")  # 1
print(f"  counter1(): {counter1()}")  # 2
print(f"  counter2(): {counter2()}")  # 1 (separate counter)
print(f"  counter1(): {counter1()}")  # 3
print(f"  counter2(): {counter2()}")  # 2

# Bonus: Practical closure example
print("\n" + "=" * 60)
print("BONUS: Practical Closure Applications")
print("-" * 60)

def create_neuron_filter(min_rate, max_rate):
    """Create a filter function for firing rates."""
    def is_valid(firing_rate):
        return min_rate <= firing_rate <= max_rate
    return is_valid

# Create different filters
normal_filter = create_neuron_filter(10, 100)
hyperactive_filter = create_neuron_filter(100, 500)

print("\nFiltering firing rates:")
test_rates = [5, 25, 75, 150, 300]

print("\nNormal range filter (10-100 Hz):")
for rate in test_rates:
    if normal_filter(rate):
        print(f"  {rate} Hz: PASS")
    else:
        print(f"  {rate} Hz: FAIL")

print("\nHyperactive range filter (100-500 Hz):")
for rate in test_rates:
    if hyperactive_filter(rate):
        print(f"  {rate} Hz: PASS")
    else:
        print(f"  {rate} Hz: FAIL")

# Demonstrating locals() and globals()
print("\n" + "=" * 60)
print("BONUS: Inspecting Namespaces")
print("-" * 60)

global_var = "I'm global"

def demo_namespace():
    local_var = "I'm local"
    
    print("\nLocal namespace:")
    local_dict = locals()
    print(f"  Local variables: {list(local_dict.keys())}")
    print(f"  local_var = {local_dict['local_var']}")
    
    print("\nGlobal namespace (selected items):")
    global_dict = globals()
    print(f"  global_var = {global_dict.get('global_var', 'not found')}")
    print(f"  Total global names: {len(global_dict)}")

demo_namespace()

# Common pitfalls
print("\n" + "=" * 60)
print("Common Namespace Pitfalls")
print("-" * 60)

# Pitfall 1: Unintended variable in loop
print("\nPitfall 1: Variables in control structures")
x = "original"

if True:
    y = "created in if"

print(f"  x = {x}")
print(f"  y = {y}")  # y exists! (unlike many languages)
print("  Note: if/for/while don't create new scope")

# Pitfall 2: Late binding in closures
print("\nPitfall 2: Late binding in closures")

def create_multipliers_wrong():
    """Common mistake with closures."""
    multipliers = []
    for i in range(3):
        multipliers.append(lambda x: x * i)
    return multipliers

funcs = create_multipliers_wrong()
print("  Expected: [0, 5, 10], Got:", [f(5) for f in funcs])
print("  Problem: All use final value of i (2)")

def create_multipliers_correct():
    """Correct way: capture value immediately."""
    multipliers = []
    for i in range(3):
        multipliers.append(lambda x, i=i: x * i)  # i=i captures current value
    return multipliers

funcs = create_multipliers_correct()
print("  Correct: ", [f(5) for f in funcs])

# Summary
print("\n" + "=" * 60)
print("SUMMARY: Scope and Namespace")
print("=" * 60)
print("""
LEGB Rule (search order):
  L - Local: Inside current function
  E - Enclosing: Inside enclosing functions
  G - Global: Module level
  B - Built-in: Python built-ins

Key concepts:
  • Assignment creates local variable (unless global/nonlocal declared)
  • Functions can read outer scopes but not modify (without keywords)
  • global: Modify global variables (avoid when possible)
  • nonlocal: Modify enclosing function variables
  • Closures: Functions that remember enclosing scope
  • Control structures (if/for/while) DON'T create new scope

Best practices:
  ✓ Use function parameters and return values
  ✓ Avoid global variables when possible
  ✓ Use closures for function factories
  ✓ Be careful with late binding in loops
  ✗ Don't shadow built-in names
  ✗ Don't rely on mutable default arguments
  ✗ Don't use global unnecessarily
""")

# Final example: Putting it all together
print("\n" + "=" * 60)
print("Complete Example: Neuron Simulator with Closures")
print("-" * 60)

def create_neuron(threshold=-55, resting_potential=-70):
    """Create a neuron simulator with internal state."""
    voltage = resting_potential
    spike_count = 0
    
    def stimulate(current):
        """Apply current and update state."""
        nonlocal voltage, spike_count
        
        # Update voltage
        voltage += current
        
        # Check for spike
        if voltage >= threshold:
            spike_count += 1
            voltage = resting_potential  # Reset after spike
            return True
        
        return False
    
    def get_state():
        """Get current neuron state."""
        return {
            'voltage': voltage,
            'spike_count': spike_count,
            'threshold': threshold
        }
    
    def reset():
        """Reset neuron state."""
        nonlocal voltage, spike_count
        voltage = resting_potential
        spike_count = 0
    
    return stimulate, get_state, reset

# Create two independent neurons
stimulate1, get_state1, reset1 = create_neuron(threshold=-55)
stimulate2, get_state2, reset2 = create_neuron(threshold=-50)  # More excitable

print("\nSimulating two neurons:")
print("\nNeuron 1 (threshold -55 mV):")
for current in [5, 10, 15]:
    spiked = stimulate1(current)
    state = get_state1()
    print(f"  Current +{current}mV: V={state['voltage']}mV, " 
          f"Spiked={spiked}, Total spikes={state['spike_count']}")

print("\nNeuron 2 (threshold -50 mV, more excitable):")
for current in [5, 10, 15]:
    spiked = stimulate2(current)
    state = get_state2()
    print(f"  Current +{current}mV: V={state['voltage']}mV, "
          f"Spiked={spiked}, Total spikes={state['spike_count']}")

print("\nEach neuron maintains independent state via closures!")
