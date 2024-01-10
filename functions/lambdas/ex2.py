#multiple expressions:
def d1(a,b,c,d):
    print(a+b)
    print(b-c)
    print(c*d)
    print(a/d)
    print(b**c)
d1(2,3,4,5)

x=lambda a,b,c,d:((a+b),(b-c),(c*d),(a/d),(b**c))
print(x(2,3,4,5))