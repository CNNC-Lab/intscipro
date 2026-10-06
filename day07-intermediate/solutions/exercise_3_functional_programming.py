"""
Exercise 3: Functional Data Processing
Solution demonstrating functional programming patterns.
"""

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
    
    # 1. Calculate firing rates for all neurons (dict comprehension)
    firing_rates = {
        neuron_id: len(spikes) / duration 
        for neuron_id, spikes in spike_data.items()
    }
    
    # 2. Filter high-rate neurons (list comprehension with filter)
    high_rate_neurons = [
        neuron_id 
        for neuron_id, rate in firing_rates.items() 
        if rate > 5
    ]
    
    # 3. Calculate mean rate across neurons (using map and reduce)
    # Alternative 1: Using reduce
    rates = list(firing_rates.values())
    mean_rate = reduce(lambda acc, rate: acc + rate, rates, 0.0) / len(rates)
    
    # Alternative 2: More Pythonic
    # mean_rate = np.mean(list(firing_rates.values()))
    
    # 4. Calculate total spike count (using reduce)
    total_spikes = reduce(
        lambda acc, spikes: acc + len(spikes), 
        spike_data.values(), 
        0
    )
    
    # Alternative: Using sum
    # total_spikes = sum(len(spikes) for spikes in spike_data.values())
    
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
    # Use reduce to apply transformations sequentially
    # Each transformation is applied to all neurons in the dictionary
    def apply_transform_to_dict(data: Dict[str, np.ndarray], 
                               func: Callable) -> Dict[str, np.ndarray]:
        """Apply a single transformation to all neurons."""
        return {neuron_id: func(spikes) for neuron_id, spikes in data.items()}
    
    # Apply all transformations in sequence using reduce
    return reduce(apply_transform_to_dict, transforms, spike_data)


def test_analysis():
    """Test spike train analysis."""
    print("Testing functional programming analysis...")
    
    results = analyze_spike_trains(spike_data, duration=1.0)
    
    print(f"\nFiring rates:")
    for neuron_id, rate in results['firing_rates'].items():
        print(f"  {neuron_id}: {rate:.2f} Hz")
    
    print(f"\nHigh-rate neurons (>5 Hz): {results['high_rate_neurons']}")
    print(f"Mean rate: {results['mean_rate']:.2f} Hz")
    print(f"Total spikes: {results['total_spikes']}")
    
    # Assertions
    assert len(results['firing_rates']) == 4, "Should have 4 neurons"
    assert results['mean_rate'] > 0, "Mean rate should be positive"
    assert results['total_spikes'] > 0, "Should have spikes"
    assert results['total_spikes'] == 24, "Should have 24 total spikes"
    
    print("\n✓ Analysis tests passed!")


def test_transformations():
    """Test spike time transformations."""
    print("\nTesting transformations...")
    
    # Create test data in milliseconds
    test_data = {
        'n1': np.array([100, 200, 300, 400, 500]),
        'n2': np.array([150, 250, 350, 450, 550])
    }
    
    # Define transformations
    transforms = [
        lambda t: t / 1000.0,      # Convert ms to seconds
        lambda t: t[t < 0.4]       # Keep only spikes before 400ms
    ]
    
    # Apply transformations
    result = transform_spike_times(test_data, transforms)
    
    print(f"Original n1: {test_data['n1']}")
    print(f"Transformed n1: {result['n1']}")
    print(f"Original n2: {test_data['n2']}")
    print(f"Transformed n2: {result['n2']}")
    
    # Assertions
    assert len(result['n1']) == 3, "n1 should have 3 spikes after filtering"
    assert len(result['n2']) == 3, "n2 should have 3 spikes after filtering"
    assert np.allclose(result['n1'], [0.1, 0.2, 0.3]), "Values should be in seconds"
    
    print("✓ Transformation tests passed!")


def test_functional_patterns():
    """Test various functional programming patterns."""
    print("\nTesting functional patterns...")
    
    # Test 1: Map pattern
    spike_counts = list(map(len, spike_data.values()))
    print(f"Spike counts (using map): {spike_counts}")
    assert all(count == 6 for count in spike_counts), "All neurons should have 6 spikes"
    
    # Test 2: Filter pattern
    active_neurons = list(filter(
        lambda item: len(item[1]) > 5, 
        spike_data.items()
    ))
    print(f"Active neurons (>5 spikes): {len(active_neurons)}")
    assert len(active_neurons) == 4, "All neurons are active"
    
    # Test 3: Lambda functions
    double_spikes = {
        neuron_id: spikes * 2 
        for neuron_id, spikes in spike_data.items()
    }
    print(f"First spike of n1 doubled: {double_spikes['neuron_001'][0]:.3f}")
    assert np.allclose(
        double_spikes['neuron_001'][0], 
        spike_data['neuron_001'][0] * 2
    ), "Doubling should work"
    
    # Test 4: Reduce for aggregation
    max_spike_time = reduce(
        lambda acc, spikes: max(acc, np.max(spikes)),
        spike_data.values(),
        0.0
    )
    print(f"Maximum spike time across all neurons: {max_spike_time:.3f} s")
    assert max_spike_time > 0.8, "Max spike should be > 0.8s"
    
    # Test 5: Chaining operations
    mean_spike_time_per_neuron = {
        neuron_id: np.mean(spikes)
        for neuron_id, spikes in spike_data.items()
    }
    overall_mean = np.mean(list(mean_spike_time_per_neuron.values()))
    print(f"Overall mean spike time: {overall_mean:.3f} s")
    
    print("✓ Functional pattern tests passed!")


if __name__ == '__main__':
    test_analysis()
    test_transformations()
    test_functional_patterns()
    print("\n" + "="*50)
    print("All functional programming tests passed! ✓")
    print("="*50)
