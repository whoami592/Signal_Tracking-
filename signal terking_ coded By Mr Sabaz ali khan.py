import time
import numpy as np
import scipy.signal as signal
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

# Constants
BANDWIDTH = 1000  # Bandwidth in Hz
CARRIER_FREQ = 100  # Carrier frequency in Hz
SAMPLING_FREQ = 44100  # Sampling frequency in Hz
TONE_FREQ = 1000  # Tone frequency in Hz
TONE_DURATION = 0.1  # Tone duration in seconds
TONE_AMPLITUDE = 0.5  # Tone amplitude

# Generate the tone
t = np.linspace(0, TONE_DURATION, int(TONE_DURATION * SAMPLING_FREQ), endpoint=False)
tone = TONE_AMPLITUDE * np.sin(2 * np.pi * TONE_FREQ * t)

# Generate the carrier signal
t = np.linspace(0, TONE_DURATION, int(TONE_DURATION * SAMPLING_FREQ), endpoint=False)
carrier = np.sin(2 * np.pi * CARRIER_FREQ * t)

# Mix the tone and carrier
modulated_signal = tone * carrier

# Apply a low-pass filter to the modulated signal
cutoff_freq = CARRIER_FREQ + 0.5 * BANDWIDTH
nyquist_freq = SAMPLING_FREQ / 2
cutoff_norm = cutoff_freq / nyquist_freq
b, a = signal.butter(5, cutoff_norm, 'low')
filtered_signal = signal.filtfilt(b, a, modulated_signal)

# Add noise to the filtered signal
noise = np.random.normal(0, 0.1, len(filtered_signal))
noisy_signal = filtered_signal + noise

# Plot the original and noisy signals
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(t, tone)
plt.title('Original Tone')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(1, 2, 2)
plt.plot(t, noisy_signal)
plt.title('Noisy Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Perform signal jamming
jammed_signal = noisy_signal

# Transmit the jammed signal
# (This would be done over the air, but we are simulating here)

# Receive the jammed signal
received_signal = jammed_signal

# Demodulate the received signal
demodulated_signal = received_signal * carrier

# Plot the received and demodulated signals
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(t, received_signal)
plt.title('Received Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(1, 2, 2)
plt.plot(t, demodulated_signal)
plt.title('Demodulated Tone')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()