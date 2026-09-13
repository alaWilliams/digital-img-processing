# 3c) Unsharp mask
# Calculate an unsharp mask (difference of original and blurred image) for 17.jpg.
# Sharpen the image by adding the mask with multiplier 1.

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


picture = Image.open("img/17.png")
pixels = np.array(picture)

gaussian_filter = np.array([
    [0.00390625, 0.015625,   0.0234375, 0.015625,   0.00390625],
    [0.015625,   0.0625,     0.09375,   0.0625,     0.015625],
    [0.0234375,  0.09375,    0.140625,  0.09375,    0.0234375],
    [0.015625,   0.0625,     0.09375,   0.0625,     0.015625],
    [0.00390625, 0.015625,   0.0234375, 0.015625,   0.00390625]
])

blurred = gaussian_blur(pixels, gaussian_filter)


mask = pixels.astype('float64') - blurred

multiplier = 1
sharpened = pixels.astype('float64') + multiplier * mask


sharpened_clipped = np.clip(sharpened, 0, 255)
sharpened_pixels = sharpened_clipped.round().astype('uint8')

sharpened_image = Image.fromarray(sharpened_pixels)
sharpened_image.save("17_sharpened.jpg")


mask_visual = np.clip(mask + 128, 0, 255).round().astype('uint8')
mask_image = Image.fromarray(mask_visual)
mask_image.save("17_mask.jpg")

print("Done")