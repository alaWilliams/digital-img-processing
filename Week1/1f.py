from PIL import Image
import numpy as np

picture = Image.open("images/linnanmaa.jpg")
pixels = np.array(picture)

def reduce_bits(pixels, bits):
    levels = 2**bits
    step = 255 / (levels -1)
    new_pixels = ((pixels / step).round() * step).astype('uint8')
    return new_pixels

for bits in [4, 3, 2, 1]:
    result = reduce_bits(pixels, bits)
    image = Image.fromarray(result)
    image.save(f"linnanmaa_{bits}bits.png")

