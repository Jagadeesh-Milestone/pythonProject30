#iterating over numpy arrays:
import numpy
import numpy as np
x=numpy.array([10,20,30,40])
for i in x:
    print(i)
y=numpy.array([[1,2,3],[4,5,6]])
for i in y:
    for a in i:
        print(a)
z=numpy.array([[[10,20],[40,50]],[[60,70],[80,90]]])
for i in z:
    for a in i:
        for b in a:
            print(b)

for m in np.nditer(z):
    print(m)