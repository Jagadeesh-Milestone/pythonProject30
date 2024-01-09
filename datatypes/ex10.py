#range:
#if we need any particular range of values we use range:
l=range(10)
print(l)
print(type(l))

a=list(range(10))
print(a)

b=tuple(range(10))
print(b)

c=set(range(10))
print(c)

d=frozenset(range(10))
print(d)

#we cant take range in dict
#e=dict(range(10))
#print(e)

f=list(range(10,20))
print(f)

g=tuple(range(10,50,5))
print(g)