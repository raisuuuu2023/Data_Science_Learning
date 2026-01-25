import pandas as pd
data={
    "Name":['John','Number1','Number2'],
    "Age":[40,30,20],
    "City":['Nangpur','Mumbai','Delhi']
}
df=pd.DataFrame(data)
print(df)

#df.to_csv("output.csv",index=False)
#df.to_json("output.json",index=False)
df.to_excel("output.xlsx",index=False)