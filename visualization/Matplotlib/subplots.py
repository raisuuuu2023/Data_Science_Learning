import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(10,4))

ax[0].plot([1,2,3], [1,4,9], color='blue')
ax[0].set_title("Plot 1")

ax[1].bar(["A","B","C"], [3,5,2], color='green')
ax[1].set_title("Plot 2")

fig.suptitle("Comparison of line and bar charts")
plt.tight_layout()
plt.savefig('subplots.png',dpi=300, bbox_inches='tight')

plt.show()