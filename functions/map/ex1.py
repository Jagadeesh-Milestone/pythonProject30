#map:
x=[10,20,30,40,50]
print(x*2)
for i in x:
    print(i*2)

l=[]
r=lambda n:n*2
for i in x:
    l.append(r(i))
print(l)

#using map:
def d1(n):
    return n*2
m=map(d1,x)
print(tuple(m))

#using map in lambda:
z=map(lambda y:y*2,x)
print(list(z))