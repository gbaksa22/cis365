"""Step 2: Display the Image"""
from PIL import Image

image_path = "the-rock.png"
image = Image.open(image_path)

image.show() # ChatGPT showed me how to display the image