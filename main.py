import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

axes=plt.axes(projection='3d')

a=[3,4,2]
z=[4,5,1]
sum=list()
for i in range(len(a)):
    sum+=[a[i]+z[i]]

print(sum)

# y=np.arange(0,50,0.1)

axes.quiver(0,0,0,a[0],a[1],a[2],color='orange',arrow_length_ratio=0.1)

axes.set_xlim([-7,7]) 
axes.set_ylim([-7,7])
axes.set_zlim([-7,7]) 
plt.show() 