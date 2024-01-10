#generators:
def d1():
    return 100
    return 200
    return 300
d=d1()
print(d)

def d2():
    yield 100
    yield 200
    yield 300
d=d2()
print(d)
print(next(d))
print(next(d))
print(next(d))
print(next(d))