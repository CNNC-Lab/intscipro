"""
Exercise 2: Neuron Class with Type Hints
Solution demonstrating OOP, type hints, and comprehensive docstrings.
"""

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
        # Validate parameters
        if tau_m <= 0:
            raise ValueError("tau_m must be positive")
        if R <= 0:
            raise ValueError("R must be positive")
        if v_reset >= v_thresh:
            raise ValueError("v_reset must be less than v_thresh")
        if v_rest >= v_thresh:
            raise ValueError("v_rest must be less than v_thresh")
        
        # Store parameters
        self.tau_m = tau_m
        self.v_rest = v_rest
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.R = R
        
        # Initialize state
        self.v = v_rest
        self.spike_times: List[float] = []
        self._current_time = 0.0
    
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
        # Leaky integration: dV/dt = (-(v - v_rest) + R * current) / tau_m
        dv = (-(self.v - self.v_rest) + self.R * current) / self.tau_m
        self.v += dv * dt
        
        # Update time
        self._current_time += dt
        
        # Check for spike
        if self.v >= self.v_thresh:
            self.spike_times.append(self._current_time)
            self.v = self.v_reset
            return True
        
        return False
    
    def reset(self) -> None:
        """Reset neuron to initial state."""
        self.v = self.v_rest
        self.spike_times = []
        self._current_time = 0.0
    
    @property
    def n_spikes(self) -> int:
        """Number of spikes fired."""
        return len(self.spike_times)
    
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
        if duration <= 0:
            raise ValueError("Duration must be positive")
        
        # Convert ms to seconds for Hz
        return self.n_spikes / (duration / 1000.0)
    
    def get_isi_stats(self) -> Tuple[float, float]:
        """Calculate inter-spike interval statistics.
        
        Returns
        -------
        mean_isi : float
            Mean ISI in ms
        cv_isi : float
            Coefficient of variation of ISI
        """
        if self.n_spikes < 2:
            raise ValueError("Need at least 2 spikes to calculate ISI statistics")
        
        # Calculate ISIs
        isis = np.diff(self.spike_times)
        
        # Calculate mean and CV
        mean_isi = np.mean(isis)
        cv_isi = np.std(isis) / mean_isi if mean_isi > 0 else np.inf
        
        return mean_isi, cv_isi


def test_lif_neuron():
    """Test LIF neuron implementation."""
    print("Testing LIF neuron...")
    
    # Test 1: Initialization
    neuron = LIFNeuron(tau_m=10.0, v_rest=-65.0, v_thresh=-50.0)
    assert neuron.v == -65.0, "Initial voltage should be v_rest"
    assert neuron.n_spikes == 0, "Initial spike count should be 0"
    print("✓ Initialization test passed")
    
    # Test 2: Integration without spiking
    fired = neuron.step(current=0.5, dt=0.1)
    assert not fired, "Should not spike with small current"
    assert neuron.v > -65.0, "Voltage should depolarize"
    print("✓ Integration test passed")
    
    # Test 3: Reset
    neuron.reset()
    assert neuron.v == -65.0, "Voltage should reset to v_rest"
    assert neuron.n_spikes == 0, "Spike count should reset to 0"
    print("✓ Reset test passed")
    
    # Test 4: Spiking behavior
    neuron.reset()
    spike_count = 0
    for t in np.arange(0, 100, 0.1):
        fired = neuron.step(current=2.0, dt=0.1)
        if fired:
            spike_count += 1
    
    assert spike_count > 0, "Neuron should spike with sufficient current"
    assert neuron.n_spikes == spike_count, "Spike count should match"
    print(f"✓ Spiking test passed ({spike_count} spikes)")
    
    # Test 5: Firing rate
    duration = 100.0  # ms
    rate = neuron.get_firing_rate(duration)
    assert rate > 0, "Firing rate should be positive"
    print(f"✓ Firing rate: {rate:.2f} Hz")
    
    # Test 6: ISI statistics
    if neuron.n_spikes >= 2:
        mean_isi, cv_isi = neuron.get_isi_stats()
        assert mean_isi > 0, "Mean ISI should be positive"
        assert cv_isi >= 0, "CV should be non-negative"
        print(f"✓ ISI stats: mean={mean_isi:.2f} ms, CV={cv_isi:.3f}")
    
    # Test 7: Parameter validation
    try:
        bad_neuron = LIFNeuron(tau_m=-1.0)
        print("✗ Should have raised ValueError for negative tau_m")
    except ValueError:
        print("✓ Parameter validation test passed")
    
    # Test 8: Property decorator
    assert isinstance(neuron.n_spikes, int), "n_spikes should return int"
    print("✓ Property decorator test passed")
    
    print("\nAll tests passed!")


if __name__ == '__main__':
    test_lif_neuron()
