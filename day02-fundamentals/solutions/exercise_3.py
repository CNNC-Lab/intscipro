"""
Exercise 3: List and String Slicing
Student: Solutions

Exploring slicing operations on strings and lists.
"""

# Define initial variables
mystring = '012345678'
mylist = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

print("=" * 50)
print("EXERCISE 3: List and String Slicing")
print("=" * 50)
print(f"\nInitial string: {mystring}")
print(f"Initial list: {mylist}")

# Part a: First five characters
print("\n" + "-" * 50)
print("Part a: First five characters of mystring")
a = mystring[:5]
print(f"a = mystring[:5] = '{a}'")

# Part b: Everything except first five characters
print("\nPart b: Everything except first five characters")
b = mystring[5:]
print(f"b = mystring[5:] = '{b}'")

# Part c: Second to next-to-last character
print("\nPart c: Second to next-to-last character")
c = mystring[1:-1]
print(f"c = mystring[1:-1] = '{c}'")
print("(Index 1 is second char, -1 is last char, so we get up to but not including last)")

# Part d: Set 3rd item in list to last value of string
print("\nPart d: Set 3rd item in mylist to last value of mystring")
print(f"Before: mylist = {mylist}")
mylist[2] = mystring[-1]  # Index 2 is the 3rd item (zero-indexed)
print(f"mylist[2] = mystring[-1]")
print(f"After: mylist = {mylist}")

# Part e: Try to set 3rd item in string (WILL FAIL)
print("\nPart e: Try to set 3rd item in mystring (THIS FAILS!)")
try:
    mystring[2] = mylist[-1]
    print(f"After: mystring = {mystring}")
except TypeError as e:
    print(f"ERROR: {e}")
    print("Explanation: Strings are IMMUTABLE - cannot change individual characters")
    print("\nAlternative solution: Convert to list, modify, convert back")
    temp_list = list(mystring)
    temp_list[2] = mylist[-1]
    mystring_modified = ''.join(temp_list)
    print(f"Modified version: {mystring_modified}")

# Reset mystring for remaining exercises
mystring = '012345678'
mylist = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

# Part f: Every second item
print("\nPart f: Every second item of mylist")
d = mylist[::2]
print(f"d = mylist[::2] = {d}")
print("(Start at beginning, go to end, step by 2)")

# Part g: Reverse order
print("\nPart g: Every item in reverse order")
e = mylist[::-1]
print(f"e = mylist[::-1] = {e}")
print("(Negative step reverses the sequence)")

# Part h: Middle three items
print("\nPart h (Challenge): Middle three items")
middle_index = len(mylist) // 2
middle_three = mylist[middle_index-1:middle_index+2]
print(f"middle_three = mylist[{middle_index-1}:{middle_index+2}] = {middle_three}")

print("\n" + "=" * 50)
print("SLICING SUMMARY")
print("=" * 50)
print("Syntax: sequence[start:stop:step]")
print("  start: inclusive (default: 0)")
print("  stop: exclusive (default: len(sequence))")
print("  step: increment (default: 1)")
print("\nUseful patterns:")
print("  [:5]     - First 5 elements")
print("  [5:]     - From 5th element to end")
print("  [1:-1]   - All except first and last")
print("  [::2]    - Every second element")
print("  [::-1]   - Reverse the sequence")
print("  [-3:]    - Last 3 elements")
print("\nKey difference: Lists are MUTABLE, Strings are IMMUTABLE")
