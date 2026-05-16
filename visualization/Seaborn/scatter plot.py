import seaborn as sns
import matplotlib.pyplot as plt

study_hours = [1,2,3,4,5]
marks = [20,35,50,65,80]

sns.scatterplot(x=study_hours,y=marks)

plt.title("Study Hours vs Marks")

plt.show()