#abstraction:
#it is the property in which hiding the unnecessary information
#and displaying / highlighting the necessary information.
#to work with abstraction we have to import it.
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        print('polygon has many sides')
class triangle(polygon):
    def sides(self):
        print('a triangle has 3 sides')
class square(polygon):
    def sides(self):
        print('a square has 4 sides')
class pentagon(polygon):
    def sides(self):
        print('a polygon will have 5 sides')
p=pentagon()
p.sides()

s=square()
s.sides()

t=triangle()
t.sides()

p=polygon()
p.sides()