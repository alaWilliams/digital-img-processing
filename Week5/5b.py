import numpy as np
from scipy.fft import dct, fft 
import matplotlib.pyplot as plt

N = 8
signal = np.arange(N)  


dct_coeffs = dct(signal, type=2, norm='ortho')
dft_coeffs = fft(signal)

k_values = np.arange(N)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].stem(k_values, dct_coeffs);          axes[0].set_title("DCT coefficients")
axes[1].stem(k_values, dft_coeffs.real);     axes[1].set_title("DFT coefficients (real part)")
axes[2].stem(k_values, dft_coeffs.imag);     axes[2].set_title("DFT coefficients (imaginary part)")
plt.tight_layout()
plt.savefig("5b_ramp.png", dpi=150)