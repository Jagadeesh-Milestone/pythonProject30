#tuple:
#a tuple is a collection of data and this data may be anytype.
#a tuple allows duplicate values,index calling,index slicing.
#a tuple is immutable meaning that once we create a list we cant modify
#the data.
#tuple is taken in ().
#tuple is having ordered elements.
a=()
print(a)
print(type(a))

b=(10,10.3,5+6j,True,'hello')
print(b)

c=(10,20,30,10)
print(c)

d=(10,20,30,40,50)
print(d.index(10))
print(d[3])
print(d[-3])

e=(1,2,3,4,5,6)
print(len(e))

f=(1,2,3,1,2,1)
print(f.count(1))

#concatenation:
#adding a tuple to another tuple.
g=(10,20,30,40)
h=(50,60)
print(g+h)
print(g+(100,200))

i=(10)
print(i)
print(type(i))

j=(10,)
print(j)
print(type(j))

k=(10,20,30,40)
#k.append(100)
#print(k)

#converting a list to tuple.
l=[10,20,30,40]
m=tuple(l)
print(m)
#m.append(100)
#print(m)

#converting a tuple to list.
t=(100,200,300)
u=list(t)
print(u)
u.append(1000)
print(u)

#differences between list and tuple:
#list:
#list is taken in []
#list is mutable
#we can modify the data easily
#list is less securable.
#list consumes more memory

#tuple:
#tuple is taken in ()
#tuple is immutable
#we cant modify the data
#tuple is more securable
#tuple consumes less memory compared to list


