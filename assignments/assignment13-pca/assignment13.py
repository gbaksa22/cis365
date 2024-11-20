# import image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
image = Image.open('JetSkiAir.jpg').convert('L')  # Convert to grayscale
myImage = np.asarray(image)  # Convert to NumPy array
plt.imshow(myImage, cmap='gray')
plt.title("Original Image")
plt.show()


# 1. Find the mean of the image

# 2. Subtract the mean of the image

# 3. Calculate the covariance matrix

# 4. Find the Eigenvectors and Eigenvalues of the covariance matrix.

# 5. Sort the Eigenvectors by their associated Eigenvalues (if not done already) 

# 6. Set the numberOfEigenVectorsToKeep = 15

# 7. Output the percentage of variance that those eigenvectors account for

# 8. Create a variable ‘eigenVectorsToKeep’ that only contains that number of eigenVectors

# 9. Create a variable ‘compressedImage’ it should be calculated by using:
# compressedImage = np.matmul(myImageMinusMean, eigenVectorsToKeep)

# 10. Create a lossy uncompressed image from the above variable: 
# lossyUncompressedImage = np.matmul(compressedImage, np.transpose(eigenVectorsToKeep)) + myImageMean

# 11. Output the compressed image

# Repeat the above steps with the variable numberOfEigenVectorsToKeep = {15, 100, 200}
