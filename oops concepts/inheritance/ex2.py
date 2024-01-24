#single inheritance:
#it is the property in which a single child class is inherited
#from a single parent class.
class parent:
    money=20000
    def d1(self,surname):
        print('parent surname is',surname)
        print('parent money is',self.money)
class child(parent):
    cmoney=30000
    def d2(self,surname):
        print('child surname is',surname)
        print('child money is',self.cmoney)
c=child()
c.d2('mike')
c.d1('mike')