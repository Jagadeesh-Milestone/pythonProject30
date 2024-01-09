#a function without decorator:
def d1(func):
    def d2(a):
        result=func(a*a)
        return result
    return d2
def d3(a):
    return a
d=d1(d3)
print(d(6))

#a function with decorator:
def d4(func):
    def d5(b):
        result=func(b**b)
        return result
    return d5
@d4
def d6(b):
    return b
d=d6(3)
print(d)