#index position:
import numpy as np

x=np.array([10,20,30,40])
print(x[0]+x[3])
print(x[2])

y=np.array([[1,2,3,4],[5,6,7,8]])
print(y[0])
print(y[0,1])
print(y[0,0])
print(y[1,1])

z=np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print(z)
print(z[0,0,0])
print(z[1,1,1])
print(z[2,0,1])