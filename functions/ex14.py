#variables:
#there are three types of variables.
#local variable
#global variable
#protected variable
#local variable:
#when we declare a variable locally we cant access it outside the
#function.
#print('x value before the function:',x)#x will not be accessed
#outside the function.
def d1():
    #print(x)#x is not defined yet
    x=100
    print('x value inside the function:',x)
    print(x)
    print(x)
d1()
#print('x value after the function:',x)