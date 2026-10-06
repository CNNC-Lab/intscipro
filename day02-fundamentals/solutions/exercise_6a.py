"""
Exercise 6a: Exploring List Methods
Student: Solutions

Discovering list methods using dir() and help().
"""

print("=" * 60)
print("EXERCISE 6a: Discovering List Methods")
print("=" * 60)

# Create initial list
neuron_types = ["pyramidal", "basket", "chandelier"]
print(f"\nInitial list: {neuron_types}")

# Task 1: Add element to end
print("\n" + "-" * 60)
print("Task 1: Add element to end")
print("-" * 60)
print("Method discovered: append()")
neuron_types.append("stellate")
print(f"After append('stellate'): {neuron_types}")

# Task 2: Remove last element
print("\n" + "-" * 60)
print("Task 2: Remove last element")
print("-" * 60)
print("Method discovered: pop()")
removed = neuron_types.pop()
print(f"After pop(): {neuron_types}")
print(f"Removed element: {removed}")

# Task 3: Remove first element
print("\n" + "-" * 60)
print("Task 3: Remove first element")
print("-" * 60)
print("Method discovered: pop(0)")
first = neuron_types.pop(0)
print(f"After pop(0): {neuron_types}")
print(f"Removed element: {first}")

# Reset list for remaining demonstrations
neuron_types = ["pyramidal", "basket", "chandelier", "pyramidal"]

# Task 4: Insert at specific position
print("\n" + "-" * 60)
print("Task 4: Insert at specific position")
print("-" * 60)
print("Method discovered: insert(index, element)")
print(f"Before: {neuron_types}")
neuron_types.insert(1, "stellate")
print(f"After insert(1, 'stellate'): {neuron_types}")

# Task 5: Find index of element
print("\n" + "-" * 60)
print("Task 5: Find index of element")
print("-" * 60)
print("Method discovered: index(element)")
idx = neuron_types.index("basket")
print(f"Index of 'basket': {idx}")

# Task 6: Count occurrences
print("\n" + "-" * 60)
print("Task 6: Count occurrences")
print("-" * 60)
print("Method discovered: count(element)")
count = neuron_types.count("pyramidal")
print(f"Count of 'pyramidal': {count}")

# Task 7: Sort the list
print("\n" + "-" * 60)
print("Task 7: Sort the list")
print("-" * 60)
print("Method discovered: sort()")
print(f"Before: {neuron_types}")
neuron_types.sort()
print(f"After sort(): {neuron_types}")

# Bonus: Difference between sort() and sorted()
print("\n" + "=" * 60)
print("BONUS: sort() vs sorted()")
print("=" * 60)

original = ["cortex", "hippocampus", "cerebellum", "amygdala"]
print(f"Original list: {original}")

# Using sort() - modifies in place
list1 = original.copy()
list1.sort()
print(f"\nAfter list1.sort(): {list1}")
print(f"list1.sort() returns: {list1.sort()}")  # Returns None

# Using sorted() - returns new list
list2 = original.copy()
sorted_list = sorted(list2)
print(f"\nOriginal list2: {list2}")
print(f"sorted(list2) returns: {sorted_list}")
print(f"list2 unchanged: {list2}")

print("\nKey difference:")
print("  sort() - modifies list in place, returns None")
print("  sorted() - returns new sorted list, original unchanged")

# Additional useful methods
print("\n" + "=" * 60)
print("OTHER USEFUL LIST METHODS")
print("=" * 60)

demo_list = [1, 2, 3]
print(f"Initial: {demo_list}")

# extend()
demo_list.extend([4, 5])
print(f"After extend([4, 5]): {demo_list}")

# remove()
demo_list.remove(3)
print(f"After remove(3): {demo_list}")

# reverse()
demo_list.reverse()
print(f"After reverse(): {demo_list}")

# clear()
demo_list_copy = demo_list.copy()
demo_list_copy.clear()
print(f"After clear(): {demo_list_copy}")

print("\nTo discover methods on any object:")
print("  1. Use dir(object) to see all methods")
print("  2. Use help(object.method) for documentation")
print("  3. In Jupyter/IPython: object.method? for quick help")
