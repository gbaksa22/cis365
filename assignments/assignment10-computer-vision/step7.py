"""Step 7: Calculate the Histogram of the Image Manually"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "the-rock.png"
image = Image.open(image_path).convert("RGB")
image_array = np.array(image)

red_histogram = [0] * 256
green_histogram = [0] * 256
blue_histogram = [0] * 256

for row in image_array:
    for pixel in row:
        red_value, green_value, blue_value = pixel[0], pixel[1], pixel[2]
        red_histogram[red_value] += 1
        green_histogram[green_value] += 1
        blue_histogram[blue_value] += 1

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].bar(range(256), red_histogram, color='red')
axes[0].set_title("Red Channel Histogram")
axes[0].set_xlim(0, 255)

axes[1].bar(range(256), green_histogram, color='green')
axes[1].set_title("Green Channel Histogram")
axes[1].set_xlim(0, 255)

axes[2].bar(range(256), blue_histogram, color='blue')
axes[2].set_title("Blue Channel Histogram")
axes[2].set_xlim(0, 255)

plt.show()
