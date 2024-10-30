"""Step 4: Display the Image at Different Resolutions in the Same Plot"""
from PIL import Image
import matplotlib.pyplot as plt

image_path = "the-rock.png"
image = Image.open(image_path)

small_size = (25, 25)
medium_size = (100, 100)
large_size = (400, 400)

small_image = image.resize(small_size)
medium_image = image.resize(medium_size)
large_image = image.resize(large_size)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(small_image)
axes[0].set_title("Small Resolution (25x25)")
axes[0].axis('off')

axes[1].imshow(medium_image)
axes[1].set_title("Medium Resolution (100x100)")
axes[1].axis('off')

axes[2].imshow(large_image)
axes[2].set_title("Large Resolution (400x400)")
axes[2].axis('off')

plt.show()
