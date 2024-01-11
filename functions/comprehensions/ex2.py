#square root of list of elements.
x=[1,2,3,4,5]
y=[]
for i in x:
    y.append(i*i)
print(y)

#using comprehension:
z=[i*i for i in x]
print(z)