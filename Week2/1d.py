from PIL import Image
import numpy as np

picture = Image.open("img/shirt_small.jpg")
pixels = np.array(picture)


def scale_nearest(pixels, scale):
    old_h, old_w = pixels.shape[0], pixels.shape[1]
    new_h = int(old_h * scale)
    new_w = int(old_w * scale)

    if pixels.ndim == 3:
        new_pixels = np.zeros((new_h, new_w, pixels.shape[2]), dtype=pixels.dtype)
    else:
        new_pixels = np.zeros((new_h, new_w), dtype=pixels.dtype)

    for y in range(new_h):
        for x in range(new_w):
            src_y = int(y / scale)
            src_x = int(x / scale)
            src_y = min(src_y, old_h - 1)
            src_x = min(src_x, old_w - 1)
            new_pixels[y, x] = pixels[src_y, src_x]

    return new_pixels

result_pixels = scale_nearest(pixels, 4)
result_image = Image.fromarray(result_pixels)
result_image.save("shirt_nearest.jpg")