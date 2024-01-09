#global variable:
#once we declare a variable globally we can access it anywhere in
#the program.
x=100
print('x value before the function:',x)
def d1():
    print('x value inside the function:',x)
d1()
print('x value after the function:',x)