import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures as pf
x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([1,4,9,16,25])
y1=np.array([2,9,11]).reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
poly=pf(degree=2)
xploy=poly.fit_transform(x)
poly.fit(xploy,y)
l=LinearRegression()
l.fit(xploy,y)
l.predict(ploy.fit_transform(y))
