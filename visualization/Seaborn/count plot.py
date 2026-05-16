import seaborn as sns
import matplotlib.pyplot as plt

ratings = [1,2,2,3,4,4,4,5,5,5]

sns.countplot(x=ratings)

plt.title("Ratings counts")

plt.show()