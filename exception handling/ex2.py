#exception handling:
try:
    a=10
    b=5
    c=0
    print(a/b)
    print('statement one')
    print(a/c)
    print('statement two')
    print('hello world')
except ZeroDivisionError:
    print('statement three')
    print('hello python learners')
#in the above example statement two and hello world will not be
#printed since the exception is not excepted yet.