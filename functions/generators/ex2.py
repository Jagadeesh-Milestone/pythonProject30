#for loop in generators:
def d1(n):
    for i in range(n):
        yield i
d=d1(4)
print(d)
#print(next(d))
#print(next(d))
#print(next(d))
#print(next(d))
#print(next(d))
for a in d:
    print(a)