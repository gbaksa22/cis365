"""
CIS 365 - Assignment 9

Date - 10/23/2024

This program was created by Gabe Baksa and Brenden Granzo
"""
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, threshold=0):
        # ChatGPT helped with random weights
        self.weights = np.random.randn(input_size + 1)  # +1 for the bias
        self.learning_rate = learning_rate
        self.threshold = threshold

    def activation(self, weighted_sum):
        return 1 if weighted_sum >= self.threshold else 0

    def train(self, inputs, targets, max_iterations=1000):
        inputs = np.c_[inputs, np.ones(inputs.shape[0])]  # ChatGPT recommended adding a bias term
        total_iterations = 0
        
        for iteration_count in range(max_iterations):
            total_iterations += 1
            errors = 0  # To track if the model has converged
            for i in range(len(targets)):
                weighted_sum = np.dot(self.weights, inputs[i]) # Asked ChatGPT how to find the weighted sum
                prediction = self.activation(weighted_sum)
                error = targets[i] - prediction
                if error != 0:
                    self.weights += self.learning_rate * error * inputs[i]
                    errors += 1
                    print(f"Updated weights: {self.weights}")
            if errors == 0:
                print(f"Model converged in {total_iterations} iterations.")
                break
        return total_iterations

# AND gate
inputs_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets_and = {
    (0, 0): 0,
    (0, 1): 0,
    (1, 0): 0,
    (1, 1): 1
}

# OR gate
inputs_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets_or = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 1
}

# Convert dictionary values to array for compatibility with the Perceptron
targets_and_values = np.array([targets_and[tuple(i)] for i in inputs_and])
targets_or_values = np.array([targets_or[tuple(i)] for i in inputs_or])

print("Training Perceptron for AND gate:")
perceptron_and = Perceptron(input_size=2, learning_rate=0.1)
iterations_and = perceptron_and.train(inputs_and, targets_and_values)
print(f"Final weights for AND gate: {perceptron_and.weights}\n")

print("Training Perceptron for OR gate:")
perceptron_or = Perceptron(input_size=2, learning_rate=0.1)
iterations_or = perceptron_or.train(inputs_or, targets_or_values)
print(f"Final weights for OR gate: {perceptron_or.weights}\n")
