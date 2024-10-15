import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score

# Data for problem 1
data_problem1 = { 
    "Feature 1": [0.25, 0.76, 0.34, 0.92, 0.58, 0.11, 0.48, 0.60, 0.20, 0.95, 0.31, 0.87, 0.39, 0.82, 0.67, 0.14, 0.59, 0.04, 0.73, 0.90],
    "Feature 2": [0.89, 0.45, 0.67, 0.10, 0.22, 0.85, 0.29, 0.71, 0.79, 0.15, 0.56, 0.41, 0.93, 0.25, 0.33, 0.77, 0.47, 0.90, 0.66, 0.05],
    "Class Label": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    "Predicted Label": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
}

right_answer1 = data_problem1["Class Label"]  # Actual labels
machine_answer1 = data_problem1["Predicted Label"]  # Predicted labels

# Data for problem 2
data_problem2 = {
    "Feature 1": [0.25, 0.76, 0.34, 0.92, 0.58, 0.11, 0.48, 0.60, 0.20, 0.95, 0.31, 0.87, 0.39, 0.82, 0.67, 0.14, 0.59, 0.04, 0.73, 0.90],
    "Feature 2": [0.89, 0.45, 0.67, 0.10, 0.22, 0.85, 0.29, 0.71, 0.79, 0.15, 0.56, 0.41, 0.93, 0.25, 0.33, 0.77, 0.47, 0.90, 0.66, 0.05],
    "Class Label": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    "Predicted Correctly": [True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True]
}

right_answer2 = data_problem2["Class Label"]  # Actual labels
machine_answer2 = [data_problem2["Class Label"][i] if val else (1 - data_problem2["Class Label"][i]) for i, val in enumerate(data_problem2["Predicted Correctly"])]
  # Convert True/False to 1/0

# Confusion matrices
matrix1 = confusion_matrix(right_answer1, machine_answer1)
matrix2 = confusion_matrix(right_answer2, machine_answer2)

# Accuracy scores
accuracy1 = accuracy_score(right_answer1, machine_answer1)
accuracy2 = accuracy_score(right_answer2, machine_answer2)

# Plotting Confusion Matrix 1
plt.figure(figsize=(4, 4))
sns.heatmap(matrix1, annot=True, fmt="d", cmap="Reds", xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel("Predicted Labels")
plt.ylabel("Actual Labels")
plt.title(f"Confusion Matrix 1\nAccuracy: {accuracy1:.2f}")
plt.show()

# Plotting Confusion Matrix 2
plt.figure(figsize=(4, 4))
sns.heatmap(matrix2, annot=True, fmt="d", cmap="Reds", xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel("Predicted Labels")
plt.ylabel("Actual Labels")
plt.title(f"Confusion Matrix 2\nAccuracy: {accuracy2:.2f}")
plt.show()
