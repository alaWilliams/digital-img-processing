from PIL import Image
import numpy as np

picture = Image.open("images/shirt.jpg")

new_width = int(picture.width * 0.17)
new_height = int(picture.height * 0.17)

scaled_image = picture.resize((new_width, new_height))
scaled_image.save("shirt_scaled1.jpg")
