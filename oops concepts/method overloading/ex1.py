#method overloading:
class milestone:
    def d1(self,a,b):
        print(a)
        print(b)
    def d1(self,a,b,c):
        print(a)
        print(b)
        print(c)
m=milestone()
m.d1(10,20)