#dict comprehensions:
x=[1,2,3,4,5,6,7,8,9]
y={}
for i in x:
    if i%2==0:
        y[i]=i*i
print(y)

#using dict comprehension:
z={i:i*i for i in x if i%2==1}
print(z)