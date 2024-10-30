"""Step 6: Display the Image and its RGB Channels"""
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image_path = "the-rock.png"
image = Image.open(image_path)
image_array = np.array(image)

red_channel = image_array.copy()
green_channel = image_array.copy()
blue_channel = image_array.copy()

red_channel[:, :, 1] = 0
red_channel[:, :, 2] = 0

green_channel[:, :, 0] = 0
green_channel[:, :, 2] = 0

blue_channel[:, :, 0] = 0
blue_channel[:, :, 1] = 0

fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(image_array)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(red_channel)
axes[1].set_title("Red Channel")
axes[1].axis('off')

axes[2].imshow(green_channel)
axes[2].set_title("Green Channel")
axes[2].axis('off')

axes[3].imshow(blue_channel)
axes[3].set_title("Blue Channel")
axes[3].axis('off')

plt.show()
