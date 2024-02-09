#data types in numpy:
import  numpy as np

x=np.array([10,20,30,40])
print(x.dtype)

y=np.array(['hello','python','learners','hyderabad'])
print(y.dtype)

z=np.array([True,False])
print(z.dtype)

a=np.array([5+6j])
print(a.dtype)

b=np.array([10.2,11.4,15.8,18.4])
print(b.dtype)

c=np.array([10.2,11.4,15.8,18.4],dtype=int)
print(c)
print(c.dtype)

d=np.array([12,4,8,0,3,0,2,0],dtype=bool)
print(d)
