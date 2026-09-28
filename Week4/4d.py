# 4d) Frequency domain filtering
# Remove all frequencies more than 50 distance from 0-frequency, then reconstruct the image.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

picture = Image.open("img/fox.jpg").convert("L")
pixels = np.array(picture)

F = np.fft.fft2(pixels)
F_shifted = np.fft.fftshift(F)

h, w = pixels.shape
center_y, center_x = h // 2, w // 2

y, x = np.indices((h, w))
distance = np.sqrt((y - center_y)**2 + (x - center_x)**2)
mask = distance <= 50


F_filtered = F_shifted * mask

F_unshifted = np.fft.ifftshift(F_filtered)
filtered_pixels = np.fft.ifft2(F_unshifted)
filtered_pixels = np.abs(filtered_pixels)  
filtered_pixels = filtered_pixels.round().astype('uint8')

original_spectrum = np.log(1 + np.abs(F_shifted))
filtered_spectrum = np.log(1 + np.abs(F_filtered))


fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0,0].imshow(pixels, cmap='gray')
axes[0,0].set_title("Original image")

axes[0,1].imshow(original_spectrum, cmap='gray')
axes[0,1].set_title("Original spectrum")

axes[1,0].imshow(filtered_pixels, cmap='gray')
axes[1,0].set_title("Filtered image")

axes[1,1].imshow(filtered_spectrum, cmap='gray')
axes[1,1].set_title("Filtered spectrum (low frequencies only)")

plt.tight_layout()
plt.savefig("4d_frequency_filtering.png", dpi=110)

Image.fromarray(filtered_pixels).save("fox_filtered.jpg")
print("Done")