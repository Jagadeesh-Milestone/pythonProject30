#class method:
class milestone:
    myname='jagadeesh'
    @classmethod
    def friends(cls):
        friendname='hari'
        print(friendname,'and',cls.myname,'are best friends')
m=milestone()
m.friends()

milestone.friends()