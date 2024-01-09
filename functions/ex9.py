#a function inside another function:
#the main function is called outer function
#the sub function is called inner function
def d1():
    print('hello world')
    def d2():
        print('hello python learners')
    d1()
d1()