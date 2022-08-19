import numpy as np
import matplotlib.pyplot as plt
p=np.array([50,25,25])
co=['pink','aqua','yellow']
l=['Hari','Jay','Reethu']
ex=[0,0,0.2]
plt.pie(p,colors=co,labels=l,shadow=True,explode=ex)
plt.legend(title='Details',bbox_to_anchor=(1, 1))
plt.show()
