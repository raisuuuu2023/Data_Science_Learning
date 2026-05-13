import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]

plt.plot(x,y, color='red', linestyle='--', linewidth=3, marker='*', label='students marks')

plt.title("Simple Line Plot")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.legend(loc='upper left', fontsize=12)
plt.grid(color='grey', linestyle=':', linewidth=1)
plt.xlim(0,4)
plt.ylim(0,50)
plt.xticks([1,2,3,4],['Raisa','Rahim','Karim','Jamil'])

plt.show()