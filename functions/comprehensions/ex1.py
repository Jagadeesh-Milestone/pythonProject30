#comprehensions
x=[1,2,3,4,5,6,7,8,9,10]
y=[]
for i in x:
    if i%2==0:
        y.append(i)
print(y)

#with list comprehension:
z=[i for i in x if i%2==1]
print(z)

