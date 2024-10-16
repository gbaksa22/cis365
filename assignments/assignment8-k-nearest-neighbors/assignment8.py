"""
CIS 365 - Assignment 8

Date - 10/16/2024

This program was created by Gabe Baksa and Brenden Granzo

Used Bayesian Classifier Assignment as reference
"""
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

irisDataPath = './iris/iris.data'
columnNames = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species']
iris = pd.read_csv(irisDataPath, header=None, names=columnNames)

features = iris[['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth']].values
labels = iris['species'].values

# Split the data: 60% training, 40% testing
xTrain, xTest, yTrain, yTest = train_test_split(features, labels, test_size=0.4, random_state=22)

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def knn_classifier(x_train, y_train, x_test_point, k):
    distances = []
    
    # Calculate the distance between x_test_point and all training points
    for i in range(len(x_train)):
        dist = euclidean_distance(x_train[i], x_test_point)
        distances.append((dist, y_train[i]))

    # Sort the distances, and select the k nearest points
    # Had to ask ChatGPT how to get the first element from each tuple
    distances.sort(key=lambda x: x[0])
    neighbors = [distances[i][1] for i in range(k)]

    # Return the most common class among the neighbors
    most_common = Counter(neighbors).most_common(1)
    return most_common[0][0]

def test_knn(x_train, y_train, x_test, y_test, k):
    y_pred = []
    
    for x_test_point in x_test:
        y_pred.append(knn_classifier(x_train, y_train, x_test_point, k))
    
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    
    return cm, accuracy

def plot_confusion_matrix(cm, accuracy, k, features_used):
    plt.figure(figsize=(4, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Reds")
    plt.xlabel("Predicted Labels")
    plt.ylabel("Actual Labels")
    plt.title(f"K={k}, Features: {features_used}\nAccuracy: {accuracy:.2f}")
    plt.show()

feature_sets = {
    'a': [0],  # single feature: sepalLength
    'b': [0, 1],  # two features: sepalLength, sepalWidth
    'c': [0, 1, 2],  # three features: sepalLength, sepalWidth, petalLength
    'd': [0, 1, 2, 3]  # all features
}

k_values = [3, 5, 7]

# ChatGPT helped loop through all of the options
for feature_set_key, feature_indices in feature_sets.items():
    xTrain_subset = xTrain[:, feature_indices]
    xTest_subset = xTest[:, feature_indices]
    features_used = ', '.join([columnNames[i] for i in feature_indices])

    for k in k_values:
        cm, accuracy = test_knn(xTrain_subset, yTrain, xTest_subset, yTest, k)
        plot_confusion_matrix(cm, accuracy, k, features_used)
