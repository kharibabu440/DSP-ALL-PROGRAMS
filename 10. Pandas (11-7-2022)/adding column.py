import pandas as pd
info={'id':pd.Series([115,132],index=['a','b']),
      'dep':pd.Series(['cse','ece'],index=['a','b'])
      }
df=pd.DataFrame(info)
df['mark']=pd.Series([88,98],index=['a','b'])
print(df)
