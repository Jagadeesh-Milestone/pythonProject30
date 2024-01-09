#returning a function:
def d1():
    print('hello world')
    def d2():
        return 'hello python'
    return d2()
d=d1()
print(d)
