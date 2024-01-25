#polymorphism in oops:
class bird:
    def fly(self):
        print('some birds can fly and some birds cannot fly')
class eagle(bird):
    def fly(self):
        print('an eagle can fly at very heights')
class parrot(bird):
    def fly(self):
        print('a parrot can fly but not at more heights')
class ostrich(bird):
    def fly(self):
        print('an ostrich cannot fly')
o=ostrich()
o.fly()

p=parrot()
p.fly()

e=eagle()
e.fly()