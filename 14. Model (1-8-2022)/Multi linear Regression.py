import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x=np.array([[5,2],[7,4],[4,9],[15,12],[19,17])
y=np.array([7,3,5,19,6])
model=LinearRegression.fit(x,y)
rsq=model.score(x,y)
print(rsq)
print(model.intercept_)
print(model.coef_)
ypred=model.predict(x)
print(ypred)
xnew=np.arrange(0,101.reshape(-1,2))
ynew=model.predict(xnew)
print(ynew)
