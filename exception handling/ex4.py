#exception handling:
try:
    a=10
    b=5
    c=0
    print(a/b)
    print('statement one')
    print(b/c)
    print('statement two')
except Exception:
    print('statement three')
else:
    print('statement four')
#if we have any exceptions in our code except block will be
#executed otherwise else block will be executed.
