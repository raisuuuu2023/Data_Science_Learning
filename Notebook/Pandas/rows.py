import pandas as pd
df=pd.read_json("Notebook/Pandas/palestinian_movies.json")
print('Display 2 rows of first')
print(df.head(2))
print('2 rows of last')
print(df.tail(2))