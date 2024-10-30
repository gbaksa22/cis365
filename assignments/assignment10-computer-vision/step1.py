"""Step 1: Read the Image"""
from PIL import Image

image_path = "the-rock.png"
image = Image.open(image_path)

print("Image loaded successfully!")
print(f"Format: {image.format}, Size: {image.size}, Mode: {image.mode}")