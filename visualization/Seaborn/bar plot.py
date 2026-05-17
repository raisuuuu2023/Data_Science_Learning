import seaborn as sns
import matplotlib.pyplot as plt

movies = ["A","B","C"]
ratings = [9,7,8]

sns.barplot(x=movies, y=ratings)

plt.title("Movie Ratings")

plt.show()