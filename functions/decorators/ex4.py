def d1(n):
    def d2(func):
        global i
        for i in range(n):
            func()
    return d2
#@d1(10)
def d3():
    print(i)
d=d1(20)(d3)
