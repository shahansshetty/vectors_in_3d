import matplotlib.pyplot as plt
import math
# import numpy as np
# from mpl_toolkits import mplot3d

print('3d vector addition')
print('values of a ')
a=[int(input(f'enter the {chr(120+i)} coordinate of a :'))for i in range(3)]
print('values of b ')
b=[int(input(f'enter the {chr(120+i)} coordinate of b :'))for i in range(3)]

# def draw_3d(a,b,sum,largest):
#     axes=plt.axes(projection='3d')
#     axes.quiver(0,0,0,a[0],a[1],a[2],color='orange',arrow_length_ratio=0.1)
#     axes.quiver(0,0,0,b[0],b[1],b[2],color='red',arrow_length_ratio=0.1)
#     axes.quiver(0,0,0,sum[0],sum[1],sum[2],color='green',arrow_length_ratio=0.1)
#     axes.set_xlim([-largest,largest]) 
#     axes.set_ylim([-largest,largest])
#     plt.show() 

sum=list()
for i in range(len(a)):
    sum+=[a[i]+b[i]]
    largest=max(sum)

axes=plt.axes(projection='3d')

#black line through the middle of all axis for better visulation
axes.plot([-largest, largest], [0, 0], [0, 0], color='black')  #x
axes.plot([0, 0], [-largest, largest], [0, 0], color='black')  #y
axes.plot([0, 0], [0, 0], [-largest, largest], color='black')  #z


axes.quiver(0,0,0,a[0],a[1],a[2],color='orange',arrow_length_ratio=0.1,label='a')
axes.quiver(0,0,0,b[0],b[1],b[2],color='red',arrow_length_ratio=0.1,label='b')
axes.quiver(0,0,0,sum[0],sum[1],sum[2],color='green',arrow_length_ratio=0.1,label='sum')
axes.set_xlim([-largest,largest]) 
axes.set_ylim([-largest,largest])
axes.set_zlim([-largest,largest])
axes.legend()
plt.title(f'3D_VECTOR_ADDITION , sum:{sum}')



plt.show() 




