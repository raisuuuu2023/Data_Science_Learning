import seaborn as sns
import matplotlib.pyplot as plt

ratings = [1,2,2,3,4,4,4,5,5,5]

sns.histplot(ratings)

plt.title("Ratings Distribution")

plt.show()