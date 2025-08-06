import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits import mplot3d


# a=[3,4,2]
# z=[4,5,1]

# y=np.arange(0,50,0.1)
axes=plt.axes(projection='3d')

def v_sum(a,b):
    sum=list()
    for i in range(len(a)):
        sum+=[a[i]+b[i]]
    largest=max(sum)
    return sum,largest

print('3d vector addition')
print('values of a ')
a=[int(input(f'enter the {chr(120+i)} coordinate of a :'))for i in range(3)]
b=[int(input(f'enter the {chr(120+i)} coordinate of b :'))for i in range(3)]

# if len(a) or len(z)!=3:
#     print('size of the a and b is not 3')
#     exit(0)

sum,largest=v_sum(a,b)
print(sum,largest)
# print('Here are the vector operatins avalible')
# print('1.add')
# print('2.multipy')
# print('3.divide')




# axes.quiver(0,0,0,a[0],a[1],a[2],color='orange',arrow_length_ratio=0.1)
# axes.quiver(0,0,0,z[0],z[1],z[2],color='red',arrow_length_ratio=0.1)
# axes.quiver(0,0,0,sum[0],sum[1],sum[2],color='green',arrow_length_ratio=0.1)

# axes.set_xlim([-largest,largest]) 
# axes.set_ylim([-largest,largest])
# axes.set_zlim([-largest,largest]) 
# plt.show() 
