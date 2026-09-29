import numpy as np
import matplotlib.pyplot as plt

N = 8
n_values = list(range(N))

def dct_basis(k):
    alpha_k = np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N)
    values = []
    for n in n_values:
        angle = (np.pi / N) * (n + 0.5) * k
        values.append(alpha_k * np.cos(angle))
    return values

def dft_real_part(k):
    return [np.cos(2 * np.pi * k * n / N) for n in n_values]

def dft_imag_part(k):
    return [-np.sin(2 * np.pi * k * n / N) for n in n_values]

def dft_magnitude(k):
    real = dft_real_part(k)
    imag = dft_imag_part(k)
    return [np.sqrt(r**2 + i**2) for r, i in zip(real, imag)]

fig, axes = plt.subplots(2, 4, figsize=(16, 6))

for row, k in enumerate([0, 1]):
    axes[row, 0].stem(n_values, dct_basis(k))
    axes[row, 0].set_title(f"DCT basis, k={k}")

    axes[row, 1].stem(n_values, dft_real_part(k))
    axes[row, 1].set_title(f"DFT real part, k={k}")

    axes[row, 2].stem(n_values, dft_imag_part(k))
    axes[row, 2].set_title(f"DFT imaginary part, k={k}")

    axes[row, 3].stem(n_values, dft_magnitude(k))
    axes[row, 3].set_title(f"DFT magnitude, k={k}")

plt.tight_layout()
plt.savefig("5a_basis_functions.png", dpi=150)
plt.show()