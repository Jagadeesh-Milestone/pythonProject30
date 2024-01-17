#filter:
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(i*2)
    else:
        print(i*3)

def d1(n):
    return n%2==0
f=filter(d1,l)
print(list(f))

x=filter(lambda m:m%2==1,l)
print(tuple(x))