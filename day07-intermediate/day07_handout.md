# Day 7 Handout: Intermediate Programming Concepts
*PhD Course in Integrative Neurosciences - Introduction to Scientific Programming*

---

## Table of Contents

1. [Part I: Code Quality & Reliability](#part-i)
   - Understanding Exceptions
   - Try-Except Patterns
   - Context Managers
   - Raising Exceptions & Custom Errors
   - Assertions & Input Validation
   - Debugging Strategies

2. [Part II: Type Systems & Documentation](#part-ii)
   - Type Hints: Benefits & Basics
   - Static Type Checking
   - Docstrings (PEP 257)
   - Docstring Styles (Google, NumPy)
   - Documentation Generation (Sphinx)

3. [Part III: Programming Paradigms](#part-iii)
   - Object-Oriented Programming for Science
   - Classes: Basic Structure
   - Inheritance & Composition
   - Functional Programming Concepts
   - Map, Filter, Reduce
   - Lambda Functions & List Comprehensions

4. [Part IV: Code Organization & Testing](#part-iv)
   - Project Structure & Modularity
   - Testing Scientific Code
   - Testing Pyramid & pytest

5. [Part V: Performance & Best Practices](#part-v)
   - Code Performance & Profiling
   - Best Practices Summary
   - Resources & Further Learning

---

<a id="part-i"></a>
## Part I: Code Quality & Reliability

### Understanding Exceptions

**Bugs and errors are inevitable in scientific programming.** Even experienced developers write code that fails—it's not a matter of *if*, but *when*. In scientific workflows, errors arise from unpredictable real-world data: corrupted sensor readings, missing files, unexpected user inputs, network timeouts, or numerical edge cases like division by zero. A single unhandled exception can crash an hours-long simulation, corrupt experimental data, or invalidate published results.

**This makes robust error handling critical, not optional.** In research, stakes are high: reproducibility depends on code stability, collaborators rely on your tools working consistently, and journals increasingly scrutinize computational methods. Worse, silent failures—where code produces wrong results without crashing—can propagate errors through entire analyses undetected.

#### Common Exception Types

- **`FileNotFoundError`**: File or directory doesn't exist
- **`ValueError`**: Invalid value (e.g., `int('abc')`)
- **`ZeroDivisionError`**: Division by zero
- **`KeyError`**: Dictionary key doesn't exist
- **`IndexError`**: List index out of range
- **`TypeError`**: Wrong type for operation
- **`ImportError`**: Module import fails
- **`MemoryError`**: Out of memory
- **`RuntimeError`**: General runtime error

### Try-Except Patterns

#### Basic Try-Except

```python
def load_spike_times(filename: str) -> np.ndarray:
    """Load spike times from file with error handling."""
    try:
        data = np.loadtxt(filename)
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return np.array([])
```

#### Multiple Exceptions

```python
def safe_divide(numerator: float, denominator: float) -> float:
    """Safe division with multiple exception handling."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return np.nan
    except TypeError:
        print("Both arguments must be numbers")
        return np.nan
```

#### Generic Exception Handling (Use Sparingly)

```python
def process_data(data):
    try:
        # Complex processing
        result = analyze(data)
        return result
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

**Warning:** Catching generic `Exception` can hide bugs. Use specific exceptions when possible.

#### Else & Finally Clauses

```python
def load_and_process(filename: str):
    """Complete try-except-else-finally pattern."""
    try:
        data = np.loadtxt(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    else:
        # Runs only if no exception occurred
        print(f"Loaded {len(data)} data points")
        return process(data)
    finally:
        # Always runs (cleanup code)
        print("Operation completed")
```

### Context Managers: The `with` Statement

Context managers automatically handle setup and cleanup, even when exceptions occur. This is crucial for file operations, database connections, and resource management.

#### File Operations

```python
# ❌ Without context manager (risky)
file = open('data.txt', 'r')
data = file.read()
file.close()  # May not execute if error occurs

# ✅ With context manager (safe)
with open('data.txt', 'r') as file:
    data = file.read()
# File automatically closed, even if exception occurs
```

#### Multiple Resources

```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(process(line))
```

#### Creating Custom Context Managers

```python
from contextlib import contextmanager
import time

@contextmanager
def timing(label: str):
    """Time code execution."""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{label}: {end - start:.3f}s")

# Usage
with timing("Data loading"):
    data = np.loadtxt('large_file.txt')
```

### Raising Exceptions & Custom Errors

#### When to Raise Exceptions

Use `raise` to signal errors in your code, especially for invalid inputs or unrecoverable states.

```python
def calculate_firing_rate(spike_times: np.ndarray, duration: float) -> float:
    """Calculate firing rate in Hz."""
    if duration <= 0:
        raise ValueError("Duration must be positive")
    if len(spike_times) == 0:
        raise ValueError("No spikes provided")
    return len(spike_times) / duration
```

#### Built-in Exceptions to Raise

- **`ValueError`**: Invalid value (wrong range, format)
- **`TypeError`**: Wrong type
- **`FileNotFoundError`**: File doesn't exist
- **`RuntimeError`**: General runtime issue
- **`NotImplementedError`**: Feature not yet implemented

#### Custom Exception Classes

For domain-specific errors, create custom exceptions:

```python
class DataQualityError(Exception):
    """Raised when data quality checks fail."""
    pass

class InsufficientDataError(Exception):
    """Raised when dataset is too small for analysis."""
    pass

def analyze_neurons(spike_data: dict):
    """Analyze neural data with custom error handling."""
    if len(spike_data) < 10:
        raise InsufficientDataError("Need at least 10 neurons")
    
    if not validate_spike_times(spike_data):
        raise DataQualityError("Spike times contain invalid values")
    
    # Proceed with analysis...
```

### Assertions & Input Validation

#### `assert` vs `raise`

**`assert`**: For debugging and catching programmer errors (development)
```python
def process_spike_train(spikes: np.ndarray):
    assert spikes.ndim == 1, "Spikes must be 1D array"
    assert len(spikes) > 0, "Empty spike train"
    # Process...
```

**`raise`**: For user errors and runtime validation (production)
```python
def process_spike_train(spikes: np.ndarray):
    if spikes.ndim != 1:
        raise ValueError("Spikes must be 1D array")
    if len(spikes) == 0:
        raise ValueError("Empty spike train")
    # Process...
```

**Key difference:** `assert` statements are removed when Python runs in optimized mode (`python -O`), so never rely on them for critical validation.

#### Common Validation Patterns

```python
def validate_neuron_params(tau_m: float, v_rest: float, v_thresh: float):
    """Validate neuron model parameters."""
    
    # Type checking
    if not isinstance(tau_m, (int, float)):
        raise TypeError("tau_m must be a number")
    
    # Range checking
    if tau_m <= 0:
        raise ValueError("tau_m must be positive")
    
    # Logical consistency
    if v_rest >= v_thresh:
        raise ValueError("v_rest must be less than v_thresh")
    
    # Value constraints
    if not -100 <= v_rest <= 0:
        raise ValueError("v_rest must be between -100 and 0 mV")
```

#### Defensive Programming

Validate inputs early and explicitly:

```python
def load_experimental_data(filename: str, required_fields: list):
    """Load and validate experimental data."""
    # Check file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Data file not found: {filename}")
    
    # Load data
    data = pd.read_csv(filename)
    
    # Validate required fields
    missing_fields = set(required_fields) - set(data.columns)
    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")
    
    # Check data quality
    if data.isnull().any().any():
        raise DataQualityError("Data contains missing values")
    
    return data
```

### Debugging Strategies

#### The Python Debugger (pdb)

```python
import pdb

def complex_analysis(data):
    result = []
    for item in data:
        pdb.set_trace()  # Debugger stops here
        processed = process(item)
        result.append(processed)
    return result
```

**pdb commands:**
- `n` (next): Execute next line
- `s` (step): Step into function
- `c` (continue): Continue execution
- `l` (list): Show code context
- `p variable`: Print variable value
- `q` (quit): Exit debugger

#### Using VS Code Debugger

1. Set breakpoints by clicking line numbers
2. Press F5 to start debugging
3. Inspect variables in left panel
4. Use debug console for expressions

#### Debugging Scientific Code

**Strategy 1: Reduce Problem Size**
```python
# Instead of debugging with full dataset
data = load_full_dataset()  # 100GB

# Debug with small sample
data = load_full_dataset()[:100]  # First 100 rows
```

**Strategy 2: Visualize Intermediate Results**
```python
def train_model(data, epochs=100):
    losses = []
    for epoch in range(epochs):
        loss = train_epoch(data)
        losses.append(loss)
        
        # Debug visualization
        if epoch % 10 == 0:
            plt.plot(losses)
            plt.savefig(f'debug_epoch_{epoch}.png')
    return model
```

**Strategy 3: Unit Testing as Debugging**
```python
def test_firing_rate_calculation():
    """Test with known ground truth."""
    spikes = np.array([0.1, 0.2, 0.3])
    duration = 1.0
    expected_rate = 3.0
    
    actual_rate = calculate_firing_rate(spikes, duration)
    assert np.isclose(actual_rate, expected_rate)
```

---

<a id="part-ii"></a>
## Part II: Type Systems & Documentation

### Type Hints: Benefits & Basics

#### Why Type Hints?

Type hints are **optional annotations** that specify expected types for variables, function parameters, and return values. They don't affect runtime behavior but provide multiple benefits:

1. **Catch bugs early** (via static analysis with `mypy`)
2. **Better IDE support** (autocomplete, refactoring)
3. **Self-documenting code** (types explain intent)
4. **Easier collaboration** (clear interfaces)

#### Basic Type Annotations

```python
from typing import List, Dict, Tuple, Optional

# Variables
age: int = 30
name: str = "Renato"
spike_times: List[float] = [0.1, 0.2, 0.3]

# Functions
def calculate_mean(data: List[float]) -> float:
    """Calculate mean of data."""
    return sum(data) / len(data)

# Optional types (can be None)
def find_neuron(neuron_id: int) -> Optional[dict]:
    """Find neuron by ID, return None if not found."""
    # ...
    return None
```

#### Scientific Python Types

```python
import numpy as np
import pandas as pd
from numpy.typing import NDArray

# NumPy arrays
def smooth_signal(signal: NDArray[np.float64], window: int) -> NDArray[np.float64]:
    """Smooth 1D signal with moving average."""
    # ...

# Pandas DataFrames
def process_trials(df: pd.DataFrame) -> pd.DataFrame:
    """Process experimental trial data."""
    # ...

# Multiple return values
def analyze_spikes(spike_times: NDArray) -> Tuple[float, float, int]:
    """Return mean rate, CV, and spike count."""
    rate = calculate_rate(spike_times)
    cv = calculate_cv(spike_times)
    count = len(spike_times)
    return rate, cv, count
```

#### Advanced Type Hints

```python
from typing import Union, Callable, TypeVar

# Union types (multiple allowed types)
def load_data(source: Union[str, Path]) -> np.ndarray:
    """Load from file path or Path object."""
    # ...

# Callable (function types)
def apply_transform(data: np.ndarray, 
                   func: Callable[[float], float]) -> np.ndarray:
    """Apply function to each element."""
    return np.array([func(x) for x in data])

# Generic types
T = TypeVar('T')
def first(items: List[T]) -> T:
    """Return first item (works with any type)."""
    return items[0]
```

### Static Type Checking with mypy

**Install mypy:**
```bash
pip install mypy
```

**Check your code:**
```bash
mypy script.py
```

**Example type error:**
```python
def calculate_rate(spike_count: int, duration: float) -> float:
    return spike_count / duration

rate = calculate_rate(10, "5.0")  # mypy catches this!
# error: Argument 2 has incompatible type "str"; expected "float"
```

**Configure mypy** (`mypy.ini`):
```ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = False
```

### Docstrings (PEP 257)

**PEP 257** defines conventions for Python docstrings (documentation strings).

#### One-Line Docstrings

For simple, obvious functions:

```python
def square(x: float) -> float:
    """Return the square of x."""
    return x ** 2
```

**Rules:**
- Triple double quotes (`"""`)
- Imperative mood ("Return..." not "Returns...")
- One line, fits on same line as quotes
- No blank lines before or after

#### Multi-Line Docstrings

For complex functions needing detailed explanation:

```python
def calculate_firing_rate(spike_times: np.ndarray, 
                          duration: float,
                          window: Optional[float] = None) -> float:
    """Calculate the firing rate of a neuron.
    
    Computes the average firing rate in Hz from an array of spike times.
    Optionally calculates rate within a specific time window.
    
    Args:
        spike_times: Array of spike times in seconds
        duration: Total duration of recording in seconds
        window: Optional time window for rate calculation
        
    Returns:
        Firing rate in Hz (spikes per second)
        
    Raises:
        ValueError: If duration <= 0 or spike_times is empty
        
    Example:
        >>> spikes = np.array([0.1, 0.2, 0.5, 0.8])
        >>> rate = calculate_firing_rate(spikes, duration=1.0)
        >>> print(f"{rate:.2f} Hz")
        4.00 Hz
    """
    if duration <= 0:
        raise ValueError("Duration must be positive")
    if len(spike_times) == 0:
        raise ValueError("No spikes provided")
    
    if window:
        spike_times = spike_times[spike_times <= window]
        duration = window
    
    return len(spike_times) / duration
```

**Structure:**
1. Summary line (imperative mood)
2. Blank line
3. Detailed description
4. Blank line
5. Sections: Args, Returns, Raises, Example

### Docstring Styles

#### Google Style

```python
def train_network(inputs: np.ndarray, 
                  targets: np.ndarray,
                  learning_rate: float = 0.01,
                  epochs: int = 100) -> dict:
    """Train a neural network model.
    
    Trains the network using gradient descent on the provided
    input-target pairs. Returns training history.
    
    Args:
        inputs: Input data of shape (n_samples, n_features)
        targets: Target values of shape (n_samples, n_outputs)
        learning_rate: Learning rate for gradient descent (default: 0.01)
        epochs: Number of training epochs (default: 100)
        
    Returns:
        Dictionary containing:
            - 'loss': List of loss values per epoch
            - 'accuracy': List of accuracy values per epoch
            - 'weights': Final network weights
            
    Raises:
        ValueError: If inputs and targets have incompatible shapes
        
    Example:
        >>> X = np.random.randn(100, 10)
        >>> y = np.random.randn(100, 1)
        >>> history = train_network(X, y, learning_rate=0.001)
        >>> plt.plot(history['loss'])
    """
    # Implementation...
```

#### NumPy Style

```python
def calculate_isi_distribution(spike_times: np.ndarray,
                               bins: int = 50) -> Tuple[np.ndarray, np.ndarray]:
    """Calculate inter-spike interval (ISI) distribution.
    
    Computes the distribution of time intervals between consecutive
    spikes and returns histogram values and bin edges.
    
    Parameters
    ----------
    spike_times : np.ndarray
        Array of spike times in seconds, must be sorted
    bins : int, optional
        Number of histogram bins (default: 50)
        
    Returns
    -------
    counts : np.ndarray
        Histogram counts for each bin
    edges : np.ndarray
        Bin edges (length = bins + 1)
        
    Raises
    ------
    ValueError
        If spike_times contains fewer than 2 spikes
        
    See Also
    --------
    calculate_cv : Calculate coefficient of variation
    plot_isi : Plot ISI distribution
    
    Examples
    --------
    >>> spikes = np.array([0.1, 0.15, 0.3, 0.32, 0.5])
    >>> counts, edges = calculate_isi_distribution(spikes, bins=10)
    >>> plt.stairs(counts, edges)
    """
    if len(spike_times) < 2:
        raise ValueError("Need at least 2 spikes")
    
    isis = np.diff(spike_times)
    counts, edges = np.histogram(isis, bins=bins)
    return counts, edges
```

**Key differences:**
- Google style uses indented lists
- NumPy style uses section headers with underlines
- NumPy style adds "See Also" and more structured sections

### Documentation Generation with Sphinx

**Sphinx** converts docstrings into professional HTML/PDF documentation automatically.

#### Quick Setup

```bash
# Install Sphinx
pip install sphinx sphinx-rtd-theme

# Create docs directory
mkdir docs
cd docs

# Initialize Sphinx
sphinx-quickstart

# Configure conf.py (add these lines)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google/NumPy docstrings
    'sphinx.ext.viewcode',
]
html_theme = 'sphinx_rtd_theme'
```

#### Document Your Module

Create `docs/source/index.rst`:
```rst
Welcome to My Project Documentation
====================================

.. automodule:: my_module
   :members:
   :undoc-members:
   :show-inheritance:
```

#### Build Documentation

```bash
cd docs
make html

# View in browser
open _build/html/index.html
```

#### Other Tools

- **MkDocs**: Markdown-based documentation (simpler than Sphinx)
- **pdoc**: Auto-generate API docs with zero configuration
- **Read the Docs**: Free hosting for documentation

**Examples:**
- NumPy docs: https://numpy.org/doc/
- Pandas docs: https://pandas.pydata.org/docs/
- SciPy docs: https://docs.scipy.org/

---

<a id="part-iii"></a>
## Part III: Programming Paradigms

### Object-Oriented Programming for Science

#### Why OOP?

**Use OOP when you need:**
- Complex state management (e.g., neuron models with internal variables)
- Multiple related behaviors grouped together
- Code reusability through inheritance
- Clear interfaces for large projects

**Python's philosophy:** "Everything is an object" BUT "You don't always need to create classes"

#### Core Concepts

- **Class**: Blueprint for objects (template)
- **Object**: Instance of a class (actual thing)
- **Attributes**: Data stored in object (properties)
- **Methods**: Functions that operate on object (behaviors)
- **Inheritance**: IS-A relationship (subclass inherits from parent)
- **Composition**: HAS-A relationship (object contains other objects)

#### When NOT to Use OOP

Simple scripts, data processing pipelines, quick analyses often work better with functions and dictionaries. Don't over-engineer.

### Classes: Basic Structure

```python
class Neuron:
    """Leaky integrate-and-fire neuron model."""
    
    def __init__(self, tau_m: float = 10.0, v_rest: float = -65.0, 
                 v_thresh: float = -50.0, v_reset: float = -70.0):
        """Initialize neuron parameters.
        
        Args:
            tau_m: Membrane time constant (ms)
            v_rest: Resting potential (mV)
            v_thresh: Firing threshold (mV)
            v_reset: Reset potential after spike (mV)
        """
        # Attributes
        self.tau_m = tau_m
        self.v_rest = v_rest
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.v = v_rest  # Current membrane potential
        self.spike_times: List[float] = []
    
    def integrate(self, current: float, dt: float) -> bool:
        """Integrate input current for one time step.
        
        Args:
            current: Input current (nA)
            dt: Time step (ms)
            
        Returns:
            True if neuron fired, False otherwise
        """
        # Leaky integration
        dv = (-(self.v - self.v_rest) + current) / self.tau_m * dt
        self.v += dv
        
        # Check for spike
        if self.v >= self.v_thresh:
            self.v = self.v_reset
            return True
        return False
    
    def get_firing_rate(self, duration: float) -> float:
        """Calculate average firing rate.
        
        Args:
            duration: Total simulation time (ms)
            
        Returns:
            Firing rate in Hz
        """
        return len(self.spike_times) / (duration / 1000.0)

# Usage
neuron = Neuron(tau_m=10.0, v_rest=-65.0)
for t in range(1000):
    fired = neuron.integrate(current=1.5, dt=0.1)
    if fired:
        neuron.spike_times.append(t * 0.1)

print(f"Rate: {neuron.get_firing_rate(100.0):.2f} Hz")
```

### Inheritance & Composition

#### Inheritance: IS-A Relationships

Use when subclass **is a specialized version** of parent class.

```python
class ExcitatoryNeuron(Neuron):
    """Excitatory neuron (IS-A Neuron)."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.neuron_type = "excitatory"
        self.neurotransmitter = "glutamate"
    
    def connect(self, target: 'Neuron', weight: float):
        """Connect to target with positive weight."""
        if weight < 0:
            raise ValueError("Excitatory weights must be positive")
        # Connection logic...


class InhibitoryNeuron(Neuron):
    """Inhibitory neuron (IS-A Neuron)."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.neuron_type = "inhibitory"
        self.neurotransmitter = "GABA"
    
    def connect(self, target: 'Neuron', weight: float):
        """Connect to target with negative weight."""
        if weight > 0:
            raise ValueError("Inhibitory weights must be negative")
        # Connection logic...
```

#### Composition: HAS-A Relationships

Use when class **contains** other objects as components.

```python
class NeuralNetwork:
    """Network HAS-A collection of neurons (composition)."""
    
    def __init__(self):
        self.neurons: List[Neuron] = []
        self.connections: List[Tuple[int, int, float]] = []
    
    def add_neuron(self, neuron: Neuron):
        """Add neuron to network."""
        self.neurons.append(neuron)
    
    def connect(self, source_idx: int, target_idx: int, weight: float):
        """Connect two neurons."""
        self.connections.append((source_idx, target_idx, weight))
    
    def simulate(self, duration: float, dt: float):
        """Run network simulation."""
        n_steps = int(duration / dt)
        for step in range(n_steps):
            # Update each neuron
            for i, neuron in enumerate(self.neurons):
                # Calculate input from connections
                total_input = self._calculate_input(i)
                fired = neuron.integrate(total_input, dt)
                if fired:
                    neuron.spike_times.append(step * dt)

# Usage
network = NeuralNetwork()
network.add_neuron(ExcitatoryNeuron(tau_m=10.0))
network.add_neuron(InhibitoryNeuron(tau_m=15.0))
network.connect(source_idx=0, target_idx=1, weight=0.5)
network.simulate(duration=1000.0, dt=0.1)
```

**Rule of thumb:** Favor composition over inheritance. Inheritance creates tight coupling; composition is more flexible.

### Functional Programming Concepts

#### Core Ideas

**Functional programming** emphasizes:
1. **Pure functions**: Output depends only on inputs, no side effects
2. **Immutability**: Data isn't modified in place
3. **First-class functions**: Functions as values (can be passed around)
4. **Higher-order functions**: Functions that take/return functions

#### Why Functional Programming?

**Benefits for science:**
- **Reproducibility**: Pure functions always produce same output
- **Testability**: Easy to test functions without setup/teardown
- **Parallelization**: No shared state = easier parallel execution
- **Debugging**: No hidden state changes

#### Pure vs Impure Functions

```python
# ❌ IMPURE: Modifies external state
results = []
def add_result(x):
    results.append(x * 2)
    return x * 2

# ✅ PURE: No side effects
def double(x):
    return x * 2

# Usage of pure function
results = [double(x) for x in data]
```

```python
# ❌ IMPURE: Depends on external state
threshold = 10
def above_threshold(x):
    return x > threshold  # Depends on external variable

# ✅ PURE: All dependencies are parameters
def above_threshold(x, threshold=10):
    return x > threshold
```

#### First-Class and Higher-Order Functions

```python
# Functions as values
operations = {
    'mean': np.mean,
    'std': np.std,
    'median': np.median
}

def apply_stat(data, stat_name):
    """Higher-order function: takes function name, applies it."""
    stat_func = operations[stat_name]
    return stat_func(data)

# Functions that return functions
def make_threshold_detector(threshold):
    """Returns a function that detects values above threshold."""
    def detector(x):
        return x > threshold
    return detector

detector_10 = make_threshold_detector(10)
detector_20 = make_threshold_detector(20)

print(detector_10(15))  # True
print(detector_20(15))  # False
```

### Map, Filter, Reduce

These are fundamental functional operations for transforming collections.

#### Map: Transform Each Element

```python
# Convert spike times from ms to seconds
spike_times = np.array([100, 250, 380, 520])  # ms

# Functional approach
spike_times_sec = list(map(lambda t: t / 1000, spike_times))
# [0.1, 0.25, 0.38, 0.52]

# NumPy (more efficient for arrays)
spike_times_sec = spike_times / 1000
```

#### Filter: Select Elements

```python
# Keep only spikes in first 500ms
spike_times = np.array([100, 250, 380, 520, 680])  # ms

# Functional approach
early_spikes = list(filter(lambda t: t < 500, spike_times))
# [100, 250, 380]

# NumPy (more efficient)
early_spikes = spike_times[spike_times < 500]
```

#### Reduce: Combine Elements

```python
from functools import reduce

# Calculate total inter-spike interval
spike_times = [0.1, 0.2, 0.5, 0.8]  # seconds

# Functional approach: sum of differences
isis = [spike_times[i+1] - spike_times[i] for i in range(len(spike_times)-1)]
total_isi = reduce(lambda acc, x: acc + x, isis, 0)
# 0.7 seconds

# More Pythonic
total_isi = sum(np.diff(spike_times))
```

#### Practical Example: Data Processing Pipeline

```python
# Process spike trains functionally
def process_spike_train(spike_times, duration):
    """Functional pipeline for spike train analysis."""
    # 1. Filter: Remove artifacts (ISI < 2ms)
    def valid_spike(t, prev_t):
        return (t - prev_t) >= 0.002
    
    filtered = [spike_times[0]]
    for t in spike_times[1:]:
        if valid_spike(t, filtered[-1]):
            filtered.append(t)
    
    # 2. Map: Convert to ISIs
    isis = list(map(lambda i: filtered[i+1] - filtered[i], 
                   range(len(filtered)-1)))
    
    # 3. Reduce: Calculate statistics
    mean_isi = sum(isis) / len(isis) if isis else 0
    cv = np.std(isis) / mean_isi if mean_isi > 0 else 0
    
    return {
        'rate': len(filtered) / duration,
        'cv': cv,
        'n_spikes': len(filtered)
    }
```

### Lambda Functions & List Comprehensions

#### Lambda Functions: Anonymous Functions

Lambdas are **one-line functions** without a name, useful for short operations.

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Common use: sorting
neurons = [
    {'id': 1, 'rate': 15.3},
    {'id': 2, 'rate': 8.7},
    {'id': 3, 'rate': 22.1}
]

# Sort by firing rate
sorted_neurons = sorted(neurons, key=lambda n: n['rate'])

# Multiple arguments
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Used with map/filter
spike_times = [0.1, 0.2, 0.3, 0.5, 0.8]
isis = list(map(lambda i: spike_times[i+1] - spike_times[i], 
                range(len(spike_times)-1)))
```

**When to use:** Short, throwaway functions (sorting, filtering). For complex logic, use regular functions.

#### List Comprehensions: Pythonic Loops

More readable and faster than explicit loops.

```python
# ❌ Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# ✅ List comprehension
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehension (matrix operations)
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Dictionary comprehension
neuron_ids = [1, 2, 3, 4]
firing_rates = [12.5, 8.3, 15.7, 9.2]
rate_dict = {nid: rate for nid, rate in zip(neuron_ids, firing_rates)}
# {1: 12.5, 2: 8.3, 3: 15.7, 4: 9.2}

# Set comprehension (unique values)
spike_bins = {int(t // 0.1) for t in spike_times}

# Generator expression (memory-efficient)
spike_sum = sum(t for t in spike_times if t < 1.0)  # No list created
```

#### Scientific Example: Data Transformation

```python
# Process multiple neurons efficiently
spike_data = {
    'neuron_1': np.array([0.1, 0.2, 0.5, 0.8]),
    'neuron_2': np.array([0.15, 0.3, 0.45, 0.9]),
    'neuron_3': np.array([0.05, 0.25, 0.55, 0.75])
}

# Calculate firing rates for all neurons
duration = 1.0
firing_rates = {
    neuron_id: len(spikes) / duration 
    for neuron_id, spikes in spike_data.items()
}

# Filter high-rate neurons
high_rate_neurons = [
    nid for nid, rate in firing_rates.items() 
    if rate > 3.0
]

# Calculate CV for each neuron
cvs = {
    nid: np.std(np.diff(spikes)) / np.mean(np.diff(spikes))
    for nid, spikes in spike_data.items()
    if len(spikes) > 1
}
```

---

<a id="part-iv"></a>
## Part IV: Code Organization & Testing

### Project Structure & Modularity

#### Standard Python Project Layout

```
my_project/
├── my_package/          # Main package
│   ├── __init__.py      # Makes it a package
│   ├── core.py          # Core functionality
│   ├── analysis.py      # Analysis functions
│   ├── utils.py         # Utility functions
│   └── models/          # Subpackage for models
│       ├── __init__.py
│       └── neuron.py
├── tests/               # Test directory
│   ├── test_core.py
│   └── test_analysis.py
├── data/                # Data files
├── notebooks/           # Jupyter notebooks
├── docs/                # Documentation
├── requirements.txt     # Dependencies
├── setup.py             # Installation script
└── README.md           # Project description
```

#### Modularity Principles

**1. Single Responsibility Principle (SRP)**
Each module/function should do ONE thing well.

```python
# ❌ BAD: One function does everything
def process_data(filename):
    # Loading
    data = pd.read_csv(filename)
    # Cleaning
    data = data.dropna()
    # Analysis
    result = data.mean()
    # Plotting
    plt.plot(result)
    return result

# ✅ GOOD: Separate concerns
def load_data(filename):
    return pd.read_csv(filename)

def clean_data(data):
    return data.dropna()

def analyze_data(data):
    return data.mean()

def plot_results(result):
    plt.plot(result)
```

**2. Separation of Concerns**
Organize by functionality, not file type.

```python
# ❌ BAD: Everything in one file
# analysis_script.py (1000 lines)

# ✅ GOOD: Separate modules
# data_loading.py
# preprocessing.py
# models.py
# visualization.py
# main.py (orchestrates)
```

**3. Don't Repeat Yourself (DRY)**
Reuse code through functions and modules.

**4. Clear Dependencies**
Import what you need, make dependencies explicit.

```python
# ✅ GOOD: Explicit imports
from my_package.analysis import calculate_firing_rate
from my_package.models import LIFNeuron

# ❌ AVOID: Wildcard imports
from my_package.analysis import *
```

### Testing Scientific Code

#### Why Test?

**Because bugs in science = wrong results = invalid conclusions**

Testing ensures:
1. **Correctness**: Code does what you think it does
2. **Reproducibility**: Results don't change unexpectedly
3. **Confidence**: Safe to refactor and extend code
4. **Documentation**: Tests show how code should be used

#### What to Test?

**Essential tests:**
- **Data processing**: Loading, cleaning, transformations
- **Calculations**: Statistical tests, model fitting, numerical methods
- **Edge cases**: Empty data, zero values, extreme inputs
- **Model outputs**: Expected behavior on known inputs

**Example: Test Firing Rate Calculation**

```python
import numpy as np
import pytest

def calculate_firing_rate(spike_times: np.ndarray, duration: float) -> float:
    """Calculate firing rate in Hz."""
    if duration <= 0:
        raise ValueError("Duration must be positive")
    return len(spike_times) / duration

def test_firing_rate_basic():
    """Test firing rate with known input."""
    spikes = np.array([0.1, 0.2, 0.3, 0.4])
    rate = calculate_firing_rate(spikes, duration=1.0)
    assert rate == 4.0

def test_firing_rate_empty():
    """Test with no spikes."""
    spikes = np.array([])
    rate = calculate_firing_rate(spikes, duration=1.0)
    assert rate == 0.0

def test_firing_rate_invalid_duration():
    """Test error handling for invalid duration."""
    spikes = np.array([0.1, 0.2])
    with pytest.raises(ValueError):
        calculate_firing_rate(spikes, duration=0)

def test_firing_rate_numerical():
    """Test numerical precision for scientific data."""
    spikes = np.random.rand(1000) * 10.0  # 1000 spikes over 10s
    rate = calculate_firing_rate(spikes, duration=10.0)
    # Use approximate equality for floating-point
    np.testing.assert_allclose(rate, 100.0, rtol=1e-10)
```

**For numerical tests**, use `np.testing.assert_allclose()` instead of == to handle floating-point precision.

### Testing Pyramid & pytest

#### Testing Pyramid

```
     /\
    /E2E\      ← Few: Full system tests
   /------\
  /Integration\ ← Some: Module interactions
 /------------\
/  Unit Tests  \ ← Many: Individual functions
```

- **Unit tests** (70%): Test individual functions
- **Integration tests** (20%): Test modules working together
- **End-to-end tests** (10%): Test complete workflows

Focus on unit tests—they're fast, specific, and catch most bugs.

#### pytest Basics

**Install:**
```bash
pip install pytest
```

**Run tests:**
```bash
pytest                 # Run all tests
pytest test_core.py    # Run specific file
pytest -v              # Verbose output
pytest -k "firing"     # Run tests matching "firing"
```

**Test structure:**
```python
# test_analysis.py
import pytest
import numpy as np
from my_package.analysis import calculate_cv, smooth_signal

def test_cv_regular_spiking():
    """Test CV for regular spiking (CV ≈ 0)."""
    spike_times = np.arange(0, 1.0, 0.1)  # Regular 10 Hz
    cv = calculate_cv(spike_times)
    assert cv < 0.1  # Nearly regular

def test_cv_irregular_spiking():
    """Test CV for irregular spiking (CV > 0.5)."""
    spike_times = np.array([0.01, 0.05, 0.3, 0.32, 0.9])
    cv = calculate_cv(spike_times)
    assert cv > 0.5  # Clearly irregular

def test_smooth_signal_length():
    """Test that smoothing preserves signal length."""
    signal = np.random.randn(1000)
    smoothed = smooth_signal(signal, window=5)
    assert len(smoothed) == len(signal)
```

#### Advanced pytest Features

**1. Parametrized tests** (test multiple inputs)
```python
@pytest.mark.parametrize("spike_times,duration,expected", [
    (np.array([0.1, 0.2, 0.3]), 1.0, 3.0),
    (np.array([0.1, 0.2]), 2.0, 1.0),
    (np.array([]), 1.0, 0.0),
])
def test_firing_rate_parametrized(spike_times, duration, expected):
    """Test firing rate with multiple cases."""
    rate = calculate_firing_rate(spike_times, duration)
    assert rate == expected
```

**2. Fixtures** (reusable test data)
```python
@pytest.fixture
def sample_spike_data():
    """Provide sample spike data for tests."""
    return {
        'neuron_1': np.array([0.1, 0.2, 0.5]),
        'neuron_2': np.array([0.15, 0.3, 0.45])
    }

def test_process_neurons(sample_spike_data):
    """Test processing with fixture data."""
    result = process_neurons(sample_spike_data)
    assert 'neuron_1' in result
```

**3. Testing for approximate equality**
```python
def test_mean_calculation():
    """Test mean with floating-point tolerance."""
    data = np.array([1.0, 2.0, 3.0])
    result = calculate_mean(data)
    assert result == pytest.approx(2.0, rel=1e-6)
```

**4. Testing exceptions**
```python
def test_invalid_input_raises():
    """Test that invalid input raises appropriate error."""
    with pytest.raises(ValueError, match="Duration must be positive"):
        calculate_firing_rate(np.array([0.1]), duration=-1.0)
```

---

<a id="part-v"></a>
## Part V: Performance & Best Practices

### Code Performance & Profiling

#### When to Optimize

**Rules:**
1. **"Make it work, make it right, make it fast"** (in that order)
2. **"Premature optimization is the root of all evil"** (Donald Knuth)
3. **Measure first, optimize second** (don't guess bottlenecks)

**When to care about performance:**
- Code runs repeatedly (in loops, on large datasets)
- Execution time is unacceptable for your workflow
- You've profiled and identified the bottleneck

#### Profiling with cProfile

```python
import cProfile
import pstats

def analyze_dataset(data):
    # Your analysis code
    pass

# Profile code
profiler = cProfile.Profile()
profiler.enable()

analyze_dataset(my_data)

profiler.disable()

# Print results
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 slowest functions
```

**Command-line profiling:**
```bash
python -m cProfile -s cumulative script.py
```

#### Profiling with line_profiler

For line-by-line profiling:

```bash
pip install line_profiler
```

```python
# Add @profile decorator to function
@profile
def slow_function(data):
    result = []
    for item in data:
        result.append(process(item))
    return result
```

**Run:**
```bash
kernprof -l -v script.py
```

#### Quick Performance Wins

**1. Use NumPy for numerical operations**
```python
# ❌ SLOW: Python loop
result = []
for x in data:
    result.append(x ** 2)

# ✅ FAST: NumPy vectorization
result = data ** 2  # 10-100x faster
```

**2. List comprehensions over loops**
```python
# ❌ SLOWER
result = []
for x in data:
    if x > 0:
        result.append(x ** 2)

# ✅ FASTER
result = [x**2 for x in data if x > 0]
```

**3. Avoid repeated calculations**
```python
# ❌ BAD: Recalculates len() every iteration
for i in range(len(spike_times)):
    process(spike_times[i])

# ✅ GOOD: Direct iteration
for spike_time in spike_times:
    process(spike_time)
```

**4. Use appropriate data structures**
```python
# ❌ SLOW: Check membership in list
if neuron_id in neuron_list:  # O(n)
    process(neuron_id)

# ✅ FAST: Check membership in set
if neuron_id in neuron_set:  # O(1)
    process(neuron_id)
```

### Best Practices Summary

#### Professional Code Checklist

**✅ Reliability**
- [ ] Error handling for expected failures
- [ ] Input validation for functions
- [ ] Graceful degradation (don't crash, fail informatively)

**✅ Clarity**
- [ ] Type hints for function signatures
- [ ] Docstrings for public functions/classes
- [ ] Meaningful variable names (`firing_rate` not `fr`)
- [ ] Comments for complex logic only

**✅ Organization**
- [ ] Modular structure (separate concerns)
- [ ] Reusable functions (DRY principle)
- [ ] Clear imports (no wildcards)

**✅ Testing**
- [ ] Unit tests for core functions
- [ ] Test edge cases and error conditions
- [ ] Target >70% code coverage

**✅ Version Control**
- [ ] Git repository with meaningful commits
- [ ] `.gitignore` (exclude data, `__pycache__`, etc.)
- [ ] README with usage instructions

**✅ Reproducibility**
- [ ] `requirements.txt` or `environment.yml`
- [ ] Random seeds for stochastic processes
- [ ] Document computational environment

#### The Zen of Python

**Key principles:**
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- Errors should never pass silently
- In the face of ambiguity, refuse the temptation to guess

### Day 7 Key Takeaways
1. **Error handling** is not optional—it's how code stays reliable
2. **Type hints** make code self-documenting and catch bugs early
3. **Docstrings** turn code into reusable tools
4. **OOP** is powerful when you need complex state and behavior
5. **Functional programming** makes code testable and reproducible
6. **Testing** gives confidence to change code without breaking it
7. **Profiling** finds real bottlenecks—don't optimize blindly

### Practice Exercise

**Task:** Refactor and improve this code
```python
# Bad code (fix this!)
def calc(d, t):
    r = []
    for x in d:
        if t == 1:
            r.append(x * 2)
        elif t == 2:
            r.append(x / 2)
    return r
```

**Improvements to make:**
1. Add type hints
2. Write docstring
3. Better names
4. Error handling
5. Write tests

### Resources

**Official Documentation:**
- [PEP 8 – Style Guide](https://pep8.org/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [pytest Documentation](https://docs.pytest.org/)
- [Type Hints (PEP 484)](https://peps.python.org/pep-0484/)

**Books:**
- *Effective Python* by Brett Slatkin
- *Python Testing with pytest* by Brian Okken

**Tutorials:**
- [Real Python](https://realpython.com/)
- [Python Packaging Guide](https://packaging.python.org/)

**Tools:**
- `black` – Code formatter
- `mypy` – Static type checker
- `pylint` – Code linter
- `pytest` – Testing framework

---
*This handout is part of the "Introduction to Scientific Programming" course at CNC-UC, University of Coimbra. For questions or clarifications, please contact the course instructor.*
**Document Version**: 1.0  
**License**: CC BY 4.0
