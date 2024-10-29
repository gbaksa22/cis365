"""
CIS 365 - Assignment 10

Date - 10/30/2024

This program was created by Gabe Baksa and Brenden Granzo
"""
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
image_path = "the-rock.png"
image = Image.open(image_path)

# Define the resolutions
small_size = (25, 25)    # Small resolution
medium_size = (100, 100)  # Medium resolution
large_size = (400, 400)   # Large resolution

# Resize images
small_image = image.resize(small_size)
medium_image = image.resize(medium_size)
large_image = image.resize(large_size)

# Step 4: Display all three resolutions on a single plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Small image
axes[0].imshow(small_image)
axes[0].set_title("Small Resolution (25x25)")
axes[0].axis('off')

# Medium image
axes[1].imshow(medium_image)
axes[1].set_title("Medium Resolution (100x100)")
axes[1].axis('off')

# Large image
axes[2].imshow(large_image)
axes[2].set_title("Large Resolution (400x400)")
axes[2].axis('off')

plt.show()
