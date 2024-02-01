#exception handling:
try:
    l=[10,20,30,40]
    print(l[2])
    print('statement one')
    #print(l[10])#Index Error
    #print(l.index(100))#Value error
    s={10,20,30,40}
    #s.append(100)#attribute error
    s.remove(100)#key error
    print(s)
    print('statement two')
except Exception:
    print('statement three')
