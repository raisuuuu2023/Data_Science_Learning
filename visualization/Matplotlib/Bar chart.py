import matplotlib.pyplot as plt

movies = ["Avatar", "Titanic", "Inception"]
ratings = [9, 7, 8]

plt.bar(movies, ratings, color='blue', label='movie ratings')

plt.title("Movie Ratings")
plt.xlabel("Movies")
plt.ylabel("Ratings")

plt.show()