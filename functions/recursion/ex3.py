#get and set recursion limit.
import  sys
print(sys.getrecursionlimit())
x=sys.setrecursionlimit(1200)
print(x)
print(sys.getrecursionlimit())
i=0
def d1():
    global i
    print('d1 function',i)
    i+=1
    d1()
d1()