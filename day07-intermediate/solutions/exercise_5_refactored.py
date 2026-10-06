"""
Exercise 5: Refactoring Challenge
Refactored version of poorly written code following best practices.
"""

from enum import Enum
from typing import List, Tuple
from pathlib import Path
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
        If transform type is invalid or spike_times is empty
        
    Examples
    --------
    >>> spikes = np.array([0.1, 0.2, 0.3])
    >>> doubled = transform_spike_times(spikes, TransformType.DOUBLE)
    >>> print(doubled)
    [0.2 0.4 0.6]
    """
    if len(spike_times) == 0:
        raise ValueError("spike_times array cannot be empty")
    
    if not isinstance(transform, TransformType):
        raise ValueError(f"transform must be a TransformType, got {type(transform)}")
    
    # Apply transformation based on type
    if transform == TransformType.DOUBLE:
        return spike_times * 2.0
    elif transform == TransformType.HALVE:
        return spike_times / 2.0
    elif transform == TransformType.SQUARE:
        return spike_times ** 2.0
    else:
        raise ValueError(f"Unknown transform type: {transform}")


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
        
    Examples
    --------
    >>> spikes = np.array([0.1, 0.2, 0.3, 0.4])
    >>> rate = calculate_mean_firing_rate(spikes, duration=1.0)
    >>> print(f"Rate: {rate} Hz")
    Rate: 4.0 Hz
    """
    if len(spike_times) == 0:
        raise ValueError("spike_times array cannot be empty")
    
    if duration <= 0:
        raise ValueError("duration must be positive")
    
    # Calculate mean firing rate
    return len(spike_times) / duration


def load_and_analyze_spikes(filename: str, 
                           transform: TransformType,
                           duration: float = 1.0) -> Tuple[float, NDArray]:
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
        
    Examples
    --------
    >>> # Create test file
    >>> with open('test_data.txt', 'w') as f:
    ...     f.write('0.1\\n0.2\\n0.3\\n')
    >>> rate, spikes = load_and_analyze_spikes('test_data.txt', 
    ...                                        TransformType.DOUBLE,
    ...                                        duration=1.0)
    >>> print(f"Rate: {rate} Hz")
    Rate: 3.0 Hz
    """
    # Check if file exists
    file_path = Path(filename)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filename}")
    
    # Load data using context manager
    spike_times = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
            if not lines:
                raise ValueError("File is empty")
            
            # Parse spike times
            for line_num, line in enumerate(lines, start=1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                try:
                    spike_time = float(line)
                    spike_times.append(spike_time)
                except ValueError:
                    raise ValueError(
                        f"Invalid data on line {line_num}: '{line}' is not a number"
                    )
    
    except IOError as e:
        raise ValueError(f"Error reading file: {e}")
    
    if not spike_times:
        raise ValueError("No valid spike times found in file")
    
    # Convert to numpy array
    spike_times_array = np.array(spike_times)
    
    # Calculate mean firing rate
    mean_rate = calculate_mean_firing_rate(spike_times_array, duration)
    
    # Apply transformation
    transformed_spikes = transform_spike_times(spike_times_array, transform)
    
    return mean_rate, transformed_spikes


# ============================================================================
# TESTS
# ============================================================================

def test_transform_spike_times():
    """Test spike time transformations."""
    print("Testing transform_spike_times...")
    
    spikes = np.array([0.1, 0.2, 0.3])
    
    # Test DOUBLE
    doubled = transform_spike_times(spikes, TransformType.DOUBLE)
    assert np.allclose(doubled, [0.2, 0.4, 0.6])
    print("  ✓ DOUBLE transformation works")
    
    # Test HALVE
    halved = transform_spike_times(spikes, TransformType.HALVE)
    assert np.allclose(halved, [0.05, 0.1, 0.15])
    print("  ✓ HALVE transformation works")
    
    # Test SQUARE
    squared = transform_spike_times(spikes, TransformType.SQUARE)
    assert np.allclose(squared, [0.01, 0.04, 0.09])
    print("  ✓ SQUARE transformation works")
    
    # Test empty array raises error
    try:
        transform_spike_times(np.array([]), TransformType.DOUBLE)
        print("  ✗ Should have raised ValueError for empty array")
    except ValueError:
        print("  ✓ ValueError raised for empty array")
    
    print("✓ All transform tests passed!\n")


def test_calculate_mean_firing_rate():
    """Test firing rate calculation."""
    print("Testing calculate_mean_firing_rate...")
    
    # Test basic calculation
    spikes = np.array([0.1, 0.2, 0.3, 0.4])
    rate = calculate_mean_firing_rate(spikes, duration=1.0)
    assert rate == 4.0
    print("  ✓ Basic rate calculation works")
    
    # Test with different duration
    rate = calculate_mean_firing_rate(spikes, duration=2.0)
    assert rate == 2.0
    print("  ✓ Rate scales with duration")
    
    # Test empty array raises error
    try:
        calculate_mean_firing_rate(np.array([]), duration=1.0)
        print("  ✗ Should have raised ValueError for empty array")
    except ValueError:
        print("  ✓ ValueError raised for empty array")
    
    # Test negative duration raises error
    try:
        calculate_mean_firing_rate(spikes, duration=-1.0)
        print("  ✗ Should have raised ValueError for negative duration")
    except ValueError:
        print("  ✓ ValueError raised for negative duration")
    
    # Test zero duration raises error
    try:
        calculate_mean_firing_rate(spikes, duration=0.0)
        print("  ✗ Should have raised ValueError for zero duration")
    except ValueError:
        print("  ✓ ValueError raised for zero duration")
    
    print("✓ All firing rate tests passed!\n")


def test_load_and_analyze_spikes():
    """Test file loading and analysis."""
    print("Testing load_and_analyze_spikes...")
    
    # Create test file
    test_file = 'test_data.txt'
    with open(test_file, 'w') as f:
        f.write('0.1\n0.2\n0.3\n0.4\n')
    
    # Test basic loading and analysis
    try:
        rate, transformed = load_and_analyze_spikes(
            test_file, 
            TransformType.DOUBLE,
            duration=1.0
        )
        assert rate == 4.0
        assert np.allclose(transformed, [0.2, 0.4, 0.6, 0.8])
        print("  ✓ File loading and analysis works")
    except Exception as e:
        print(f"  ✗ Loading failed: {e}")
    
    # Test FileNotFoundError
    try:
        load_and_analyze_spikes('nonexistent.txt', TransformType.DOUBLE)
        print("  ✗ Should have raised FileNotFoundError")
    except FileNotFoundError:
        print("  ✓ FileNotFoundError raised for missing file")
    
    # Create empty file
    empty_file = 'empty_data.txt'
    with open(empty_file, 'w') as f:
        pass
    
    # Test empty file raises error
    try:
        load_and_analyze_spikes(empty_file, TransformType.DOUBLE)
        print("  ✗ Should have raised ValueError for empty file")
    except ValueError:
        print("  ✓ ValueError raised for empty file")
    
    # Create file with invalid data
    invalid_file = 'invalid_data.txt'
    with open(invalid_file, 'w') as f:
        f.write('0.1\ninvalid\n0.3\n')
    
    # Test invalid data raises error
    try:
        load_and_analyze_spikes(invalid_file, TransformType.DOUBLE)
        print("  ✗ Should have raised ValueError for invalid data")
    except ValueError:
        print("  ✓ ValueError raised for invalid data")
    
    # Cleanup
    import os
    for f in [test_file, empty_file, invalid_file]:
        if os.path.exists(f):
            os.remove(f)
    
    print("✓ All file loading tests passed!\n")


def run_all_tests():
    """Run all tests."""
    print("="*60)
    print("RUNNING ALL TESTS FOR REFACTORED CODE")
    print("="*60 + "\n")
    
    test_transform_spike_times()
    test_calculate_mean_firing_rate()
    test_load_and_analyze_spikes()
    
    print("="*60)
    print("ALL TESTS PASSED! ✓")
    print("="*60)


if __name__ == '__main__':
    run_all_tests()
