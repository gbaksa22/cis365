"""
CIS 365 - Assignment 10

Date - 10/30/2024

This program was created by Gabe Baksa and Brenden Granzo
"""
from PIL import Image
import matplotlib.pyplot as plt

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image_path = "the-rock.png"
image = Image.open(image_path)

# Convert image to numpy array
image_array = np.array(image)

# Extract RGB channels
red_channel = image_array.copy()
green_channel = image_array.copy()
blue_channel = image_array.copy()

# Set non-relevant channels to zero for each color channel

# Red channel: zero out green and blue channels
red_channel = image_array.copy()
red_channel[:, :, 1] = 0  # Zero out green
red_channel[:, :, 2] = 0  # Zero out blue

# Green channel: zero out red and blue channels
green_channel = image_array.copy()
green_channel[:, :, 0] = 0  # Zero out red
green_channel[:, :, 2] = 0  # Zero out blue

# Blue channel: zero out red and green channels
blue_channel = image_array.copy()
blue_channel[:, :, 0] = 0  # Zero out red
blue_channel[:, :, 1] = 0  # Zero out green

# Step 5: Display the original image and color channels in a single plot
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

# Original image
axes[0].imshow(image_array)
axes[0].set_title("Original Image")
axes[0].axis('off')

# Red channel
axes[1].imshow(red_channel)
axes[1].set_title("Red Channel")
axes[1].axis('off')

# Green channel
axes[2].imshow(green_channel)
axes[2].set_title("Green Channel")
axes[2].axis('off')

# Blue channel
axes[3].imshow(blue_channel)
axes[3].set_title("Blue Channel")
axes[3].axis('off')

plt.show()
