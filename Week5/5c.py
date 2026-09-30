import numpy as np
from scipy.fft import dct, idct, fft, ifft
import matplotlib.pyplot as plt

N = 8
signal = np.arange(N)  
dct_coeffs = dct(signal, type=2, norm='ortho')
dft_coeffs = fft(signal)


n_zero_dct = N // 2
zero_idx_dct = np.argsort(np.abs(dct_coeffs))[:n_zero_dct]
dct_coeffs_zeroed = dct_coeffs.copy()
dct_coeffs_zeroed[zero_idx_dct] = 0


n_unique = N // 2 + 1
n_zero_dft = n_unique // 2
zero_idx_unique = np.argsort(np.abs(dft_coeffs[:n_unique]))[:n_zero_dft]

dft_coeffs_zeroed = dft_coeffs.copy()
for k in zero_idx_unique:
    dft_coeffs_zeroed[k] = 0
    if k != 0 and k != N // 2:
        dft_coeffs_zeroed[N - k] = 0   

reconstructed_dct = idct(dct_coeffs_zeroed, type=2, norm='ortho')
reconstructed_dft = np.real(ifft(dft_coeffs_zeroed))

n = np.arange(N)
plt.figure(figsize=(8, 5))
plt.plot(n, signal, 'o-', label="Original ramp", linewidth=2)
plt.plot(n, reconstructed_dct, 's--', label="Reconstructed from DCT (half zeroed)")
plt.plot(n, reconstructed_dft, '^--', label="Reconstructed from DFT (half zeroed)")
plt.xlabel("n")
plt.ylabel("value")
plt.title("Original vs. reconstructed signal (half coefficients zeroed)")
plt.legend()
plt.savefig("5c_reconstruction.png", dpi=150)
plt.show()