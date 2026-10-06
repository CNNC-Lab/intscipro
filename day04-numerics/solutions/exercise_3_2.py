# Exercise 3.2: Signal Processing
from scipy import signal as sig
import matplotlib.pyplot as plt
import numpy as np

# Create signal
fs = 1000
t = np.linspace(0, 1, fs)

signal_5hz = np.sin(2 * np.pi * 5 * t)
signal_50hz = 0.5 * np.sin(2 * np.pi * 50 * t)
noise = 0.2 * np.random.randn(len(t))
signal_combined = signal_5hz + signal_50hz + noise

# a) Plot original signal
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(t[:200], signal_combined[:200])  # Show first 200ms
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original Signal')
plt.grid(True, alpha=0.3)

# b) Design lowpass filter
cutoff = 10  # Hz
order = 4
b, a = sig.butter(order, cutoff, btype='low', fs=fs)

# c) Apply filter
filtered = sig.filtfilt(b, a, signal_combined)

# d) Compare original and filtered
plt.subplot(3, 2, 2)
plt.plot(t[:200], signal_combined[:200], alpha=0.5, label='Original')
plt.plot(t[:200], filtered[:200], linewidth=2, label='Filtered')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original vs Filtered')
plt.legend()
plt.grid(True, alpha=0.3)

# e) Power spectral density
freqs, psd = sig.welch(signal_combined, fs=fs, nperseg=256)

plt.subplot(3, 2, 3)
plt.semilogy(freqs, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')
plt.title('PSD of Original Signal')
plt.xlim(0, 100)
plt.grid(True, alpha=0.3)

# f) Find peaks
peaks, properties = sig.find_peaks(filtered, distance=100)

plt.subplot(3, 2, 4)
plt.plot(t, filtered, alpha=0.7, label='Filtered signal')
plt.plot(t[peaks], filtered[peaks], 'ro', markersize=8, label='Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title(f'Peak Detection ({len(peaks)} peaks found)')
plt.legend()
plt.grid(True, alpha=0.3)

# Bonus: Show filter frequency response
plt.subplot(3, 2, 5)
w, h = sig.freqz(b, a, worN=2000, fs=fs)
plt.plot(w, 20 * np.log10(abs(h)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Filter Frequency Response')
plt.axvline(cutoff, color='r', linestyle='--', label=f'Cutoff={cutoff}Hz')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 100)

plt.tight_layout()
plt.show()

print(f"Original signal contains: 5 Hz + 50 Hz + noise")
print(f"Filter cutoff: {cutoff} Hz")
print(f"Number of peaks detected: {len(peaks)}")
print(f"Expected peaks in 1 second at 5 Hz: ~5")
