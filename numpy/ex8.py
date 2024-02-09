#array reshape:
import  numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x.shape)
y=x.reshape(2,2,3)
print(y)
print(y.ndim)
print(y[0,0,0])
print(y[1,1,1])
z=x.reshape(3,4)
print(z)
print(z[2,0])