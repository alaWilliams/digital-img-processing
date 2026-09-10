# Use shirt_small.jpg. Scale it's size up by factor 4 using the function you implemented last week.

# Implement a new scaling function that does the scaling using bilinear interpolation. Repeat the upscaling using this function.

from PIL import Image
import numpy as np

picture = Image.open("img/shirt_small.jpg")
pixels = np.array(picture)

def scale_bilinear(pixels, scale):
    old_h, old_w = pixels.shape[0], pixels.shape[1]
    new_h = int(old_h * scale)
    new_w = int(old_w * scale)
    
    new_pixels = np.zeros((new_h, new_w, pixels.shape[2]), dtype=pixels.dtype)
    
    for y in range(new_h):
        for x in range(new_w):
            src_y = y / scale
            src_x = x / scale
            y0 = int(src_y)
            y1 = y0 + 1
            x0 = int(src_x)
            x1 = x0 + 1
            dy = src_y - y0
            dx = src_x - x0
            x1 = min(x0 + 1, old_w - 1)
            y1 = min(y0 + 1, old_h - 1)

            top_left = pixels[y0, x0]
            top_right = pixels[y0, x1]
            bottom_left = pixels[y1, x0]
            bottom_right = pixels[y1, x1]

            top_blend_x = top_left * (1 - dx) + top_right * dx
            bottom_blend_x = bottom_left * (1-dx) + bottom_right*dx

            result = top_blend_x * (1 - dy) + bottom_blend_x * dy

            new_pixels[y, x] = result.round().astype('uint8')    
    return new_pixels

result_pixels = scale_bilinear(pixels, 4)
result_image = Image.fromarray(result_pixels)
result_image.save("shirt_bilinear.jpg")