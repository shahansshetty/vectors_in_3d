import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

axes=plt.axes(projection='3d')

a=[1,3,8]
z=[2,4,8]
sum=list()
for i in range(len(a)):
    sum+=[a[i]+z[i]]

print(sum)

# y=np.arange(0,50,0.1)

axes.quiver(0,0,0,sum[0],sum[1],sum[2])
axes.set_xlim[-3,3] 
axes.set_ylim[-3,3]
axes.set_zlim[-3,3] 
plt.show() 