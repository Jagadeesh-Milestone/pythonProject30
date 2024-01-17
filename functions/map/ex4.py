#map:
l=['python','java','ruby','hello','bangalore']
for i in l:
    print(list(reversed(i)))
for a in l:
    print(a[::-1])
#using map function:
def d1(n):
    return n[::-1]
m=map(d1,l)
print(list(m))

#using map in lambda:
x=map(lambda y:y[::-1],l)
print(tuple(x))