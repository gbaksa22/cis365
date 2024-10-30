"""Step 7: Calculate the Histogram of the Image Manually with Bins"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "the-rock.png"
image = Image.open(image_path).convert("RGB")
image_array = np.array(image)

bin_size = 5
num_bins = 256 // bin_size
red_histogram = [0] * num_bins
green_histogram = [0] * num_bins
blue_histogram = [0] * num_bins

for row in image_array:
    for pixel in row:
        red_value, green_value, blue_value = pixel[0], pixel[1], pixel[2]
        
        red_bin = red_value // bin_size
        green_bin = green_value // bin_size
        blue_bin = blue_value // bin_size
        
        if red_bin < num_bins:
            red_histogram[red_bin] += 1
        if green_bin < num_bins:
            green_histogram[green_bin] += 1
        if blue_bin < num_bins:
            blue_histogram[blue_bin] += 1

def plot_histogram(histogram, color, title):
    plt.figure(figsize=(12, 6))
    plt.bar(range(num_bins), histogram, color=color, width=0.6)
    plt.title(title)
    plt.xticks(
        ticks=range(num_bins),
        labels=[f"{i * bin_size}-{(i + 1) * bin_size - 1}" for i in range(num_bins)],
        rotation=45,
        ha='right'
    )
    plt.xlim(0, num_bins - 1)
    plt.xlabel("Intensity Ranges")
    plt.ylabel("Pixel Count")
    plt.tight_layout()
    plt.show()

plot_histogram(red_histogram, 'red', "Red Channel Histogram with Bins Every 5 (0-4, 5-9, ...)")
plot_histogram(green_histogram, 'green', "Green Channel Histogram with Bins Every 5 (0-4, 5-9, ...)")
plot_histogram(blue_histogram, 'blue', "Blue Channel Histogram with Bins Every 5 (0-4, 5-9, ...)")
