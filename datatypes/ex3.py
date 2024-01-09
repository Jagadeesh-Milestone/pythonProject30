#sequences:
#list:
#a list is a collection of data and this data may be anytype.
#a list allows duplicate values,index calling,index slicing.
#a list is mutable meaning that once we create a list we can modify
#the data.
#list is taken in [].
#list is having ordered elements.
#empty list:
a=[]
print(a)
print(type(a))

#list
b=[10,10.2,'hello',True,5+6j]
print(b)

#list allows duplicate values.
c=[10,20,30,10,20]
print(c)

#len:
#it is used to find the no of values in a list.
d=[1,2,3,4,3,66,7,5]
print(len(d))

#count:
#it is used to find the no of appearance of an element.
e=[10,20,30,10,20,10]
print(e.count(10))

#copy
#it is used to store the copy of a list
f=[100,200,300,400]
g=f.copy()
print(g)

#clear:
#it is used to clear the list elements
h=[10,20,30,40]
h.clear()
print(h)

#append:
#it is used to add an element at the end of a list.
i=[10,20,30,40]
i.append(100)
print(i)

#index:
#the index position of first element is always 0,second is 1,..
j=[10,20,30,30]
print(j.index(30))
print(j[1])
#print(j[4])

#negative index:
#from right to left
#index position of first element is -1,second is -2,...
print(j[-1])
#print(j[-10])

#pop:
#it is used to remove an element from the end of a list:
k=[1,2,3,4,5]
k.pop()
print(k)
#we can remove particular element by using index position.
k.pop(-2)
print(k)

#extend:
#it is used to add multiple elements at the end of a list.'
l=[10,20,30,40]
l.extend([60,70,80])
print(l)

#insert:
#it is used to insert an element at a particular index position:
m=[1,2,3,5,6,7,9]
m.insert(3,4)
print(m)
#if there is no particular index position the value will be added
#at the end of a list.

#remove:
#it is used to remove an element from the list.
n=[100,200,300,400]
n.remove(200)
print(n)

#sort:
#it is used to arrange the elements in ascending or descending order
o=[10,50,40,23,70]
o.sort(reverse=False)
print(o)
o.sort(reverse=True)
print(o)

#find the second largest/second lowest number in a list of elements
l=[4,3,5,7,2,8,10]
print(max(l))
print(min(l))
l.sort()
print(l[-2])
print(l[1])

#reverse:
l=[10,40,30,20]
l.reverse()
print(l)
