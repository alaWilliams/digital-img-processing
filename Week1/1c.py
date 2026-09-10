# You can load a picture and stores it's pixel values into numpy array with following lines:

#    Image.open("IMAGE")
#    pixels=np.array(picture)
 
# A single pixel value can be accessed with
#    pixels[y,x,COLOR]
# Where color is 0,1,2 which are red, green,blue. Each color is an 8-bit value.
 
# Load linnanmaa.jpg
 
# Write a program that prints the color values of any pixel in the image.
# What is the color code of the pixel in upper left corner of the image?
 
# What are the width and height of the image in pixels?

from PIL import Image
import numpy as np

picture = Image.open("images/linnanmaa.jpg")
pixels = np.array(picture)

def print_pixel(y, x):
  r, g, b = pixels[y, x, 0], pixels[y, x, 1], pixels[y, x, 2]
  print(f"Pixel at (x={x}, y={y}) is R={r}, G={g}, B={b}")


print_pixel(0,0)

print(f"Picture width is: {picture.width}. Picture height is {picture.height}")



