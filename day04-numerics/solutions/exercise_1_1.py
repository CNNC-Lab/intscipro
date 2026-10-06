# Exercise 1.1: Array Creation and Basic Operations
import numpy as np

# a) Array from 10 to 50
a = np.arange(10, 51)
print("a:", a)

# b) 4x5 zeros
b = np.zeros((4, 5))
print("b:\n", b)

# c) 3x3 identity
c = np.eye(3)
print("c:\n", c)

# d) 50 evenly spaced values
d = np.linspace(0, 10, 50)
print("d:", d[:5], "...")  # Show first 5

# e) 3x4 random integers
e = np.random.randint(1, 21, size=(3, 4))
print("e:\n", e)

# f) Logarithmically spaced
f = np.logspace(0, 3, 10)
print("f:", f)
