# -*- coding: utf-8 -*-
"""gan_tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x-4UoqBjamVVNNPlEBXOD4RKoCTE6b_W

Imports
"""

from numpy.random import rand
from numpy import hstack
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model
import numpy as np
from numpy.random import rand, randn
from matplotlib import pyplot

"""1. Select a One-Dimensional Function


"""

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

"""2. Define a Discriminator Model"""

def define_discriminator(n_inputs=2):
    model = Sequential()
    # Add a hidden layer with 25 nodes, ReLU activation, and He weight initialization
    model.add(Dense(25, activation='relu', kernel_initializer='he_uniform', input_dim=n_inputs))
    # Add output layer with sigmoid activation for binary classification
    model.add(Dense(1, activation='sigmoid'))
    # Compile the model with binary cross-entropy loss and Adam optimizer
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Define the discriminator model
model = define_discriminator()

# Summarize the model
model.summary()

# Optional: Plot the model if pydot and graphviz are installed
plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)

# Generate n real samples with class labels
def generate_real_samples(n):
    # Generate inputs in [-0.5, 0.5]
    X1 = rand(n) - 0.5
    # Generate outputs X^2
    X2 = X1 * X1
    # Stack arrays
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    # Generate class labels
    y = np.ones((n, 1))
    return X, y

# Generate n fake samples with class labels
def generate_fake_samples(n):
    # Generate inputs in [-1, 1]
    X1 = -1 + rand(n) * 2
    # Generate outputs in [-1, 1]
    X2 = -1 + rand(n) * 2
    # Stack arrays
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    # Generate class labels
    y = np.zeros((n, 1))
    return X, y

# Train the discriminator model
def train_discriminator(model, n_epochs=1000, n_batch=128):
    half_batch = int(n_batch / 2)
    # Run epochs manually
    for i in range(n_epochs):
        # Generate real examples
        X_real, y_real = generate_real_samples(half_batch)
        # Update model on real examples
        model.train_on_batch(X_real, y_real)
        # Generate fake examples
        X_fake, y_fake = generate_fake_samples(half_batch)
        # Update model on fake examples
        model.train_on_batch(X_fake, y_fake)
        # Evaluate the model
        _, acc_real = model.evaluate(X_real, y_real, verbose=0)
        _, acc_fake = model.evaluate(X_fake, y_fake, verbose=0)
        print(f"Epoch {i+1}/{n_epochs}: acc_real={acc_real:.3f}, acc_fake={acc_fake:.3f}")

# Define the discriminator model
model = define_discriminator()

# Train the discriminator
train_discriminator(model)

"""3. Define a Generator Model"""

# Define the standalone generator model
def define_generator(latent_dim, n_outputs=2):
    model = Sequential()
    # Hidden layer with 15 nodes, ReLU activation, and He weight initialization
    model.add(Dense(15, activation='relu', kernel_initializer='he_uniform', input_dim=latent_dim))
    # Output layer with 2 nodes and linear activation
    model.add(Dense(n_outputs, activation='linear'))
    return model

# Generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n):
    # Generate points from a standard Gaussian distribution
    x_input = randn(latent_dim * n)
    # Reshape into a batch of inputs for the generator
    x_input = x_input.reshape(n, latent_dim)
    return x_input

# Use the generator to generate n fake examples and plot the results
def generate_fake_samples(generator, latent_dim, n):
    # Generate points in the latent space
    x_input = generate_latent_points(latent_dim, n)
    # Predict outputs using the generator
    X = generator.predict(x_input)
    # Plot the results
    pyplot.scatter(X[:, 0], X[:, 1])
    pyplot.show()

# Size of the latent space
latent_dim = 5

# Define the generator model
generator = define_generator(latent_dim)

# Summarize the generator model
generator.summary()

# Generate and plot fake samples
generate_fake_samples(generator, latent_dim, 100)

"""4. Training the Generator Model"""

# Define the combined generator and discriminator model, for updating the generator
def define_gan(generator, discriminator):
    # Make the discriminator not trainable when part of the GAN
    discriminator.trainable = False
    # Create a composite model
    model = Sequential()
    # Add generator
    model.add(generator)
    # Add discriminator
    model.add(discriminator)
    # Compile the model with binary cross-entropy loss and Adam optimizer
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model

# Train the composite GAN model
def train_gan(gan_model, latent_dim, n_epochs=10000, n_batch=128):
    for i in range(n_epochs):
        # Generate random points in latent space
        x_gan = generate_latent_points(latent_dim, n_batch)
        # Create inverted labels (all ones) to "trick" the discriminator
        y_gan = np.ones((n_batch, 1))
        # Train the generator via the composite GAN model
        gan_model.train_on_batch(x_gan, y_gan)

# Size of the latent space
latent_dim = 5

# Create the discriminator
discriminator = define_discriminator()

# Create the generator
generator = define_generator(latent_dim)

# Create the composite GAN model
gan_model = define_gan(generator, discriminator)

# Summarize the GAN model
gan_model.summary()

# Train the GAN
train_gan(gan_model, latent_dim, n_epochs=1000, n_batch=128)

"""5. Evaluating the Performance of the GAN"""

# Generate real samples with class labels
def generate_real_samples(n):
    # Generate inputs in the range [-0.5, 0.5]
    X1 = rand(n) - 0.5
    # Generate outputs using the quadratic function
    X2 = X1 * X1
    # Stack arrays
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    # Generate class labels (real samples labeled as 1)
    y = np.ones((n, 1))
    return X, y

# Generate fake samples using the generator
def generate_fake_samples(generator, latent_dim, n):
    # Generate points in latent space
    x_input = generate_latent_points(latent_dim, n)
    # Predict outputs using the generator
    X = generator.predict(x_input)
    # Assign class labels (fake samples labeled as 0)
    y = np.zeros((n, 1))
    return X, y

# Evaluate the discriminator and plot real vs. fake points
def summarize_performance(epoch, generator, discriminator, latent_dim, n=100):
    # Prepare real samples
    x_real, y_real = generate_real_samples(n)
    # Evaluate discriminator on real samples
    _, acc_real = discriminator.evaluate(x_real, y_real, verbose=0)
    # Prepare fake samples
    x_fake, y_fake = generate_fake_samples(generator, latent_dim, n)
    # Evaluate discriminator on fake samples
    _, acc_fake = discriminator.evaluate(x_fake, y_fake, verbose=0)
    # Print accuracy
    print(f"Epoch {epoch}: Real Accuracy={acc_real:.2f}, Fake Accuracy={acc_fake:.2f}")
    # Scatter plot for real (red) and fake (blue) samples
    pyplot.scatter(x_real[:, 0], x_real[:, 1], color='red', label='Real')
    pyplot.scatter(x_fake[:, 0], x_fake[:, 1], color='blue', label='Fake')
    pyplot.legend()
    pyplot.show()

# Train the generator and discriminator
def train(g_model, d_model, gan_model, latent_dim, n_epochs=10000, n_batch=128, n_eval=2000):
    # Determine half the size of one batch for updating the discriminator
    half_batch = int(n_batch / 2)
    # Manually iterate through epochs
    for i in range(n_epochs):
        # Prepare real samples
        x_real, y_real = generate_real_samples(half_batch)
        # Prepare fake samples
        x_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
        # Update discriminator on real and fake samples
        d_model.train_on_batch(x_real, y_real)
        d_model.train_on_batch(x_fake, y_fake)
        # Prepare points in latent space for the generator
        x_gan = generate_latent_points(latent_dim, n_batch)
        # Create inverted labels (all ones) for the fake samples
        y_gan = np.ones((n_batch, 1))
        # Update the generator via the discriminator's error
        gan_model.train_on_batch(x_gan, y_gan)
        # Evaluate the model at specified intervals
        if (i + 1) % n_eval == 0:
            summarize_performance(i + 1, g_model, d_model, latent_dim)

"""6. Complete Example of Training the GAN"""

from numpy import hstack, zeros, ones
from numpy.random import rand, randn
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot
from tqdm import tqdm  # Progress bar library

# Define the standalone discriminator model
def define_discriminator(n_inputs=2):
    model = Sequential()
    model.add(Dense(25, activation='relu', kernel_initializer='he_uniform', input_dim=n_inputs))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Define the standalone generator model
def define_generator(latent_dim, n_outputs=2):
    model = Sequential()
    model.add(Dense(15, activation='relu', kernel_initializer='he_uniform', input_dim=latent_dim))
    model.add(Dense(n_outputs, activation='linear'))
    return model

# Define the combined generator and discriminator model, for updating the generator
def define_gan(generator, discriminator):
    discriminator.trainable = False
    model = Sequential()
    model.add(generator)
    model.add(discriminator)
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model

# Generate n real samples with class labels
def generate_real_samples(n):
    X1 = rand(n) - 0.5
    X2 = X1 * X1
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    y = ones((n, 1))
    return X, y

# Generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n):
    x_input = randn(latent_dim * n)
    x_input = x_input.reshape(n, latent_dim)
    return x_input

# Use the generator to generate n fake examples, with class labels
def generate_fake_samples(generator, latent_dim, n):
    x_input = generate_latent_points(latent_dim, n)
    X = generator.predict(x_input)
    y = zeros((n, 1))
    return X, y

# Evaluate the discriminator and plot real and fake points
def summarize_performance(epoch, generator, discriminator, latent_dim, n=100):
    x_real, y_real = generate_real_samples(n)
    _, acc_real = discriminator.evaluate(x_real, y_real, verbose=0)
    x_fake, y_fake = generate_fake_samples(generator, latent_dim, n)
    _, acc_fake = discriminator.evaluate(x_fake, y_fake, verbose=0)
    print(f"Epoch {epoch}: Real Accuracy={acc_real:.2f}, Fake Accuracy={acc_fake:.2f}")
    pyplot.scatter(x_real[:, 0], x_real[:, 1], color='red', label='Real')
    pyplot.scatter(x_fake[:, 0], x_fake[:, 1], color='blue', label='Fake')
    pyplot.legend()
    pyplot.show()

# Train the generator and discriminator
def train(g_model, d_model, gan_model, latent_dim, n_epochs=10000, n_batch=128, n_eval=2000):
    half_batch = int(n_batch / 2)
    for i in tqdm(range(n_epochs), desc="Training Progress"):
        # Prepare real samples
        x_real, y_real = generate_real_samples(half_batch)
        # Prepare fake samples
        x_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
        # Update discriminator on real samples
        d_loss_real = d_model.train_on_batch(x_real, y_real)
        # Update discriminator on fake samples
        d_loss_fake = d_model.train_on_batch(x_fake, y_fake)
        # Prepare points in latent space for the generator
        x_gan = generate_latent_points(latent_dim, n_batch)
        # Create inverted labels (all ones) for the fake samples
        y_gan = ones((n_batch, 1))
        # Update the generator via the discriminator's error
        g_loss = gan_model.train_on_batch(x_gan, y_gan)

        # Handle loss formatting based on the return type
        d_loss_real_value = d_loss_real if isinstance(d_loss_real, float) else d_loss_real[0]
        d_loss_fake_value = d_loss_fake if isinstance(d_loss_fake, float) else d_loss_fake[0]
        g_loss_value = g_loss if isinstance(g_loss, float) else g_loss[0]

        # Log progress every 100 epochs
        if (i + 1) % 100 == 0:
            print(f"Epoch {i+1}/{n_epochs}, D Loss Real: {d_loss_real_value:.3f}, "
                  f"D Loss Fake: {d_loss_fake_value:.3f}, G Loss: {g_loss_value:.3f}")

        # Evaluate the model every n_eval epochs
        if (i + 1) % n_eval == 0:
            summarize_performance(i + 1, g_model, d_model, latent_dim)


# Size of the latent space
latent_dim = 5

# Create the discriminator
discriminator = define_discriminator()

# Create the generator
generator = define_generator(latent_dim)

# Create the composite GAN model
gan_model = define_gan(generator, discriminator)

# Train the GAN
train(generator, discriminator, gan_model, latent_dim, n_epochs=10000, n_batch=128, n_eval=2000)