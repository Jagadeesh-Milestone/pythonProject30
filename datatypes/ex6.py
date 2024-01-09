#set:
#a set is a collection of data and this data may be any type
#a set is having unordered elements
#it dont allow index calling ,index slicing and duplicate values.
#set is taken in {}.
#set is mutable.
s={10,20,30,40}
print(s)
print(type(s))

#set dont allows duplicate values:
a={10,10.2,'hello',5+6j,10,10}
print(a)
print(len(a))

#set dont allows index calling:
b={100,200,300,1000}
#print(b.index(100))

#add method:
c={10,20,30,40}
c.add(100)
print(c)

#update:
d={1,2,3,4}
d.update([10,20,30,40])
print(d)

#pop:
e={100,200,300}
e.pop()
print(e)

#remove:
f={1,2,3,4}
f.remove(3)
print(f)

#discard:
g={10,20,30,40}
g.discard(20)
print(g)

#difference between remove and discard:
h={10,20,30,40,50}
#h.remove(100)
#print(h)
h.discard(100)
print(h)
#if we remove the element which is not in set we get key error.
#if we discard the element which is not in the set we dont get any
#error.

#clear:
j={10,20,30}
j.clear()
print(j)

#copy:
k={1,2,3,4,5}
l=k.copy()
print(l)

#union:
#it is used to combine the two set elements.
m={10,20,30,40}
n={50,40,30,60}
print(m.union(n))

#intersection:
#it is used to print the common elements in two sets
o={1,2,3,4}
p={3,4,5,6}
print(o.intersection(p))

#subset:
#it returns true if all the elements of one set are found in another set
q={1,2,3}
r={1,2,3,4,5,6}
print(q.issubset(r))

#superset:
s={1,2,3,4,5}
t={2,3,4}
print(s.issuperset(t))

#disjoint:
u={10,20,30,40}
v={1,2,3,4}
print(u.isdisjoint(v))

#difference:
w={1,2,3,4}
x={1,2,10,20,30}
print(w.difference(x))
