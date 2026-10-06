"""
Exercise 1: Robust Data Loading
Solution demonstrating error handling, type hints, and docstrings.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional


class DataQualityError(Exception):
    """Raised when data quality checks fail."""
    pass


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
    # Check if file exists
    file_path = Path(filename)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filename}")
    
    # Load CSV using pandas
    try:
        data = pd.read_csv(filename)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")
    
    # Check if time_column exists
    if time_column not in data.columns:
        raise ValueError(
            f"Column '{time_column}' not found in file. "
            f"Available columns: {list(data.columns)}"
        )
    
    # Extract spike times
    spike_times = data[time_column]
    
    # Validate data: check for NaN
    if spike_times.isna().any():
        raise DataQualityError(
            f"Data contains {spike_times.isna().sum()} NaN values"
        )
    
    # Validate data: check if numeric
    try:
        spike_times = spike_times.astype(float)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Data contains non-numeric values: {e}")
    
    # Validate data: check for negative times
    if (spike_times < 0).any():
        n_negative = (spike_times < 0).sum()
        raise DataQualityError(
            f"Data contains {n_negative} negative time values"
        )
    
    # Convert to numpy array
    spike_times = spike_times.values
    
    # Filter by max_time if provided
    if max_time is not None:
        spike_times = spike_times[spike_times <= max_time]
    
    # Return sorted array
    return np.sort(spike_times)


def test_load_spike_data():
    """Test the load_spike_data function."""
    # Create test data
    test_data = pd.DataFrame({
        'spike_times': [0.1, 0.25, 0.38, 0.52, 0.67]
    })
    test_data.to_csv('test_spikes.csv', index=False)
    
    # Test cases
    print("Testing load_spike_data function...")
    
    # Test 1: Basic loading
    try:
        spikes = load_spike_data('test_spikes.csv')
        print(f"✓ Loaded {len(spikes)} spikes")
        assert len(spikes) == 5
        assert np.allclose(spikes, [0.1, 0.25, 0.38, 0.52, 0.67])
    except Exception as e:
        print(f"✗ Basic loading failed: {e}")
    
    # Test 2: FileNotFoundError
    try:
        spikes = load_spike_data('nonexistent.csv')
        print("✗ Should have raised FileNotFoundError")
    except FileNotFoundError:
        print("✓ FileNotFoundError caught correctly")
    except Exception as e:
        print(f"✗ Wrong exception: {e}")
    
    # Test 3: ValueError for wrong column
    try:
        spikes = load_spike_data('test_spikes.csv', time_column='wrong_column')
        print("✗ Should have raised ValueError")
    except ValueError:
        print("✓ ValueError caught for wrong column")
    except Exception as e:
        print(f"✗ Wrong exception: {e}")
    
    # Test 4: max_time filtering
    try:
        spikes = load_spike_data('test_spikes.csv', max_time=0.4)
        print(f"✓ Filtered to {len(spikes)} spikes with max_time=0.4")
        assert len(spikes) == 3
        assert np.allclose(spikes, [0.1, 0.25, 0.38])
    except Exception as e:
        print(f"✗ max_time filtering failed: {e}")
    
    # Test 5: NaN handling
    test_data_nan = pd.DataFrame({
        'spike_times': [0.1, np.nan, 0.3]
    })
    test_data_nan.to_csv('test_spikes_nan.csv', index=False)
    try:
        spikes = load_spike_data('test_spikes_nan.csv')
        print("✗ Should have raised DataQualityError for NaN")
    except DataQualityError:
        print("✓ DataQualityError caught for NaN values")
    except Exception as e:
        print(f"✗ Wrong exception: {e}")
    
    # Test 6: Negative values handling
    test_data_neg = pd.DataFrame({
        'spike_times': [0.1, -0.5, 0.3]
    })
    test_data_neg.to_csv('test_spikes_neg.csv', index=False)
    try:
        spikes = load_spike_data('test_spikes_neg.csv')
        print("✗ Should have raised DataQualityError for negative values")
    except DataQualityError:
        print("✓ DataQualityError caught for negative values")
    except Exception as e:
        print(f"✗ Wrong exception: {e}")
    
    # Cleanup
    import os
    for f in ['test_spikes.csv', 'test_spikes_nan.csv', 'test_spikes_neg.csv']:
        if os.path.exists(f):
            os.remove(f)
    
    print("\nAll tests completed!")


if __name__ == '__main__':
    test_load_spike_data()
