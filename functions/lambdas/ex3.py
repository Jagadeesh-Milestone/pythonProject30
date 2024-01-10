#default args:
def d1(a,b=20):
    print(a+b)
    print(a-b)
d1(10)
d1(10,40)
x=lambda a,b=20:((a+b),(a-b))
print(x(10))
print(x(10,40))