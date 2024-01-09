#global keyword:
#it is used to access the local variable globally when both local
#and global variables having same variable name.
x=100
print('global x value is:',x)
def d1():
    global x
    x=200
    print('local x value is:',x)
d1()
print('local x value is:',x)
print(x)
print(x)