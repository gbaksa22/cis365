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
yValues = iris['species'].values # target

# asked ChatGPT how to split the data
# random_state can be any integer but needs to be set so it is the same split every time
xTrain, xTest = train_test_split(xValues, test_size=0.4, random_state=22)

xTrain, xTest, yTrain, yTest = train_test_split(xValues, yValues, test_size=0.4, random_state=22)

# holds mean and std dev for each species
specieStats = {}
# holds number of correct and incorrect predictions
count = {}
for species in np.unique(yTrain):
    specieData = xTrain[yTrain == species]
    mean = np.mean(specieData)
    stdDev = np.std(specieData)
    specieStats[species] = (mean, stdDev)
    count[species] = {'correct': 0, 'incorrect': 0}

def gaussianProbability(x, mean, stdDev):
    exponent = -((x - mean) ** 2) / (2 * (stdDev ** 2))
    probability = (1 / (stdDev * math.sqrt(2 * math.pi))) * math.exp(exponent)
    return probability

def predict(speciesStats, x):
    probabilities = {}
    for species, (mean, stdDev) in speciesStats.items():
        probabilities[species] = gaussianProbability(x, mean, stdDev)
    
    # needed some help from ChatGPT to get the keys
    predictedSpecies = max(probabilities, key=probabilities.get) 
    return predictedSpecies

for x, y in zip(xTest, yTest): # asked ChatGPT how to loop both at the same time
    predictedSpecies = predict(specieStats, x)
    if predictedSpecies == y:
        count[predictedSpecies]['correct'] += 1
    else:
        count[predictedSpecies]['incorrect'] += 1


for species in count.keys():
    correct = count[species]['correct']
    incorrect = count[species]['incorrect']
    print(f"{species}: {correct} correct, {incorrect} incorrect ({correct / (correct + incorrect)*100:.2f}%)")