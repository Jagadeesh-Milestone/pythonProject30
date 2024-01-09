#globals method:
#it is used to access the global variable locally when both local
#and global variables having same variable name.
x=100
print('global x value is:',x)
def d1():
    x=200
    print('local x value is:',x)
    print('global x value is:',globals()['x'])
d1()
print('global x value is:',x)