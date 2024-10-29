"""
CIS 365 - Assignment 10

Date - 10/30/2024

This program was created by Gabe Baksa and Brenden Granzo
"""

from PIL import Image

# Step 1: Read the image
image_path = "the-rock.png"
image = Image.open(image_path)

# Display basic information about the image
print("Image loaded successfully!")
print(f"Format: {image.format}, Size: {image.size}, Mode: {image.mode}")

# Show the image (optional)
image.show()
