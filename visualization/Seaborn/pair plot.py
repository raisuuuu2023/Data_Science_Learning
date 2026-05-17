import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("darkgrid")

df = pd.DataFrame({
    "math": [80,70,90,60],
    "physics": [85,65,95,70],
    "chemistry": [78,60,88,65]
})

sns.pairplot(df)

plt.show()