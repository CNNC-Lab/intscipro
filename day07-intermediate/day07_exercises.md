# Day 7 Exercises: Intermediate Programming Concepts
_PhD Course in Integrative Neurosciences - Introduction to Scientific Programming_

## Overview
These exercises build on Day 7 concepts: error handling, type hints, documentation, OOP, functional programming, testing, and best practices. Work through them progressively—each exercise reinforces multiple concepts.

---
## Exercise 1: Robust Data Loading

### Learning Goals
- Error handling with try-except
- Input validation
- Type hints
- Docstrings

### Task
Write a function `load_spike_data()` that safely loads spike time data from a CSV file with robust error handling.

**Requirements:**
```python
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional

def load_spike_data(filename: str, 
                    time_column: str = 'spike_times',
                    max_time: Optional[float] = None) -> np.ndarray:
    """Load spike time data from CSV file with validation.
    
    Parameters
    ----------
    filename : str
        Path to CSV file containing spike times
    time_column : str, optional
        Name of column containing spike times (default: 'spike_times')
    max_time : float, optional
        Maximum valid spike time in seconds. If provided, filter out
        spikes beyond this time.
        
    Returns
    -------
    np.ndarray
        Array of valid spike times in seconds, sorted
        
    Raises
    ------
    FileNotFoundError
        If file doesn't exist
    ValueError
        If time_column not in file, or data contains invalid values
    DataQualityError
        If data contains negative values or NaN
        
    Examples
    --------
    >>> spikes = load_spike_data('neuron_001.csv', max_time=10.0)
    >>> print(f"Loaded {len(spikes)} spikes")
    Loaded 342 spikes
    """
    # TODO: Implement this function
    pass


# Custom exception
class DataQualityError(Exception):
    """Raised when data quality checks fail."""
    pass
```

**Your implementation should:**
1. Check if file exists (raise `FileNotFoundError` if not)
2. Load CSV using pandas
3. Check if `time_column` exists (raise `ValueError` if not)
4. Validate data:
   - No NaN values (raise `DataQualityError`)
   - No negative times (raise `DataQualityError`)
   - All values are numeric (raise `ValueError`)
5. Filter by `max_time` if provided
6. Return sorted numpy array

**Test your function:**
```python
# Create test data
test_data = pd.DataFrame({
    'spike_times': [0.1, 0.25, 0.38, 0.52, 0.67]
})
test_data.to_csv('test_spikes.csv', index=False)

# Test cases
try:
    spikes = load_spike_data('test_spikes.csv')
    print(f"✓ Loaded {len(spikes)} spikes")
    
    spikes = load_spike_data('nonexistent.csv')
except FileNotFoundError:
    print("✓ FileNotFoundError caught correctly")
    
try:
    spikes = load_spike_data('test_spikes.csv', time_column='wrong_column')
except ValueError:
    print("✓ ValueError caught for wrong column")
```

---
## Exercise 2: Neuron Class with Type Hints

### Learning Goals
- Object-oriented programming
- Type hints for classes
- Comprehensive docstrings
- Property decorators

### Task
Implement a `LIFNeuron` (Leaky Integrate-and-Fire) class with full type hints and documentation.

**Requirements:**
```python
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

class LIFNeuron:
    """Leaky integrate-and-fire neuron model.
    
    Simulates a simple point neuron with leaky integration and
    threshold-based spiking. Uses Euler integration for membrane
    potential dynamics.
    
    Parameters
    ----------
    tau_m : float
        Membrane time constant in milliseconds (default: 10.0)
    v_rest : float
        Resting membrane potential in mV (default: -65.0)
    v_thresh : float
        Spike threshold in mV (default: -50.0)
    v_reset : float
        Reset potential after spike in mV (default: -70.0)
    R : float
        Membrane resistance in MΩ (default: 10.0)
        
    Attributes
    ----------
    v : float
        Current membrane potential in mV
    spike_times : List[float]
        List of spike times in ms
        
    Examples
    --------
    >>> neuron = LIFNeuron(tau_m=10.0, v_rest=-65.0)
    >>> for t in np.arange(0, 100, 0.1):
    ...     fired = neuron.step(current=1.5, dt=0.1)
    ...     if fired:
    ...         print(f"Spike at {t:.1f} ms")
    """
    
    def __init__(self, 
                 tau_m: float = 10.0,
                 v_rest: float = -65.0,
                 v_thresh: float = -50.0,
                 v_reset: float = -70.0,
                 R: float = 10.0):
        """Initialize neuron parameters."""
        # TODO: Validate parameters (all positive, v_rest < v_thresh, etc.)
        # TODO: Initialize attributes
        pass
    
    def step(self, current: float, dt: float) -> bool:
        """Integrate membrane potential for one time step.
        
        Uses Euler integration to update membrane potential based on
        input current and leak.
        
        Parameters
        ----------
        current : float
            Input current in nA
        dt : float
            Time step in ms
            
        Returns
        -------
        bool
            True if neuron spiked, False otherwise
        """
        # TODO: Implement leaky integration
        # dV/dt = (-(v - v_rest) + R * current) / tau_m
        pass
    
    def reset(self) -> None:
        """Reset neuron to initial state."""
        # TODO: Reset membrane potential and clear spike times
        pass
    
    @property
    def n_spikes(self) -> int:
        """Number of spikes fired."""
        # TODO: Return spike count
        pass
    
    def get_firing_rate(self, duration: float) -> float:
        """Calculate average firing rate.
        
        Parameters
        ----------
        duration : float
            Total simulation time in ms
            
        Returns
        -------
        float
            Firing rate in Hz
        """
        # TODO: Calculate rate (convert ms to seconds)
        pass
    
    def get_isi_stats(self) -> Tuple[float, float]:
        """Calculate inter-spike interval statistics.
        
        Returns
        -------
        mean_isi : float
            Mean ISI in ms
        cv_isi : float
            Coefficient of variation of ISI
        """
        # TODO: Calculate ISI mean and CV
        pass
```

**Test your class:**

```python
def test_lif_neuron():
    """Test LIF neuron implementation."""
    neuron = LIFNeuron(tau_m=10.0, v_rest=-65.0, v_thresh=-50.0)
    
    # Test initialization
    assert neuron.v == -65.0
    assert neuron.n_spikes == 0
    
    # Test integration without spiking
    fired = neuron.step(current=0.5, dt=0.1)
    assert not fired
    assert neuron.v > -65.0  # Depolarized
    
    # Test reset
    neuron.reset()
    assert neuron.v == -65.0
    assert neuron.n_spikes == 0
    
    print("✓ All tests passed!")

test_lif_neuron()
```

---
## Exercise 3: Functional Data Processing

### Learning Goals
- Functional programming patterns
- Map, filter, reduce
- Lambda functions
- List comprehensions

### Task

Implement a functional pipeline to analyze spike train data from multiple neurons.

**Requirements:**

```python
from typing import Dict, List, Callable
import numpy as np
from functools import reduce

# Sample data
spike_data = {
    'neuron_001': np.array([0.012, 0.145, 0.289, 0.456, 0.601, 0.778]),
    'neuron_002': np.array([0.098, 0.234, 0.401, 0.589, 0.723, 0.891]),
    'neuron_003': np.array([0.056, 0.167, 0.298, 0.445, 0.612, 0.801]),
    'neuron_004': np.array([0.023, 0.189, 0.356, 0.512, 0.689, 0.834]),
}

def analyze_spike_trains(spike_data: Dict[str, np.ndarray], 
                        duration: float = 1.0) -> Dict:
    """Analyze multiple spike trains using functional programming.
    
    Parameters
    ----------
    spike_data : Dict[str, np.ndarray]
        Dictionary mapping neuron IDs to spike time arrays
    duration : float
        Recording duration in seconds
        
    Returns
    -------
    Dict
        Analysis results with keys:
        - 'firing_rates': Dict of neuron_id -> rate (Hz)
        - 'high_rate_neurons': List of neuron IDs with rate > 5 Hz
        - 'mean_rate': Average firing rate across all neurons
        - 'total_spikes': Total spike count across all neurons
    """
    
    # TODO: 1. Calculate firing rates for all neurons (use dict comprehension)
    firing_rates = {}
    
    # TODO: 2. Filter high-rate neurons (use filter or comprehension)
    high_rate_neurons = []
    
    # TODO: 3. Calculate mean rate across neurons (use map and reduce, or mean)
    mean_rate = 0.0
    
    # TODO: 4. Calculate total spike count (use reduce or sum)
    total_spikes = 0
    
    return {
        'firing_rates': firing_rates,
        'high_rate_neurons': high_rate_neurons,
        'mean_rate': mean_rate,
        'total_spikes': total_spikes
    }


def transform_spike_times(spike_data: Dict[str, np.ndarray],
                         transforms: List[Callable]) -> Dict[str, np.ndarray]:
    """Apply sequence of transformations to spike times.
    
    Parameters
    ----------
    spike_data : Dict[str, np.ndarray]
        Dictionary mapping neuron IDs to spike time arrays
    transforms : List[Callable]
        List of transformation functions to apply in sequence
        
    Returns
    -------
    Dict[str, np.ndarray]
        Transformed spike data
        
    Examples
    --------
    >>> # Convert ms to seconds, then filter early spikes
    >>> transforms = [
    ...     lambda t: t / 1000.0,  # ms to seconds
    ...     lambda t: t[t < 0.5]   # keep only first 500ms
    ... ]
    >>> result = transform_spike_times(data, transforms)
    """
    # TODO: Use reduce to apply transformations sequentially
    # Hint: reduce(lambda data, func: {k: func(v) for k, v in data.items()}, ...)
    pass


# Test functions
def test_analysis():
    """Test spike train analysis."""
    results = analyze_spike_trains(spike_data, duration=1.0)
    
    print(f"Firing rates: {results['firing_rates']}")
    print(f"High-rate neurons: {results['high_rate_neurons']}")
    print(f"Mean rate: {results['mean_rate']:.2f} Hz")
    print(f"Total spikes: {results['total_spikes']}")
    
    assert len(results['firing_rates']) == 4
    assert results['mean_rate'] > 0
    assert results['total_spikes'] > 0

test_analysis()
```

---

## Exercise 4: Unit Testing with pytest

### Learning Goals
- Writing unit tests
- pytest features (parametrize, fixtures, approx)
- Testing edge cases
- Test-driven development

### Task

Write comprehensive tests for a spike analysis module.

**First, implement the functions to test:**

```python
# spike_analysis.py
import numpy as np
from numpy.typing import NDArray
from typing import Optional

def calculate_firing_rate(spike_times: NDArray, duration: float) -> float:
    """Calculate firing rate in Hz."""
    if duration <= 0:
        raise ValueError("Duration must be positive")
    return len(spike_times) / duration


def calculate_cv(spike_times: NDArray) -> float:
    """Calculate coefficient of variation of ISI.
    
    CV = std(ISI) / mean(ISI)
    """
    if len(spike_times) < 2:
        raise ValueError("Need at least 2 spikes")
    
    isis = np.diff(spike_times)
    if np.mean(isis) == 0:
        return np.inf
    
    return np.std(isis) / np.mean(isis)


def bin_spike_train(spike_times: NDArray, 
                   bin_size: float,
                   duration: float) -> NDArray:
    """Bin spike train into time windows.
    
    Parameters
    ----------
    spike_times : NDArray
        Spike times in seconds
    bin_size : float
        Bin size in seconds
    duration : float
        Total duration in seconds
        
    Returns
    -------
    NDArray
        Spike counts per bin
    """
    if bin_size <= 0:
        raise ValueError("Bin size must be positive")
    
    n_bins = int(np.ceil(duration / bin_size))
    counts, _ = np.histogram(spike_times, bins=n_bins, range=(0, duration))
    return counts


def detect_bursts(spike_times: NDArray,
                 max_isi: float = 0.01,
                 min_spikes: int = 3) -> list:
    """Detect bursts in spike train.
    
    A burst is defined as min_spikes consecutive spikes with
    ISI < max_isi.
    
    Parameters
    ----------
    spike_times : NDArray
        Spike times in seconds
    max_isi : float
        Maximum ISI within burst (default: 0.01s = 10ms)
    min_spikes : int
        Minimum spikes to constitute a burst (default: 3)
        
    Returns
    -------
    list
        List of tuples (burst_start_idx, burst_end_idx)
    """
    if len(spike_times) < min_spikes:
        return []
    
    isis = np.diff(spike_times)
    bursts = []
    burst_start = None
    burst_count = 1
    
    for i, isi in enumerate(isis):
        if isi < max_isi:
            if burst_start is None:
                burst_start = i
            burst_count += 1
        else:
            if burst_start is not None and burst_count >= min_spikes:
                bursts.append((burst_start, i))
            burst_start = None
            burst_count = 1
    
    # Check if we ended in a burst
    if burst_start is not None and burst_count >= min_spikes:
        bursts.append((burst_start, len(spike_times) - 1))
    
    return bursts
```

**Now write tests:**

```python
# test_spike_analysis.py
import pytest
import numpy as np
from spike_analysis import (
    calculate_firing_rate, 
    calculate_cv,
    bin_spike_train,
    detect_bursts
)

# Fixtures for reusable test data
@pytest.fixture
def regular_spikes():
    """Regular 10 Hz spiking."""
    return np.arange(0, 1.0, 0.1)

@pytest.fixture
def irregular_spikes():
    """Irregular spiking pattern."""
    return np.array([0.01, 0.05, 0.3, 0.32, 0.9])

@pytest.fixture
def burst_spikes():
    """Spike train with clear bursts."""
    return np.array([0.1, 0.105, 0.11, 0.115,  # Burst 1
                    0.5, 0.506, 0.512, 0.518,  # Burst 2
                    0.9])                        # Isolated spike


class TestFiringRate:
    """Tests for firing rate calculation."""
    
    def test_basic_rate(self):
        """Test basic firing rate calculation."""
        spikes = np.array([0.1, 0.2, 0.3, 0.4])
        rate = calculate_firing_rate(spikes, duration=1.0)
        assert rate == 4.0
    
    def test_empty_spikes(self):
        """Test with no spikes."""
        # TODO: Test that empty array returns 0 Hz
        pass
    
    @pytest.mark.parametrize("n_spikes,duration,expected", [
        (10, 1.0, 10.0),
        (20, 2.0, 10.0),
        (5, 0.5, 10.0),
        (100, 10.0, 10.0),
    ])
    def test_rate_parametrized(self, n_spikes, duration, expected):
        """Test firing rate with multiple parameter combinations."""
        # TODO: Generate spike array and test
        pass
    
    def test_negative_duration_raises(self):
        """Test that negative duration raises ValueError."""
        # TODO: Use pytest.raises
        pass
    
    def test_zero_duration_raises(self):
        """Test that zero duration raises ValueError."""
        # TODO: Use pytest.raises
        pass


class TestCoefficientOfVariation:
    """Tests for CV calculation."""
    
    def test_regular_spiking_low_cv(self, regular_spikes):
        """Regular spiking should have CV ≈ 0."""
        cv = calculate_cv(regular_spikes)
        assert cv < 0.1  # Nearly regular
    
    def test_irregular_spiking_high_cv(self, irregular_spikes):
        """Irregular spiking should have CV > 0.5."""
        # TODO: Calculate CV and assert it's high
        pass
    
    def test_poisson_cv_around_one(self):
        """Poisson process should have CV ≈ 1."""
        np.random.seed(42)
        isis = np.random.exponential(scale=0.1, size=1000)
        spike_times = np.cumsum(isis)
        cv = calculate_cv(spike_times)
        # TODO: Assert CV is close to 1.0 (use pytest.approx)
        pass
    
    def test_insufficient_spikes_raises(self):
        """Test that < 2 spikes raises ValueError."""
        # TODO: Test with 0 and 1 spike
        pass


class TestBinning:
    """Tests for spike train binning."""
    
    def test_bin_counts(self):
        """Test basic binning."""
        spikes = np.array([0.05, 0.15, 0.25, 0.35])
        counts = bin_spike_train(spikes, bin_size=0.1, duration=1.0)
        # TODO: Assert correct bin counts
        pass
    
    def test_bin_size_invalid_raises(self):
        """Test that invalid bin size raises ValueError."""
        # TODO: Test with negative and zero bin sizes
        pass
    
    def test_empty_bins(self):
        """Test that bins without spikes are zero."""
        spikes = np.array([0.5])
        counts = bin_spike_train(spikes, bin_size=0.1, duration=1.0)
        # TODO: Assert most bins are zero, one bin is 1
        pass


class TestBurstDetection:
    """Tests for burst detection."""
    
    def test_detect_bursts(self, burst_spikes):
        """Test burst detection with clear bursts."""
        bursts = detect_bursts(burst_spikes, max_isi=0.01, min_spikes=3)
        # TODO: Assert 2 bursts detected
        pass
    
    def test_no_bursts_in_regular(self, regular_spikes):
        """Regular spiking should have no bursts."""
        # TODO: Assert no bursts with tight ISI threshold
        pass
    
    def test_min_spikes_threshold(self):
        """Test minimum spike requirement for burst."""
        # Burst with only 2 spikes
        spikes = np.array([0.1, 0.105, 0.5])
        bursts = detect_bursts(spikes, max_isi=0.01, min_spikes=3)
        # TODO: Assert no bursts detected (need min 3 spikes)
        pass


# Run tests
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
```

**Your task:**
1. Complete all `# TODO` items in the test file
2. Run tests: `pytest test_spike_analysis.py -v`
3. Ensure all tests pass
4. Add at least 2 more test cases of your own

---

## Exercise 5: Refactoring Challenge

### Learning Goals
- Code refactoring
- Applying best practices
- Type hints and documentation
- Error handling

### Task

Refactor this poorly written code to follow professional standards.

**Bad code:**

```python
import numpy as np

def process(d, p):
    r = []
    for i in range(len(d)):
        if p == 1:
            r.append(d[i] * 2)
        elif p == 2:
            r.append(d[i] / 2)
        elif p == 3:
            r.append(d[i] ** 2)
    return r

def calc(data):
    m = 0
    for x in data:
        m = m + x
    m = m / len(data)
    return m

def analyze(filename):
    file = open(filename)
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(float(line))
    result = calc(data)
    processed = process(data, 1)
    return result, processed

# Usage
result, processed = analyze('data.txt')
print(result, processed)
```

**Your refactored version should:**

1. **Meaningful names**: Replace `d`, `p`, `r`, `m`, `calc`, etc.
2. **Type hints**: Add type annotations to all functions
3. **Docstrings**: Add Google-style or NumPy-style docstrings
4. **Error handling**: Handle file errors, empty data, invalid parameters
5. **Context managers**: Use `with` for file operations
6. **Better structure**: Use enums or constants instead of magic numbers
7. **Functional approach**: Use map/list comprehensions where appropriate
8. **Testing**: Write at least 3 unit tests

**Expected result:**

```python
from enum import Enum
from typing import List
import numpy as np
from numpy.typing import NDArray

class TransformType(Enum):
    """Spike time transformation types."""
    DOUBLE = 'double'
    HALVE = 'halve'
    SQUARE = 'square'

def transform_spike_times(spike_times: NDArray, 
                         transform: TransformType) -> NDArray:
    """Apply transformation to spike times.
    
    Parameters
    ----------
    spike_times : NDArray
        Array of spike times in seconds
    transform : TransformType
        Type of transformation to apply
        
    Returns
    -------
    NDArray
        Transformed spike times
        
    Raises
    ------
    ValueError
        If transform type is invalid
    """
    # TODO: Implement with proper error handling
    pass

def calculate_mean_firing_rate(spike_times: NDArray, duration: float) -> float:
    """Calculate mean firing rate.
    
    Parameters
    ----------
    spike_times : NDArray
        Array of spike times in seconds
    duration : float
        Recording duration in seconds
        
    Returns
    -------
    float
        Mean firing rate in Hz
        
    Raises
    ------
    ValueError
        If spike_times is empty or duration is non-positive
    """
    # TODO: Implement
    pass

def load_and_analyze_spikes(filename: str, 
                           transform: TransformType,
                           duration: float = 1.0) -> tuple:
    """Load spike data from file and perform analysis.
    
    Parameters
    ----------
    filename : str
        Path to file containing spike times (one per line)
    transform : TransformType
        Transformation to apply to spike times
    duration : float
        Recording duration in seconds (default: 1.0)
        
    Returns
    -------
    mean_rate : float
        Mean firing rate in Hz
    transformed_spikes : NDArray
        Transformed spike times
        
    Raises
    ------
    FileNotFoundError
        If file doesn't exist
    ValueError
        If file is empty or contains invalid data
    """
    # TODO: Implement with context manager and error handling
    pass

# Write tests
def test_transform_spike_times():
    """Test spike time transformations."""
    # TODO: Test double, halve, square operations
    pass

def test_calculate_mean_firing_rate():
    """Test firing rate calculation."""
    # TODO: Test with known inputs
    pass

def test_load_and_analyze_spikes():
    """Test file loading and analysis."""
    # TODO: Create test file, load, and verify
    pass
```

---

## Bonus Challenge: Complete Pipeline

### Task

Build a complete analysis pipeline that demonstrates all Day 7 concepts:

**Requirements:**

```python
"""
Neural Spike Analysis Pipeline
===============================

This module provides a complete pipeline for analyzing neural spike trains.
Demonstrates: OOP, error handling, type hints, functional programming, testing.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Protocol
import numpy as np
from numpy.typing import NDArray
from pathlib import Path
import json

@dataclass
class SpikeTrainStats:
    """Statistics for a single spike train."""
    neuron_id: str
    n_spikes: int
    firing_rate: float
    cv_isi: float
    mean_isi: float
    burst_count: int

class SpikeAnalyzer(Protocol):
    """Protocol for spike analyzers."""
    def analyze(self, spike_times: NDArray) -> dict:
        """Analyze spike train and return statistics."""
        ...

class NeuralDataset:
    """Container for multiple neurons' spike data."""
    
    def __init__(self):
        self.neurons: Dict[str, NDArray] = {}
        self.duration: float = 0.0
        self.metadata: dict = {}
    
    @classmethod
    def from_directory(cls, data_dir: Path) -> 'NeuralDataset':
        """Load all spike data from directory."""
        # TODO: Implement
        pass
    
    def add_neuron(self, neuron_id: str, spike_times: NDArray):
        """Add neuron to dataset."""
        # TODO: Validate and add
        pass
    
    def get_neuron(self, neuron_id: str) -> Optional[NDArray]:
        """Get spike times for neuron."""
        # TODO: Implement with error handling
        pass
    
    def filter_by_rate(self, min_rate: float, max_rate: float) -> 'NeuralDataset':
        """Filter neurons by firing rate."""
        # TODO: Use functional programming
        pass
    
    def analyze_all(self) -> List[SpikeTrainStats]:
        """Analyze all neurons in dataset."""
        # TODO: Return list of stats for all neurons
        pass
    
    def to_json(self, filename: Path):
        """Export dataset to JSON."""
        # TODO: Implement with context manager
        pass
    
    @classmethod
    def from_json(cls, filename: Path) -> 'NeuralDataset':
        """Load dataset from JSON."""
        # TODO: Implement
        pass


class AnalysisPipeline:
    """Complete analysis pipeline."""
    
    def __init__(self, dataset: NeuralDataset):
        self.dataset = dataset
        self.results: Optional[List[SpikeTrainStats]] = None
    
    def run(self) -> List[SpikeTrainStats]:
        """Run complete analysis pipeline."""
        # TODO: 
        # 1. Validate data
        # 2. Analyze each neuron
        # 3. Store results
        # 4. Return summary
        pass
    
    def generate_report(self, output_file: Path):
        """Generate analysis report."""
        # TODO: Create markdown report with results
        pass


# Complete test suite
class TestNeuralDataset:
    """Tests for NeuralDataset."""
    
    # TODO: Write comprehensive tests
    pass

class TestAnalysisPipeline:
    """Tests for AnalysisPipeline."""
    
    # TODO: Write comprehensive tests
    pass
```

**Your implementation should:**
1. Complete all `TODO` items
2. Use type hints throughout
3. Include docstrings for all public methods
4. Implement error handling
5. Write at least 10 unit tests
6. Use functional programming where appropriate
7. Include at least one context manager
8. Pass `mypy` type checking

---

```bash
# Style check
black your_code.py

# Type check
mypy your_code.py

# Run tests
pytest -v

# Check coverage
pytest --cov=your_module --cov-report=term
```

---

**Remember: focus on writing clean, well-tested, professional code.**


*Exercises prepared for CNC-UC Introduction to Scientific Programming*  
*University of Coimbra*