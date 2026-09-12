# 3a) Expanding image for convolution filtering:
# Write a function that expands an image from it's edges by 2 pixels on each edge by copying the adjacent pixel.
# Test the function using a random data matrix of size 5,5,3 (y size = 5, x size = 5, 3 color channels) that you can generate your self. 

from PIL import Image
import numpy as np


# picture = Image.open("img/17.png")
# pixels = np.array(picture)
pixels = np.random.randint(0, 256, size=(5, 5, 3), dtype='uint8')

old_h, old_w, channels = pixels.shape

pad = 2

new_h = old_h + pad * 2
new_w = old_w + pad * 2

new_pixels = np.zeros((new_h, new_w, channels), dtype=pixels.dtype)
new_pixels[pad:pad+old_h, pad:pad+old_w] = pixels

# print(pixels.shape)
# print(new_pixels.shape)

# print(new_pixels)

top_row = pixels[0, :, :]

print(top_row)

print(pixels)