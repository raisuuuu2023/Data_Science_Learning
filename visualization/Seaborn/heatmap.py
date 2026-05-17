import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([
    [5,4,0],
    [3,0,2],
    [4,5,1]
])

sns.heatmap(matrix, annot=True)

plt.title("Ratings Heatmap")

plt.show()