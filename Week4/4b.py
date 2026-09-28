import numpy as np
import matplotlib.pyplot as plt

fs = 100000          
duration = 0.01       
t = np.arange(0, duration, 1/fs)
N = len(t)


sine1k = np.sin(2 * np.pi * 1000 * t)

square1k = np.sign(np.sin(2 * np.pi * 1000 * t))

sine_sum = np.sin(2 * np.pi * 1000 * t) + np.sin(2 * np.pi * 8000 * t)

signals = {
    "1 kHz sine wave": sine1k,
    "1 kHz square wave": square1k,
    "1 kHz + 8 kHz sine sum": sine_sum
}

freqs = np.fft.fftfreq(N, d=1/fs)
pos_mask = freqs >= 0

fig, axes = plt.subplots(3, 2, figsize=(14, 10))

for i, (name, signal) in enumerate(signals.items()):
    axes[i,0].plot(t[:200], signal[:200])
    axes[i,0].set_title(f"{name} - time domain")
    axes[i,0].set_xlabel("Time (s)")
    axes[i,0].set_ylabel("Amplitude")

    spectrum = np.fft.fft(signal)
    magnitude = np.abs(spectrum) / N

    axes[i,1].plot(freqs[pos_mask], magnitude[pos_mask])
    axes[i,1].set_title(f"{name} - frequency domain")
    axes[i,1].set_xlabel("Frequency (Hz)")
    axes[i,1].set_ylabel("Magnitude")
    axes[i,1].set_xlim(0, 20000)

plt.tight_layout()
plt.savefig("4b_signals_and_spectra.png", dpi=110)