# 3a) Expanding image for convolution filtering:
# Write a function that expands an image from it's edges by 2 pixels on each edge by copying the adjacent pixel.
# Test the function using a random data matrix of size 5,5,3 (y size = 5, x size = 5, 3 color channels) that you can generate your self. 

import numpy as np

np.set_printoptions(linewidth=200)



def expand_image(pixels, pad):

  old_h, old_w, channels = pixels.shape 
  new_h = old_h + pad * 2
  new_w = old_w + pad * 2

  new_pixels = np.zeros((new_h, new_w, channels), dtype=pixels.dtype)

  # placing img in the center
  new_pixels[pad:pad+old_h, pad:pad+old_w] = pixels

  #top & bottom borders  
  top_row = pixels[0, :, :]
  new_pixels[0:pad, pad:pad+old_w] = top_row

  bottom_row = pixels[-1, :, :]
  new_pixels[new_h - pad : new_h, pad:pad+old_w] = bottom_row

  # left & right borders
  left_col = pixels[:, 0:1, :]
  new_pixels[pad:pad+old_h, 0:pad] = left_col

  right_col = pixels[:, -1:, :]
  new_pixels[pad:pad+old_h, new_w-pad:new_w] = right_col


  # corners
  top_left_pixel = pixels[0, 0, :]
  top_right_pixel = pixels[0, -1, :]
  bottom_left_pixel = pixels[-1, 0, :]
  bottom_right_pixel = pixels[-1, -1, :]

  new_pixels[0:pad, 0:pad] = top_left_pixel
  new_pixels[0:pad, new_w-pad:new_w] = top_right_pixel
  new_pixels[new_h-pad:new_h, 0:pad] = bottom_left_pixel
  new_pixels[new_h-pad:new_h, new_w-pad:new_w] = bottom_right_pixel

  return new_pixels

if __name__ == "__main__":
    pixels = np.random.randint(0, 256, size=(5, 5, 3), dtype='uint8')
    expanded = expand_image(pixels, pad=2)

    print("Original:")
    print(pixels)
    print("\nExpanded:")
    print(expanded)