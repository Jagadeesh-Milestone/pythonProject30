#hybrid inheritance:
#it is the combination of two or more inheritances.
class grandparent:
    gproperty=100
    def d1(self):
        print('g property is:',self.gproperty)
class parent(grandparent):
    pproperty=200
    def d2(self):
        print('p property is:',self.pproperty)
class child(parent,grandparent):
    cproperty=300
    def d3(self):
        print('c property is:',self.cproperty)
c=child()
c.d3()
c.d2()
c.d1()

p=parent()
p.d2()
p.d1()
