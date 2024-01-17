#map:
l=[1,2,3,4,5,11]
m=[6,7,8,9,10,2]
#print(l*m)
for (i,k) in zip(l,m):
    print(i*k)
#using map:
def d1(a,b):
    return a*b
z=map(d1,l,m)
print(list(z))

#map in lambda:
x=map(lambda c,d:(c*d),l,m)
print(list(x))