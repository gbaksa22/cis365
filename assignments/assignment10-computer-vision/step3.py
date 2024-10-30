"""Step 3: Display the Image at Different Resolutions in Seperate Plots"""
from PIL import Image
import matplotlib.pyplot as plt

image_path = "the-rock.png"
image = Image.open(image_path)

small_size = (25, 25)
medium_size = (100, 100)
large_size = (400, 400)

small_image = image.resize(small_size)
plt.figure("Small Resolution - 25x25", figsize=(5, 5))
plt.imshow(small_image)
plt.title("Small Resolution (25x25)")
plt.axis('off')
plt.show()

medium_image = image.resize(medium_size)
plt.figure("Medium Resolution - 100x100", figsize=(5, 5))
plt.imshow(medium_image)
plt.title("Medium Resolution (100x100)")
plt.axis('off')
plt.show()

large_image = image.resize(large_size)
plt.figure("Large Resolution - 400x400", figsize=(5, 5))
plt.imshow(large_image)
plt.title("Large Resolution (400x400)")
plt.axis('off')
plt.show()