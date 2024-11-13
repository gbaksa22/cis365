import numpy as np
from scipy.spatial.distance import pdist

data = np.random.rand(10, 2)

distances = pdist(data)

avg_distance = np.mean(distances)

print(avg_distance)