# 3d) Anti-alias
# Blur shirt.jpg first, then scale down by 0.17 to reduce aliasing.

from PIL import Image
import numpy as np
from week3a import expand_image

def gaussian_blur(pixels, gaussian_filter):
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

    return output


def scale_nearest(pixels, scale):
    old_h, old_w = pixels.shape[0], pixels.shape[1]
    new_h = int(old_h * scale)
    new_w = int(old_w * scale)

    new_pixels = np.zeros((new_h, new_w, pixels.shape[2]), dtype=pixels.dtype)

    for y in range(new_h):
        for x in range(new_w):
            src_y = int(y / scale)
            src_x = int(x / scale)
            src_y = min(src_y, old_h - 1)
            src_x = min(src_x, old_w - 1)
            new_pixels[y, x] = pixels[src_y, src_x]

    return new_pixels


picture = Image.open("img/shirt.jpg")
pixels = np.array(picture)

gaussian_filter = np.array([
    [0.00390625, 0.015625,   0.0234375, 0.015625,   0.00390625],
    [0.015625,   0.0625,     0.09375,   0.0625,     0.015625],
    [0.0234375,  0.09375,    0.140625,  0.09375,    0.0234375],
    [0.015625,   0.0625,     0.09375,   0.0625,     0.015625],
    [0.00390625, 0.015625,   0.0234375, 0.015625,   0.00390625]
])

blurred = gaussian_blur(pixels, gaussian_filter)
blurred_pixels = blurred.round().astype('uint8')

scaled_blurred = scale_nearest(blurred_pixels, 0.17)
Image.fromarray(scaled_blurred).save("shirt_scaled_blurred.jpg")

scaled = scale_nearest(pixels, 0.17)
Image.fromarray(scaled).save("shirt_scaled.jpg")

print("Done")