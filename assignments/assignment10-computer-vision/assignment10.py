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

# Define the updated resolutions
small_size = (25, 25)    # Small resolution
medium_size = (100, 100)  # Medium resolution
large_size = (400, 400)   # Large resolution

# Step 3a: Display the small resolution image in a new window
small_image = image.resize(small_size)
plt.figure("Small Resolution - 25x25", figsize=(5, 5))
plt.imshow(small_image)
plt.title("Small Resolution (25x25)")
plt.axis('off')
plt.show()

# Step 3b: Display the medium resolution image in a new window
medium_image = image.resize(medium_size)
plt.figure("Medium Resolution - 100x100", figsize=(5, 5))
plt.imshow(medium_image)
plt.title("Medium Resolution (100x100)")
plt.axis('off')
plt.show()

# Step 3c: Display the large resolution image in a new window
large_image = image.resize(large_size)
plt.figure("Large Resolution - 400x400", figsize=(5, 5))
plt.imshow(large_image)
plt.title("Large Resolution (400x400)")
plt.axis('off')
plt.show()
