#print/return/yield
def d1():
    print('hello world')
d1()

def d2():
    return 'hello python learners'
d=d2()
print(d)
print(d2())

def d3():
    yield 100
    yield 200
d=d3()
print(next(d))
print(next(d))
for i in d:
    print(i)