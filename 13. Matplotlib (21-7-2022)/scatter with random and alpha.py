import matplotlib.pyplot as plt
import numpy as np
a=np.random.rand(70)
b=np.random.rand(70)
co=np.random.rand(70)
size=1500*np.random.rand(70)
plt.scatter(a,b,c=co,s=size,alpha=0.5)
plt.colorbar()
plt.show()
