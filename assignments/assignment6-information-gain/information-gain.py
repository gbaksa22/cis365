import pandas as pd
import math

#ChatGPT wrote the dataset from the image for me
data = { 
    'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak'],
    'Play Outside?': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

def entropy(dataset):
    label_counts = {}
    total_instances = len(dataset)
    
    for label in dataset:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    
    entropy_value = 0.0
    for count in label_counts.values():
        probability = count / total_instances
        entropy_value -= probability * math.log2(probability)
        
    return entropy_value


def information_gain(df, target_col, attribute):
    original_entropy = entropy(df[target_col])
    
    values = df[attribute].unique()
    
    weighted_entropy = 0
    for value in values:
        subset = df[df[attribute] == value][target_col]
        weighted_entropy += (len(subset) / len(df)) * entropy(subset)
    
    return original_entropy - weighted_entropy

attributes = ['Weather', 'Temperature', 'Humidity', 'Wind']

target_col = 'Play Outside?'
info_gains = {attribute: information_gain(df, target_col, attribute) for attribute in attributes}


print("Information Gain for each attribute:")
for attribute, gain in info_gains.items():
    print(f"{attribute}: {gain:.4f}")

# Split the data by the first level of Weather
sunny_subset = df[df['Weather'] == 'Sunny']
rainy_subset = df[df['Weather'] == 'Rainy']

# Calculate Information Gain for the Sunny subset
remaining_attributes_sunny = ['Temperature', 'Humidity', 'Wind']
sunny_info_gains = {attribute: information_gain(sunny_subset, target_col, attribute) for attribute in remaining_attributes_sunny}

print("\nInformation Gain for Sunny subset:")
for attribute, gain in sunny_info_gains.items():
    print(f"{attribute}: {gain:.4f}")

# Calculate Information Gain for the Rainy subset
remaining_attributes_rainy = ['Temperature', 'Humidity', 'Wind']
rainy_info_gains = {attribute: information_gain(rainy_subset, target_col, attribute) for attribute in remaining_attributes_rainy}

print("\nInformation Gain for Rainy subset:")
for attribute, gain in rainy_info_gains.items():
    print(f"{attribute}: {gain:.4f}")