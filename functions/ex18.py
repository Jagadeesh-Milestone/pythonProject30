#function as an argument value to another function:
def d1(a):
    return 'hello world',a
def d2():
    return 'hello python learners'
d=d1(d2())
print(d)

def d3(b,c):
    return 'hello milestone',b,c
def d4(d):
    return 'hello HTML learners',d
def d5():
    return 'hello JAVA learners'
d=d3(d4(d5()),d5())
print(d)