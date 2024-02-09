#copy and view:
import numpy as np
x=np.array([10,20,30,40])
y=x.copy()
x[1]=100
print(x)
print(y)
#in the above example copied array is not affected with the original
#array
y[0]=200
print(x)
print(y)
#in the above example original array is not affected with the copied
#array
a=np.array([100,200,300,400])
b=a.view()
a[1]=10
print(a)
print(b)
#in the above example viewed array is affected with the original
#array
b[0]=20
print(a)
print(b)
#in the above example original array is affected with the viewed
#array