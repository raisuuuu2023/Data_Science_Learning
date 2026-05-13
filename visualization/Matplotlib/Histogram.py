import matplotlib.pyplot as plt

ratings = [1,2,7,3,10,9,4,5,8,13,5]

plt.hist(ratings,bins=5, color='purple', edgecolor='black')

plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.show()