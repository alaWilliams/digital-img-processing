import numpy as np
from scipy.fft import dctn
from PIL import Image
import matplotlib.pyplot as plt

filenames = ["img/smooth.png", "img/vertical_stripes.png", "img/checkerboard.png"]
titles = ["smooth.png", "vertical_stripes.png", "checkerboard.png"]

fig, axes = plt.subplots(2, 3, figsize=(13, 8))

for col, (fname, title) in enumerate(zip(filenames, titles)):
    img = np.array(Image.open(fname).convert("L"), dtype=float)

    dct2 = dctn(img, type=2, norm="ortho")

    axes[0, col].imshow(img, cmap="gray")
    axes[0, col].set_title(title)
    axes[0, col].axis("off")

    axes[1, col].imshow(np.log(np.abs(dct2) + 1), cmap="viridis")
    axes[1, col].set_title(f"2D DCT of {title}")
    axes[1, col].axis("off")

plt.tight_layout()
plt.savefig("5d_dct_images.png", dpi=150)