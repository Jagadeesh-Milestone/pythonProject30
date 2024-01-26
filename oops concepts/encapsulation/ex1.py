#encapsulation:
#It is the property in which wrapping up of data(attributes and methods)\
#into a single entity is called encapsulation.
class base:
    def __init__(self):
        self._a=100
        print('i am a base class property')
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a)
        self._a=200
        print(self._a)
        print(' i am a derived class property')
d=derived()
print('derived class a value is:',d._a)
b=base()
print('base class a value is:',b._a)