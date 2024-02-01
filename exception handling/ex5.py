#exception handling:
try:
    l=[10,20,30,40]
    print(l[0])
    print('statement one')
except Exception:
    print('statement two')
else:
    print('statement three')
finally:
    print('statement four')
#finally block will be executed in the both conditions(code with
#exceptions and code without exceptions).
