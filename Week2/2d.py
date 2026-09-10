# 2d) Cumulative density function

# Implement a function that converts histogram into a cumulative densify function (CDF). 

# Attach the function into your report.

# Plot histogram, CDF and the picture flower.jpg, and attach them into your report.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

picture = Image.open("img/flower.jpg")
pixels = np.array(picture)

def make_cdf(counts):
    cdf = np.cumsum(counts)
    return cdf

def make_histogram(pixels):
    gray = pixels[:, :, 0]
    counts, bin_edges = np.histogram(gray, bins=256, range=(0, 256))
    return counts

counts = make_histogram(pixels)  
cdf = make_cdf(counts)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(pixels, cmap='gray')
plt.title("Flower")

plt.subplot(1, 3, 2)
plt.bar(range(256), counts)
plt.title("Histogram")
plt.xlabel("Pixel brightness")
plt.ylabel("Number of pixels")

plt.subplot(1, 3, 3)
plt.plot(cdf)
plt.title("CDF")
plt.xlabel("Pixel brightness")
plt.ylabel("Cumulative pixel count")

plt.savefig("flower_analysis.png")
plt.show()