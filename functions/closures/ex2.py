#use of closure:
#eventhough we delete the actual function we can use its functionality.
def d1():
    def d2():
        return 'hello world'
    return d2()
d=d1()
print(d)
del d1 #here we deleted the d1 function
print(d)#we are using d1 after its deletion.
print(d)