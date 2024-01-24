#multiple inheritance:
#it is the property in which a single child class is derived from
#more than one parent classes.
class grandparent:
    gmoney=1000
    def d1(self):
        print('g money is:',self.gmoney)
class parent:
    pmoney=2000
    def d2(self):
        print('p money is:',self.pmoney)
class child(grandparent,parent):
    cmoney=3000
    def d3(self):
        print('c money is:',self.cmoney)
c=child()
c.d1()
c.d2()
c.d3()

