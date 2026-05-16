import seaborn as sns
import matplotlib.pyplot as plt

data = [10,12,13,15,18,100]

sns.boxplot(x=data)

plt.title("box plot")

plt.show()