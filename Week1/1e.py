# Write a python program that changes the original image so, that all three color channels have same information - average of the original R,G,B values. 

from PIL import Image
import numpy as np

picture = Image.open("images/shirt.jpg")
pixels = np.array(picture)

result = np.mean(pixels, axis=2).astype('uint8')

final = np.stack([result, result, result], axis = 2)

gray_image = Image.fromarray(final)
gray_image.save("shirt_gray.jpg")