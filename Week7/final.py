import numpy as np
from PIL import Image

picture = Image.open("photo.bmp")
img = np.array(picture)

# print(img.shape)
# print(img.dtype)

counter = 0
for y in range(0, 640, 8):
  # print(x)
  for x in range (0,640, 8):
    block = img[y:y+8, x:x+8]
    counter += 1

print(counter)

block =img[0:8, 0:8]
print(block.min())
print(block.max())
shifted = block.astype(np.float64) - 128
print(shifted.min())
print(shifted.max())

def dct_matrix(n):
  matrix = np.zeros((n, n))
  for u in range (n) : 
    for x in range (n):
      if (u == 0):
        matrix[u][x] = np.sqrt(1/n) * np.cos((2*x + 1) * u * np.pi / (2*n))
      else: 
        matrix[u][x] = np.sqrt(2/n) * np.cos((2*x + 1) * u * np.pi / (2*n))        
  return matrix

print(dct_matrix(2))

