
#we cant use the arguments of inner function inside outer function.
def d1():
    print(a*b)
    def d2(a,b):
        print(a+b)
    d2(10,20)
d1()