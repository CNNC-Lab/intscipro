"""
Exercise 16: Neuroscience Functions
Student: Solutions

Collection of functions for common neuroscience calculations.
"""

import numpy as np

print("=" * 60)
print("EXERCISE 16: Neuroscience Functions")
print("=" * 60)

# Part a: Firing Rate Calculator
print("\nPart a: Firing Rate Calculator")
print("-" * 60)

def calculate_firing_rate(spike_count, duration):
    """
    Calculate firing rate in Hz.
    
    Parameters:
    -----------
    spike_count : int
        Number of spikes observed
    duration : float
        Recording duration in seconds
    
    Returns:
    --------
    float
        Firing rate in Hz (spikes/second)
    
    Raises:
    -------
    ValueError
        If duration is zero or negative
    """
    if duration <= 0:
        raise ValueError("Duration must be positive")
    
    return spike_count / duration

# Test firing rate calculator
test_cases = [
    (150, 10.0, "Normal recording"),
    (75, 5.0, "Shorter recording"),
    (0, 10.0, "Silent neuron"),
]

print("\nFiring Rate Examples:")
for spike_count, duration, description in test_cases:
    rate = calculate_firing_rate(spike_count, duration)
    print(f"  {description}: {spike_count} spikes in {duration}s = {rate:.2f} Hz")

# Part b: Inter-Spike Interval Analysis
print("\n" + "=" * 60)
print("Part b: Inter-Spike Interval Analysis")
print("-" * 60)

def calculate_isi_statistics(spike_times):
    """
    Calculate inter-spike interval statistics.
    
    Parameters:
    -----------
    spike_times : list or array
        List of spike times in seconds (must be sorted)
    
    Returns:
    --------
    dict
        Dictionary containing:
        - 'isis': list of inter-spike intervals
        - 'mean_isi': mean ISI in seconds
        - 'std_isi': standard deviation of ISI
        - 'cv': coefficient of variation (std/mean)
        - 'firing_rate': instantaneous firing rate (1/mean_isi)
    
    Raises:
    -------
    ValueError
        If fewer than 2 spikes provided
    """
    if len(spike_times) < 2:
        raise ValueError("Need at least 2 spikes to calculate ISI")
    
    # Calculate ISIs (differences between consecutive spikes)
    isis = []
    for i in range(1, len(spike_times)):
        isi = spike_times[i] - spike_times[i-1]
        isis.append(isi)
    
    # Calculate statistics
    mean_isi = sum(isis) / len(isis)
    
    # Calculate standard deviation
    variance = sum((isi - mean_isi)**2 for isi in isis) / len(isis)
    std_isi = variance ** 0.5
    
    # Calculate coefficient of variation
    cv = std_isi / mean_isi if mean_isi > 0 else 0
    
    # Calculate firing rate
    firing_rate = 1.0 / mean_isi if mean_isi > 0 else 0
    
    return {
        'isis': isis,
        'mean_isi': mean_isi,
        'std_isi': std_isi,
        'cv': cv,
        'firing_rate': firing_rate
    }

# Test ISI analysis
spike_trains = {
    "Regular firing": [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3],
    "Irregular firing": [0.1, 0.15, 0.4, 0.45, 0.9, 1.5, 1.55],
    "Bursting": [0.1, 0.12, 0.14, 0.5, 0.52, 0.54, 0.9],
}

print("\nISI Analysis Examples:")
for description, spikes in spike_trains.items():
    stats = calculate_isi_statistics(spikes)
    print(f"\n{description}:")
    print(f"  Spike times: {spikes[:3]}... ({len(spikes)} spikes)")
    print(f"  Mean ISI: {stats['mean_isi']:.3f} s")
    print(f"  SD ISI: {stats['std_isi']:.3f} s")
    print(f"  CV: {stats['cv']:.3f}")
    print(f"  Firing rate: {stats['firing_rate']:.2f} Hz")
    print(f"  Interpretation: ", end="")
    if stats['cv'] < 0.5:
        print("Regular firing pattern")
    elif stats['cv'] < 1.0:
        print("Moderately irregular")
    else:
        print("Highly irregular or bursting")

# Part c: Voltage Classifier
print("\n" + "=" * 60)
print("Part c: Voltage Classifier")
print("-" * 60)

def classify_membrane_state(voltage):
    """
    Classify membrane potential state.
    
    Parameters:
    -----------
    voltage : float
        Membrane potential in mV
    
    Returns:
    --------
    str
        State classification
    
    Classifications:
        hyperpolarized: < -80 mV
        resting: -80 to -65 mV
        depolarized: -65 to -30 mV
        action_potential: > -30 mV
    """
    if voltage < -80:
        return 'hyperpolarized'
    elif voltage < -65:
        return 'resting'
    elif voltage < -30:
        return 'depolarized'
    else:
        return 'action_potential'

# Test voltage classifier
test_voltages = [-90, -70, -60, -50, -30, 0, 40]

print("\nVoltage Classification:")
print(f"{'Voltage (mV)':<15} {'State':<20} {'Description'}")
print("-" * 65)

descriptions = {
    'hyperpolarized': 'Below resting potential',
    'resting': 'Normal resting state',
    'depolarized': 'Above threshold, ready to fire',
    'action_potential': 'Active spike'
}

for v in test_voltages:
    state = classify_membrane_state(v)
    desc = descriptions[state]
    print(f"{v:<15} {state:<20} {desc}")

# Part d: Batch Processing
print("\n" + "=" * 60)
print("Part d: Batch Processing")
print("-" * 60)

def analyze_recordings(recordings):
    """
    Analyze multiple spike train recordings.
    
    Parameters:
    -----------
    recordings : list of dict
        Each dict must contain:
        - 'spike_times': list of spike times
        - 'duration': recording duration
        Optional:
        - 'cell_id': identifier for the recording
    
    Returns:
    --------
    list of dict
        Analysis results for each recording including:
        - All input fields
        - 'firing_rate': overall firing rate
        - 'isi_stats': ISI statistics dict
        - 'regularity': classification based on CV
    """
    results = []
    
    for rec in recordings:
        # Extract data
        spike_times = rec['spike_times']
        duration = rec['duration']
        cell_id = rec.get('cell_id', 'Unknown')
        
        # Calculate firing rate
        spike_count = len(spike_times)
        firing_rate = calculate_firing_rate(spike_count, duration)
        
        # Calculate ISI statistics (if enough spikes)
        if len(spike_times) >= 2:
            isi_stats = calculate_isi_statistics(spike_times)
            cv = isi_stats['cv']
            
            # Classify regularity
            if cv < 0.5:
                regularity = "regular"
            elif cv < 1.0:
                regularity = "irregular"
            else:
                regularity = "highly_irregular_or_bursting"
        else:
            isi_stats = None
            regularity = "insufficient_spikes"
        
        # Compile results
        result = {
            'cell_id': cell_id,
            'spike_count': spike_count,
            'duration': duration,
            'firing_rate': firing_rate,
            'isi_stats': isi_stats,
            'regularity': regularity
        }
        
        results.append(result)
    
    return results

# Test batch processing
test_recordings = [
    {
        'cell_id': 'Neuron_A',
        'spike_times': [0.1, 0.3, 0.5, 0.9, 1.2, 1.5, 1.8],
        'duration': 2.0
    },
    {
        'cell_id': 'Neuron_B',
        'spike_times': [0.05, 0.15, 0.35, 0.55, 0.75],
        'duration': 1.0
    },
    {
        'cell_id': 'Neuron_C',
        'spike_times': [0.1, 0.12, 0.14, 0.5, 0.52, 0.54, 1.0],
        'duration': 1.5
    },
]

results = analyze_recordings(test_recordings)

print("\nBatch Analysis Results:")
print("=" * 80)

for i, result in enumerate(results, 1):
    print(f"\nRecording {i}: {result['cell_id']}")
    print(f"  Spikes: {result['spike_count']} in {result['duration']:.1f}s")
    print(f"  Firing rate: {result['firing_rate']:.2f} Hz")
    print(f"  Regularity: {result['regularity']}")
    
    if result['isi_stats']:
        stats = result['isi_stats']
        print(f"  Mean ISI: {stats['mean_isi']:.3f}s (CV: {stats['cv']:.3f})")

# Bonus: Advanced neuroscience functions
print("\n" + "=" * 60)
print("BONUS: Additional Neuroscience Functions")
print("-" * 60)

def detect_bursts(spike_times, max_isi=0.1, min_spikes=3):
    """
    Detect burst events in spike train.
    
    A burst is defined as min_spikes or more spikes with ISI < max_isi.
    """
    if len(spike_times) < min_spikes:
        return []
    
    bursts = []
    current_burst = [spike_times[0]]
    
    for i in range(1, len(spike_times)):
        isi = spike_times[i] - spike_times[i-1]
        
        if isi < max_isi:
            current_burst.append(spike_times[i])
        else:
            if len(current_burst) >= min_spikes:
                bursts.append(current_burst)
            current_burst = [spike_times[i]]
    
    # Check last burst
    if len(current_burst) >= min_spikes:
        bursts.append(current_burst)
    
    return bursts

def calculate_fano_factor(spike_counts):
    """
    Calculate Fano factor (variance/mean) of spike counts.
    
    Used to quantify variability in neural responses.
    FF = 1: Poisson-like variability
    FF < 1: More regular than Poisson
    FF > 1: More variable than Poisson
    """
    mean_count = sum(spike_counts) / len(spike_counts)
    variance = sum((c - mean_count)**2 for c in spike_counts) / len(spike_counts)
    return variance / mean_count if mean_count > 0 else 0

# Test burst detection
print("\nBurst Detection:")
bursting_train = [0.1, 0.12, 0.14, 0.16, 0.5, 0.52, 0.54, 1.0, 1.02, 1.04, 1.06]
bursts = detect_bursts(bursting_train)
print(f"Detected {len(bursts)} bursts:")
for i, burst in enumerate(bursts, 1):
    print(f"  Burst {i}: {len(burst)} spikes from {burst[0]:.2f}s to {burst[-1]:.2f}s")

# Test Fano factor
print("\nFano Factor Analysis:")
spike_count_trials = [
    [10, 12, 11, 9, 10, 11],  # Regular
    [5, 15, 8, 12, 10, 20],   # Variable
]
for i, counts in enumerate(spike_count_trials, 1):
    ff = calculate_fano_factor(counts)
    mean = sum(counts) / len(counts)
    print(f"  Trial set {i}: Mean={mean:.1f}, FF={ff:.2f}")

print("\n" + "=" * 60)
print("SUMMARY")
print("-" * 60)
print("""
Neuroscience function library created with:
  • Firing rate calculation
  • ISI statistics (mean, SD, CV)
  • Membrane potential classification
  • Batch processing capabilities
  • Burst detection
  • Fano factor calculation

These functions form a reusable toolkit for spike train analysis!
""")
