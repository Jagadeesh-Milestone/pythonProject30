#multi level inheritance:
#it is the property in which more than one base class and one derived
#class.
class grandparent:
    gmoney=10000
    def d1(self):
        print('g property is',self.gmoney)
class parent(grandparent):
    pmoney=20000
    def d2(self):
        print('p money is',self.pmoney)
class child(parent):
    cmoney=30000
    def d3(self):
        print('c money is',self.cmoney)
c=child()
c.d1()
c.d2()
c.d3()

p=parent()
p.d1()
p.d2()