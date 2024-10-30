"""Step 10: Smoothing Filter"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

image_path = "the-rock.png"
image = Image.open(image_path).convert("RGB")
image_array = np.array(image)

smoothing_filter = np.array([[1/9, 1/9, 1/9],
                              [1/9, 1/9, 1/9],
                              [1/9, 1/9, 1/9]])

# Got some help from ChatGPT for a lot of the smoothing process below
# Apply the filter to each channel separately
red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]

smoothed_red = convolve(red_channel, smoothing_filter)
smoothed_green = convolve(green_channel, smoothing_filter)
smoothed_blue = convolve(blue_channel, smoothing_filter)

# Combine the smoothed channels back into one image
smoothed_image = np.stack((smoothed_red, smoothed_green, smoothed_blue), axis=-1)

# Ensure pixel values are in the correct range (0-255)
smoothed_image = np.clip(smoothed_image, 0, 255).astype(np.uint8)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image_array)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(smoothed_image)
axes[1].set_title("Smoothed Image with 3x3 Filter")
axes[1].axis('off')

plt.show()
