#default argument value:
def d1(country='India'):
    print('i am from',country)
d1('australia')
d1()
d1('pakistan')
d1()

def d2(a,b=20):
    print(a+b)
d2(10,40)
d2(5)
#d2()