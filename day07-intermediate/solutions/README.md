# Day 7 Exercise Solutions

Complete solutions for all Day 7 exercises on intermediate programming concepts.

## Overview

These solutions demonstrate:
- ✅ Error handling with try-except
- ✅ Type hints and type checking
- ✅ Comprehensive docstrings (NumPy style)
- ✅ Object-oriented programming
- ✅ Functional programming patterns
- ✅ Unit testing with pytest
- ✅ Code refactoring and best practices
- ✅ Context managers
- ✅ Protocols and dataclasses

## Files

### Exercise 1: Robust Data Loading
**File:** `exercise_1_robust_data_loading.py`

Implements a robust spike data loader with:
- Custom exception class (`DataQualityError`)
- Comprehensive error handling
- Input validation (NaN, negative values, missing columns)
- Type hints and detailed docstrings
- Built-in test suite

**Run:**
```bash
python exercise_1_robust_data_loading.py
```

### Exercise 2: LIF Neuron Class
**File:** `exercise_2_lif_neuron.py`

Complete Leaky Integrate-and-Fire neuron implementation with:
- Full type hints including `numpy.typing.NDArray`
- Property decorators (`@property`)
- Parameter validation
- Comprehensive docstrings
- Methods for firing rate and ISI statistics

**Run:**
```bash
python exercise_2_lif_neuron.py
```

### Exercise 3: Functional Programming
**File:** `exercise_3_functional_programming.py`

Demonstrates functional programming patterns:
- Map, filter, reduce operations
- Lambda functions
- List/dict comprehensions
- Function composition
- Transformation pipelines

**Run:**
```bash
python exercise_3_functional_programming.py
```

### Exercise 4: Unit Testing
**Files:** 
- `spike_analysis.py` - Module to test
- `test_spike_analysis.py` - Complete test suite

Comprehensive pytest test suite featuring:
- Fixtures for reusable test data
- Parametrized tests
- Test classes for organization
- Edge case testing
- `pytest.approx` for floating-point comparisons
- `pytest.raises` for exception testing

**Run:**
```bash
# Run all tests
pytest test_spike_analysis.py -v

# Run with coverage
pytest test_spike_analysis.py --cov=spike_analysis --cov-report=term

# Run specific test class
pytest test_spike_analysis.py::TestFiringRate -v
```

### Exercise 5: Refactoring Challenge
**File:** `exercise_5_refactored.py`

Professional refactoring demonstrating:
- Meaningful variable/function names
- Enum for constants (no magic numbers)
- Type hints throughout
- Google/NumPy style docstrings
- Context managers for file I/O
- Comprehensive error handling
- Built-in test suite

**Run:**
```bash
python exercise_5_refactored.py
```

### Bonus Challenge: Complete Pipeline
**File:** `bonus_complete_pipeline.py`

Full-featured analysis pipeline showcasing:
- Dataclasses (`@dataclass`)
- Protocols for duck typing
- OOP with multiple classes
- Functional programming patterns
- JSON serialization/deserialization
- Context managers
- Comprehensive test suite
- Report generation

**Run:**
```bash
python bonus_complete_pipeline.py
```

## Testing

All solutions include built-in tests. To run individual solutions:

```bash
# Exercise 1
python exercise_1_robust_data_loading.py

# Exercise 2
python exercise_2_lif_neuron.py

# Exercise 3
python exercise_3_functional_programming.py

# Exercise 4 (requires pytest)
pytest test_spike_analysis.py -v

# Exercise 5
python exercise_5_refactored.py

# Bonus
python bonus_complete_pipeline.py
```

## Code Quality Checks

These solutions are designed to pass professional code quality tools:

```bash
# Type checking with mypy
mypy exercise_1_robust_data_loading.py
mypy exercise_2_lif_neuron.py
mypy bonus_complete_pipeline.py

# Code formatting with black
black *.py

# Linting with flake8
flake8 *.py
```

## Key Concepts Demonstrated

### 1. Error Handling
- Custom exceptions
- Try-except blocks
- Informative error messages
- Input validation

### 2. Type Hints
- Function signatures
- Return types
- Optional types
- NumPy array typing
- Generic types (List, Dict, Tuple)

### 3. Documentation
- NumPy-style docstrings
- Parameters section
- Returns section
- Raises section
- Examples section

### 4. Object-Oriented Programming
- Classes with `__init__`
- Instance methods
- Property decorators
- Class methods (`@classmethod`)
- Magic methods (`__len__`, `__repr__`)
- Protocols for duck typing

### 5. Functional Programming
- Map, filter, reduce
- Lambda functions
- List/dict comprehensions
- Function composition
- Immutability principles

### 6. Testing
- pytest fixtures
- Parametrized tests
- Test classes
- Edge case testing
- Assertion methods
- Test organization

### 7. Best Practices
- Context managers (`with` statements)
- Enums for constants
- Meaningful names
- Single responsibility principle
- DRY (Don't Repeat Yourself)
- Type safety

## Example Usage

### Loading and Analyzing Spike Data

```python
from exercise_1_robust_data_loading import load_spike_data
import pandas as pd

# Create sample data
data = pd.DataFrame({'spike_times': [0.1, 0.2, 0.3, 0.4, 0.5]})
data.to_csv('neuron_001.csv', index=False)

# Load with validation
spikes = load_spike_data('neuron_001.csv', max_time=0.35)
print(f"Loaded {len(spikes)} spikes")  # Output: Loaded 3 spikes
```

### Simulating a Neuron

```python
from exercise_2_lif_neuron import LIFNeuron
import numpy as np

# Create neuron
neuron = LIFNeuron(tau_m=10.0, v_rest=-65.0, v_thresh=-50.0)

# Simulate
for t in np.arange(0, 100, 0.1):
    fired = neuron.step(current=2.0, dt=0.1)
    if fired:
        print(f"Spike at {t:.1f} ms")

# Get statistics
rate = neuron.get_firing_rate(100.0)
mean_isi, cv_isi = neuron.get_isi_stats()
print(f"Rate: {rate:.2f} Hz, CV: {cv_isi:.3f}")
```

### Complete Analysis Pipeline

```python
from bonus_complete_pipeline import NeuralDataset, AnalysisPipeline
import numpy as np
from pathlib import Path

# Create dataset
dataset = NeuralDataset()
dataset.add_neuron('n1', np.array([0.1, 0.2, 0.3, 0.4, 0.5]))
dataset.add_neuron('n2', np.array([0.15, 0.25, 0.35, 0.45]))
dataset.duration = 1.0

# Run pipeline
pipeline = AnalysisPipeline(dataset)
results = pipeline.run()

# Generate report
pipeline.generate_report(Path('analysis_report.md'))

# Save dataset
dataset.to_json(Path('dataset.json'))
```

## Dependencies

```bash
pip install numpy pandas pytest
```

For type checking:
```bash
pip install mypy
```

For code formatting:
```bash
pip install black flake8
```

## Learning Outcomes

After working through these solutions, you should be able to:

1. ✅ Write robust code with comprehensive error handling
2. ✅ Use type hints to improve code clarity and catch bugs
3. ✅ Document code professionally with detailed docstrings
4. ✅ Design object-oriented systems with classes and protocols
5. ✅ Apply functional programming patterns effectively
6. ✅ Write comprehensive unit tests with pytest
7. ✅ Refactor code to follow best practices
8. ✅ Build complete analysis pipelines for neuroscience data

## Notes

- All solutions follow PEP 8 style guidelines
- Type hints are compatible with Python 3.9+
- Tests are designed to be run with pytest 6.0+
- Code is optimized for readability and maintainability
- Examples use realistic neuroscience scenarios

---

*Solutions prepared for CNC-UC Introduction to Scientific Programming*  
*University of Coimbra*
