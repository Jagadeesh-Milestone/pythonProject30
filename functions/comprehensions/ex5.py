#generator comprehension:
x=(i for i in range(10))
print(x)
print(next(x))
print(next(x))
for i in x:
    print(i,end=" ")
print(type(x))