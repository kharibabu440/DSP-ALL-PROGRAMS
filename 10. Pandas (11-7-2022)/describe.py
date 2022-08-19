import pandas as pd
df=pd.read_csv('data.csv')
b=df.describe()
print(b)
