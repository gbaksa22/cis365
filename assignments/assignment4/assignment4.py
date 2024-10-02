"""
CIS 365 - Assignment 4

Date - 10/2/2024

This program was created by Gabe Baksa and Brenden Granzo

Used Animal Image Classifier from Summer 2023 as reference
"""
import math
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

irisDataPath = './iris/iris.data'

columnNames = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species']

# asked ChatGPT how to read the data
iris = pd.read_csv(irisDataPath, header=None, names=columnNames)

featureColumn = 'petalLength'
xValues = iris[featureColumn].values

# asked ChatGPT how to split the data
# random_state can be any integer but needs to be set so it is the same split every time
xTrain, xTest = train_test_split(xValues, test_size=0.4, random_state=22)

meanTrain = np.mean(xTrain)
stdDevTrain = np.std(xTrain)

print(f"Mean ({featureColumn}) on training data: {meanTrain}")
print(f"Standard Deviation ({featureColumn}) on training data: {stdDevTrain}")

def gaussianProbability(x, mean, stdDev):
    exponent = -((x - mean) ** 2) / (2 * (stdDev ** 2))
    probability = (1 / (stdDev * math.sqrt(2 * math.pi))) * math.exp(exponent)
    return probability
