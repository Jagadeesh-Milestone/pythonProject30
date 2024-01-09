#frozenset:
#it is the immutable version of set.
#we cant create frozenset individually we have to convert the already
#existing set to frozen:
s={10,20,30,40}
a=frozenset(s)
print(a)
print(type(a))
#a.add(100)
#print(a)
l=[10,20,30]
m=frozenset(l)
print(m)
print(type(m))