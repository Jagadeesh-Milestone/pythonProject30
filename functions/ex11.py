#we can use the arguments of outer function inside inner function.
def d1(x,y):
    def d2():
        print(x+y)
    d2()
d1(10,20)

