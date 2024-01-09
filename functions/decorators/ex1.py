#decorators:
#decorators are used to add extra functionality to the already
#existing function.
#we use @ annotation as a decorator.
#a function without decorator:
def d1(func):
    def d2():
        result=func()
        return result+"world"
    return d2()
def d3():
    return "hello"
d=d1(d3)
print(d)

#a function with decorator:
def d4(func):
    def d5():
        result=func()
        return  result+"python learners"
    return d5
@d4
def d6():
    return "Welcome"
d=d6()
print(d)