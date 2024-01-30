import jagadeesh
from jagadeesh import userdetails
from jagadeesh import userdetails as u#aliyas name
x=dir(jagadeesh)
print(x)

a=jagadeesh.d1()
print(a)

b=jagadeesh.d2(4,5)
print(b)

c=jagadeesh.userdetails.keys()
print(c)

d=userdetails['name']
print(d)

e=u.values()
print(e)