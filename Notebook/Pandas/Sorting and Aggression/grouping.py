import pandas as pd
data={
    "Name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[28,34,22,28,34],
    "Salary": [1000,2000,3000,4000,5000]
}
df=pd.DataFrame(data)
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)