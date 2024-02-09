#array shape:
#array shape is the no of elements in each dimension.
import  numpy as np

x=np.array([10,20,30,40])
print(x.shape)

y=np.array([[1,2,3],[4,5,6]])
print(y.shape)

z=np.array([100,200,300,400],ndmin=6)
print(z.shape)