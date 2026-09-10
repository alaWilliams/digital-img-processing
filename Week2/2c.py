# Write a function that makes a histogram of a black and white picture. Plot histogram of pictures flower.jpg and dark_flower.jpg.
# Attach the function into your report.
# Attach both pictures and their histograms into your report.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

picture = Image.open("img/flower.jpg")
pixels = np.array(picture)


def make_histogram(pixels):
    # reducing the image from 3 to 2 channels
    gray = pixels[:, :, 0]
    counts, bin_edges = np.histogram(gray, bins=256, range=(0, 256))
    return counts

counts = make_histogram(pixels)
x_positions = range(256)

plt.bar(x_positions, counts)
plt.xlabel("Pixel brightness")
plt.ylabel("Number of pixels")
plt.title("Histogram of flower.jpg")
plt.show()
plt.savefig("flower_hist.png")

picture2 = Image.open("img/dark_flower.jpg")
pixels2 = np.array(picture2)

counts2 = make_histogram(pixels2)

plt.bar(range(256), counts2)
plt.xlabel("Pixel brightness")
plt.ylabel("Number of pixels")
plt.title("Histogram of dark_flower.jpg")
plt.show()
plt.savefig("dark_flower_hist.png")