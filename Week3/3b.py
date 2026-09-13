# 3b) convolution filter
# Write a program that allows using a convolution filter of size 5x5 pixels to be used on the image. (use the function written at 3a to avoid making the image smaller)
# Use a gaussian filter of size 5x5:
# [[0.00390625 0.015625   0.0234375  0.015625   0.00390625]
#  [0.015625   0.0625     0.09375    0.0625     0.015625  ]
#  [0.0234375  0.09375    0.140625   0.09375    0.0234375 ]
#  [0.015625   0.0625     0.09375    0.0625     0.015625  ]
#  [0.00390625 0.015625   0.0234375  0.015625   0.00390625]]
#  to blur image "shirt.jpg"

from PIL import Image
import numpy as np
from week3a import expand_image



picture = Image.open("img/shirt.jpg")
pixels = np.array(picture)

gaussian_filter = np.array([
    [0.00390625, 0.015625,   0.0234375, 0.015625,   0.00390625],
    [0.015625,   0.0625,     0.09375,   0.0625,     0.015625],
    [0.0234375,  0.09375,    0.140625,  0.09375,    0.0234375],
    [0.015625,   0.0625,     0.09375,   0.0625,     0.015625],
    [0.00390625, 0.015625,   0.0234375, 0.015625,   0.00390625]
])

pad = 2
padded_pixels = expand_image(pixels, pad)

old_h, old_w, channels = pixels.shape
output = np.zeros((old_h, old_w, channels), dtype='float64')


gaussian_filter_3d = gaussian_filter[:, :, np.newaxis]


for y in range(old_h):
    for x in range(old_w):
        window = padded_pixels[y : y + 2*pad + 1, x : x + 2*pad + 1, :]
        product = window * gaussian_filter_3d
        result = product.sum(axis=(0, 1))
        output[y, x] = result

print("Loop finished")

blurred_pixels = output.round().astype('uint8')
blurred_image = Image.fromarray(blurred_pixels)
blurred_image.save("shirt_blurred.jpg")
print("Saved")

diff = np.abs(pixels.astype(int) - blurred_pixels.astype(int))
print("Max difference:", diff.max())
print("Mean difference:", diff.mean())
print("% pixels that changed at all:", (diff.sum(axis=2) > 0).mean() * 100)