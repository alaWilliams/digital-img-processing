import numpy as np
from PIL import Image

picture = Image.open("photo.bmp")
img = np.array(picture)

print(img.shape)
print(img.dtype)
