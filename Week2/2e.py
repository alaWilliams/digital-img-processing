# 3e) Histogram matching:
# Implement a function that will make a mapping between intensity values of histogram A into histogram B.  
# Attach the function into your report.
# Make histogram matching for dark_flower.jpg using histogram of flower.jpg.
# Attach the code, both original pictures, and the resulting picture into your report.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def make_histogram(pixels):
    gray = pixels[:, :, 0]
    counts, bin_edges = np.histogram(gray, bins=256, range=(0, 256))
    return counts

def make_cdf(counts):
    cdf = np.cumsum(counts)
    return cdf

def make_mapping(cdf_a, cdf_b):
    mapping = np.zeros(256, dtype='uint8')
    for v in range(256):
        diff = np.abs(cdf_b - cdf_a[v])
        mapping[v] = np.argmin(diff)
    return mapping

def apply_mapping(pixels, mapping):
    gray = pixels[:, :, 0]
    matched_gray = mapping[gray]
    matched = np.stack([matched_gray, matched_gray, matched_gray], axis=2)
    return matched


dark_picture = Image.open("img/dark_flower.jpg")
dark_pixels = np.array(dark_picture)

flower_picture = Image.open("img/flower.jpg")
flower_pixels = np.array(flower_picture)

# Build histograms and CDFs
counts_dark = make_histogram(dark_pixels)
cdf_dark = make_cdf(counts_dark)

counts_flower = make_histogram(flower_pixels)
cdf_flower = make_cdf(counts_flower)

mapping = make_mapping(cdf_dark, cdf_flower)

matched_pixels = apply_mapping(dark_pixels, mapping)

matched_image = Image.fromarray(matched_pixels)
matched_image.save("dark_flower_matched.jpg")

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(dark_pixels, cmap='gray')
plt.title("dark_flower.jpg (original)")

plt.subplot(1, 3, 2)
plt.imshow(flower_pixels, cmap='gray')
plt.title("flower.jpg (reference)")

plt.subplot(1, 3, 3)
plt.imshow(matched_pixels, cmap='gray')
plt.title("dark_flower.jpg (matched)")

plt.savefig("histogram_matching_result.png")
plt.show()