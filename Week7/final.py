import numpy as np
from PIL import Image
import os

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

# print(counter)

block =img[0:8, 0:8]
# print(block.min())
# print(block.max())
shifted = block.astype(np.float64) - 128
# print(shifted.min())
# print(shifted.max())

def dct_matrix(n):
  matrix = np.zeros((n, n))
  for u in range (n) : 
    for x in range (n):
      if (u == 0):
        matrix[u][x] = np.sqrt(1/n) * np.cos((2*x + 1) * u * np.pi / (2*n))
      else: 
        matrix[u][x] = np.sqrt(2/n) * np.cos((2*x + 1) * u * np.pi / (2*n))        
  return matrix

# print(dct_matrix(2))

C = dct_matrix(8)
N=8

def dct2(block):
  return C @ block @ C.T

test = np.full((8, 8), 10.0)

# print(np.round(dct2(test), 2))

def quantize(coeffs, Q):
  result = np.round(coeffs / Q)
  result = np.clip(result, -128, 127).astype(np.int8)
  return result

coeffs = dct2(shifted)
quantized= quantize(coeffs, 16)
# print(q)
d=3
def diagonal(d, n):
  cells = []
  for r in range(n):
      if d-r >= 0 and d-r <= n-1:
        cells.append((r, d-r))
  if d % 2 == 0:
    cells.reverse()
  return cells

def zigzag_order(n):
    order = []
    for d in range(2 * n - 1):
        order.extend(diagonal(d, n))
    return order

order = zigzag_order(N)

def zigzag(block):
    values = []
    for r, c in order:
        values.append(block[r][c])
    return np.array(values)

def rle_encode(values):
    out = []
    zeros = 0
    for v in values:
        if v == 0:
            zeros += 1
        else:
            if zeros > 0:
                out.extend([0, zeros])
                zeros = 0
            out.append(int(v))
    if zeros > 0:
        out.extend([0, zeros])
    return out

encoded = rle_encode(zigzag(quantized))

def compress(img, Q):
  h, w = img.shape
  shifted = img.astype(np.float64) - 128                      
  stream = []
  for by in range(0, h, N): 
    for bx in range(0, w, N):
      block = shifted[by:by + N, bx:bx + N]
      coeffs = dct2(block)                                
      q = np.round(coeffs / Q)                           
      q = np.clip(q, -128, 127).astype(np.int8)
      stream.extend(rle_encode(zigzag(q))) 
  return np.array(stream, dtype=np.int8)

compressed = compress(img, 16)
# print(len(compressed))

compressed.tofile("compressed.bin")
from_file = np.fromfile("compressed.bin", dtype=np.int8)

def rle_decode_block(data, pos):
  coeffs = []
  while len(coeffs) < 64:
      v = int(data[pos])
      pos += 1
      if v == 0:
        run = int(data[pos])
        pos += 1
        coeffs.extend([0] * run)
      else:
        coeffs.append(v)
  return np.array(coeffs, dtype=np.int16), pos

def inverse_zigzag(vec):
    block = np.zeros((N, N))
    for i, (r, c) in enumerate(order):
        block[r][c] = vec[i]
    return block

def inverse_dct2(block):
   return C.T @ block @ C

back = inverse_dct2(dct2(shifted))
print(np.allclose(back, shifted))

def decode_block(data, pos, Q):
  coeffs, pos = rle_decode_block(data, pos)
  quantized = inverse_zigzag(coeffs)
  dct_block = quantized * Q
  block = inverse_dct2(dct_block) + 128
  block = np.clip(np.round(block), 0, 255).astype(np.uint8)
  return block, pos


data = np.array(rle_encode(zigzag(quantized)), dtype=np.int8)
rec, pos = decode_block(data, 0, 16)
orig = img[0:8, 0:8]
print(np.abs(rec.astype(int) - orig.astype(int)).max())
print(pos)
print(len(data))

def decompress(data, Q, h=640, w=640,):
  rec = np.zeros((h, w))
  pos = 0
  for by in range(0, h, N):
    for bx in range(0, w, N):
      coeffs, pos = rle_decode_block(data, pos)           
      q = inverse_zigzag(coeffs).astype(np.float64)       
      dct_block = q * Q                                    
      block = inverse_dct2(dct_block)                             
      rec[by:by + N, bx:bx + N] = block + 128              
  return np.clip(np.round(rec), 0, 255).astype(np.uint8)       

from_file = np.fromfile("compressed.bin", dtype=np.int8)
rec = decompress(from_file, 16)
print(rec.shape, rec.dtype)
Image.fromarray(rec).save("reconstructed_Q16.bmp")

for Q in (16, 32, 64, 128):
  compressed = compress(img, Q)
  filename = f"compressed_Q{Q}.bin"
  compressed.tofile(filename)                                
  from_file = np.fromfile(filename, dtype=np.int8)            
  assert np.array_equal(compressed, from_file)
  rec = decompress(from_file, Q=Q)                         # i)
  Image.fromarray(rec).save(f"reconstructed_Q{Q}.bmp")
  size = os.path.getsize(filename)
  original_bytes = img.size
  print(f"{Q:>4} {size:>17} {original_bytes / size:>8.2f}")