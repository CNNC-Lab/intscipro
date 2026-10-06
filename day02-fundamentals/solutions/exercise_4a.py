"""
Exercise 4a: Writing to Screen
Student: Solutions

Basic output formatting with f-strings.
"""

print("=" * 50)
print("EXERCISE 4a: Writing to Screen")
print("=" * 50)

# Basic information
name = "Ana Silva"
research_interest = "Synaptic plasticity in hippocampal neurons"

# Method 1: Simple prints
print("\nMethod 1: Simple prints")
print("Name:", name)
print("Research interest:", research_interest)

# Method 2: F-strings (recommended for Python 3.6+)
print("\nMethod 2: F-strings")
print(f"Name: {name}")
print(f"Research interest: {research_interest}")

# Method 3: Combined message
print("\nMethod 3: Combined formatted message")
message = f"Hello! I'm {name} and I study {research_interest}."
print(message)

# Method 4: Multi-line formatted output
print("\nMethod 4: Professional format")
print("-" * 60)
print(f"{'Researcher Profile':^60}")
print("-" * 60)
print(f"Name:               {name}")
print(f"Research Area:      {research_interest}")
print(f"Institution:        Center for Neuroscience and Cell Biology")
print(f"University:         University of Coimbra")
print("-" * 60)

# Additional formatting examples
print("\nBonus: Advanced formatting")
hours_per_week = 45
success_rate = 0.847

print(f"Hours per week:     {hours_per_week:>3d}")
print(f"Success rate:       {success_rate:>6.1%}")
print(f"Success rate:       {success_rate:.3f}")
