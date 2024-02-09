#dimensions of an array:
import numpy as np

#zero dimensional array
x=np.array(10)
print(x)
print(x.ndim)

#one dimensional array
y=np.array([10,20,30])
print(y)
print(y.ndim)

#two dimensional array
z=np.array([[10,20,30],[40,50,60]])
print(z)
print(z.ndim)

#three dimensional array
a=np.array([[[10,20],[40,50]],[[60,70],[80,90]]])
print(a)
print(a.ndim)

#multi dimensional array:
b=np.array([10,20,30,40],ndmin=10)
print(b)
print(b.ndim)

