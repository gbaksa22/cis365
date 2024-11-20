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
myImageMean = np.mean(myImage, axis=0)

# 2. Subtract the mean of the image
myImageMinusMean = myImage - myImageMean

# 3. Calculate the covariance matrix
covarianceMatrix = np.cov(myImageMinusMean, rowvar=False)

# 4. Find the Eigenvectors and Eigenvalues of the covariance matrix.
eigenValues, eigenVectors = np.linalg.eigh(covarianceMatrix)

# 5. Sort the Eigenvectors by their associated Eigenvalues (if not done already) 
sortedIndices = np.argsort(eigenValues)[::-1]
eigenValues = eigenValues[sortedIndices]
eigenVectors = eigenVectors[:, sortedIndices]

# 6. Set the numberOfEigenVectorsToKeep = 15
numberOfEigenVectorsToKeep = 200

# 7. Output the percentage of variance that those eigenvectors account for
def variance_explained(eigenValues, numVectors):
    totalVariance = np.sum(eigenValues)
    explainedVariance = np.sum(eigenValues[:numVectors])
    return (explainedVariance / totalVariance) * 100

variance = variance_explained(eigenValues, numberOfEigenVectorsToKeep)
print(f"{numberOfEigenVectorsToKeep} eigenvectors account for {variance:.2f}% of the variance.")

# 8. Create a variable ‘eigenVectorsToKeep’ that only contains that number of eigenVectors
eigenVectorsToKeep = eigenVectors[:, :numberOfEigenVectorsToKeep]

# 9. Create a variable ‘compressedImage’ it should be calculated by using:
compressedImage = np.matmul(myImageMinusMean, eigenVectorsToKeep)

# 10. Create a lossy uncompressed image from the above variable: 
lossyUncompressedImage = np.matmul(compressedImage, np.transpose(eigenVectorsToKeep)) + myImageMean

# 11. Output the compressed image
plt.imshow(lossyUncompressedImage, cmap='gray')
plt.title(f"Reconstructed Image with {numberOfEigenVectorsToKeep} Eigenvectors")
plt.show()
# Repeat the above steps with the variable numberOfEigenVectorsToKeep = {15, 100, 200}
