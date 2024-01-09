#a function inside another function with arguments:
def d1(a,b):
    print(a+b)
    def d2(c,d):
        print(c+d)
    d2(10,20)
d1(20,30)