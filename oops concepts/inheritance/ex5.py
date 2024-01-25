#hirercheal inheritance:
#it is the property in which more than one child classes are derived
#from a single parent class.
class grandparent:
    gmoney=10
    def d1(self):
        print('g money is:',self.gmoney)
class parent(grandparent):
    pmoney=20
    def d2(self):
        print('p money is:',self.pmoney)
class child(grandparent):
    cmoney=30
    def d3(self):
        print('c money is:',self.cmoney)
c=child()
c.d3()
c.d1()

p=parent()
p.d2()
p.d1()