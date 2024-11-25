# 1. Select a One-Dimensional Function
# Import required libraries
from numpy.random import rand
from numpy import hstack
from matplotlib import pyplot as plt

# Function to generate random samples from x^2
def generate_samples(n=100):
    # Generate random inputs in the range [-0.5, 0.5]
    X1 = rand(n) - 0.5
    # Generate outputs as X^2 (quadratic function)
    X2 = X1 * X1
    # Reshape arrays for stacking
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    # Stack input and output arrays horizontally
    return hstack((X1, X2))

# Generate samples
data = generate_samples()

# Plot the samples using a scatter plot
plt.scatter(data[:, 0], data[:, 1], color='blue', alpha=0.7, label="Samples")
plt.title("Random Samples from y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)  # Optional: Adds a grid for better visualization
plt.show()

# 2. Define a Discriminator Model 
# 3. Define a Generator Model 
# 4. Training the Generator Model 
# 5. Evaluating the Performance of the GAN 
# 6. Complete Example of Training the GAN