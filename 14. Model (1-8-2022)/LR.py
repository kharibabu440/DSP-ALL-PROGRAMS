import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x=np.array([10,2,3,8,19]).reshape(-1,1)
y=np.array([2,4,9,10,12])
model=LinearRegression()
model.fit(x,y)
ypred=model.predict(x)
print(ypred)
print(model.score[x,ypred])
plt.scatter(x,y)
plt.plot(x,ypred)
plt.show()
