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
largest=max(sum)

# y=np.arange(0,50,0.1)

axes.quiver(0,0,0,a[0],a[1],a[2],color='orange',arrow_length_ratio=0.1)
axes.quiver(0,0,0,z[0],z[1],z[2],color='red',arrow_length_ratio=0.1)
axes.quiver(0,0,0,sum[0],sum[1],sum[2],color='green',arrow_length_ratio=0.1)

axes.set_xlim([-largest,largest]) 
axes.set_ylim([-largest,largest])
axes.set_zlim([-largest,largest]) 
plt.show() 