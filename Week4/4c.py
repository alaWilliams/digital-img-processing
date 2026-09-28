from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

filenames = ["img/vl.png", "img/hl.png", "img/diag.png"]

fig, axes = plt.subplots(len(filenames), 2, figsize=(10, 12))

for i, filename in enumerate(filenames):
    picture = Image.open(filename).convert("L")  
    pixels = np.array(picture)

    F = np.fft.fft2(pixels)
    F_shifted = np.fft.fftshift(F)
    visual_spectrum = np.log(1 + np.abs(F_shifted))

    axes[i, 0].imshow(pixels, cmap='gray')
    axes[i, 0].set_title(f"{filename} - image")

    axes[i, 1].imshow(visual_spectrum, cmap='gray')
    axes[i, 1].set_title(f"{filename} - spectrum")

plt.tight_layout()
plt.savefig("4c_images_and_spectra.png", dpi=110)
print("Done")