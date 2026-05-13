import matplotlib.pyplot as plt

study_hours = [1,2,3,4,5]
marks = [20,35,50,65,80]

plt.scatter(study_hours, marks, color='green', marker='o', label='Student Data')

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.show()