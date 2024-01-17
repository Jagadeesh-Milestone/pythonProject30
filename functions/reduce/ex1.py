#reduce:
#reduce is a function which is used to apply a particular function
#passed
#in its argument to all of the elememts.
#to use reduce we have to import it from the functool module.
from functools import reduce
x=[3,4,5,6,7,8,9,10]
def d1(a,b):
    return a+b
y=reduce(d1,x)
print(y)

z=reduce(lambda m,n:m+n,x)
print(z)