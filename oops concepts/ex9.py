#class/instance/static methods in a single class.
class milestone:
    myname='jagadeesh'
    def d1(self,friendname):
        print(self.myname,'and',friendname,'are friends')
    @staticmethod
    def d2(friendname):
        print(milestone.myname,'and',friendname,'are best friends')
    @classmethod
    def d3(cls,friendname):
        print(cls.myname,'and',friendname,'are good friends')
m=milestone()
m.d1('hari')
m.d2('mahesh')
m.d3('suresh')