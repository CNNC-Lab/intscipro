# check_installation.py: run after extending the environment for Day 4
#   conda env update -n scientific-programming -f environment.yml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("All packages imported successfully!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")

# Create a simple plot to test matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Test Plot - Installation Successful!")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()