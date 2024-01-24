class milestone:
    a=10
    b=20
m=milestone()
print(m)
print(id(m))
n=milestone()
print(n)
print(id(n))

x=milestone.a
print(x)
print(id(x))
x=milestone.b
print(x)
print(id(x))

y=milestone.a
print(id(y))

z=milestone.a
print(id(z))